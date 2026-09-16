---
epoch: 1789290669599
mode: agent
backendId: claude
sessionId: "528a6867-15dd-4bf2-ab3b-41548ce15d67"
agentLabel: "Fais moi des exos sur ce qu'il ya dans la séquence"
usage: '{"usedTokens":30834,"contextWindow":200000,"inputTokens":3,"outputTokens":1,"cacheReadTokens":30566,"cacheWriteTokens":264,"updatedAt":1789293251026}'
tags:
  - copilot-conversation
---

**user**: Fais moi des exos sur ce qu'il ya dans la séquence
[Timestamp: 2026/09/13 11:11:09]

**ai**: Je vais lire la séquence pour voir ce qu'elle contient.Voici des exercices basés sur le contenu de ta séquence sur la mole :

---

## Exercices — La mole et les solutions

### Partie 1 : La mole et la constante d'Avogadro

**Exercice 1**
Un échantillon de fer contient $3,01 \times 10^{24}$ atomes de fer.
1. Rappelle la valeur de la constante d'Avogadro $N_A$.
2. Calcule la quantité de matière $n$ contenue dans cet échantillon.

**Exercice 2**
On dispose de 0,25 mol de molécules d'eau.
1. Combien de molécules d'eau cela représente-t-il ?
2. Combien d'atomes d'hydrogène cela représente-t-il ? (rappel : une molécule d'eau contient 2 atomes H)

---

### Partie 2 : Masse molaire

**Exercice 3**
Calcule la masse molaire des espèces suivantes (données : $M_H = 1{,}0\ \text{g·mol}^{-1}$, $M_C = 12{,}0\ \text{g·mol}^{-1}$, $M_O = 16{,}0\ \text{g·mol}^{-1}$, $M_N = 14{,}0\ \text{g·mol}^{-1}$) :
1. Le dioxyde de carbone $CO_2$
2. L'éthanol $C_2H_6O$
3. L'ammoniac $NH_3$

**Exercice 4**
La vanilline a une masse molaire $M = 152\ \text{g·mol}^{-1}$.
1. Quelle masse faut-il prélever pour avoir $5,0 \times 10^{-2}\ \text{mol}$ de vanilline ?
2. Quelle quantité de matière contient un échantillon de 30,4 g de vanilline ?

---

### Partie 3 : Concentration en masse et concentration molaire

**Exercice 5**
Une solution de glucose contient 9,0 g de glucose dissous dans 500 mL de solution.
1. Calcule la concentration en masse $C_m$ de cette solution en $\text{g·L}^{-1}$.
2. La masse molaire du glucose ($C_6H_{12}O_6$) est $M = 180\ \text{g·mol}^{-1}$. Calcule la quantité de matière $n$ de glucose dissous.
3. Calcule la concentration molaire $C$ de cette solution en $\text{mol·L}^{-1}$.

**Exercice 6**
Une solution de chlorure de sodium (sel) a une concentration molaire $C = 0,10\ \text{mol·L}^{-1}$ et un volume $V = 250\ \text{mL}$.
1. Calcule la quantité de matière $n$ de sel dans cette solution.
2. $M_{NaCl} = 58{,}5\ \text{g·mol}^{-1}$. Quelle masse de sel a été dissoute ?

---

### Partie 4 : Mélanges de gaz (volume molaire)

**Exercice 7**
Un mélange gazeux de volume total $V = 3{,}6\ \text{L}$ est composé de dioxygène $O_2$ et de diazote $N_2$. Le volume molaire vaut $V_m = 24\ \text{L·mol}^{-1}$.
1. Calcule la quantité de matière totale $n_{tot}$ du mélange.
2. Le mélange contient $0,08\ \text{mol}$ de dioxygène. Quelle est la quantité de matière de diazote ?

---

Bon courage ! Si tu veux les corrections, dis-le moi.
[Timestamp: 2026/09/13 11:11:09]

**user**: sur pour $3,01 \times 10^{24}$
[Timestamp: 2026/09/13 11:16:04]

**ai**: Oui, c'est volontaire ! $3,01 \times 10^{24}$ est le double de $N_A = 6,02 \times 10^{23}$, donc le calcul donne un résultat "rond" :

$$n = \frac{N}{N_A} = \frac{3,01 \times 10^{24}}{6,02 \times 10^{23}} = 5\ \text{mol}$$

C'est fait exprès pour que le calcul soit faisable sans calculatrice et que tu vérifies bien que tu maîtrises la formule. Tu veux essayer les autres exercices ?
[Timestamp: 2026/09/13 11:16:04]

**user**: ## 1
1) $6,02\times 10^{23}$
2) $n=\frac {3.01\times 10^{24}} {6.02\times 10^{23}}=5\text { moles}$ 
## 2
1) $1.5\times 10^{23}$ molécules d'eau
2) $3\times 10^{23}$ atomes
## 3
1) $M_{CO_2}=12+16\times 2=44$ g par mol$^{-1}$ 
2) $M_{C_2H_6O}=2\times 12+6+16=46$ g par mol$^{-1}$
3) $M_{NH_3}=14+3=17$ g par mol$^{-1}$
## 4
 1) 7.6
 2) 0.2
## 5
1) 18
2)  0.05
3) 0.1
## 6
1) 0,025
2) 1,46
## 7
1) 86.4
2) 86.32
[Timestamp: 2026/09/13 11:51:02]

**ai**: Très bon travail dans l'ensemble ! Quelques corrections :

---

**Exercice 2 — question 1** : erreur de calcul.

$$N = N_A \times n = 6{,}02 \times 10^{23} \times 0{,}25 = 1{,}505 \times 10^{23}\ \text{molécules}$$

C'est bien $1{,}505 \times 10^{23}$, pas $1{,}5 \times 10^{23}$ (attention à la précision).
Et pour la question 2 : $3{,}01 \times 10^{23}$ atomes (le double). ✓ dans l'idée.

---

**Exercice 7 — question 1** : erreur de formule. Tu as multiplié au lieu de diviser.

$$n_{tot} = \frac{V}{V_m} = \frac{3{,}6}{24} = 0{,}15\ \text{mol}$$

**Question 2** : même erreur de base, mais la logique $n' = n_{tot} - n$ est bonne.

$$n_{N_2} = 0{,}15 - 0{,}08 = 0{,}07\ \text{mol}$$

---

**Tout le reste est correct** (exercices 3, 4, 5, 6). Bien joué !
[Timestamp: 2026/09/13 11:51:02]

**user**: quel est le triangle multiplication division ?
[Timestamp: 2026/09/13 11:53:02]

**ai**: C'est un triangle qui aide à retrouver les formules quand on a $a = b \times c$. Pour la mole par exemple :

$$m = n \times M$$

```
        m
    ─────────
    n  │  M
```

- Tu cherches $m$ → tu **multiplies** : $m = n \times M$
- Tu cherches $n$ → tu **divises** : $n = \dfrac{m}{M}$
- Tu cherches $M$ → tu **divises** : $M = \dfrac{m}{n}$

Le même triangle existe pour $C = \dfrac{n}{V}$, $C_m = \dfrac{m}{V}$, $n = \dfrac{N}{N_A}$, etc. Tu veux que je te les fasse tous ?
[Timestamp: 2026/09/13 11:53:02]

**user**: pour la 7 j'ai utilisé en haut mol en bas à gauche mol/L et à droite L
[Timestamp: 2026/09/13 11:53:54]

**ai**: Tu as inversé $V_m$ ! Le volume molaire s'exprime en **L/mol**, pas mol/L.

Le bon triangle pour $n = \dfrac{V}{V_m}$ :

```
        V      (en L)
    ─────────
    n  │  Vm
(mol)  │ (L/mol)
```

Donc si tu mets mol/L en bas à droite, tu obtiens $n = V \times \frac{\text{mol}}{L}$, ce qui donne des mol²/L² — ça n'a pas de sens physiquement.

Avec L/mol : $n\ (\text{mol}) = V\ (L) \div V_m\ (L/\text{mol})$ ✓ les unités s'annulent bien.
[Timestamp: 2026/09/13 11:53:54]