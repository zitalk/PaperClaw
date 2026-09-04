/* Shared pure filtering helpers, also exercised by Node tests. */
const PaperClawFilters = {
  categories(paper) {
    if (Array.isArray(paper.categories)) return paper.categories;
    // Compatibility with a briefly cached old dataset during deployment.
    const category = paper.category === "多模态显著目标检测" ? "多模态视觉学习" : paper.category;
    return category && category !== "待归类" ? [category] : [];
  },
  topics(directions, category = "") {
    return directions.filter((d) => !category || d.name === category)
      .flatMap((d) => d.topics.map((topic) => ({ ...topic, category: d.name })));
  },
  filter(papers, state) {
    const query = (state.query || "").trim().toLowerCase();
    return papers.filter((paper) => {
      const categories = this.categories(paper);
      const topics = paper.topics || [];
      if (state.category && !categories.includes(state.category)) return false;
      if (state.topic && !topics.some((topic) => topic.id === state.topic)) return false;
      if (state.date && paper.date !== state.date) return false;
      if (!query) return true;
      return [paper.title, paper.authors, paper.institution, paper.summary, paper.arxiv_id,
        paper.source_label, ...categories, ...topics.map((t) => t.name),
        ...(paper.search_keywords || []), categories.length ? "" : "待归类"]
        .join(" ").toLowerCase().includes(query);
    });
  }
};
if (typeof module !== "undefined" && module.exports) module.exports = PaperClawFilters;
