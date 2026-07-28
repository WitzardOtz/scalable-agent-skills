# Scalable Intelligence — comparabili & benchmark reali (add-on API, modalità EVALUATOR)

Add-on **opzionale, gratuito in fase di lancio**: catalogo reale di oltre 2.000 startup europee (dataset Scalable)
per sanity-check esterno su sizing, concorrenza, benchmark di round e replicabilità.

> **Graceful degradation — leggi prima.** È un add-on. Se la API key non è configurata o
> l'API non risponde, **non bloccarti**: prosegui la diagnosi con ragionamento generico e
> segnalalo ("benchmark Scalable non disponibili senza l'add-on"). La skill resta pienamente
> utilizzabile senza chiave.

## Attivazione della chiave — cosa fare quando l'utente vuole il premium

Se l'utente chiede del premium, di "attivare la chiave", o incolla una chiave in chat:

1. **Non ha ancora la chiave** → indirizzalo a https://www.scalablepod.it/scalable-intelligence/
   (pagina "Attiva la chiave"): inserisce l'email e riceve subito la chiave.
2. **Incolla la chiave in chat** → salvala TU, subito, secondo l'ambiente in cui giri:
   - Se puoi impostare variabili d'ambiente persistenti (Codex CLI, Antigravity, shell
     locale dell'utente): imposta `SCALABLE_API_KEY`.
   - In ogni caso salva anche `~/.scalable_api_key` (solo la stringa della chiave) — è il
     fallback che `api_client.py` legge ovunque.
   - Se l'ambiente è sandboxed e la home non persiste tra sessioni (es. Claude Cowork):
     salva una copia in `.scalable_api_key` nella cartella di lavoro/dossier dell'utente
     e, a inizio sessione, se `~/.scalable_api_key` manca ma la copia nel workspace esiste,
     ripristinala senza chiedere nulla.
3. **Verifica subito** con una chiamata reale (es. `bench --sub payments`): se
   `available: true` conferma "chiave attiva ✓"; altrimenti riporta `reason` all'utente.
4. **Riservatezza**: non ripetere mai la chiave in chat, nei file di output o nei report.

## Come si consulta

Helper `assets/scalable_intel/api_client.py`:

```bash
python assets/scalable_intel/api_client.py comps --sub payments --country IT --limit 10
python assets/scalable_intel/api_client.py comps --macro fintech --stage "Series A"
python assets/scalable_intel/api_client.py bench --sub payments
python assets/scalable_intel/api_client.py find <slug-o-nome>
```

Controlla sempre il campo `available`: se `false`, leggi `reason` e procedi senza comparabili
(coerente con `MATERIALE_INSUFFICIENTE`: dichiara il gap, non inventare). Slug validi in
`assets/scalable_intel/taxonomy_quick_ref.md`.

## Privacy

Il client invia all'API **solo filtri di tassonomia** (settore, paese, stadio), mai il
materiale riservato della startup valutata.

## Quando consultarlo (strumento per strumento)

- **4 — Customer/Market/Competition.** `comps` per competitor reali; "no competitor" + molti
  risultati → `STATUS_QUO_SOTTOVALUTATO`. Confronta il moat dichiarato coi comparabili.
- **6 — TAM/SAM/SOM & Metrics.** `bench --sub` per sgonfiare un TAM top-down (operatori noti ≠ domanda).
- **7 — Capability ↔ use-case fit.** Quali use case sono già presidiati con la stessa capability.
- **8b — Replication risk.** Molti comparabili con round chiusi → rischio replicabilità più alto.
- **9 — Pitch & Fundraising.** `bench`/`comps --stage` per confrontare la richiesta coi
  comparabili; segnala lo scostamento, non dire se la valuation è "giusta".

## Citazione e limiti

1. Etichetta: "comparabili/benchmark dal dataset Scalable".
2. Copertura non uniforme (macro≈100%, subsector≈50%, funding≈20%, competitor≈6%); bias
   geografico (~58% IT). Dato mancante = gap esplicito.
3. Non è un verdetto: informa il risk memo, non lo sostituisce. Chiudi sempre con: *This is
   not investment advice. It is an early-stage risk diagnosis based on the available
   information.* (`NOT_INVESTMENT_ADVICE`)
