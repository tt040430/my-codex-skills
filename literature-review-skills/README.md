# Literature Review Skills

A practical five-skill workflow for planning, structuring, and sharpening literature reviews. It helps you refine a question, break the review into modules, compare methods, handle contradictions, and locate a defensible research gap. It does not write the review for you; you still make the academic decisions, verify the literature, and write the final argument.

[中文说明](README.zh-CN.md)

## Who This Is For

- Graduate students preparing a thesis proposal, course paper, or dissertation literature review.
- Researchers who need to turn scattered readings into a clear review structure.
- Supervisors who want a repeatable workflow for guiding students through review design.
- Claude Code and Codex users who want reusable skills for academic thinking tasks.

## The Five-Skill Workflow

| Step | Skill | Use it to |
|---|---|---|
| 1 | `refine-literature-question` | Turn a broad topic into a focused review question that guides search and screening. |
| 2 | `decompose-review-modules` | Break the question into 3-5 review modules with clear boundaries. |
| 3 | `compare-research-methods` | Compare method routes and explain what each method can and cannot answer. |
| 4 | `map-literature-contradictions` | Turn conflicting findings into structured synthesis instead of vague disagreement. |
| 5 | `locate-review-research-gap` | Convert the synthesis into a concrete, defensible research gap or future direction. |

## Disciplines And Drafting

v0.3 keeps the five stages and adds discipline guides loaded only when relevant.

| Discipline | Focus |
| --- | --- |
| Journalism and communication | News production, journalism, platforms, audiences, and credibility; distinguish text-, person-, organization-, and platform-level evidence. |
| Library and information science | Information behavior, retrieval, knowledge organization, bibliometrics, scholarly communication, and services; separate system metrics, task outcomes, and user experience. |
| Other or interdisciplinary topics | Use the general workflow and state when no dedicated guide exists. Combine two guides when needed without forcing one field's assumptions onto another. |

“News” means scholarly journalism/communication reviews, not news digests. Ambiguous uses of “intelligence” require clarification; a security-intelligence guide is not included.

The workflow supports planning and drafting narrative, scoping, systematic, and conceptual/historical reviews: define the question and review type, document searches and screening, extract evidence, synthesize, then draft with traceable claims. It does not claim to complete a systematic review from a prompt alone.

```text
Use literature-review-skills for a journalism and communication review on AI-generated
news disclosure and audience credibility judgments. Grill me one question at a time
to settle concepts, scope, and review type. I have no papers yet; do not invent findings.
```

```text
Use literature-review-skills for an information-science review of AI-assisted scholarly
search. I will provide records, abstracts, and reading notes. Build an evidence table,
distinguish retrieval performance from task success and user experience, then propose
an outline. Do not rank scores from different datasets and metrics directly.
```

Ask for “grill me” to work through one decision at a time, or “proceed without questions” to get a plan with explicit assumptions. Once evidence is available, ask for a draft based on the evidence table. Missing sources remain gaps to verify, not invented answers.

See [usage examples](examples/discipline-workflows.md). To add a field, use the [discipline template](references/disciplines/_template.md), register it in the [routing table](references/discipline-routing.md), and add behavioral cases.

## Install This Skill Set

You do not need to copy commands for each individual skill. This repository includes a root `SKILL.md` as the entry point, plus the five working skills under `skills/`.

### Method 1: One-Line Install (Recommended)

If your environment supports the Agent Skills installer, run:

```bash
npx skills add https://github.com/xingtaxueshu/literature-review-skills
```

Follow the installer's prompts to select your agent and skills, then check that the files are present. Discovery and copying behavior can vary by installer version; see the validation limits below.

### Method 2: Ask Your Agent To Install It

Ask Claude Code, Codex, Cursor, or any compatible coding agent:

```text
Please find and install this skill set: https://github.com/xingtaxueshu/literature-review-skills
```

Ask the agent to inspect its skills directory, download the repository, and verify that it can read the entry point. Completion depends on its file and network permissions.

### Method 3: Manual Clone

For Claude Code users:

```bash
git clone https://github.com/xingtaxueshu/literature-review-skills.git ~/.claude/skills/literature-review-skills
```

For Codex users:

```bash
git clone https://github.com/xingtaxueshu/literature-review-skills.git ~/.agents/skills/literature-review-skills
```

After installation, ask your agent to use the skill set:

```text
Use literature-review-skills to help me turn my broad topic into a literature review question, modules, method comparison, contradiction map, and research gap.
```

The root entry reads the relevant stage instructions. Manual cloning does not necessarily register all five stages as individually callable skills. To invoke one by name, select it in the installer or place its complete folder, including `references/`, in your agent's skills directory:

```text
Use refine-literature-question on this topic: rural e-commerce participation.
```

## Suggested Workflow

Sample prompt:

```text
I am writing a literature review on how rural e-commerce affects household income and local development. Help me turn this broad topic into a review question, modules, method comparison, contradiction map, and research gap.
```

Recommended sequence:

1. Use `refine-literature-question` to convert the topic into a focused question, such as how rural e-commerce changes household income through market access, labor allocation, or platform participation.
2. Use `decompose-review-modules` to create review sections, such as adoption conditions, income mechanisms, platform roles, regional differences, and policy environment.
3. Use `compare-research-methods` to understand what surveys, panel data, interviews, case studies, and mixed methods can and cannot answer.
4. Use `map-literature-contradictions` to compare studies that report positive, weak, uneven, or negative effects and identify why results differ.
5. Use `locate-review-research-gap` to state what the literature explains, where it gets stuck, and what a next study could examine.

## Responsible Use

These skills are a thinking workflow, not a ghostwriter. Use them to clarify questions, organize evidence, test logic, and improve research design. Do not use them to fabricate sources, outsource academic judgment, or submit generated prose without checking it against real literature and your own argument.

Since v0.2.0 the skills follow [`references/source-integrity.md`](references/source-integrity.md): only sources you provided or that have been verified are used, each is tagged (用户提供 / 已核验 / 未核验), and anything not found is written as "未查到" rather than filled in. Final deliverables end with a to-verify list and an author-question section, and generated paragraphs are labelled as drafts for you to rewrite and check ([output contract](references/output-contract.md)). These are process rules for the agent, not a guarantee; check every citation yourself.

## Limitations And Unverified Items

This is an early version. Please read the following before relying on it.

- **No quality evaluation.** The repository includes [behavioral cases](evals/scenarios.json) and reference-sync tests, but no completed model-behavior evaluation, baseline comparison, or real-manuscript quality assessment. Benefits described here are design intent, not measured results.
- **Usage feedback has not been collected systematically.** Earlier external use mainly came through WeChat posts. The v0.3 discipline guides and interview workflow have not been validated on real manuscripts.
- **The example has no real sources.** `examples/` is a method demonstration; its claims are illustrative, not drawn from specific papers, and must not be cited.
- **Install methods are not individually tested.** We have not verified the `npx skills add` command, agent-assisted install, or manual clone in each environment (Claude Code, Codex, Cursor). The `agents/openai.yaml` files are also untested. So that a skill still works if an installer copies only one skill folder, each skill folder bundles its own copy of `references/`, and the core rules are also repeated in each skill's Guardrails.
- **Source verification depends on the agent's tools.** Without network or search access, the agent cannot verify anything and will leave sources as 用户提供 or 未核验. Crossref and OpenAlex coverage of Chinese-language and book literature is incomplete.
- **Chinese databases still require authorized manual access.** Bilingual search planning, search logs, CSSCI filtering scope, and record checks are included, not automated database login or guaranteed citation-style compliance.
- **Discipline guides are not comprehensive methods textbooks.** Conceptual/historical questions and field-specific appraisal checks are included, but need adjustment to the research tradition and corpus.
- **Outputs need spot-checking.** Models may skip sections, mislabel sources, or ignore interview constraints. Intermediate interview turns are exempt from the full delivery template; final deliverables retain the verification and author-question sections.

## Contact

Questions, examples, or collaboration ideas are welcome. Please use [GitHub Issues](https://github.com/xingtaxueshu/literature-review-skills/issues/new/choose) for usage feedback.

- WeChat: `xingtacc`
- Email: [xingtaxueshu@outlook.com](mailto:xingtaxueshu@outlook.com)

Scan the QR code to add the WeChat account:

<img src="assets/wechat-qr.jpg" alt="WeChat QR code for 星塔学术" width="260">

Follow the WeChat Official Account **星塔学术** (scan the QR code, or search for it in WeChat) for walkthroughs and updates:

<img src="assets/wechat-official-account-qr.png" alt="WeChat Official Account QR code for 星塔学术 · StarTower Academic" width="260">

## Contributing

Contributions are welcome if they make the workflow clearer, more practical, or easier to use. Good contributions include sharper skill instructions, better examples, field-specific templates, and corrections to installation notes. Keep examples realistic and avoid inflated claims.

`skills/*/references/` are copies of the authoritative root `references/`. After editing, run `python3 scripts/sync_references.py`, then `bash scripts/check_references_sync.sh`. The check includes nested discipline files and unexpected copies.

Design references include grill-me / grilling for interviewing, K-Dense literature-review for search and verification, and GPT Researcher for separating plans, source material, and reports. See [design references](docs/design-references.md) for scope and attribution. None is a runtime dependency.

## Related Projects

- [xingta-polish-en](https://github.com/xingtaxueshu/xingta-polish-en): a fidelity-first agent skill for polishing the English of academic paragraphs, from the same team (星塔学术 · StarTower Academic).

## License

This project is released under the MIT License. See `LICENSE` for the full text. Maintained by 星塔学术 · StarTower Academic ([www.xingta.cc](https://www.xingta.cc)).
