# TalentBridge UI Prototype (Tailwind CSS v4)

This repository contains a production-oriented static HTML prototype for a multi-role recruitment platform.

## Scope delivered

- Authentication: candidate registration, recruiter sign-up, login with role-aware access states
- Candidate: profile setup/searchable toggle, dashboard, job search filters, job details, chat, offers/interview responses
- Recruiter: limited account dashboard, upgrade request workflow, full dashboard, candidate review, messaging, offer tracking
- Admin: recruiter approval, monitoring, communication logs, reporting with export actions

## Tech

- Plain HTML + Tailwind CSS v4 browser build (`@tailwindcss/browser`)
- Lightweight shared stylesheet for baseline behavior and accessibility helpers

## Run locally

```bash
cd ui
python -m http.server 4173
```

Open: `http://localhost:4173`
