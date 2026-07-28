# Scalable Intelligence — comparabili & benchmark reali (add-on API, modalità FOUNDER)

Add-on **opzionale, gratuito in fase di lancio**: dà accesso a un catalogo reale di oltre 2.000 startup europee
(dataset Scalable) per ancorare le risposte a comparabili e benchmark reali.

> **Graceful degradation — leggi prima di tutto.** Questo è un add-on. Se la API key non è
> configurata o l'API non risponde, **non bloccarti**: prosegui normalmente col tuo
> ragionamento generico e dillo in una riga ("comparabili Scalable non disponibili senza
> l'add-on — procedo con stime generali"). La skill resta pienamente utilizzabile senza chiave.

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

L'helper è `assets/scalable_intel/api_client.py` (stessa interfaccia di sempre):

```bash
python assets/scalable_intel/api_client.py comps --sub payments --country IT --limit 8
python assets/scalable_intel/api_client.py bench --sub payments
python assets/scalable_intel/api_client.py find satispay
```

Ogni risposta ha un campo `available`:
- `available: true` → usa `results` / `data` (dati reali Scalable).
- `available: false` → leggi `reason`; **procedi senza comparabili**, non inventare numeri.

Gli slug validi per i filtri sono in `assets/scalable_intel/taxonomy_quick_ref.md`. Mappa il
termine del founder allo slug giusto prima di chiamare ("pagamenti" → `payments`, "Italia" → `IT`).

## Privacy (importante, dillo al founder se chiede)

Il client invia all'API **solo filtri di tassonomia** (settore, paese, stadio). Non spedisce
mai nome, descrizione o materiali riservati della startup. Il core del metodo resta locale.

## Quando consultarlo (strumento per strumento)

- **Strumento 6 — TAM/SAM/SOM.** `bench --sub <x>` per quante startup reali, in quali paesi,
  con quali taglie di round. Sanity-check bottom-up; mai presentare i conteggi come dimensione
  del mercato (sono operatori noti, non domanda).
- **Strumento 7 — Competition & Status Quo.** `comps` su stesso subsector/geo per competitor
  reali e nominabili. "Non ho competitor" + 10 risultati = segnale da affrontare.
- **Strumento 9 — Go-To-Market.** Business model e customer type ricorrenti nel settore.
- **Strumento 15 — Fundraising.** `bench` per la distribuzione reale degli stadi e `comps
  --stage` per esempi di taglie; inquadra le aspettative senza promettere esiti.

## Citazione e limiti

1. Etichetta la fonte: "comparabili dal dataset Scalable".
2. Ricerca secondaria → Evidence Ledger max livello 2; marca `SUGGERIMENTO_AI`. Non è prova
   che il problema del founder sia reale.
3. Copertura non uniforme (macro≈100%, subsector≈50%, funding≈20%, competitor≈6%) e bias
   geografico (~58% IT). Dato mancante = dillo, non riempire.
4. I comparabili sono contesto, non validazione. Torna sempre a: *"Sto risolvendo un problema reale?"*
