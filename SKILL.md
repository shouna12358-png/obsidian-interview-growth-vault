---
name: obsidian-interview-growth-vault
description: Create, initialize, upgrade, and operate a privacy-safe AI + Obsidian interview-growth vault. Use when a user wants a complete Obsidian job-search template, imports a resume/JD/interview screenshot, builds a true-question bank or STAR story bank, generates linked 2–3 minute answers, predicts interview questions, records prediction hits, or shares the workflow with others.
---

# Obsidian Interview Growth Vault

Build and maintain an Obsidian vault that grows from resumes, JDs, external interview reports, daily practice, and the user's own interviews.

## Initialize a vault

1. Ask for the target folder if it is not explicit. Accept a new folder or an existing Obsidian vault.
2. For a new/empty folder, run:

   `python scripts/install_vault.py --target "<absolute-path>" --mode create`

3. For an existing vault, first run with `--dry-run`, report the planned changes, then run:

   `python scripts/install_vault.py --target "<absolute-path>" --mode upgrade`

4. Never use `--mode create` on a non-empty folder. Never delete or overwrite personal notes.
5. After installation, direct the user to `<target>/00 首页.md` and `<target>/99 系统/第一次使用.md`.

The installer copies `assets/vault-template`. Upgrade mode overwrites only managed files in `99 模板` and `99 系统`, backing up changed versions under `_系统备份/<timestamp>` first. All other existing files are skipped.

## Operate the vault

Before handling a JD, resume, interview screenshot, question, answer, or review task:

1. Read `<vault>/99 系统/AI 工作台.md` completely.
2. Read only the relevant template in `<vault>/99 模板`.
3. Follow the data rules in `<vault>/99 系统/字段规范.md` and `references/vault-spec.md`.
4. Search before creating. Reuse semantic duplicates and append provenance.

### Route requests

- Resume import or fact extraction → Flow A.
- New JD, match analysis, tailored resume, or Top 20 prediction → Flow B.
- User's real interview and prediction calibration → Flow C.
- Daily mock interview → Flow D.
- Weekly self-growth maintenance → Flow E.
- Create or complete one answer → Flow F.
- Xiaohongshu, Nowcoder, Maimai, or other screenshot true questions → Flow G.

## Non-negotiable rules

- Preserve the original resume, JD, screenshot, interview wording, and source URL.
- Separate fact, user-confirmed claim, external report, and model inference.
- Never fabricate experience, numbers, tools, employers, interview questions, or outcomes.
- Behavioral and resume answers may use only confirmed resume facts and real story-bank material.
- Store questions and answers separately; make question text link directly to its answer.
- Generate a natural 2–3 minute complete answer when facts are sufficient. Otherwise mark `needs-input` and ask one highest-value question.
- Treat external-platform questions as `external-real`, not as an official company question bank.
- Treat the user's own interview questions as `self-real`; use them to record prediction hits and future priority.
- In job pages, show predicted questions as three-row vertical blocks: question, prediction basis, usable real story. Do not display a redundant competency column.
- Never change the manual application checkboxes in `01 岗位库/_投递清单.md`.
- Never put personal material into this distributable skill directory.

## Share or publish

Read `references/vault-spec.md` before changing the bundled template. To share, publish the entire skill folder or the generated zip. Recipients install the skill from the repository and invoke `$obsidian-interview-growth-vault` with a target folder.

