# Evaluator — Catalogo sticker (max 3 per turno)

Applica l'etichetta onesta, non quella comoda. Aggiorna quando cambia fase, strumento o
qualità dell'evidenza. Distingui sempre dati / ipotesi / giudizi.

**Sessione/scope:** EVALUATOR_MODE · SCREENING_PRELIMINARE · MATERIALE_INSUFFICIENTE ·
NEEDS_DEEPER_DILIGENCE · NOT_INVESTMENT_ADVICE (chiudi sempre i deliverable con questo)

**Evidenza:** EVIDENZA_DEBOLE · EVIDENZA_FORTE

**Problema/cliente/mercato:** PROBLEMA_NON_DIMOSTRATO · PROBLEMA_VALIDATO_PRELIMINARE ·
TARGET_CONFUSO · BEACHHEAD_CHIARO · STATUS_QUO_SOTTOVALUTATO

**GTM/clienti:** GTM_NON_CREDIBILE · PRIMI_CLIENTI_CREDIBILI

**PMF/metriche/economics:** PMF_NON_DIMOSTRATO · METRICHE_DEBOLI · VANITY_METRICS ·
UNIT_ECONOMICS_NON_VERIFICATI

**Capability/use case:** CAPABILITY_FORTE · CAPABILITY_NON_DIMOSTRATA · USE_CASE_DEBOLE ·
USE_CASE_PROMETTENTE · REPOSITIONING_POSSIBILE

**Team:** TEAM_FIT_FORTE · TEAM_FIT_DEBOLE · TEAM_GTM_GAP · TEAM_MARKET_FIT

**Corporate/esito:** OPEN_INNOVATION_FIT · PARTNERSHIP_POTENTIAL · INVESTMENT_READY_PRELIMINARE

## Nuovi sticker (da casi reali) — max 3 per turno
**Discrepanze/narrativa:** DOCUMENT_INCONSISTENCY · NARRATIVE_METRICS_MISMATCH ·
GROWTH_DECELERATION · SATURATION_RISK
**Replicabilità/fisico:** REPLICATION_RISK · MULTI_SITE_EXECUTION_RISK ·
CAPABILITY_PERSONA_DIPENDENTE · CAPABILITY_SISTEMICA_NON_DIMOSTRATA · PROTOCOLIZATION_REQUIRED ·
LOCAL_TRUST_BOTTLENECK
**Governance/valuation:** GOVERNANCE_CLARIFICATION_NEEDED · VALUATION_METHOD_RISK ·
COMPARABLES_SCALE_MISMATCH
**Team/fase:** TEAM_STAGE_MISMATCH · TEAM_COMMITMENT_UNCLEAR
**Disclosure forensics (campagne):** QA_MATERIAL_DISCLOSURE · DILIGENCE_DEFERRED · ADJUSTED_VS_STATUTORY_GAP · DEAL_NATURE_MISREPRESENTED · RAISE_COUNTER_INFLATED
**Valuation-belief / GTM / posizionamento (lente VC):** VALUATION_BELIEF_GAP ·
GTM_FOUNDER_DEPENDENT · POSITIONING_NON_LEGGIBILE

- `VALUATION_BELIEF_GAP` — il numero/valuation presuppone rimossi rischi che le evidenze non
  mostrano ancora rimossi; premio da "magic multiple" non dimostrato. Resta NOT_INVESTMENT_ADVICE.
- `GTM_FOUNDER_DEPENDENT` — la traction dipende dall'eroismo del founder (deal chiusi solo
  perché ci va lui), non da un sistema ripetibile. Distinto da CAPABILITY_PERSONA_DIPENDENTE
  (delivery vs acquisizione). Dettaglio in `vc_lens.md` §4b.
- `POSITIONING_NON_LEGGIBILE` — la startup non è spiegabile in una frase al buyer giusto:
  difficile da capire, comprare e finanziare. Spesso sintomo di USE_CASE_DEBOLE/TARGET_CONFUSO.

- `QA_MATERIAL_DISCLOSURE` — un dato materiale (numero reale, natura di un contratto, rischio)
  emerge SOLO dalla bacheca Q&A pubblica, non dalle voci in evidenza. Sia dato sia segnale di
  trasparenza. Cita la domanda.
- `DILIGENCE_DEFERRED` — a domande dirette su numeri chiave (CAC/LTV, quota di raccolta al debito)
  la risposta e' "ne parliamo in call" senza cifre. Reindirizzamento = segnale.
- `ADJUSTED_VS_STATUTORY_GAP` — cifra in evidenza "adjusted"/gestionale materialmente sopra lo
  statutario/contabile (es. EBITDA 37% adjusted vs ~18% contabile). Riporta entrambi.
- `DEAL_NATURE_MISREPRESENTED` — M&A/partnership/contratto vantato ha forma giuridica reale piu'
  debole (es. affitto di ramo da liquidazione con scadenza e senza riscatto; LOI non vincolante).
- `RAISE_COUNTER_INFLATED` — il contatore di raccolta include SAFE/round pre-esistenti; la raccolta
  crowdfunding reale e' molto piu' bassa.

## Regola metriche (non usare METRICHE_DEBOLI a caso)
- Metriche **assenti** → METRICHE_DEBOLI / MATERIALE_INSUFFICIENTE
- Metriche **presenti ma problematiche** → NARRATIVE_METRICS_MISMATCH / GROWTH_DECELERATION / SATURATION_RISK
- Metriche **buone ma non replicabili** → REPLICATION_RISK / PMF_NON_DIMOSTRATO / UNIT_ECONOMICS_NON_VERIFICATI
- Headline a crescita cumulata pluriennale → controlla SEMPRE la YoY più recente.

## Stage dichiarato vs da evidenze
Ogni memo distingue *Fase dichiarata* (claim della startup) da *Fase da evidenze* (cosa
reggono i dati). Non prendere per buono lo stage dichiarato.
