# Changelog

本文件记录版本变化；Git 标签和 Release 是否发布，以仓库对应页面为准。

## 未发布（Unreleased）

暂无。

## v0.3.0 (2026-11-02)

- 新增新闻传播学、图书情报与信息科学指南：概念区分、双语检索词、证据提取、方法评价、综合与空白判断。
- 新增学科路由和扩展模板；跨学科选题按需加载，其他学科回退到通用流程。
- 参考 grill-me / grilling 增加研究追问：按决策依赖推进、默认一轮一问、等待回答、保留作者决定；支持直接出方案。
- 补充检索记录、筛选、证据表和有来源支撑的草稿流程；没有文献时只交付计划和提纲。
- 总入口明确读取五个阶段的指令文件；每个阶段自带嵌套学科文件，仍可单独安装。
- 不再强制因果型综述问题；允许一篇文献跨模块编码；不从提纲推断文献密度；区分方法评价与新研究设计。
- 更新中英文 README、学科示例与设计参考；保留安装方式、个人微信、邮箱和公众号二维码。
- 新增递归引用文件同步、六项脚本单元测试和八项待执行的模型行为用例。尚未完成真实稿件验证或质量对照评测。

### v0.2 后的文档维护

README 中英文去掉具体 star 数；联系方式保留个人微信号、邮箱，并加上 GitHub Issues 与公众号入口；两个二维码缩小；新增“相关项目”；新增使用反馈 Issue 模板和 `SECURITY.md`。

## v0.2.0

本版重点是补上来源核验和输出结构，不扩展新 skill。以下改动尚未经过系统评测，也尚未在真实稿件上验证。此前的版本已被不少外部作者自发使用，但使用反馈没有系统收集。

### 新增
- `references/source-integrity.md`：来源完整性规则。只使用用户提供或已核验的文献；每条文献带状态标签（用户提供 / 已核验 / 未核验）；给出核验步骤（Crossref、OpenAlex、出版社页面、CNKI/万方人工检索）并要求记录核验方式；查不到一律写“未查到”，不补全作者、年份、期刊、页码。
- `references/output-contract.md`：固定各 skill 的输出段落名和顺序。
- 每个 `skills/<name>/references/` 下自带 `source-integrity.md` 和 `output-contract.md` 的副本，使单个 skill 目录被单独复制时也能找到规则文件。根 `references/` 是权威版本，`skills/*/references/` 是副本，修改时需同步。
- `scripts/check_references_sync.sh`：比较根 `references/` 与各 skill 副本，有差异则非零退出。
- `CHANGELOG.md`。
- README 中英文新增“局限与未验证项”一节。

### 修改
- 5 个 skill 的 Guardrails 各加一条来源完整性规则（引用 skill 目录内的 `references/source-integrity.md`；根 `SKILL.md` 仍引用根 `references/`），根 `SKILL.md` 新增 “Source Integrity” 一节。
- 输出契约：
  - `map-literature-contradictions` 的矛盾矩阵新增“出处/核验状态”列。
  - 各 skill 输出末尾固定加“待核实清单”和“给作者的问题”。
  - “Ready-To-Use Paragraph” / “Justification Paragraph” / “Synthesis Paragraph” 统一改为“段落草稿（需作者改写并核对来源）”，并加来源核对提示。
- `examples/` 顶部加声明“方法演示，非真实文献结论”，示例中的矛盾表加“无出处”标注，不含任何编造的出处。
- 根 `SKILL.md` 的 description 改为用户意图型（用户要做文献综述但不知从哪步开始时使用）；5 个 skill 的 description 追加中文触发词。
- 各 `SKILL.md` frontmatter 增加 `metadata.version: "0.2.0"`；description 改用双引号包裹。
- README 的 Responsible Use / 使用边界补充来源核验说明。

### 已知问题
- 各安装方式未逐一实测。各 skill 已自带 `references/` 副本，并在 Guardrails 里重复了核心规则；但副本需要和根 `references/` 手动同步（用 `scripts/check_references_sync.sh` 校验）。
- 未覆盖中文文献的专门流程。

## v0.1.0 (2026-07-07)

初版：根 `SKILL.md` 入口和 5 个 skill（`refine-literature-question`、`decompose-review-modules`、`compare-research-methods`、`map-literature-contradictions`、`locate-review-research-gap`），中英文 README，示例，MIT 协议。
