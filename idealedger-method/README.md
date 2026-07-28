# IdeaLedger Method — Agent Skill

**A diagnostic founder coach that runs the IdeaLedger startup validation method inside your AI agent — Claude, Codex, or Antigravity.**

→ [Download `idealedger-method.skill`](./idealedger-method.skill) · [More info](https://www.scalablepod.it/learn/)

---

## What it does

This skill turns Claude into a rigorous startup validation coach. It doesn't cheer you on — it helps you figure out if you're building the wrong thing before it's too late.

It runs the **IdeaLedger method**: 15 diagnostic tools across 5 phases, from clarifying your idea to assessing fundraising readiness. The approach is non-linear: it first diagnoses where *you* actually are, then applies the right tool for your most urgent risk.

**The one question it keeps returning to:**
> *"Am I solving a real problem?"*

---

## Who it's for

Founders and aspiring founders who want to:
- Validate a new startup idea before building
- Pressure-test assumptions in an existing deck or canvas
- Run structured customer discovery
- Size a market (TAM/SAM/SOM)
- Plan an MVP or first 10 customers
- Assess fundraising readiness

---

## The 5 phases

| Phase | Focus |
|---|---|
| 1 | Clarify the idea |
| 2 | Validate the problem |
| 3 | Define customer, market, competition |
| 4 | GTM & first 10 customers |
| 5 | Scale & fundraise |

---

## How it works

- **Starts with Gate 00**: a diagnostic intake before any tool is applied
- **One question at a time**: never a questionnaire dump
- **Saves output locally**: produces markdown files on your machine
- **No account, no API key, no backend**: the method runs locally — your output files stay on your machine. An optional Scalable Intelligence add-on (below) pulls real data, sending only sector/geography filters — never your private materials.

---

## Trigger phrases

The skill activates automatically when you say things like:

- "Voglio validare la mia idea"
- "Stress test the concept"
- "Help me with customer discovery"
- "What's my TAM?"
- "Is my MVP ready?"
- "Should I raise now?"

---

## Install

**Claude (Cowork / Code)**
1. Download [`idealedger-method.skill`](./idealedger-method.skill)
2. Claude Cowork → Settings → Capabilities → Skills → drag & drop

**OpenAI Codex**
`$skill-installer WitzardOtz/scalable-agent-skills/idealedger-method` — or copy this folder into `~/.codex/skills/`

**Google Antigravity**
Copy this folder into your workspace's `.agents/skills/` directory.
---

## Scalable Intelligence add-on (optional — free during launch)

The base skill reasons from general knowledge. The **Scalable Intelligence add-on** (free during launch) connects it to the
Scalable Intelligence database: real comparables and benchmarks from 2,000+ mapped European
startups, used by the market-sizing, competition, GTM, and fundraising tools.

**How to activate — 3 steps:**

1. Get your key at [scalablepod.it/scalable-intelligence](https://www.scalablepod.it/scalable-intelligence/) (enter your email, key issued instantly)
2. Paste this message in your agent chat (Claude, Codex, or Antigravity): `Attiva la chiave Scalable: <your-key>`
3. Done — the skill saves the key on your machine and reuses it in future sessions

Without a key the skill simply proceeds with generic reasoning — nothing breaks.

---

## Part of the IdeaLedger family

| Skill | Use when |
|---|---|
| **idealedger-method** (this one) | You are the founder validating your own idea |
| [`idealedger-evaluator`](../idealedger-evaluator/) | You are evaluating someone else's startup |

---

→ [scalablepod.it/learn](https://www.scalablepod.it/learn/)
