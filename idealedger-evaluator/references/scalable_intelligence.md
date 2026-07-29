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
2. **Incolla la chiave in chat** → salvala TU, subito, SENZA mostrarla. Usa l'helper `save-key`
   di `api_client.py`: scrive il file con permessi `600` (dove supportato) e non stampa mai la
   chiave. Passa la chiave via stdin (o `SCALABLE_API_KEY`), MAI come argomento da riga di comando
   (finirebbe nella cronologia/argv):

   - **Home persistente** (Codex CLI, Antigravity, shell locale) — posizione preferita:
     ```bash
     printf %s "<CHIAVE>" | python assets/scalable_intel/api_client.py save-key --scope home
     ```
     Se puoi, esporta anche `SCALABLE_API_KEY` per la sessione corrente.

   - **Sandbox / home non persistente** (es. Claude Cowork) — fallback nel workspace:
     ```bash
     printf %s "<CHIAVE>" | python assets/scalable_intel/api_client.py save-key --scope workspace --workspace <cartella-dossier>
     ```
     `save-key` salva `.scalable_api_key` nel workspace e aggiorna in modo IDEMPOTENTE il
     `.gitignore` di quella cartella (aggiunge solo le righe mancanti `.scalable_api_key` e
     `api_key.txt`, senza mai sovrascrivere regole esistenti, senza pattern allargati).

   Ordine di lettura di `api_client.py`: `SCALABLE_API_KEY` → `~/.scalable_api_key` →
   `.scalable_api_key` nel workspace corrente. Se la home non persiste ma la copia nel workspace
   esiste, l'API la legge comunque dal workspace: nessuna azione manuale a inizio sessione.
3. **Verifica subito** con una chiamata reale (es. `bench --sub payments`): se `available: true`
   conferma "chiave salvata e verificata ✓" (senza mostrarla, nemmeno in parte); altrimenti
   riporta `reason` all'utente.
4. **Riservatezza**: non mostrare mai la chiave — né in chat, né nei file di output, nei report,
   nei log, negli URL o negli eventi analytics. Nei test usa solo valori fittizi (es. `test_key_not_real`).

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
