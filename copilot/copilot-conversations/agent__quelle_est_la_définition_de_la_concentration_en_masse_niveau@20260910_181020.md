---
epoch: 1789056620000
mode: agent
backendId: claude
sessionId: "092ae5d1-3af1-44c3-a4b8-80a675038244"
agentLabel: "quelle est la définition de la concentration en masse niveau…"
usage: '{"usedTokens":46908,"contextWindow":200000,"inputTokens":2,"outputTokens":2,"cacheReadTokens":0,"cacheWriteTokens":46904,"updatedAt":1789062777333}'
tags:
  - copilot-conversation
---

**user**: quelle est la définition de la concentration en masse niveau première
[Timestamp: 2026/09/10 18:10:20]

**ai**: ## Concentration en masse (niveau première)

**Définition.** La concentration en masse $c_m$ d'une espèce chimique dissoute (le **soluté**) dans une solution est la **masse de ce soluté** divisée par le **volume de la solution** :

$$c_m = \frac{m_{\text{soluté}}}{V_{\text{solution}}}$$

- $m$ : masse de soluté dissous, en grammes (g)
- $V$ : volume **de la solution** (pas du solvant seul !), en litres (L)
- $c_m$ : en **g·L⁻¹**

Autrement dit : c'est la masse de soluté contenue dans un litre de solution. Une solution de sel à $c_m = 20$ g·L⁻¹ contient 20 g de sel dissous par litre de solution.

### Les trois points de vigilance classiques
- **$V$ est le volume de la solution finale**, obtenu après dissolution et ajustement au trait de jauge de la fiole jaugée.
- La concentration en masse est **indépendante du volume prélevé** : c'est une grandeur *intensive*. Si tu prélèves 10 mL d'une solution à 20 g·L⁻¹, ce prélèvement est toujours à 20 g·L⁻¹.
- Elle ne peut pas dépasser la **solubilité** $s$ du soluté dans le solvant (au-delà, il reste du solide non dissous : la solution est saturée).

### Lien avec la concentration en quantité de matière
C'est le pont avec ta séquence sur la mole, dans [[Séquence - Mole]] :

$$C = \frac{n}{V} \quad \text{(en mol·L}^{-1}\text{)} \qquad \text{et} \qquad n = \frac{m}{M}$$

En combinant :

$$\boxed{c_m = C \times M}$$

où $M$ est la masse molaire du soluté (g·mol⁻¹).

**Exemple.** On dissout $m = 5{,}85$ g de chlorure de sodium NaCl dans de l'eau pour obtenir $V = 500$ mL de solution.

- $c_m = \dfrac{5{,}85}{0{,}500} = 11{,}7$ g·L⁻¹
- $M_{\text{NaCl}} = 23{,}0 + 35{,}5 = 58{,}5$ g·mol⁻¹
- $C = \dfrac{c_m}{M} = \dfrac{11{,}7}{58{,}5} = 0{,}200$ mol·L⁻¹

---

Aucune note de ton vault ne traite pour l'instant de la concentration (j'ai cherché : rien dans `content/`). Si tu veux, j'ajoute cette définition en section dans [[Séquence - Mole]], ou je crée une note dédiée dans `content/Physique Chimie/`.
[Timestamp: 2026/09/10 18:10:20]

**user**: l'unité de cette grandeur est la mm que la masse volumique. Après avoir rappelé la formule permettant de calculer une masse volumique, établir les différences entre ces deux grandeurs
[Timestamp: 2026/09/10 18:15:43]

**ai**: ## Rappel : la masse volumique

La masse volumique $\rho$ (lettre grecque « rhô ») d'un échantillon de matière est :

$$\rho = \frac{m}{V}$$

- $m$ : masse de l'échantillon considéré
- $V$ : volume **occupé par cet échantillon lui-même**
- unité usuelle : g·L⁻¹, mais aussi g·mL⁻¹, g·cm⁻³ ou kg·m⁻³ (unité SI)

Tu as raison : $c_m$ et $\rho$ sont toutes deux un quotient « masse / volume », donc **même dimension et mêmes unités possibles**. C'est précisément pour ça qu'il faut être rigoureux sur *quelle* masse et *quel* volume on met dans la formule.

## Les différences

| | Masse volumique $\rho$ | Concentration en masse $c_m$ |
| --- | --- | --- |
| Système décrit | un **corps** (espèce pure, matériau, ou un mélange pris en bloc) | une **espèce dissoute** dans une solution |
| Masse au numérateur | masse **totale** de l'échantillon | masse du **seul soluté** (pas celle de la solution) |
| Volume au dénominateur | volume **de l'échantillon lui-même** | volume **de la solution entière** (soluté + solvant) |
| Nature de la grandeur | **propriété physique caractéristique** du corps, à $T$ et $P$ fixées : elle est tabulée et sert à identifier une espèce | grandeur de **composition** : elle décrit une préparation, pas une substance |
| Peut-on la choisir ? | **non** — imposée par la nature du corps | **oui** — on la fixe en pesant le soluté, et on la modifie par dilution |
| Existe-t-elle pour un corps pur seul ? | oui, toujours | non : elle n'a de sens que **dans une solution** |

### Les trois idées à retenir

**1. Le volume n'est pas le même objet.** Dans $\rho$, le volume est celui de la matière pesée. Dans $c_m$, le volume est celui de la solution : le soluté dissous n'occupe plus un volume propre identifiable. C'est l'erreur la plus fréquente — écrire $c_m = \frac{m_{\text{soluté}}}{V_{\text{soluté}}}$ n'a aucun sens.

**2. La masse n'est pas la même non plus.** Pour une solution, on peut calculer les deux grandeurs, et elles ne donnent pas le même nombre :
- $\rho_{\text{solution}} = \dfrac{m_{\text{solution}}}{V_{\text{solution}}}$ (masse totale, solvant compris)
- $c_m(\text{soluté}) = \dfrac{m_{\text{soluté}}}{V_{\text{solution}}}$ (masse du soluté seul)

Donc toujours $c_m < \rho_{\text{solution}}$.

**3. Caractéristique vs. réglable.** $\rho_{\text{eau}} = 1{,}00$ g·mL⁻¹ : c'est une donnée de l'eau, on ne peut pas la changer. En revanche une solution de sel peut être à 5, 20 ou 100 g·L⁻¹ selon ce qu'on a préparé. Deux solutions de même soluté ont la même $\rho$ du soluté solide, mais des $c_m$ différentes.

### Exemple chiffré

On dissout $m = 20$ g de sel NaCl dans de l'eau, pour obtenir $V = 1{,}0$ L de solution de masse $m_{\text{solution}} = 1013$ g.

- $c_m(\text{NaCl}) = \dfrac{20}{1{,}0} = 20$ g·L⁻¹
- $\rho_{\text{solution}} = \dfrac{1013}{1{,}0} = 1013$ g·L⁻¹ (soit $1{,}013$ g·mL⁻¹)
- $\rho_{\text{NaCl solide}} = 2160$ g·L⁻¹ (donnée tabulée, indépendante de l'expérience)

Trois valeurs, trois significations, **une seule unité**.

### Le point de contact entre les deux

Quand le soluté est un **liquide** que l'on prélève à la pipette, on passe de l'un à l'autre : le volume $V_0$ prélevé donne la masse par $m = \rho \times V_0$, puis

$$c_m = \frac{\rho \times V_0}{V_{\text{solution}}}$$

C'est le lien exigible en première pour préparer une solution par dissolution d'un liquide.

Veux-tu que j'ajoute cette comparaison (tableau inclus) dans [[Séquence - Mole]], ou plutôt dans une note dédiée du type *Concentration en masse et masse volumique* ?
[Timestamp: 2026/09/10 18:15:43]

**user**: que veut dire _m dans C_m
[Timestamp: 2026/09/10 18:21:39]

**ai**: Le petit **`m` en indice veut dire « massique »** : $c_m$ se lit « concentration massique », c'est-à-dire concentration **en masse**.

C'est une simple **étiquette de notation**, pas une grandeur qui intervient dans le calcul. Elle sert à répondre à la question : *une concentration, oui, mais concentration de quoi ?*

- $c_m$ → concentration **en masse** (massique) : on compte le soluté en **grammes**, unité g·L⁻¹
- $c$ ou $C$ → concentration **en quantité de matière** (molaire) : on compte le soluté en **moles**, unité mol·L⁻¹

Les deux décrivent la même solution, mais avec deux « unités de comptage » différentes du soluté, reliées par la masse molaire :

$$c_m = c \times M$$

### Attention à deux confusions fréquentes

**1. Le `m` en indice n'est pas le $m$ de la formule.** Dans $c_m = \dfrac{m}{V}$, le $m$ du numérateur est une *masse en grammes* (une valeur numérique), alors que le $m$ en indice est juste une abréviation du mot « massique ». Ils se ressemblent, mais l'un est une grandeur, l'autre est une étiquette.

**2. Les notations varient selon les manuels.** Tu peux rencontrer, pour la même chose :
- $c_m$ (le plus courant en première)
- $t$ ou $t_m$ (« titre massique »)
- parfois $\gamma$ (gamma) dans des ouvrages plus anciens

Et inversement, certains manuels écrivent la concentration molaire $c_n$ (indice $n$ pour « quantité de matière »), pour rester symétriques. Le principe reste le même : **l'indice indique en quoi on exprime la quantité de soluté**.

En cas de doute dans un exercice, l'**unité tranche toujours** : g·L⁻¹ → concentration en masse ; mol·L⁻¹ → concentration en quantité de matière.
[Timestamp: 2026/09/10 18:21:39]

**user**: donne la définition de concentration molaire en quantité de matière
[Timestamp: 2026/09/10 18:30:31]

**ai**: ## Concentration en quantité de matière

D'abord un point de vocabulaire : « concentration molaire » et « concentration en quantité de matière » désignent **la même grandeur**. « Concentration molaire » est l'ancien nom, encore très utilisé à l'oral ; le programme actuel dit « concentration en quantité de matière ». Dire « concentration molaire en quantité de matière » est donc un pléonasme — un seul des deux suffit.

**Définition.** La concentration en quantité de matière d'une espèce chimique dissoute dans une solution est la **quantité de matière de ce soluté** divisée par le **volume de la solution** :

$$c = \frac{n_{\text{soluté}}}{V_{\text{solution}}}$$

- $n$ : quantité de matière de soluté dissous, en **moles** (mol)
- $V$ : volume **de la solution**, en litres (L)
- $c$ : en **mol·L⁻¹**

Autrement dit : c'est le nombre de moles de soluté contenues dans un litre de solution. Une solution à $c = 0{,}10$ mol·L⁻¹ contient 0,10 mol de soluté par litre de solution.

### Notations

- $c$ ou $C$, avec précision de l'espèce entre parenthèses : $c(\text{NaCl})$
- $[\,X\,]$ (entre crochets) : notation équivalente, $[\text{NaCl}] = 0{,}10$ mol·L⁻¹

### Formule combinée

En reprenant $n = \dfrac{m}{M}$ de [[Séquence - Mole]], on obtient la formule qui part directement de la masse pesée :

$$c = \frac{n}{V} = \frac{m}{M \times V}$$

et le lien avec la concentration en masse :

$$c_m = c \times M \qquad \Longleftrightarrow \qquad c = \frac{c_m}{M}$$

### Points de vigilance

- $V$ est le volume de la **solution finale**, jamais celui du solvant ajouté ni celui du soluté.
- Grandeur **intensive** : un prélèvement de 10 mL d'une solution à 0,10 mol·L⁻¹ est toujours à 0,10 mol·L⁻¹. Ce qui change avec le volume prélevé, c'est $n$, pas $c$.
- Bien convertir les volumes en **litres** avant de calculer (250 mL = 0,250 L).

### Exemple

On dissout $m = 4{,}0$ g d'hydroxyde de sodium NaOH ($M = 40{,}0$ g·mol⁻¹) pour obtenir $V = 500$ mL de solution.

- $n = \dfrac{4{,}0}{40{,}0} = 0{,}10$ mol
- $c = \dfrac{0{,}10}{0{,}500} = 0{,}20$ mol·L⁻¹
- vérification par l'autre chemin : $c_m = \dfrac{4{,}0}{0{,}500} = 8{,}0$ g·L⁻¹, puis $c = \dfrac{8{,}0}{40{,}0} = 0{,}20$ mol·L⁻¹ ✓
[Timestamp: 2026/09/10 18:30:31]

**user**: si on double la quantité de matière comment évolue la concentration molaire
[Timestamp: 2026/09/10 18:47:05]

**ai**: À **volume de solution constant**, la concentration $c$ **double** elle aussi.

## Justification

$$c = \frac{n}{V}$$

$n$ est au numérateur et $V$ est fixé : $c$ est donc **proportionnelle** à $n$. Si on remplace $n$ par $2n$ :

$$c' = \frac{2n}{V} = 2 \times \frac{n}{V} = 2c$$

Plus généralement, si la quantité de matière est multipliée par un facteur $k$ à volume constant, la concentration est multipliée par le même facteur $k$ (triple → triple, divisée par 5 → divisée par 5).

**Exemple.** Dans $V = 0{,}500$ L :

- $n = 0{,}10$ mol → $c = \dfrac{0{,}10}{0{,}500} = 0{,}20$ mol·L⁻¹
- $n = 0{,}20$ mol → $c = \dfrac{0{,}20}{0{,}500} = 0{,}40$ mol·L⁻¹ ✓

## Le piège à éviter

La précision « **à volume constant** » est essentielle, parce qu'il y a deux façons très différentes de « doubler la quantité de matière » :

- **On dissout deux fois plus de soluté dans la même fiole de 500 mL** → $n$ double, $V$ inchangé, donc **$c$ double**. C'est le cas de la question.
- **On prélève deux fois plus de la même solution** (100 mL au lieu de 50 mL) → $n$ double *aussi* dans le prélèvement, mais $V$ double en même temps, donc $c$ est **inchangée**. C'est la nature *intensive* de la concentration : $\frac{2n}{2V} = \frac{n}{V} = c$.

Autrement dit, $c$ ne dépend pas de la taille de l'échantillon, mais du **rapport** entre soluté et volume de solution. Ce n'est que si l'un des deux varie *seul* que $c$ change.

## Deux remarques de rigueur

- La concentration en masse suit exactement la même logique : $c_m = \dfrac{m}{V}$ double aussi (cohérent avec $c_m = c \times M$, puisque $M$ ne change pas).
- On ne peut pas doubler indéfiniment : au-delà de la **solubilité** du soluté, l'excès ne se dissout plus et reste au fond. La solution est saturée, et $c$ plafonne à sa valeur maximale.
[Timestamp: 2026/09/10 18:47:05]

**user**: comment calculer la masse molaire
[Timestamp: 2026/09/10 18:57:58]

**ai**: ## Principe

La masse molaire $M$ d'une entité est la masse d'**une mole** de cette entité, c'est-à-dire de $6{,}02 \times 10^{23}$ exemplaires. Elle s'exprime en **g·mol⁻¹**.

Il y a trois cas, du plus simple au plus courant.

### 1. Masse molaire atomique

Elle ne se calcule pas : on la **lit dans le tableau périodique** (ou dans les données de l'exercice). Les valeurs à connaître de tête :

| Élément | H | C | N | O | Na | S | Cl |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $M$ (g·mol⁻¹) | 1,0 | 12,0 | 14,0 | 16,0 | 23,0 | 32,1 | 35,5 |

### 2. Masse molaire moléculaire

C'est le cas quasi systématique. La méthode :

- **Étape 1** — écrire la formule brute de la molécule et repérer combien il y a d'atomes de chaque élément.
- **Étape 2** — pour chaque élément, multiplier sa masse molaire atomique par son nombre d'atomes.
- **Étape 3** — additionner le tout.

$$M(\text{molécule}) = \sum \left( n_{\text{atome}} \times M_{\text{atome}} \right)$$

**Exemple : l'eau $H_2O$** (déjà dans [[Séquence - Mole]])

$$\begin{align} M_{H_2O} &= 2 \times M_H + M_O \\ &= 2 \times 1{,}00 + 16{,}0 \\ &= 18{,}0 \ \text{g·mol}^{-1} \end{align}$$

**Exemple plus lourd : l'acide éthanoïque $CH_3COOH$**, soit $C_2H_4O_2$

$$\begin{align} M &= 2 \times 12{,}0 + 4 \times 1{,}00 + 2 \times 16{,}0 \\ &= 24{,}0 + 4{,}0 + 32{,}0 \\ &= 60{,}0 \ \text{g·mol}^{-1} \end{align}$$

### 3. Masse molaire ionique

Exactement la même méthode : on **ignore la charge**, car la masse des électrons gagnés ou perdus est négligeable.

- $M(Na^+) = 23{,}0$ g·mol⁻¹
- $M(SO_4^{2-}) = 32{,}1 + 4 \times 16{,}0 = 96{,}1$ g·mol⁻¹
- Pour un solide ionique, on somme les ions du motif : $M(NaCl) = 23{,}0 + 35{,}5 = 58{,}5$ g·mol⁻¹

## Points de vigilance

- **Les indices se lisent bien.** Dans $Ca(OH)_2$, le 2 porte sur tout le groupe $OH$ : $M = 40{,}1 + 2 \times (16{,}0 + 1{,}00) = 74{,}1$ g·mol⁻¹. Erreur classique : n'appliquer le 2 qu'à l'hydrogène.
- **On additionne, on ne multiplie pas** les masses molaires entre elles.
- **Chiffres significatifs** : garde le même nombre de chiffres que tes données (en général 3), et n'arrondis qu'à la fin.
- **L'unité est toujours g·mol⁻¹** — pas des grammes. Une masse molaire n'est pas une masse.

## À quoi ça sert ensuite

La masse molaire est la charnière entre ce qu'on **pèse** (une masse, en g) et ce qu'on **compte** (une quantité de matière, en mol) :

$$n = \frac{m}{M} \qquad m = n \times M \qquad c = \frac{c_m}{M}$$

C'est pour ça qu'elle apparaît dans presque tous les calculs de la séquence.
[Timestamp: 2026/09/10 18:57:58]

**user**: et piu68H8O3
[Timestamp: 2026/09/10 19:01:16]

**ai**: 
[Timestamp: 2026/09/10 19:01:16]

**user**: C8H8O3
[Timestamp: 2026/09/10 19:01:25]

**ai**: $$\begin{align} M_{C_8H_8O_3} &= 8 \times M_C + 8 \times M_H + 3 \times M_O \\ &= 8 \times 12{,}0 + 8 \times 1{,}00 + 3 \times 16{,}0 \\ &= 96{,}0 + 8{,}0 + 48{,}0 \\ &= 152{,}0 \ \text{g·mol}^{-1} \end{align}$$

Soit **152 g·mol⁻¹** (3 chiffres significatifs).

Cette formule brute est celle de la **vanilline**, un classique des exercices et TP de première (dosage par étalonnage d'un extrait de vanille ou d'un sucre vanillé). Si c'est le contexte de ton exercice, les deux calculs qui suivent en général :

- une masse pesée → $n = \dfrac{m}{152}$
- une concentration en masse d'une solution étalon → $c = \dfrac{c_m}{152}$

Par exemple, pour une solution étalon à $c_m = 30$ mg·L⁻¹ = $0{,}030$ g·L⁻¹ :

$$c = \frac{0{,}030}{152} = 2{,}0 \times 10^{-4} \ \text{mol·L}^{-1}$$
[Timestamp: 2026/09/10 19:01:25]

**user**: on prélève 2.9*10-2 déduire la quantité préelvée
[Timestamp: 2026/09/10 19:06:57]

**ai**: L'unité manque dans ton énoncé, et elle change le calcul. Les deux cas possibles :

## Cas 1 — c'est une masse : $m = 2{,}9 \times 10^{-2}$ g

C'est le plus probable si l'exercice enchaîne sur la masse molaire que l'on vient de calculer. On utilise :

$$n = \frac{m}{M}$$

$$n = \frac{2{,}9 \times 10^{-2}}{152} = 1{,}9 \times 10^{-4} \ \text{mol}$$

La quantité de matière prélevée est donc d'environ **$1{,}9 \times 10^{-4}$ mol** de vanilline (soit 0,19 mmol).

## Cas 2 — c'est un volume : $V = 2{,}9 \times 10^{-2}$ L (= 29 mL)

Là, il faut la concentration $c$ de la solution dans laquelle on prélève :

$$n = c \times V$$

Il me manque la valeur de $c$ (ou de $c_m$) donnée par ton exercice pour finir le calcul.

---

Peux-tu me donner l'unité du 2,9×10⁻² (grammes ? litres ? mL ?) et la phrase complète de l'énoncé ? Je te confirme le bon calcul. Si c'était bien une masse en grammes, le résultat ci-dessus est ta réponse.
[Timestamp: 2026/09/10 19:06:57]

**user**: c'est en mol
[Timestamp: 2026/09/10 19:09:56]

**ai**: Si la valeur est **en mol**, alors elle *est déjà* une quantité de matière — il n'y a rien à en déduire directement. Ce qu'on te demande porte donc sur une des deux situations suivantes.

## Lecture A — c'est une concentration : $c = 2{,}9 \times 10^{-2}$ mol·L⁻¹

C'est le cas le plus probable (« mol » dit rapidement pour « mol·L⁻¹ »). On prélève alors un **volume** $V$ de cette solution :

$$n = c \times V$$

Il me faut le volume prélevé pour conclure. Deux valeurs classiques, à titre d'illustration :

- $V = 10{,}0$ mL $= 1{,}00 \times 10^{-2}$ L → $n = 2{,}9 \times 10^{-2} \times 1{,}00 \times 10^{-2} = 2{,}9 \times 10^{-4}$ mol
- $V = 20{,}0$ mL $= 2{,}00 \times 10^{-2}$ L → $n = 5{,}8 \times 10^{-4}$ mol

## Lecture B — c'est la quantité totale : $n_{\text{tot}} = 2{,}9 \times 10^{-2}$ mol dans toute la solution

On prélève une fraction du volume total, et la quantité prélevée suit la même proportion :

$$n_{\text{prélevée}} = n_{\text{tot}} \times \frac{V_{\text{prélevé}}}{V_{\text{total}}}$$

(ce qui revient au même : on calcule d'abord $c = \frac{n_{\text{tot}}}{V_{\text{total}}}$, puis $n = c \times V_{\text{prélevé}}$)

---

**Donne-moi le volume prélevé** (et le volume total de la solution si tu es dans la lecture B), et je fais le calcul. Le réflexe à retenir dans tous les cas : `quantité prélevée = concentration × volume prélevé`, avec le volume **converti en litres**.
[Timestamp: 2026/09/10 19:09:56]

**user**: c'est en mol
[Timestamp: 2026/09/10 19:11:13]

**ai**: D'accord, je te suis : la valeur est bien en mol.

Dans ce cas, la **quantité de matière prélevée est directement** :

$$n = 2{,}9 \times 10^{-2} \ \text{mol}$$

soit 29 mmol. Il n'y a pas de calcul intermédiaire : la quantité de matière *est* la grandeur qui s'exprime en mol, donc l'énoncé te la donne telle quelle. La « déduction » consiste simplement à reconnaître que l'unité mol identifie une quantité de matière — c'est ta réponse.

Les grandeurs que tu peux en tirer ensuite, si la suite de l'exercice les demande :

**La masse correspondante** (avec $M = 152$ g·mol⁻¹ pour $C_8H_8O_3$) :

$$m = n \times M = 2{,}9 \times 10^{-2} \times 152 = 4{,}4 \ \text{g}$$

**Le nombre d'entités** prélevées :

$$N = n \times N_A = 2{,}9 \times 10^{-2} \times 6{,}02 \times 10^{23} = 1{,}7 \times 10^{22} \ \text{molécules}$$

**Le volume prélevé**, si tu connais la concentration $c$ de la solution :

$$V = \frac{n}{c}$$

Si tu me colles la question exacte de l'exercice (et la question précédente), je te dis précisément laquelle de ces trois lignes on attend de toi.
[Timestamp: 2026/09/10 19:11:13]

**user**: n=2,9*10-2 mol
[Timestamp: 2026/09/10 19:14:45]

**ai**: Oui, c'est bien ça :

$$n = 2{,}9 \times 10^{-2} \ \text{mol}$$

C'est la quantité de matière prélevée, correctement exprimée en mol avec 2 chiffres significatifs.

Si la question suivante porte sur la masse de vanilline correspondante :

$$m = n \times M = 2{,}9 \times 10^{-2} \times 152 = 4{,}4 \ \text{g}$$
[Timestamp: 2026/09/10 19:14:45]

**user**: quelle unité
[Timestamp: 2026/09/10 19:16:10]

**ai**: La quantité de matière $n$ s'exprime en **mole**, de symbole **mol**. C'est l'unité SI de la quantité de matière.

Donc ici : $n = 2{,}9 \times 10^{-2}$ **mol** (soit 29 mmol, la millimole étant très pratique pour ces ordres de grandeur).

Les unités des grandeurs voisines, pour comparaison :

| Grandeur | Symbole | Unité |
| --- | --- | --- |
| Quantité de matière | $n$ | mol |
| Masse | $m$ | g (ou kg) |
| Masse molaire | $M$ | g·mol⁻¹ |
| Volume | $V$ | L (ou mL) |
| Concentration en quantité de matière | $c$ | mol·L⁻¹ |
| Concentration en masse | $c_m$ | g·L⁻¹ |
| Nombre d'entités | $N$ | sans unité |

Si ta question portait en fait sur une autre grandeur de l'exercice, dis-moi laquelle.
[Timestamp: 2026/09/10 19:16:10]

**user**: je veux dire quel unité pour le résultat
[Timestamp: 2026/09/10 19:18:35]

**ai**: Le dernier résultat calculé était la masse : l'unité est le **gramme (g)**.

$$m = 4{,}4 \ \text{g}$$

La vérification se fait par les unités elles-mêmes — c'est un bon réflexe de contrôle :

$$n \times M \ \longrightarrow \ \text{mol} \times \frac{\text{g}}{\text{mol}} = \text{g}$$

Les « mol » se simplifient, il ne reste que des grammes. Si tu avais obtenu des mol² ou des g·mol⁻¹, c'est que la formule était inversée (tu aurais divisé au lieu de multiplier).

Même contrôle pour les autres calculs de la séquence :

- $n = \dfrac{m}{M} \longrightarrow \dfrac{\text{g}}{\text{g·mol}^{-1}} = \text{mol}$
- $c = \dfrac{n}{V} \longrightarrow \dfrac{\text{mol}}{\text{L}} = \text{mol·L}^{-1}$
- $N = n \times N_A \longrightarrow$ sans unité (un nombre d'entités)
[Timestamp: 2026/09/10 19:18:35]

**user**: comment calculer la quantité de matière totale ntot avec V=3L n=0,05mol et une quantité n' de diazote à 21°C et 1013hpa
[Timestamp: 2026/09/10 19:27:26]

**ai**: ## L'idée

Le mélange gazeux occupe tout le volume $V = 3$ L. Donc l'**équation d'état du gaz parfait** appliquée au mélange entier donne directement la quantité de matière **totale** :

$$P \times V = n_{\text{tot}} \times R \times T \qquad \Longrightarrow \qquad \boxed{n_{\text{tot}} = \frac{P \times V}{R \times T}}$$

Ensuite, comme le mélange ne contient que les deux gaz :

$$n_{\text{tot}} = n + n' \qquad \Longrightarrow \qquad n' = n_{\text{tot}} - n$$

## Étape 1 — convertir les données en unités SI

C'est l'étape où l'on perd le plus de points. Avec $R = 8{,}314$ J·K⁻¹·mol⁻¹, il faut impérativement :

- **Pression en pascals** : $P = 1013$ hPa $= 1013 \times 100 = 1{,}013 \times 10^{5}$ Pa
- **Volume en m³** : $V = 3$ L $= 3 \times 10^{-3}$ m³ (car 1 L = 1 dm³ = $10^{-3}$ m³)
- **Température en kelvins** : $T = \theta + 273 = 21 + 273 = 294$ K

## Étape 2 — calculer $n_{\text{tot}}$

$$n_{\text{tot}} = \frac{1{,}013 \times 10^{5} \times 3 \times 10^{-3}}{8{,}314 \times 294} = \frac{304}{2444} = 0{,}124 \ \text{mol}$$

**$n_{\text{tot}} \approx 0{,}12$ mol**

Vérification des unités : $\dfrac{\text{Pa} \times \text{m}^3}{\text{J·K}^{-1}\text{·mol}^{-1} \times \text{K}} = \dfrac{\text{J}}{\text{J·mol}^{-1}} = \text{mol}$ ✓ (car 1 Pa·m³ = 1 J)

## Étape 3 — en déduire $n'$

$$n' = n_{\text{tot}} - n = 0{,}124 - 0{,}05 = 0{,}074 \ \text{mol}$$

**$n' \approx 0{,}07$ mol** de diazote (le résultat est limité par les 2 chiffres significatifs de $n = 0{,}05$ mol).

## Méthode alternative : le volume molaire

Même résultat, présentation parfois attendue. Le volume molaire dans ces conditions vaut :

$$V_m = \frac{R \times T}{P} = \frac{8{,}314 \times 294}{1{,}013 \times 10^{5}} = 2{,}41 \times 10^{-2} \ \text{m}^3\text{·mol}^{-1} = 24{,}1 \ \text{L·mol}^{-1}$$

$$n_{\text{tot}} = \frac{V}{V_m} = \frac{3}{24{,}1} = 0{,}124 \ \text{mol}$$

À retenir : $V_m \approx 24$ L·mol⁻¹ à 20 °C et pression atmosphérique (et 22,4 L·mol⁻¹ à 0 °C). C'est un bon ordre de grandeur pour contrôler ton résultat.

## Le point clé à comprendre

L'équation des gaz parfaits ne distingue pas les gaz entre eux : à $P$, $V$ et $T$ donnés, le nombre de moles est le même quelle que soit la nature du gaz. C'est pourquoi $\frac{PV}{RT}$ donne le **total** du mélange, et non la quantité d'un seul des deux gaz. On accède à $n'$ uniquement par différence.
[Timestamp: 2026/09/10 19:27:26]

**user**: ah et on connait deja le volume molaire V_m=24 L mol-1
[Timestamp: 2026/09/10 19:42:40]

**ai**: Parfait, ça simplifie beaucoup : plus besoin de l'équation des gaz parfaits ni de convertir en unités SI. Les données 21 °C et 1013 hPa servent alors juste à justifier **quelle** valeur de $V_m$ on utilise.

## Calcul

$$n_{\text{tot}} = \frac{V}{V_m} = \frac{3}{24} = 0{,}125 \ \text{mol}$$

$$n' = n_{\text{tot}} - n = 0{,}125 - 0{,}05 = 0{,}075 \ \text{mol}$$

Soit **$n_{\text{tot}} = 0{,}125$ mol** et **$n' \approx 0{,}075$ mol** de diazote (arrondi à 0,08 mol si tu t'en tiens à 2 chiffres significatifs).

## À retenir sur cette formule

$$n = \frac{V}{V_m}$$

- $V$ : volume du gaz, en **L**
- $V_m$ : volume molaire, en **L·mol⁻¹**
- $n$ : en mol

Ici les deux volumes sont dans la même unité (L), donc **aucune conversion** : les litres se simplifient et il reste des mol. C'est le pendant exact de $n = \frac{m}{M}$ pour les solides et liquides — on divise ce qu'on mesure par la « taille d'une mole » :

| Ce qu'on mesure | Grandeur « par mole » | Formule |
| --- | --- | --- |
| une masse $m$ (g) | masse molaire $M$ (g·mol⁻¹) | $n = \dfrac{m}{M}$ |
| un volume de gaz $V$ (L) | volume molaire $V_m$ (L·mol⁻¹) | $n = \dfrac{V}{V_m}$ |
| un nombre d'entités $N$ | constante d'Avogadro $N_A$ | $n = \dfrac{N}{N_A}$ |

Ces trois lignes couvrent tous les calculs de quantité de matière de la séquence [[Séquence - Mole]].
[Timestamp: 2026/09/10 19:42:40]

**user**: comment déduire n'
[Timestamp: 2026/09/10 19:52:24]

**ai**: ## Le raisonnement

La quantité de matière est un **comptage d'entités**. Dans le récipient, il n'y a que deux sortes de molécules : celles du premier gaz (comptées par $n$) et celles du diazote (comptées par $n'$). Le total est donc leur somme :

$$n_{\text{tot}} = n + n'$$

C'est ce qu'on appelle l'**additivité des quantités de matière** : contrairement aux concentrations ou aux volumes, les quantités de matière d'un mélange s'additionnent sans précaution.

On isole ensuite $n'$ en faisant passer $n$ de l'autre côté :

$$n' = n_{\text{tot}} - n$$

## Application

$$n' = 0{,}125 - 0{,}05 = 0{,}075 \ \text{mol}$$

## La logique d'ensemble

Le point important, c'est **l'ordre des étapes** — tu ne peux pas calculer $n'$ directement :

- Le gaz parfait (ou $V_m$) te donne **le total**, parce qu'il ne distingue pas les gaz : $n_{\text{tot}} = \dfrac{V}{V_m} = 0{,}125$ mol.
- L'énoncé te donne **une des deux parts** : $n = 0{,}05$ mol.
- L'autre part s'obtient donc forcément **par différence**.

## Vérification

Un bon réflexe pour valider : on recompose le total.

$$0{,}05 + 0{,}075 = 0{,}125 \ \text{mol} = n_{\text{tot}} \ ✓$$

Et le résultat est cohérent en ordre de grandeur : $n'$ est du même ordre que $n$, et positif — si tu avais trouvé une valeur négative, cela signifierait une erreur (le plus souvent une conversion de volume ou de température ratée en amont).
[Timestamp: 2026/09/10 19:52:24]