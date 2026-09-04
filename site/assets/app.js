const state = { papers: [], reports: [], directions: [], visible: 12, query: "", category: "", topic: "", date: "" };
const el = (id) => document.getElementById(id);
const researchDirections = [
  "多模态视觉学习",
  "多视角与多目标感知",
  "无人机视觉",
  "免训练开放集分割"
];

const latexSymbols = {
  alpha: "α", beta: "β", gamma: "γ", delta: "δ", epsilon: "ε", theta: "θ",
  lambda: "λ", mu: "μ", pi: "π", sigma: "σ", phi: "φ", omega: "ω",
  Gamma: "Γ", Delta: "Δ", Theta: "Θ", Lambda: "Λ", Pi: "Π", Sigma: "Σ",
  Phi: "Φ", Omega: "Ω", times: "×", cdot: "·", pm: "±", leq: "≤", geq: "≥",
  neq: "≠", approx: "≈", infty: "∞", to: "→", rightarrow: "→", leftarrow: "←"
};

function plainMath(value) {
  return value
    .replace(/\\(?:mathrm|mathbf|mathit|mathsf|text)\s*\{([^{}]*)\}/g, "$1")
    .replace(/\\([A-Za-z]+)/g, (match, command) => latexSymbols[command] || command)
    .replace(/\\([{}_$%&#])/g, "$1")
    .replace(/[{}]/g, "");
}

function appendMath(container, source) {
  const tokenPattern = /([_^])\s*(?:\{([^{}]*)\}|\\([A-Za-z]+)|([^\s]))/g;
  let cursor = 0;
  for (const match of source.matchAll(tokenPattern)) {
    if (match.index > cursor) {
      container.append(document.createTextNode(plainMath(source.slice(cursor, match.index))));
    }
    const script = document.createElement(match[1] === "^" ? "sup" : "sub");
    script.textContent = plainMath(match[2] ?? (match[3] ? `\\${match[3]}` : match[4]));
    container.append(script);
    cursor = match.index + match[0].length;
  }
  if (cursor < source.length) {
    container.append(document.createTextNode(plainMath(source.slice(cursor))));
  }
}

function renderInlineMath(container, value) {
  container.replaceChildren();
  const source = value || "";
  const delimiterPattern = /\$([^$]+)\$|\\\((.*?)\\\)/g;
  let cursor = 0;
  for (const match of source.matchAll(delimiterPattern)) {
    if (match.index > cursor) {
      container.append(document.createTextNode(source.slice(cursor, match.index)));
    }
    appendMath(container, match[1] ?? match[2]);
    cursor = match.index + match[0].length;
  }
  if (cursor < source.length) {
    container.append(document.createTextNode(source.slice(cursor)));
  }
}

function formatDate(value) {
  if (!/^\d{8}$/.test(value || "")) return value || "—";
  return `${value.slice(0, 4)}-${value.slice(4, 6)}-${value.slice(6, 8)}`;
}

function setOptions(select, values) {
  values.forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    select.appendChild(option);
  });
}

function renderLatest() {
  const latest = state.reports[0];
  if (!latest) return;
  el("report-count").textContent = state.reports.length;
  el("paper-count").textContent = state.papers.length;
  el("latest-date").textContent = formatDate(latest.date).slice(5);
  el("report-month").textContent = `${latest.date.slice(0, 4)} · ${latest.date.slice(4, 6)}`;
  el("report-day").textContent = latest.date.slice(6, 8);
  el("report-overview").textContent = latest.overview || "本期日报已生成。";
  el("latest-report-link").href = latest.github_url;
  const list = el("report-highlights");
  list.replaceChildren();
  latest.highlights.forEach((highlight) => {
    const item = document.createElement("li");
    renderInlineMath(item, highlight);
    list.appendChild(item);
  });
}

function filteredPapers() {
  return PaperClawFilters.filter(state.papers, state);
}

function updateTopicOptions() {
  const select = el("topic-filter");
  select.replaceChildren(new Option("全部子方向", ""));
  PaperClawFilters.topics(state.directions, state.category).forEach((topic) => {
    select.appendChild(new Option(state.category ? topic.name : `${topic.category} · ${topic.name}`, topic.id));
  });
  select.value = state.topic;
}

function selectCategory(category, topic = "") {
  state.category = category;
  state.topic = topic;
  state.visible = 12;
  el("category-filter").value = category;
  updateTopicOptions();
  renderPapers();
}

function createPaperCard(paper) {
  const fragment = el("paper-template").content.cloneNode(true);
  const categories = PaperClawFilters.categories(paper);
  const labels = fragment.querySelector(".paper-categories");
  categories.forEach((category) => {
    const tag = document.createElement("button");
    tag.type = "button";
    tag.className = "paper-category";
    tag.textContent = category;
    tag.addEventListener("click", () => selectCategory(category));
    labels.appendChild(tag);
  });
  if (!categories.length) {
    const pending = document.createElement("span");
    pending.className = "paper-category pending";
    pending.textContent = "待归类";
    labels.appendChild(pending);
  }
  const topicLabels = fragment.querySelector(".paper-topics");
  const topics = paper.topics || [];
  const makeTopic = (topic) => {
    const tag = document.createElement("button");
    tag.type = "button";
    tag.className = "paper-topic";
    tag.textContent = topic.name;
    tag.title = topic.category;
    tag.addEventListener("click", () => selectCategory(topic.category, topic.id));
    return tag;
  };
  topics.slice(0, 3).forEach((topic) => topicLabels.appendChild(makeTopic(topic)));
  if (topics.length > 3) {
    const more = document.createElement("details");
    more.className = "paper-topic-more";
    const summary = document.createElement("summary");
    summary.textContent = `+${topics.length - 3} 个子方向`;
    more.appendChild(summary);
    const rest = document.createElement("div");
    topics.slice(3).forEach((topic) => rest.appendChild(makeTopic(topic)));
    more.appendChild(rest);
    topicLabels.appendChild(more);
  }
  topicLabels.hidden = !topics.length;
  fragment.querySelector("time").textContent = formatDate(paper.date);
  fragment.querySelector("time").dateTime = formatDate(paper.date);
  renderInlineMath(fragment.querySelector("h3"), paper.title);
  fragment.querySelector(".paper-summary").textContent = paper.summary;
  fragment.querySelector(".paper-institution-value").textContent = paper.display_institution || paper.institution || "暂无";
  fragment.querySelector(".paper-authors-value").textContent = paper.display_authors || paper.authors || "未公开";
  fragment.querySelector(".issue-link").href = paper.issue_url;
  const source = fragment.querySelector(".source-link");
  source.textContent = `来源 · ${paper.source_label || "来源"} ↗`;
  if (paper.source_url || paper.arxiv_url) source.href = paper.source_url || paper.arxiv_url;
  else source.remove();
  const ccf = fragment.querySelector(".ccf-badge");
  if (paper.ccf_grade) ccf.textContent = `CCF ${paper.ccf_grade}`;
  else ccf.remove();
  const code = fragment.querySelector(".code-link");
  if (paper.code_url) code.href = paper.code_url;
  else code.remove();
  return fragment;
}

function renderPapers() {
  const papers = filteredPapers();
  const shown = papers.slice(0, state.visible);
  const grid = el("paper-grid");
  grid.replaceChildren();
  shown.forEach((paper) => grid.appendChild(createPaperCard(paper)));
  if (!shown.length) {
    const empty = document.createElement("p");
    empty.className = "empty";
    empty.textContent = "没有找到匹配论文，试试更短的关键词。";
    grid.appendChild(empty);
  }
  el("result-count").textContent = `显示 ${shown.length} / ${papers.length} 篇`;
  el("load-more").hidden = shown.length >= papers.length;
}

function bindEvents() {
  el("search-input").addEventListener("input", (event) => {
    state.query = event.target.value;
    state.visible = 12;
    renderPapers();
  });
  el("category-filter").addEventListener("change", (event) => {
    selectCategory(event.target.value);
  });
  el("topic-filter").addEventListener("change", (event) => {
    state.topic = event.target.value;
    state.visible = 12;
    renderPapers();
  });
  el("date-filter").addEventListener("change", (event) => {
    state.date = event.target.value;
    state.visible = 12;
    renderPapers();
  });
  el("load-more").addEventListener("click", () => {
    state.visible += 12;
    renderPapers();
  });
  document.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      el("search-input").focus();
    }
  });
}

async function initialize() {
  try {
    const [paperResponse, reportResponse] = await Promise.all([
      fetch("data/papers.json", { cache: "no-cache" }), fetch("data/reports.json", { cache: "no-cache" })
    ]);
    if (!paperResponse.ok || !reportResponse.ok) throw new Error("数据文件不可用");
    const paperData = await paperResponse.json();
    state.directions = paperData.directions || researchDirections.map((name) => ({name, topics: []}));
    const keywords = new Map(PaperClawFilters.topics(state.directions).map((t) => [t.id, t.keywords || []]));
    state.papers = (paperData.papers || []).map((paper) => ({...paper,
      search_keywords: (paper.topics || []).flatMap((t) => keywords.get(t.id) || [])}));
    state.reports = (await reportResponse.json()).reports || [];
    const dates = [...new Set(state.papers.map((paper) => paper.date))].sort().reverse();
    setOptions(el("category-filter"), state.directions.map((d) => d.name));
    updateTopicOptions();
    dates.forEach((date) => {
      const option = document.createElement("option");
      option.value = date;
      option.textContent = formatDate(date);
      el("date-filter").appendChild(option);
    });
    renderLatest();
    renderPapers();
    bindEvents();
  } catch (error) {
    el("result-count").textContent = "数据载入失败";
    const message = document.createElement("p");
    message.className = "empty";
    message.textContent = error.message;
    el("paper-grid").replaceChildren(message);
  }
}

initialize();
