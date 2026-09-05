---
epoch: 1774344171294
modelKey: "eu.anthropic.claude-opus-4-6-v1|amazon-bedrock"
topic: "Erreur MathJax signalée"



tags:
  - copilot-conversation
---

**user**: ya une erreur mathjax
[Context: Notes: content/Physique-Chimie/Chapitre 10 - Transformations chimiques.md]
[Timestamp: 2026/03/24 10:22:51]

**ai**: 
<think>Let me look at the note for MathJax errors.

The issue is in the last chemical equation:

$1H_2O+12CO_2→C_12_H_22_O_11+O_2$

The subscripts are wrong. It should be $C_{12}H_{22}O_{11}$ with curly braces for multi-digit subscripts. Also the coefficients need to be fixed for balancing.

Let me also check the other equations for MathJax issues:

- $2C+2O_2 → 2CO_2$ ✓
- $Cu^{2+}+2Ag → Cu+2Ag^-$ - should be $Ag^+$ not $Ag^-$ for silver ions? Actually, looking at the reaction: Cu²⁺ + 2Ag → Cu + 2Ag⁺. So the product should be $Ag^+$ not $Ag^-$. But the user asked about MathJax errors specifically.


- $C_2H_4+3O_2 → 2CO_2+2H_2O$ ✓
- $2CO+O_2 → 2CO_2$ ✓
- $N_2+3H_2 → 2NH_3$ ✓
- $N_2+2H_2 → N_2H_4$ ✓
- $2C_2H_6+7O_2 → 6H_2O + 4CO_2$ ✓
- $CuO+2H^+→Cu^{2+}+H_2O$ ✓

The rest of the equations look fine with proper MathJax formatting.</think>Oui, l'erreur est dans la dernière équation :

```
$1H_2O+12CO_2→C_12_H_22_O_11+O_2$
```

Le problème c'est que quand un indice a **plus d'un chiffre**, il faut mettre des **accolades `{}`** autour. Sinon MathJax affiche n'importe quoi.

Il faut écrire :

```
$12H_2O+12CO_2→C_{12}H_{22}O_{11}+12O_2$
```

Ça donnera : $12H_2O+12CO_2→C_{12}H_{22}O_{11}+12O_2$

En gros, la règle c'est : `_2` ça marche pour un seul caractère, mais dès qu'il y en a plusieurs comme 12, 22, 11, faut faire `_{12}`, `_{22}`, `_{11}`.
[Timestamp: 2026/03/24 10:23:10]