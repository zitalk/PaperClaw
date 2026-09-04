const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const filters = require('../site/assets/paper-filters.js');
const directions = JSON.parse(fs.readFileSync('skills/rs-paper-pipeline/scripts/config/research_taxonomy.json', 'utf8')).directions;
const papers = [
  {issue_number: 1, title: 'RGB-T UAV saliency', categories: ['多模态视觉学习', '无人机视觉'], topics: [{id:'mm-sod', name:'显著目标检测（SOD）'}], date:'20260901'},
  {issue_number: 2, title: 'Multi-camera UAV tracking', categories: ['多视角与多目标感知', '无人机视觉'], topics: [{id:'mv-mtmc', name:'多相机与跨相机跟踪'}], date:'20260902'},
  {issue_number: 3, title: 'Uncertain paper', categories: [], topics: [], date:'20260902'}
];
test('each cross-direction paper is reachable from both directions', () => {
  assert.deepEqual(filters.filter(papers, {category:'无人机视觉'}).map(p=>p.issue_number), [1,2]);
  assert.deepEqual(filters.filter(papers, {category:'多模态视觉学习'}).map(p=>p.issue_number), [1]);
});
test('all papers are counted once, not once per category', () => {
  assert.equal(filters.filter(papers, {}).length, 3);
});
test('topic options follow the selected parent', () => {
  assert(filters.topics(directions,'多模态视觉学习').some(t=>t.id==='mm-cod'));
  assert(!filters.topics(directions,'无人机视觉').some(t=>t.id==='mm-cod'));
});
test('topic, date and direction filters intersect', () => {
  assert.equal(filters.filter(papers,{category:'无人机视觉',topic:'mv-mtmc',date:'20260902'}).length,1);
  assert.equal(filters.filter(papers,{category:'多模态视觉学习',topic:'mv-mtmc'}).length,0);
});
test('query finds topic labels and unclassified papers', () => {
  assert.equal(filters.filter(papers,{query:'SOD'})[0].issue_number,1);
  assert.equal(filters.filter(papers,{query:'待归类'})[0].issue_number,3);
});
test('legacy saliency label migrates while cached metadata loads', () => {
  assert.deepEqual(filters.categories({category:'多模态显著目标检测'}),['多模态视觉学习']);
  assert.deepEqual(filters.categories({category:'多模态视觉学习',categories:[]}),[]);
});

test('extended reading is a flat direction with no subtopics', () => {
  const extended = {issue_number: 4, title:'Radar detection', categories:['拓展阅读'], topics:[], date:'20260903'};
  const dataset = [...papers, extended];
  assert.deepEqual(filters.filter(dataset,{category:'拓展阅读'}).map(p=>p.issue_number),[4]);
  assert.equal(filters.filter(dataset,{category:'拓展阅读',topic:'ext-sensors'}).length,0);
  assert.equal(filters.filter(dataset,{category:'拓展阅读',topic:'mm-sod'}).length,0);
  assert.equal(filters.topics(directions,'拓展阅读').length,0);
  assert.equal(filters.filter(dataset,{}).length,4);
});
