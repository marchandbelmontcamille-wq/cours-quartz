---
epoch: 1776416446433
modelKey: "eu.anthropic.claude-opus-4-6-v1|amazon-bedrock"
topic: "Définir une loi de probabilité"



tags:
  - copilot-conversation
---

**user**: comment dfinir une loi de probabilité
[Context: Notes: content/Mathématiques/Exercices.md]
[Timestamp: 2026/04/17 11:00:46]

**ai**: 
<think>The user is asking how to define a probability law (loi de probabilité), which relates to their current chapter on probability (CHAP12) in their math notes.</think># Comment définir une loi de probabilité

En gros, une **loi de probabilité**, c'est le fait d'**associer à chaque issue** (résultat possible) d'une expérience aléatoire **une probabilité** (un nombre entre 0 et 1).

## Les deux conditions à respecter :

- Chaque probabilité doit être **comprise entre 0 et 1** :
$$0 \leq P(issue) \leq 1$$

- La **somme de toutes les probabilités** doit être **égale à 1** :
$$P(e_1) + P(e_2) + \cdots + P(e_n) = 1$$

## Exemple concret :

Si on lance un dé truqué à 3 faces (1, 2, 3), on peut avoir cette loi de probabilité :

| Issue | 1 | 2 | 3 |
|---|---|---|---|
| Probabilité | 1/6 | 1/2 | 1/3 |

On vérifie : $\frac{1}{6} + \frac{1}{2} + \frac{1}{3} = \frac{1}{6} + \frac{3}{6} + \frac{2}{6} = \frac{6}{6} = 1$ ✅

*(D'ailleurs c'est exactement l'exercice 27 que t'as dans ta note !)*

## En résumé :

> Définir une loi de probabilité, c'est donner la liste de **toutes les issues possibles** et attribuer à **chacune** une probabilité, de sorte que le **total fasse 1**.

Si c'est une situation d'**équiprobabilité** (toutes les issues ont la même chance), alors chaque probabilité vaut $\frac{1}{n}$ où $n$ est le nombre total d'issues (genre un dé normal : chaque face a une proba de $\frac{1}{6}$).
[Timestamp: 2026/04/17 11:01:00]