# IdeaLedger Evaluator — Agent Skill

**A structured risk-diagnosis skill for angels, scouts, and accelerators evaluating early-stage startups.**

→ [Download `idealedger-evaluator.skill`](./idealedger-evaluator.skill)

---

## What it does

This skill turns Claude into a sharp early-stage evaluator — think of an ex open-innovation lead or angel who has screened hundreds of decks. It helps you assess a third-party startup with the IdeaLedger method and produces a structured **risk diagnosis**, not a verdict.

**The question it keeps returning to:**
> *"Is this startup applying the right team, capability, and capital to the right problem and use case?"*

Every output ends with a clear disclaimer: *This is not investment advice. It is an early-stage risk diagnosis based on available information.*

---

## Who it's for

- Angel investors screening inbound deals
- VC scouts doing first-pass evaluation
- Accelerator and incubator program managers
- Corporate open-innovation leads
- Advisors preparing for a first founder call

---

## What you get

A structured **Risk Diagnosis** covering:

- Problem validation: is the pain real and specific?
- Team/capability fit: does this team have the right to win?
- Market size and timing
- Competitive landscape red flags
- Key questions to ask the founder
- A clear signal: *worth a call / not yet / pass*

Output is saved as a local markdown file; your inputs stay on your machine. (The optional Scalable Intelligence add-on sends only sector/geography filters to the API — never your deck or the startup's private materials.)

---

## How to use it

Paste or describe:
- A pitch deck (text or summary)
- A one-pager or executive summary
- A founder intro email
- Notes from a first call

The skill asks clarifying questions one at a time, then produces the diagnosis.

---

## Trigger phrases

- "Valuta questa startup"
- "Screening del pitch deck"
- "Is this worth a call?"
- "Red flags on this deal?"
- "Prepare my questions for the founder meeting"
- "Accelerator application review"

---

## Install

**Claude (Cowork / Code)**
1. Download [`idealedger-evaluator.skill`](./idealedger-evaluator.skill)
2. Claude Cowork → Settings → Capabilities → Skills → drag & drop

**OpenAI Codex**
`$skill-installer WitzardOtz/scalable-agent-skills/idealedger-evaluator` — or copy this folder into `~/.codex/skills/`

**Google Antigravity**
Copy this folder into your workspace's `.agents/skills/` directory.
---

## Scalable Intelligence add-on (optional — free during launch)

The base skill is complete and free. The **Scalable Intelligence add-on** (also free during launch) connects it to the Scalable
Intelligence database: real comparables and benchmarks from 2,000+ mapped European startups,
used by the PMF, market-sizing, competition, GTM, and replication-risk tools.

**How to activate — 3 steps:**

1. Get your key at [scalablepod.it/scalable-intelligence](https://www.scalablepod.it/scalable-intelligence/) (enter your email, key issued instantly)
2. Paste this message in your agent chat (Claude, Codex, or Antigravity): `Attiva la chiave Scalable: <your-key>`
3. Done — the skill saves the key on your machine and reuses it in future sessions

Without a key the skill simply proceeds with generic reasoning — nothing breaks.

---

## Part of the IdeaLedger family

| Skill | Use when |
|---|---|
| [`idealedger-method`](../idealedger-method/) | You are the founder validating your own idea |
| **idealedger-evaluator** (this one) | You are evaluating someone else's startup |

---

→ [scalablepod.it/learn](https://www.scalablepod.it/learn/)
