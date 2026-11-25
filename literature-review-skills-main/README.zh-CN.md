# 文献综述 Skills

文献综述写不顺，常常并非因为你读得太少。更常见的问题是：问题没有收紧，结构只是按作者堆材料，方法选择说不清理由，互相矛盾的研究被放在一起却没有解释，最后的 research gap 也站不稳。

这组 Skills 处理的是这些环节。它们帮你把综述从“资料很多”推进到“问题清楚、结构能展开、判断有依据”。

它不是代写工具，也不适合拿来绕过学术训练。AI 在这里扮演研究助理：帮你提问、拆分、比较、追问和检查逻辑。最终判断仍然属于研究者，文献核验、论证取舍和正文写作也必须由你自己完成。

[English README](README.md)

## 适合谁

- 正在准备课程论文、开题报告、硕博士论文文献综述的研究生。
- 已经读了不少文献，却还停留在“一个作者接一个作者介绍”的写作者。
- 需要把零散阅读整理成问题链、方法链和论证结构的研究者。
- 在 Claude Code 或 Codex 工作流里，希望把学术思考步骤固定成可复用 Skills 的用户。

## 五个 Skills 怎么配合

| Skill                           | 作用                                   |
| ------------------------------- | ------------------------------------ |
| `refine-literature-question`    | 把宽泛选题收紧成可综述的问题，明确对象、关系、范围和可讨论的边界。    |
| `decompose-review-modules`      | 把综述问题拆成几个模块，避免按作者流水账排列，让每一节都有自己的任务。  |
| `compare-research-methods`      | 比较不同研究方法能回答什么、回答不了什么，帮助你解释方法选择背后的理由。 |
| `map-literature-contradictions` | 把相互冲突的发现整理成可分析的差异，而不是简单写成“研究结论不一致”。  |
| `locate-review-research-gap`    | 在已有共识、分歧和限制的基础上，定位一个更具体、更能辩护的研究空缺。   |

## 学科与写作支持

v0.3 保留原来的五步工作流，增加按需读取的学科指南，不需要为每个学科再装一套 Skills。

| 学科 | 专门处理的问题 |
| --- | --- |
| 新闻传播学 | 新闻生产、记者与编辑室、平台传播、受众与可信度；区分文本、个人、组织和平台层面的证据。 |
| 图书情报与信息科学 | 信息行为、信息检索、知识组织、文献计量、学术交流与信息服务；区分系统指标、任务效果和用户体验。 |
| 其他或交叉学科 | 先用通用流程，明确尚无专门指南；交叉选题可以组合两份指南，不把某个学科的假设硬套进去。 |

这里的“新闻”指新闻传播学文献综述，不是新闻摘要；“情报”如果指国家安全情报研究，需要先说明，本版没有该方向的专门指南。

可以协助叙述性、范围、系统性、概念／历史型综述的规划与写作，但不会仅凭一个提示词就宣称完成了系统综述。流程是：确定问题与综述类型 → 记录检索和筛选 → 提取证据 → 比较与综合 → 形成可逐句核对的草稿。数据库访问、原文阅读深度和遗漏都会明确记录。

### 新闻传播学示例

```text
请使用 literature-review-skills。我想写“生成式 AI 新闻中的来源披露与受众可信度判断”的文献综述。
先用 grill me 模式，每次只问我一个关键问题，帮我确定概念、范围和综述类型。
目前还没有文献，请不要编写已有研究结论。
```

### 情报学示例

```text
请使用 literature-review-skills，学科是图书情报与信息科学，主题是生成式 AI 辅助学术检索。
我会提供题录、摘要和阅读笔记。请先整理证据表，区分检索效果、任务完成与用户体验，
再提出综述结构。不要直接比较不同数据集、不同指标的分数。
```

### 追问或直接开始

- 说“grill me／追问／模拟答辩”：先检查已有材料，每轮追问一个会影响后续判断的问题，等待你的回答，再继续。
- 说“直接给方案，不再追问”：列出必要假设后继续；缺文献就留待核实，不替你编答案。
- 材料齐备后说“按证据表写草稿”：按论证任务组织段落，保留来源标记、反例、解释边界和待核实事项。

更多可直接使用的提示见[学科用法示例](examples/discipline-workflows.md)。后续增加学科，只需按[模板](references/disciplines/_template.md)新增指南、登记[路由表](references/discipline-routing.md)，并补充行为用例。

## 安装这套 Skills

你不需要一个一个复制 5 个 Skill。本仓库已经在根目录放了 `SKILL.md` 作为总入口，真正执行的 5 个 Skills 放在 `skills/` 目录下。

### 方式一：一行安装（推荐）

如果你的环境支持 Agent Skills 安装器，可以直接运行：

```bash
npx skills add https://github.com/xingtaxueshu/literature-review-skills
```

按安装器提示选择目标 Agent 和需要的 Skill；安装后检查文件是否完整。不同安装器版本的发现与复制行为可能不同，见下方验证边界。

### 方式二：让 AI 自己装

对 Claude Code、Codex、Cursor 或其他兼容 Agent 说一句：

```text
请帮我查找并安装这个 skill set：https://github.com/xingtaxueshu/literature-review-skills
```

让 Agent 检查自己的 skills 目录、下载仓库并确认入口可读取。是否能完成，取决于它的文件与网络权限。

### 方式三：手动 clone

如果你使用 Claude Code：

```bash
git clone https://github.com/xingtaxueshu/literature-review-skills.git ~/.claude/skills/literature-review-skills
```

如果你使用 Codex：

```bash
git clone https://github.com/xingtaxueshu/literature-review-skills.git ~/.agents/skills/literature-review-skills
```

装好后，可以直接对 Agent 说：

```text
请使用 literature-review-skills，帮我把一个宽泛选题整理成文献综述问题、模块、方法比较、矛盾梳理和研究 gap。
```

总入口会读取仓库内对应阶段的指令。手动 clone 不代表五个子 Skill 都会被 Agent 单独注册；如需直接调用某个名称，请通过安装器选装它，或将对应的完整子目录（含 `references/`）放入 Agent 的 skills 目录：

```text
请用 refine-literature-question 帮我打磨这个主题：农村电商参与意愿。
```

## 推荐用法

可以从一个真实但还比较宽的题目开始。比如：

```text
我准备写一篇关于“农村电商如何影响家庭收入和地方发展”的文献综述。请帮我把这个宽泛主题转成综述问题，再拆成模块，比较常见研究方法，梳理文献中的矛盾结论，最后定位一个可以继续研究的 gap。
```

建议按这个顺序走：

1. 用 `refine-literature-question` 先收紧问题。比如把“农村电商影响发展”改成“农村电商通过市场接入、劳动配置和平台参与影响农户收入的机制是什么”。
2. 用 `decompose-review-modules` 拆出综述模块。可以围绕采用条件、收入机制、平台角色、地区差异、政策环境来安排。
3. 用 `compare-research-methods` 检查方法路线。问清楚问卷、面板数据、访谈、案例研究和混合方法各自适合处理哪类问题。
4. 用 `map-literature-contradictions` 处理相互冲突的发现。不要只写“有正向影响，也有影响不明显”，要追问样本地区、时间窗口、指标选择和识别策略的差异。
5. 用 `locate-review-research-gap` 收束到一个更具体的空缺。好的 gap 通常不是“研究较少”这么简单，而是已有研究在机制、情境、方法或解释层面还没有接上。

## 使用边界

这组 Skills 能帮你做三件事：把题目问得更准，把材料放进更合理的结构，把含混的分歧改写成可以继续分析的问题。它们适合用在开题前、读文献中期、写综述提纲前，也适合拿来和导师讨论前先做一轮自查。

它们不能替你读完真实文献，不能保证某个判断在你的学科里一定成立，也不能替你完成引用核验。遇到关键结论，仍然要回到原文，看样本、变量、方法、数据来源和论证限制。AI 给出的 gap 只能作为候选，需要你用真实文献和研究设计去筛掉站不住的版本。

更稳妥的用法是：先让 Skill 给出结构和问题，再把你手头的真实文献逐篇放进去校正。不要把生成内容直接当成论文段落提交，也不要让 AI 编造作者、年份、期刊或 DOI。

从 v0.2.0 起，这组 Skills 遵循 [`references/source-integrity.md`](references/source-integrity.md)：只使用你提供或已核验的文献，每条文献标注状态（用户提供 / 已核验 / 未核验），查不到就写“未查到”，不补全作者、年份、期刊、页码。正式交付的末尾固定有“待核实清单”和“给作者的问题”，生成的段落统一叫“段落草稿（需作者改写并核对来源）”（见[输出契约](references/output-contract.md)）。这些是对 Agent 的流程约束，不是保证；每条引用仍要你自己核对。

## 局限与未验证项

这是早期版本，使用前请先看下面几条。

- **没有质量对照评测。** 已加入[行为用例](evals/scenarios.json)与同步脚本测试，但还没有完成模型行为评测、普通提示词对照或真实稿件质量评估。文中描述的是设计意图，不是效果证明。
- **使用反馈没有系统收集。** 此前的外部使用主要来自公众号传播，没有系统收集反馈。v0.3 的学科指南与追问流程尚未在真实稿件上验证。
- **示例没有真实文献出处。** `examples/` 只是方法演示，里面的论断是示意性的，不来自具体论文，不能引用。
- **安装方式没有逐一实测。** `npx skills add`、让 Agent 代装、手动 clone 三种方式，没有在 Claude Code、Codex、Cursor 里逐一验证；`agents/openai.yaml` 同样没有测过。为避免安装器只复制单个 skill 目录时找不到规则文件，每个 skill 目录下都自带一份 `references/` 副本，核心规则在 Guardrails 里也重复写了一遍。
- **来源核验取决于 Agent 的工具。** 没有联网或检索能力时，Agent 无法核验，只会把来源标为“用户提供”或“未核验”。Crossref、OpenAlex 对中文文献和图书的覆盖不完整。
- **中文数据库仍需有权限的人工检索。** 已补充双语检索词、检索记录、CSSCI 筛选口径与中文题录检查，但没有自动登录 CNKI、万方、维普，也不保证特定引注格式完全合规。
- **学科指南不是完整方法教材。** 已补充概念／历史型问题以及两类学科的评价要点，仍需作者按自己的研究传统和材料修订。
- **输出仍需抽查。** 模型可能漏段、错标来源或忽略追问约束。追问中的单轮回复不输出完整交付模板；正式交付仍保留核实清单和作者问题。

## 联系方式

如果你想交流使用问题、补充案例，或讨论科研 AI 工作流，欢迎通过 [GitHub Issues](https://github.com/xingtaxueshu/literature-review-skills/issues/new/choose) 提交使用反馈，也可以通过下面方式联系：

- 微信号：`xingtacc`
- 邮箱：[xingtaxueshu@outlook.com](mailto:xingtaxueshu@outlook.com)

也可以扫描二维码添加微信：

<img src="assets/wechat-qr.jpg" alt="星塔学术微信二维码" width="260">

关注微信公众号 **“星塔学术”**（扫描二维码，或在微信里搜索），可以看到使用演示与更新说明：

<img src="assets/wechat-official-account-qr.png" alt="星塔学术 · StarTower Academic 微信公众号二维码" width="260">

## 贡献

欢迎改进这些 Skills。比较有价值的贡献包括：更清晰的指令、更贴近学科场景的例子、更好的方法比较模板，以及安装说明中的错误修正。

`skills/*/references/` 是根目录 `references/` 的副本，根目录版本为权威版本。修改后运行 `python3 scripts/sync_references.py` 同步，再运行 `bash scripts/check_references_sync.sh` 校验；检查包括嵌套学科文件和多余副本。

设计参考了 grill-me / grilling 的追问方式、K-Dense literature-review 的检索与核验流程，以及 GPT Researcher 对研究计划、材料和报告的分离。具体借鉴内容与边界见[设计参考](docs/design-references.md)；这些项目不是运行依赖。

提交修改时，请保持语气克制，避免夸大工具作用。这个项目关心的是研究过程是否更清楚，不是把 AI 包装成学术捷径。

## 相关项目

- [xingta-polish-en](https://github.com/xingtaxueshu/xingta-polish-en)：同一团队的开源项目，面向中文人文社科作者的保真优先英文学术润色 Agent Skill。

## 许可

本项目使用 MIT License 发布。完整条款见 `LICENSE`。由 星塔学术 · StarTower Academic（[www.xingta.cc](https://www.xingta.cc)）维护。
