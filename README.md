# TalentBridge UI Prototype (Tailwind CSS v4)

Production-ready static frontend prototype for role-based recruitment workflows.

## Conflict resolution status

This branch has been reconciled with `main` and all listed conflicted UI files were normalized to a consistent template system and refreshed visual style.

## Included flows

- Auth: login, candidate registration, recruiter sign-up
- Candidate: dashboard, profile, search, job details, chat
- Recruiter: limited/full dashboards, upgrade request, candidate review, chat
- Admin: approvals, monitoring, reports

## Run locally

```bash
cd ui
python -m http.server 4173
```

Open: `http://localhost:4173`

## Quality check

```bash
python scripts/validate_ui_links.py
```
