# TalentBridge UI Prototype (Tailwind CSS v4)

Production-ready static frontend prototype for role-based recruitment workflows.

## Tailwind v4 implementation

This UI now uses a **Tailwind v4 CSS-first approach**:

- `@theme` tokens are defined in page-level `style type="text/tailwindcss"` blocks.
- shared semantic utilities (`card`, `btn-primary`, `btn-secondary`) are defined via `@utility`.
- pages are rendered with `@tailwindcss/browser@4` and use v4 tokenized classes (`bg-brand-*`, etc.).

## Included flows

- Auth: login, candidate registration, recruiter sign-up
- Candidate: dashboard, profile, search, job details, chat, offers
- Recruiter: limited/full dashboards, upgrade request, candidate review, chat, offers
- Admin: approvals, monitoring, logs, reports

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
