# Discipline Routing

Read this index at the beginning of a review or a standalone stage. Resolve links relative to this file. Load only the profiles relevant to the user's question.

| ID | User terms / scope | Profile |
|---|---|---|
| journalism-communication | 新闻学、新闻传播、传播学、媒介研究、journalism、communication studies | [Journalism and communication](disciplines/journalism-communication.md) |
| information-science | 情报学、图书情报、信息科学、信息行为、知识组织、文献计量、information science、LIS | [Library and information science](disciplines/information-science.md) |

These profiles are research-design aids, not authoritative field surveys or lists of established findings. They do not supply citations for empirical claims.

## Ambiguity and Overlap

- For 新闻类, use journalism/communication when the user wants scholarly literature synthesis. A news digest or article-writing request is outside this workflow.
- For 情报 alone, ask whether they mean library/information science, competitive/scientific intelligence, or intelligence studies. Do not silently translate every occurrence as national-security intelligence.
- For interdisciplinary work, identify a primary question and load at most two relevant profiles. Keep constructs and units of analysis separate; do not treat communication credibility and retrieval relevance as synonyms.
- For another discipline, use the generic workflow and label the profile as not yet available. Ask for the field's concepts and evidence conventions when needed; do not quietly reuse a news or LIS template.
- State the chosen profile and review type in the session brief. A user correction overrides keyword routing.

## Adding A Discipline

Create `references/disciplines/<stable-kebab-case-id>.md` using [the template](disciplines/_template.md), add a row to this index, and include a realistic example plus an ambiguous or unsupported case in `evals/scenarios.json`. Run `python3 scripts/sync_references.py`, then `bash scripts/check_references_sync.sh`. This distributes nested profiles to independently installed stage skills.

Keep the five core stages unchanged unless the new discipline needs a genuinely different process. Profiles should customize constructs, evidence, search and appraisal, not multiply near-identical skills.
