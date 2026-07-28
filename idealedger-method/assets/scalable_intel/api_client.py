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

CONFIG
------
- URL:  variabile d'ambiente SCALABLE_API_URL, altrimenti il valore in config.json
- KEY:  variabile d'ambiente SCALABLE_API_KEY, altrimenti file api_key.txt accanto
        allo script, altrimenti ~/.scalable_api_key

USO CLI (identico a prima)
  python api_client.py comps --sub payments --country IT --limit 8
  python api_client.py bench --sub payments
  python api_client.py find satispay
  python api_client.py sectors
"""
import os, sys, json, argparse, urllib.parse, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))

def _cfg():
    url = os.environ.get("SCALABLE_API_URL")
    if not url:
        try:
            with open(os.path.join(HERE, "config.json"), encoding="utf-8") as f:
                url = json.load(f).get("api_url")
        except Exception:
            url = None
    key = os.environ.get("SCALABLE_API_KEY")
    if not key:
        for p in (os.path.join(HERE, "api_key.txt"), os.path.expanduser("~/.scalable_api_key")):
            try:
                with open(p, encoding="utf-8") as f:
                    key = f.read().strip()
                    if key:
                        break
            except Exception:
                pass
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
    print(json.dumps(res, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
