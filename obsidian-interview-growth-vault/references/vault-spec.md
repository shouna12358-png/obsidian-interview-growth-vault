# Vault specification

## Contents

1. Folder contract
2. Evidence levels
3. Managed upgrade scope
4. Publishing checklist

## Folder contract

| Folder | Responsibility |
|---|---|
| `00 临时收集表` | Unprocessed text, URLs, and notes |
| `01 岗位库` | JD archive, concise analysis, application checklist |
| `02 能力库` | Reusable competency definitions and evidence |
| `03 面试题库` | Questions, provenance, practice state, true-question sources |
| `04 答案库/题目答案` | Independent answer pages |
| `04 答案库/故事库` | Confirmed STAR/CAR story bank |
| `05 面试记录` | Original real and mock interview records |
| `06 每日训练` | Daily practice and review notes |
| `07 简历库` | Original files, fact base, master resume, tailored versions |
| `98 附件` | Images and source attachments |
| `99 模板` | Managed note templates |
| `99 系统` | Managed instructions and schemas |

Keep detailed JD-to-resume evidence mapping in the tailored resume, not the job page. Keep the job page concise.

## Evidence levels

Use this prediction order:

1. User's own interview at the same company and role.
2. External reported questions for the same company and role.
3. User/external questions from the same role family.
4. JD Must Have, Hidden Signals, resume risks, and industry patterns.

External reports are not official company questions. Preserve platform and source records even when the main index hides the platform column.

## Managed upgrade scope

The installer may replace only files below `99 模板` and `99 系统`, after backup. It may add missing files anywhere in the template. It must skip every existing personal note outside managed folders.

## Publishing checklist

- Search the skill folder for names, phones, email addresses, resume facts, company-specific private notes, and local absolute paths.
- Ensure `assets/vault-template` contains no JD, screenshot, true question, personal answer, or application status.
- Run `scripts/install_vault.py` in create and upgrade test modes.
- Run Skill Creator `quick_validate.py`.
- Publish the complete skill directory or its zip; `SKILL.md` is the GitHub landing document.

