# Special evaluation rules + quality checklist

Leggi questo file prima di produrre qualunque deliverable (memo, flags, readiness, delta).
Le regole vengono da valutazioni reali (un caso deeptech e un caso retail/wellness) e
servono a leggere materiale disordinato e marketing-oriented.

## Declared stage vs evidence-based stage
Mai prendere per buona la fase dichiarata — le campagne la gonfiano. Ogni memo riporta
entrambe: *Fase dichiarata* (es. "Go To Market", "scaling multi-site") e *Fase da evidenze*
(es. "prototipazione avanzata / primi PoC non dimostrati", "singolo centro validato
localmente, replicabilità non dimostrata"). Il gap tra le due è spesso la vera storia.

## Metrics present ≠ metrics weak
Non timbrare `METRICHE_DEBOLI` per riflesso quando i dati esistono. Tre casi:
(a) metriche *assenti* → `METRICHE_DEBOLI` / `MATERIALE_INSUFFICIENTE`;
(b) metriche *presenti ma in tensione con la narrativa* → `NARRATIVE_METRICS_MISMATCH`,
`GROWTH_DECELERATION`, `SATURATION_RISK`;
(c) metriche *buone ma non ancora replicabili* → `REPLICATION_RISK`, `PMF_NON_DIMOSTRATO`,
`UNIT_ECONOMICS_NON_VERIFICATI`.
Se un headline usa crescita cumulata pluriennale ("+317% dal 2022 al 2025"), controlla
sempre l'ultimo YoY: se l'ultimo anno è +11%, segnala la decelerazione. Il materiale più
ricco non è automaticamente il più solido.

## Document inconsistency
Se due materiali ufficiali della stessa startup/campagna si contraddicono (ruoli team,
full-time vs advisor, cap table, metriche, ricavi, clienti, valuation, use of funds,
mercato, competitor, governance, struttura del deal): (1) dichiaralo come **fatto**, non
opinione; (2) `DOCUMENT_INCONSISTENCY`; (3) mettilo nelle top 3 domande di diligence;
(4) NON risolverlo per inferenza; (5) chiedi chiarimento diretto. Formula: *"Questa è una
discrepanza fattuale tra due materiali ufficiali, non un giudizio del valutatore. Va
chiarita prima di qualunque decisione."*

## Evidence Update / Delta Memo
Nuovo materiale dopo un primo memo → NON riscrivere da zero. Produci prima un
`## Evidence Update / Delta Memo` (formato in `references/formats.md`): cosa c'è di nuovo ·
cosa cambia rispetto al memo precedente (gap chiusi, rischi ridotti/rafforzati, rischi
nuovi) · cambio di verdetto · nuove domande prioritarie · cosa resta incerto. Log in
`13_evidence_update_log.md`. Se il nuovo doc aggiunge dati contraddittori o più rischiosi,
dillo chiaramente. Formula: *"Il nuovo materiale non migliora o peggiora automaticamente il
quadro: sposta la valutazione da 'mancano dati' a 'i dati ci sono e sollevano domande
precise'."*

## Valuation / comparables
Se c'è una valuation pre-money da comparabili/multipli: valuta scala, settore, maturità e
revenue/EBITDA dei comparabili, lo sconto applicato, e se i multipli sono aspirazionali o
davvero comparabili. Comparabili su scala radicalmente diversa →
`COMPARABLES_SCALE_MISMATCH` + `VALUATION_METHOD_RISK`. Formula: *"Non significa che la
valutazione sia sbagliata, ma la metodologia va chiarita: i comparabili operano su scale e
maturità radicalmente diverse."*

## Crowdfunding caveat
Fonte = campagna equity crowdfunding → materiale marketing-oriented, cifre possibilmente
gestionali/non certificate. Verifica KIIS/KIID, statuto, bilanci, cap table, share terms e
diritti degli investitori; liquidation preference, SPV, azioni A/B, governance, exit
rights. Non confondere fondi raccolti/grant/incentivi fiscali con validazione di mercato,
né narrativa di campagna con trazione commerciale. Output: **Crowdfunding Material
Caveat** + **Missing Legal/Financial Documents** + **Governance Questions**
(`GOVERNANCE_CLARIFICATION_NEEDED` quando rilevante).

## Bacheca Q&A pubblica (leggila SEMPRE)
Se la campagna ha una bacheca domande/risposte pubblica, **leggila per intero prima del memo**:
spesso l'informazione decisiva emerge solo perche' un altro investitore l'ha chiesta, non dalle
voci in evidenza. Riconcilia ogni risposta col resto del materiale. Quando un dato materiale (un
numero reale, la natura di un contratto, un rischio) compare **solo** nella Q&A e non nei documenti
ufficiali, dichiaralo e taggalo `QA_MATERIAL_DISCLOSURE`: e' sia un dato sia un segnale sulla
trasparenza spontanea. Cita la domanda. Osserva anche il *comportamento di risposta*: rispondere
nel merito con numeri e' positivo; reindirizzare a una call senza dare cifre e' `DILIGENCE_DEFERRED`.

## Disclosure forensics — numeri "adjusted", natura dei deal, contatore raccolta
Tre controlli obbligatori, perche' e' dove le "highlight" divergono dai fatti:
- **Adjusted vs statutario.** Se una cifra in evidenza e' "adjusted"/gestionale (es. "EBITDA 860k€,
  37%"), cerca il valore **statutario/contabile** (es. ~420k€, ~18%) in bilanci/KIIS e **riporta
  entrambi**; il gap va nelle domande di diligence. Tag `ADJUSTED_VS_STATUTORY_GAP`.
- **Natura reale dei deal vantati.** Verifica la sostanza legale di M&A / "acquisizioni" /
  partnership / contratti: un'"acquisizione" puo' essere un affitto di ramo da liquidazione
  giudiziale (con scadenza, senza opzione di riscatto), una "partnership" una LOI non vincolante.
  Riporta la forma giuridica reale, non l'etichetta di marketing. Tag `DEAL_NATURE_MISREPRESENTED`
  (+ `DOCUMENT_INCONSISTENCY` se contraddice altro materiale).
- **Contatore raccolta.** Separa la **raccolta crowdfunding reale** da SAFE/round pre-esistenti
  conteggiati nella barra (es. contatore al 96% che include 505k€ di SAFE → raccolta reale ~23k€).
  Tag `RAISE_COUNTER_INFLATED`.

## Objective framing
L'obiettivo è *supportare un assessment preliminare pre-investimento* — rischi, evidenze
mancanti, domande di diligence — mai decidere se investire. Non dire investi / non
investire / "decidere se investire". Dì: supportare un assessment preliminare, preparare
una call, identificare rischi, produrre domande di diligence, valutare readiness.

## Quality checklist (prima di consegnare qualunque memo)
Verifica di aver: distinto *fase dichiarata* vs *fase da evidenze* · separato dati/ipotesi/
giudizi · separato capability tecnica da validazione commerciale · verificato il fit
capability→use case · valutato team-capability / team-market / team-GTM / team-stage fit ·
segnalato le incoerenze documentali · verificato che le metriche supportino la narrativa
(incluso ultimo YoY) · considerato il replication risk per modelli physical/retail/service ·
rivisto metodologia comparabili/valuation se presente · verificato se la valuation
presuppone rischio già rimosso che le evidenze non supportano (`VALUATION_BELIEF_GAP`) ·
verificato se il GTM è un sistema ripetibile o founder-heroics (`GTM_FOUNDER_DEPENDENT`) ·
verificato se il positioning è leggibile in una frase (`POSITIONING_NON_LEGGIBILE`) ·
letto la **bacheca Q&A** pubblica e segnalato i dati emersi solo da li' · riconciliato cifre **adjusted vs statutarie** · verificato la **natura legale reale** dei deal vantati · separato la **raccolta reale** da SAFE/round nel contatore · evitato investment advice · prodotto domande di diligence concrete · esplicitato "what
would change my mind".
