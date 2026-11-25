# Research Interview / Grill Me

Use when explicitly requested (grill me, 追问我, 模拟答辩, 压力测试) or when a decision blocks the current stage. This is an original research-specific adaptation of decision-tree interviewing; see `docs/design-references.md` in the repository for provenance. It requires no external grill-me installation.

## Turn Protocol

1. Inspect supplied notes and sources first. Do not ask for facts already available. Distinguish facts you can verify from choices only the author can make.
2. Track dependencies: review purpose -> question/concepts -> scope/evidence -> method/synthesis -> contribution. Ask a downstream question only when its prerequisite is settled.
3. Default to one high-impact question per turn. State why it matters; offer a tentative recommendation and its tradeoff when useful, without treating it as the answer. Wait for the user before the next dependent question. Never invent the user's answer.
4. Batch up to three independent questions only if the user requests a faster interview. Keep a respectful tone; challenge claims, not competence.
5. After each answer, record the decision, its rationale and remaining uncertainty. Check a counterexample or an alternative explanation before accepting a proposed contribution.
6. Stop when the required decisions for the requested stage are settled, the user asks to stop, or further answers require unavailable evidence. Do not exhaust an entire question bank. If the user asks for no questions, proceed with explicitly provisional assumptions and list blockers.

## First-Turn Examples

- Broad news topic: “你更想研究新闻生产，还是受众如何判断新闻可信度？这会决定我们以新闻机构还是受众为分析单位。”
- Ambiguous 情报 topic: “这里的情报指图书情报／信息科学，还是竞争情报或情报研究？”
- Gap claim: “哪条已读文献最可能反驳你说的‘还没人研究’？我们先检查这条，再决定空白是否成立。”

## Session Brief

At a useful checkpoint, summarize: discipline, review type, anchor question, concepts/units, scope, evidence available, decisions and reasons, unresolved assumptions, next stage. Save to `review-brief.md` only when file output is requested; otherwise keep it in the conversation. Resume from the brief instead of restarting the interview.

## Output Contract

Intermediate interview turns contain the question and short rationale only; do not append full review tables or the fixed closing sections every turn. At handoff to a stage or final draft, apply `output-contract.md` and list unresolved decisions. No references means planning only, even if the user requests an impressive-looking research gap.
