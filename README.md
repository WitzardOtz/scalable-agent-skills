# Scalable Agent Skills

**Agent skills for Startup People.**

Three production-ready skills for founders, investors, and operators — written once in
the standard `SKILL.md` format, running on **Claude** (Cowork / Code), **OpenAI Codex**,
and **Google Antigravity** without modification.

Made by **Witzard of Otz** — host of [Scalable](https://www.scalablepod.it), the Italian
podcast on European startup ecosystems.

---

## Skills in this repo

| Skill | Who it's for | What it does |
| --- | --- | --- |
| [`idealedger-method`](./idealedger-method) | Founders | Validates startup ideas with the IdeaLedger 5-phase method |
| [`idealedger-evaluator`](./idealedger-evaluator) | Angels, scouts, accelerators | Produces a structured risk diagnosis on third-party startups |
| [`career-headhunter`](./career-headhunter) | Job seekers | Builds a candidate brief, scores opportunities, prepares applications |

Each skill folder contains the **full source** (`SKILL.md`, `references/`, `scripts/`,
`assets/`) plus a packaged `.skill` file for Claude.

---

## How to install

**Claude (Cowork / Code)** — download the `.skill` file from the skill's folder, then
Settings → Capabilities → Skills → drag & drop.

**OpenAI Codex** — `$skill-installer WitzardOtz/scalable-agent-skills/<skill-name>`,
or copy the skill folder into `~/.codex/skills/`. Check with `/skills`.

**Google Antigravity** — copy the skill folder into your workspace's `.agents/skills/`
directory. The agent picks it up automatically.

The skill activates automatically when your message matches its triggers, in your
language (Italian and English fully supported).

---

## The IdeaLedger method

The two startup skills are built on **IdeaLedger**, a validation method developed to answer one recurring question:

> *"Is this startup solving a real problem — for real people — with the right team and capability?"*

The method runs across 5 phases and 15 diagnostic tools, from idea clarification to fundraising readiness. The skills are the **light, local version**: no account, no backend, all output files stay on your machine. An optional premium add-on (below) connects the two IdeaLedger skills to real startup data.

More at [scalablepod.it/learn](https://www.scalablepod.it/learn/)

---

## Free vs Premium (IdeaLedger skills only)

| | Free (this repo) | Premium add-on |
|---|---|---|
| Full method, all tools | ✅ | ✅ |
| Local markdown dossier | ✅ | ✅ |
| Real comparables & benchmarks (2,000+ EU startups) | — | ✅ |

**Premium in 3 steps:** get a key at [scalablepod.it/scalable-intelligence](https://www.scalablepod.it/scalable-intelligence/) → paste `Attiva la chiave Scalable: <your-key>` in a Claude chat → the skill saves and reuses it automatically. No key? Everything still works with generic reasoning.

---

## About

I built these while running Scalable — a media project covering European startup ecosystems through a weekly podcast, a curated startup database, and editorial content.

→ [scalablepod.it](https://www.scalablepod.it)

---

## License

MIT — use freely, attribution appreciated.
