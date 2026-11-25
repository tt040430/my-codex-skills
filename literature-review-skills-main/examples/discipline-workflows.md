# 学科用法 / Discipline Workflows

以下是提示词和流程示例，不是已执行检索，不含可引用的文献结论。收到题录不等于已读全文；只有真实材料才能填入证据表。

## 新闻传播：先问清楚研究对象

```text
请使用 literature-review-skills，主题是生成式 AI 与新闻可信度。
先 grill me，每轮一个问题。我还没确定是新闻文本、编辑室还是受众视角，也还没有文献。
```

合适的第一轮可以是：

> 你想解释受众如何判断新闻可信度，还是新闻机构如何决定披露 AI 参与？这会决定分析单位和检索范围。若你的兴趣是“读者信不信”，建议先选受众判断，但这不能同时解释编辑室决策。

到这里应当等待回答，不继续替作者选研究对象、理论和方法。范围确定后，产出检索计划与待填证据表，不生成“已有研究普遍发现”的段落。

## 图书情报：先检查证据是否可比

```text
请使用 compare-research-methods。我的综述研究生成式 AI 辅助学术检索。
下面是我提供的真实文献笔记：[在此提供材料]。
请区分检索指标、任务完成和用户体验，检查语料、评测任务、比较基线和指标定义是否一致。
我是在评价综述中的研究，不是要设计一个新实验。
```

输出应说明不同研究各自支持什么判断，哪些结果不能直接比较。检索排名指标、自报满意度和实际任务完成不能自动合成一个“系统更好”的结论。只有题录或摘要时，未读取的全文方法细节保持空缺。

## 从证据表写到草稿

```text
请使用 literature-review-skills。沿用已确认的综述问题和范围。
依据我提供的全文、阅读笔记和证据表，先检查每个模块有哪些来源支持，
再写各节草稿。每个文献论断附来源 ID、核验状态及页码或段落定位；
保留反例，区分文献结论与我们的解释，不够支撑的部分不要补写。
最后列出待核实清单和需要我判断的问题。
```

产物顺序：范围与检索说明 → 证据表 → 论证提纲 → 带来源的段落草稿 → 待核实清单 → 给作者的问题。三种来源状态仍是“用户提供／已核验／未核验”，并另记“题录／摘要／全文／用户笔记”的阅读层级。

## 跨学科与快速模式

```text
我研究推荐系统怎样影响新闻接触，涉及新闻传播和信息检索。
请先以受众新闻接触为主问题，结合两个学科的指南，不要把点击率当成信任。
直接给工作方案，不再追问；未知范围请列为假设，不要编造研究结论。
```

## English Prompt

```text
Use literature-review-skills for a library and information science review on
AI-assisted scholarly search. Start with my attached abstracts and notes.
Build an evidence table, mark what has and has not been read, and separate retrieval
performance, task outcomes, and user experience. Grill me one question at a time
only when a scope decision blocks progress. Draft supported sections after I confirm
the outline, keeping source IDs, counterevidence, and limitations visible.
```

## 后续扩展

教育学、社会学等未配置学科先走通用流程，不宣称已有专门支持。维护者可复制 [学科模板](../references/disciplines/_template.md)，补充指南和 [行为用例](../evals/scenarios.json)，再按 [贡献说明](../CONTRIBUTING.md)同步到独立 Skill。不能只新增一组关键词，就宣称已经支持整个学科。
