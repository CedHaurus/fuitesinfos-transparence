# Fuites Infos

**Le site de recensement des fuites de données impactant la France** —
[fuitesinfos.fr](https://fuitesinfos.fr)

---

## Registre public des changements

Ce dépôt est le registre des changements apportés au catalogue publié sur
fuitesinfos.fr. Il consigne, dans l'ordre où ils sont survenus, les entrées
ajoutées, celles qui ont été retirées, et les corrections faites après
publication.

Il ne contient aucune donnée personnelle et ne reproduit pas le contenu des
fiches. Uniquement : le nom de l'entité concernée, la date de sa fiche, et ce
qui a changé.

---

## Le catalogue

fuitesinfos.fr recense les fuites de données touchant des organisations
établies en France : entreprises, associations, fédérations, établissements
publics. Chaque fiche indique l'entité concernée, la date de l'incident, la
nature des données en cause, le volume annoncé et l'état de l'information —
selon qu'elle repose sur une revendication publiée par un tiers, ou qu'elle a
été confirmée par l'entité elle-même ou par une source officielle.

Le catalogue est tenu à la main, entrée par entrée. Il n'y a ni collecte
automatique, ni republication en masse : chaque fiche est établie
individuellement, et c'est pourquoi elle peut être corrigée individuellement.

Cette distinction entre **revendiqué** et **confirmé** est au cœur du travail.
Une revendication publiée sur un forum n'est pas une preuve, et le catalogue ne
la présente jamais comme telle. Quand une entité confirme, la fiche change de
statut — et ce changement apparaît dans ce registre.

## Pourquoi ce registre

Un catalogue de ce type fait l'objet de demandes : demandes de correction,
demandes de retrait, et parfois de pressions plus directes. Sans trace
publique, deux affirmations opposées se valent — celle qui prétend qu'une fiche
a été modifiée en douce, et celle qui prétend qu'elle ne l'a jamais été.

Le registre tranche, dans les deux sens. Si une correction a été faite, elle
est ici, avec l'ancienne et la nouvelle valeur. Si un retrait a été consenti,
il est ici aussi, avec son motif. Cela protège autant les entités concernées,
qui peuvent vérifier qu'une correction obtenue a bien été appliquée, que le
catalogue lui-même, qui peut démontrer ce qu'il a fait et ce qu'il n'a pas
fait.

## Les fichiers

| Fichier | À quoi il sert |
|---|---|
| **[REGISTRE.md](REGISTRE.md)** | Le registre, lisible, du plus récent au plus ancien. C'est le fichier à ouvrir. |
| `registre.jsonl` | Le même contenu en format machine, une ligne par événement, avec le détail complet. |
| `EMPREINTE.txt` | L'empreinte de l'ensemble du registre à ce jour. |
| `ANCRAGES.md` | La liste des empreintes publiées hors de ce dépôt, avec leur date. |
| `verifier.py` | Contrôle que le registre n'a pas été retouché après coup. |

## Lire une ligne

```
2026-08-13 — Santé publique France (fiche du 2026-08-11) · Statut : Revendiquée → Confirmée
```

La première date est celle du changement. Le nom est celui de l'entité
concernée, suivi de la date de l'incident auquel sa fiche se rapporte — les
deux dates sont distinctes et ne se confondent pas.

Quand une date porte la mention `(constaté)`, elle signifie que le changement a
été relevé ce jour-là mais a pu intervenir un peu avant. Le registre ne prétend
alors pas à une précision qu'il n'a pas.

Quatre natures d'événement :

- **entrée ajoutée** — une fiche est mise en ligne ;
- **ENTRÉE RETIRÉE** — une fiche cesse d'être publiée, toujours accompagnée
  d'un motif ;
- **correction** — un élément d'une fiche déjà publiée change ; l'ancienne et
  la nouvelle valeur sont données ;
- **révision groupée** — un même élément change sur vingt fiches ou plus dans
  un même lot. Ces révisions sont regroupées en une ligne pour rester lisibles,
  mais le détail fiche par fiche reste dans `registre.jsonl`.

## Ce que le registre ne contient pas

Il ne recopie pas le contenu des fiches. Ni description, ni sources, ni
captures, ni évaluation de gravité. Et aucune donnée personnelle, sous aucune
forme.

Les textes longs ne sont jamais reproduits, même lorsqu'ils sont corrigés. Le
registre publie à la place leur empreinte avant et après. Une empreinte est une
suite de caractères calculée à partir d'un texte : elle ne permet pas de
reconstituer ce texte, mais quiconque possède une copie de l'ancienne version
peut vérifier qu'elle correspond bien. La preuve est donc disponible sans que
le registre republie ce qui a été retiré ou réécrit.

## Retraits

**Tout retrait est inscrit ici, sans exception**, y compris lorsqu'il résulte
d'un accord amiable. Ce point n'est pas négociable et il est annoncé d'avance :
une demande de retrait peut être acceptée, elle ne peut pas être discrète.

À ce jour, **une entrée a été retirée du catalogue**. Aucun retrait n'est
intervenu à la demande d'une entreprise, ni sur décision de justice.

Ce décompte n'est pas une déclaration d'intention : le compteur en tête de
[REGISTRE.md](REGISTRE.md) est recalculé à chaque mise à jour, et chaque
retrait y figure avec sa date, l'entité concernée et son motif.

Chaque retrait porte l'un de ces motifs, et un seul :

| Motif | Ce qu'il signifie |
|---|---|
| **Erreur de notre part** | La fiche était fausse. Le retrait est une correction. |
| **Information devenue inexacte** | Les faits ont évolué : revendication démentie, source rétractée. |
| **Doublon ou regroupement de fiches** | Ménage interne, sans enjeu sur le fond. |
| **Retrait sur demande, sans erreur constatée** | La fiche n'était pas fausse. Le retrait relève d'un choix, pas d'une correction. |
| **Décision de justice** | Retrait sous contrainte judiciaire. |

La distinction entre les deux derniers cas et les premiers est délibérée. Un
retrait pour erreur et un retrait consenti sans erreur ne disent pas la même
chose, et les confondre reviendrait à laisser croire que toute fiche retirée
était fausse.

Le motif, lui, est déclaratif : c'est nous qui le renseignons. La date du
retrait, en revanche, est établie par la mécanique décrite plus bas.

## Portée et limites

Ces limites sont réelles. Les taire rendrait le reste suspect.

**Le registre commence le 5 juillet 2026.** À cette date, 580 fiches publiques
existaient déjà. Leur historique antérieur n'est pas reconstituable et ne
figure pas ici. Le registre couvre ce qui s'est passé depuis, pas avant.

**Les corrections suivies sont limitées à un ensemble défini** : nom de
l'entité, date de l'incident, statut, volume concerné, secteur, SIREN,
catégorie, exactitude de la revendication, site de l'entité, nature des données,
type d'incident et description publique. Les éléments internes ne sont pas
suivis.

**Le seuil de regroupement est de vingt fiches.** Au-delà, un changement
portant sur le même élément dans un même lot est affiché en une ligne. La règle
est fixe et publiée ici précisément pour qu'on ne puisse pas s'en servir pour
noyer un changement isolé.

## Vérifier que le registre n'a pas été retouché

Un dépôt que son auteur contrôle ne prouve rien par lui-même : il pourrait être
réécrit. Deux mécanismes empêchent cela.

**Les lignes sont chaînées.** Chaque ligne du registre contient l'empreinte de
la précédente. Modifier une ligne ancienne change son empreinte, donc celle de
la suivante, et de proche en proche jusqu'à la dernière. Une retouche ne peut
pas rester locale : elle déplace l'empreinte finale, qui est publiée.

Pour le contrôler vous-même :

```
python3 verifier.py
```

Le script relit tout le registre et recalcule la chaîne. Il n'a besoin d'aucune
installation et ne se connecte à rien.

**L'empreinte finale est publiée hors de ce dépôt.** À chaque mise à jour, elle
est diffusée sur le réseau Nostr, depuis le compte public du catalogue et vers
des relais indépendants que nous n'administrons pas. Une empreinte ainsi
diffusée ne peut plus être reprise ni effacée. Il suffit donc d'en avoir relevé
une, à n'importe quelle date, pour pouvoir prouver plus tard que tout ce qui la
précédait est resté intact. La liste de ces publications, avec leurs
identifiants, est tenue dans [ANCRAGES.md](ANCRAGES.md).

## Signaler une erreur

Si une fiche vous concerne et comporte une inexactitude, écrivez-nous via le
[formulaire de contact](https://fuitesinfos.fr/contact.php). Une erreur
démontrée est corrigée, et la correction apparaît dans ce registre avec
l'ancienne et la nouvelle valeur. C'est aussi votre meilleure garantie que la
correction a bien eu lieu.

## Liens utiles

- **Le catalogue** — [fuitesinfos.fr](https://fuitesinfos.fr)
- **Questions fréquentes** — [fuitesinfos.fr/faq](https://fuitesinfos.fr/faq/)
- **Signaler une fuite** — [fuitesinfos.fr/signaler](https://fuitesinfos.fr/signaler/)
- **Contact** — [fuitesinfos.fr/contact.php](https://fuitesinfos.fr/contact.php)
- **Mentions légales** — [fuitesinfos.fr/mentions-legales](https://fuitesinfos.fr/mentions-legales/)
- **LinkedIn** — [linkedin.com/company/fuites-infos](https://www.linkedin.com/company/fuites-infos)
- **X** — [@fuitesinfos](https://x.com/fuitesinfos)
- **Nostr** — `npub1f7ghcvvu0ef4q905khx7yzxa74ue0wv07zmz0zvnrgjggllupf5qp4vc9q`
