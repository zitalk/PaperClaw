const state = { papers: [], reports: [], visible: 12, query: "", category: "", date: "" };
const el = (id) => document.getElementById(id);
const researchDirections = [
  "多模态显著目标检测",
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
  const query = state.query.trim().toLowerCase();
  return state.papers.filter((paper) => {
    if (state.category && paper.category !== state.category) return false;
    if (state.date && paper.date !== state.date) return false;
    if (!query) return true;
    return [paper.title, paper.authors, paper.institution, paper.summary, paper.arxiv_id, paper.source_label]
      .join(" ").toLowerCase().includes(query);
  });
}

function createPaperCard(paper) {
  const fragment = el("paper-template").content.cloneNode(true);
  fragment.querySelector(".paper-category").textContent = paper.category;
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
    state.category = event.target.value;
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
      fetch("data/papers.json"), fetch("data/reports.json")
    ]);
    if (!paperResponse.ok || !reportResponse.ok) throw new Error("数据文件不可用");
    state.papers = (await paperResponse.json()).papers || [];
    state.reports = (await reportResponse.json()).reports || [];
    const dates = [...new Set(state.papers.map((paper) => paper.date))].sort().reverse();
    setOptions(el("category-filter"), researchDirections);
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
    el("paper-grid").innerHTML = `<p class="empty">${error.message}</p>`;
  }
}

initialize();
