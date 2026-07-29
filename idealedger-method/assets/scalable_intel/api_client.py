#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
api_client.py — client del Scalable Intelligence API (add-on gratuito in fase di lancio).

Stessa interfaccia di prima (comps / bench / find / sectors), ma invece di leggere
un dataset locale CHIAMA L'API remota usando una API key.

GRACEFUL DEGRADATION
--------------------
Se la chiave non è configurata o la rete non è disponibile, NON va in errore fatale:
stampa {"available": false, "reason": ...}. La skill deve interpretarlo come
"procedi col ragionamento generico, senza comparabili Scalable".

PRIVACY
-------
Invia all'API SOLO filtri di tassonomia (settore, paese, stadio...). Mai dati
riservati della startup. Non spedire nomi, descrizioni o materiali del founder.

CHIAVE — ordine di lettura (dal più al meno prioritario)
--------------------------------------------------------
1. variabile d'ambiente SCALABLE_API_KEY
2. file persistente nella home:      ~/.scalable_api_key
3. copia locale nel workspace:       ./.scalable_api_key  (cartella di lavoro corrente)
4. (legacy) api_key.txt accanto allo script

La chiave NON viene mai stampata, messa nei log, nei report o negli URL.

CHIAVE — salvataggio (subcomando save-key)
------------------------------------------
Per salvare la chiave senza esporla (mai come argomento CLI: si legge da stdin o
dalla variabile d'ambiente SCALABLE_API_KEY):

  # home persistente (posizione preferita)
  printf %s "<CHIAVE>" | python api_client.py save-key --scope home

  # fallback nel workspace (home non persistente, es. sandbox)
  printf %s "<CHIAVE>" | python api_client.py save-key --scope workspace --workspace <DIR>

save-key scrive il file con permessi 600 (dove supportato) e, in modalità workspace,
aggiorna in modo IDEMPOTENTE il .gitignore della cartella (aggiunge solo le righe
mancanti `.scalable_api_key` e `api_key.txt`, senza mai sovrascrivere regole esistenti).
Stampa solo un esito, MAI la chiave.

CONFIG
------
- URL:  variabile d'ambiente SCALABLE_API_URL, altrimenti il valore in config.json

USO CLI (invariato)
  python api_client.py comps --sub payments --country IT --limit 8
  python api_client.py bench --sub payments
  python api_client.py find satispay
  python api_client.py sectors
"""
import os, sys, json, argparse, urllib.parse, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))

# righe minime da garantire nel .gitignore del workspace (nessun pattern allargato)
GITIGNORE_LINES = [".scalable_api_key", "api_key.txt"]


def _read_key_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            k = f.read().strip()
            return k or None
    except Exception:
        return None


def _cfg():
    url = os.environ.get("SCALABLE_API_URL")
    if not url:
        try:
            with open(os.path.join(HERE, "config.json"), encoding="utf-8") as f:
                url = json.load(f).get("api_url")
        except Exception:
            url = None
    # ordine di lettura chiave: env -> home -> workspace(cwd) -> legacy(script dir)
    key = os.environ.get("SCALABLE_API_KEY")
    if not key:
        for p in (
            os.path.expanduser("~/.scalable_api_key"),
            os.path.join(os.getcwd(), ".scalable_api_key"),
            os.path.join(HERE, "api_key.txt"),
        ):
            key = _read_key_file(p)
            if key:
                break
    return url, key


def _call(endpoint, params):
    url, key = _cfg()
    if not url:
        return {"available": False, "reason": "api_url non configurato (config.json o SCALABLE_API_URL)"}
    if not key:
        return {"available": False, "reason": "nessuna API key (add-on Scalable non attivo) — procedi con contenuto generico"}
    qs = urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, "")})
    full = f"{url.rstrip('/')}/v1/{endpoint}?{qs}"
    req = urllib.request.Request(full, headers={"Authorization": f"Bearer {key}"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode("utf-8"))
            data["available"] = True
            return data
    except urllib.error.HTTPError as e:
        body = {}
        try:
            body = json.loads(e.read().decode("utf-8"))
        except Exception:
            pass
        return {"available": False, "reason": f"HTTP {e.code}", "detail": body}
    except Exception as e:
        return {"available": False, "reason": f"rete non disponibile: {e}"}


def _write_key_file(path, key):
    """Scrive la chiave e prova a impostare i permessi 600. Non stampa mai la chiave."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(key.strip() + "\n")
    try:
        os.chmod(path, 0o600)
        return "ok"
    except Exception:
        # chmod non supportato (es. Windows/alcuni FS): non è un errore bloccante
        return "unsupported"


def _ensure_gitignore(dirpath):
    """Garantisce le righe minime nel .gitignore del workspace. Idempotente:
    aggiunge solo le righe mancanti, non sovrascrive mai regole esistenti."""
    gi = os.path.join(dirpath, ".gitignore")
    if os.path.exists(gi):
        with open(gi, encoding="utf-8") as f:
            existing = f.read()
        present = {ln.strip() for ln in existing.splitlines()}
        missing = [ln for ln in GITIGNORE_LINES if ln not in present]
        if not missing:
            return "already-ok"
        sep = "" if existing.endswith("\n") or existing == "" else "\n"
        with open(gi, "a", encoding="utf-8") as f:
            f.write(sep + "\n".join(missing) + "\n")
        return "updated"
    with open(gi, "w", encoding="utf-8") as f:
        f.write("# Scalable Intelligence — chiave API locale (non committare)\n")
        f.write("\n".join(GITIGNORE_LINES) + "\n")
    return "created"


def _read_key_from_stdin_or_env():
    """Legge la chiave da stdin (preferito) o da SCALABLE_API_KEY. MAI da argv."""
    key = None
    try:
        if not sys.stdin.isatty():
            key = sys.stdin.read().strip()
    except Exception:
        key = None
    if not key:
        key = (os.environ.get("SCALABLE_API_KEY") or "").strip()
    return key or None


def _cmd_save_key(scope, workspace):
    key = _read_key_from_stdin_or_env()
    if not key:
        return {"saved": False, "reason": "nessuna chiave fornita: passala via stdin o SCALABLE_API_KEY (mai come argomento CLI)"}
    if scope == "workspace":
        wsdir = os.path.abspath(workspace or os.getcwd())
        os.makedirs(wsdir, exist_ok=True)
        target = os.path.join(wsdir, ".scalable_api_key")
        chmod = _write_key_file(target, key)
        gi = _ensure_gitignore(wsdir)
        return {"saved": True, "scope": "workspace", "location": target, "chmod": chmod, "gitignore": gi}
    target = os.path.expanduser("~/.scalable_api_key")
    chmod = _write_key_file(target, key)
    return {"saved": True, "scope": "home", "location": target, "chmod": chmod}


def main():
    ap = argparse.ArgumentParser(description="Scalable Intelligence API client")
    sp = ap.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("comps")
    for o in ["macro", "sub", "bmodel", "customer", "country", "ecosystem", "stage"]:
        c.add_argument("--" + o, default=None)
    c.add_argument("--min-year", dest="min_year", default=None)
    c.add_argument("--limit", default="12")
    b = sp.add_parser("bench")
    b.add_argument("--macro", default=None); b.add_argument("--sub", default=None); b.add_argument("--bmodel", default=None)
    f = sp.add_parser("find"); f.add_argument("query")
    sp.add_parser("sectors")
    sk = sp.add_parser("save-key")
    sk.add_argument("--scope", choices=["home", "workspace"], default="home")
    sk.add_argument("--workspace", default=None, help="cartella del workspace/dossier (default: cwd)")
    a = ap.parse_args()

    if a.cmd == "comps":
        res = _call("comps", {k: getattr(a, k) for k in
                    ["macro","sub","bmodel","customer","country","ecosystem","stage","min_year","limit"]})
    elif a.cmd == "bench":
        res = _call("bench", {"macro": a.macro, "sub": a.sub, "bmodel": a.bmodel})
    elif a.cmd == "find":
        res = _call("find", {"q": a.query})
    elif a.cmd == "sectors":
        res = _call("sectors", {})
    elif a.cmd == "save-key":
        res = _cmd_save_key(a.scope, a.workspace)
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
