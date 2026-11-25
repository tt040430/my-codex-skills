# Library and Information Science / 图书情报与信息科学

## Scope and Disambiguation

Cover information behavior, retrieval, knowledge organization, bibliometrics/scientometrics, scholarly communication, information services and research on scientific/competitive intelligence. Clarify 情报 when its meaning is uncertain; intelligence studies is not automatically this profile.

## Question and Concepts

Choose the unit: user, task, query, document, relevance judgment, knowledge entity, citation, institution or service. Separate retrieval effectiveness, user satisfaction, task success, information quality, trust and adoption. A ranking improvement does not by itself demonstrate improved learning or decision quality.

Possible lenses include information needs, information seeking, relevance, knowledge organization and scholarly communication. Use them as candidate organizing concepts, not as verified claims about named theories. Support conceptual and historical reviews as well as empirical studies.

## Search Plan

- Candidate sources: [Information Science & Technology Abstracts](https://www.ebsco.com/products/research-databases/information-science-technology-abstracts), LISTA, multidisciplinary indexes, CNKI/万方/维普, and ACM/IEEE collections for retrieval or HCI questions. Verify actual coverage and access; no database count guarantees completeness.
- Term families: 信息行为 / information behavior or information seeking; 知识组织 / knowledge organization; 相关性 / relevance; 文献计量 / bibliometrics; 科学计量 / scientometrics; 学术交流 / scholarly communication; 检索增强生成 / retrieval-augmented generation.
- Illustrative seed, not an executed search: `("generative AI" OR "conversational search" OR "retrieval augmented generation") AND ("information seeking" OR "information retrieval") AND (relevance OR "task success" OR trust)`. Adapt syntax per database and test recall with known relevant papers.
- Keep benchmark datasets, software docs, policy documents and peer-reviewed studies distinguishable. Link preprints to published reports rather than counting them as independent studies.

## Extraction and Appraisal

Add task, corpus/dataset version, query population, relevance definition, baseline, metric, evaluation split and user population to the common evidence table.

| Design | Inspect | Inference boundary |
|---|---|---|
| Offline retrieval evaluation | Corpus, query set, relevance judgments, splits/leakage, baselines, nDCG/MAP/recall definitions | Scores from different collections or cutoffs are not directly comparable |
| User study | Recruitment, tasks, counterbalancing, measures, time and learning effects | Satisfaction is not retrieval accuracy or task success |
| Bibliometrics/knowledge mapping | Database/date coverage, query, deduplication, author disambiguation, thresholds and normalization | Cluster size/citation count does not prove quality, consensus or a research gap |
| Knowledge organization | Category definitions, annotation procedure, agreement and maintenance | Ontology coverage does not alone prove downstream utility |
| Interviews/qualitative information behavior | Context, sampling, analytical trace and counterexamples | Accounts support interpretation, not population prevalence |
| Scientific/competitive intelligence study | Source provenance, update lag, validation target and analyst assumptions | More retrieved information does not establish better decisions |

## Synthesis and Gap

Possible modules: needs and tasks; system/retrieval mechanisms; evaluation evidence; use and governance. Separate system-centered and user-centered findings before integrating them. For bibliometric reviews, use maps to guide reading and follow with content-based synthesis.

Challenge a proposed gap with: is the missing link a task-specific need, a dataset limitation, a construct mismatch, or simply a part of the literature not searched yet?

## Interview Prompts

- 你的研究对象是用户的信息行为，还是检索系统的性能？
- 你说的“效果更好”指相关性、任务完成，还是满意度？
- 两篇论文使用同一数据集、相关性标准和指标截断值吗？
- 如果已有一篇论文填补了这个“空白”，你的研究价值还剩什么？

## Planning Example (No Literature Claims)

Topic: generative AI and information seeking. Candidate anchor: how do conversational search interfaces support source evaluation in academic information-seeking tasks? Clarify user group and task, distinguish source checking from satisfaction, and compare offline scores separately from user evidence. Do not infer a field-wide gap without a documented search.
