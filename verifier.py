#!/usr/bin/env python3
"""Vérifie que le registre n'a pas été retouché après coup.

    python3 verifier.py

Aucune dépendance : Python 3 suffit. Le script relit registre.jsonl, recalcule
la chaîne d'empreintes de la première ligne à la dernière, et compare le
résultat à ce qui est publié dans EMPREINTE.txt.

Chaque ligne contient l'empreinte de la précédente. Modifier, insérer ou
supprimer une ligne ancienne change son empreinte, donc celle de la suivante,
et ainsi de suite jusqu'à la fin : l'empreinte de tête ne correspond plus. Si
vous avez conservé une empreinte de tête publiée à une date antérieure, vous
pouvez donc vérifier que tout ce qui la précédait est resté intact.
"""

import hashlib
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent


def main() -> int:
    chemin = ICI / "registre.jsonl"
    if not chemin.exists():
        print("registre.jsonl introuvable", file=sys.stderr)
        return 2

    lignes = [json.loads(l) for l in chemin.read_text(encoding="utf-8").splitlines() if l.strip()]
    precedente = "0" * 64

    for attendu, ligne in enumerate(lignes, start=1):
        if ligne.get("seq") != attendu:
            print(f"ligne {attendu} : numéro de séquence {ligne.get('seq')} — "
                  f"une ligne a été insérée ou supprimée", file=sys.stderr)
            return 1
        if ligne.get("empreinte_precedente") != precedente:
            print(f"ligne {attendu} : la chaîne est rompue — cette ligne ne suit pas "
                  f"celle qui la précède", file=sys.stderr)
            return 1

        publiee = ligne.pop("empreinte", None)
        canonique = json.dumps(ligne, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        calculee = hashlib.sha256(canonique.encode("utf-8")).hexdigest()
        if calculee != publiee:
            print(f"ligne {attendu} : le contenu a été modifié après publication",
                  file=sys.stderr)
            return 1
        precedente = calculee

    tete = ICI / "EMPREINTE.txt"
    if tete.exists():
        declaree = ""
        for l in tete.read_text(encoding="utf-8").splitlines():
            if l.startswith("empreinte_tete:"):
                declaree = l.split(":", 1)[1].strip()
        if declaree and declaree != precedente:
            print(f"l'empreinte de tête publiée ne correspond pas au registre\n"
                  f"  publiée  : {declaree}\n  calculée : {precedente}", file=sys.stderr)
            return 1

    print(f"registre intact — {len(lignes)} événements vérifiés")
    print(f"empreinte de tête : {precedente}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
