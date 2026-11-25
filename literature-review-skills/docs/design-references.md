# Design References / 设计参考

查阅日期：2026-11-02。以下用于比较工作流，不代表对方参与、背书或验证本项目。本次没有复制这些项目的代码或指令正文，也不要求安装它们。

## grill-me / grilling

- 项目：[mattpocock/skills](https://github.com/mattpocock/skills)
- 入口：[grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
- 实际流程：[grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)

查阅时 grill-me 已是调用 grilling 的入口。借鉴的是按决策依赖安排追问、先查已有资料、给建议但不替用户回答、在关键决定明确后停止。这里改成研究访谈，默认每轮一个问题，增加文献证据、反例、概念边界与“不再追问”模式；没有照搬产品开发访谈问题。

## K-Dense Literature Review

- [claude-scientific-skills / literature-review](https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/skills/literature-review/SKILL.md)

参考检索、筛选、提取、评价、综合与引用核验的阶段划分，以及题录核验和论断支持之间的区别。保留本项目五步思考流程，增加证据表和检索记录；没有照搬其依赖、数据库组合或报告工具，也不把医学研究模板直接套到新闻传播与情报学。

## GPT Researcher

- [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)

参考把研究计划、资料收集和报告写作分开的组织方式。这里是 Agent 指令，不是其检索引擎或多 Agent 系统的移植；没有实现 MCP 集成或自动并行研究。

## 学科检索入口

- [EBSCO Communication & Mass Media Complete](https://www.ebsco.com/products/research-databases/communication-mass-media-complete)
- [EBSCO Information Science & Technology Abstracts](https://www.ebsco.com/products/research-databases/information-science-technology-abstracts)
- [EBSCO LISTA coverage list](https://www.ebsco.com/m/ee/Marketing/titleLists/lxh-coverage.pdf)

这些页面只支持候选检索库的选择，不证明任一数据库能完整覆盖某个选题。实际检索前仍需检查机构权限、当期覆盖与检索语法。学科指南中的理论视角和关键词是候选设计，不是对已发表研究的结论，也不是可用于论文的引用。

## What Changed Here

The implementation uses two optional discipline profiles, a research-specific interview, and an evidence-to-draft workflow. It retains independent stage installation and the existing source-status contract. External projects informed the design; they are not runtime dependencies or evidence of this project's effectiveness.
