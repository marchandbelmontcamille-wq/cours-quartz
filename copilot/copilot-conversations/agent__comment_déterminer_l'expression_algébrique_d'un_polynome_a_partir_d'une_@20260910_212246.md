---
epoch: 1789068166846
mode: agent
backendId: claude
sessionId: "03850031-6187-416a-a210-c74aae384f40"
agentLabel: "comment déterminer l'expression algébrique d'un polynome a p…"
usage: '{"usedTokens":37900,"contextWindow":200000,"inputTokens":2,"outputTokens":3,"cacheReadTokens":33932,"cacheWriteTokens":3963,"updatedAt":1789068401822}'
tags:
  - copilot-conversation
---

**user**: comment déterminer l'expression algébrique d'un polynome a partir d'une courbe
[Timestamp: 2026/09/10 21:22:46]

**ai**: I'll look at your note d'exercices to voir le contexte exact.## Le principe général

Une fonction polynôme du second degré $f(x)=ax^2+bx+c$ est déterminée par **3 inconnues** : $a$, $b$ et $c$. Il faut donc récupérer **3 informations** sur la courbe pour les trouver. Chaque point lu sur la parabole donne une équation, du type :

$$f(x_A)=y_A$$

La stratégie est toujours la même : lire les informations « gratuites » d'abord, puis compléter avec des points quelconques.

## Étape 1 — Lire les informations gratuites

**L'ordonnée à l'origine donne $c$ directement.**
C'est la propriété de ton chapitre : la parabole coupe l'axe des ordonnées en $(0;c)$. Donc si la courbe passe par $(0;1)$, alors $c=1$. Une inconnue éliminée sans calcul.

**Le signe de $a$ se lit sur l'orientation.**
Branches vers le haut → $a>0$ ; branches vers le bas → $a<0$. Ça ne donne pas la valeur, mais ça permet de **vérifier** ton résultat à la fin.

**L'axe de symétrie aide beaucoup.**
Si tu repères deux points $M$ et $N$ de même ordonnée (même image), l'axe de symétrie passe par le milieu de $[MN]$ : $x=\alpha$ avec $\alpha=\frac{x_M+x_N}{2}$. Le sommet a donc pour abscisse $\alpha$. C'est exactement le raisonnement que tu as fait dans la Partie B, question 4 de tes exercices.

## Étape 2 — Écrire une équation par point lu

Pour chaque point $A(x_A;y_A)$ visiblement sur la courbe (choisis des points aux coordonnées entières, sinon la lecture est fausse) :

$$a\,x_A^{\,2}+b\,x_A+c=y_A$$

## Étape 3 — Résoudre le système

Exemple sur ta Partie D : la courbe passe par $A(0;1)$ et $B(1;5)$.

- $A(0;1)$ donne $c=1$, donc $f(x)=ax^2+bx+1$
- $B(1;5)$ donne $f(1)=5$ :

$$a\times 1^2+b\times 1+1=5 \quad\Longrightarrow\quad a+b=4$$

Il reste **deux** inconnues et **une seule** équation : il faut donc lire un troisième point sur le graphique. Par exemple si la courbe passe aussi par $C(-1;1)$ :

$$a\times(-1)^2+b\times(-1)+1=1 \quad\Longrightarrow\quad a-b=0 \quad\Longrightarrow\quad a=b$$

En remplaçant dans $a+b=4$ : $2a=4$, donc $a=2$ et $b=2$, ce qui donne $f(x)=2x^2+2x+1$.

## Étape 4 — Vérifier

Reprends un point de la courbe **que tu n'as pas utilisé** et calcule son image. Si tu retrouves l'ordonnée lue, l'expression est bonne. Vérifie aussi que le signe de $a$ correspond bien à l'orientation des branches.

## Les raccourcis quand la courbe est bien placée

Ces deux cas font gagner beaucoup de temps, mais ils supposent des formes que ton chapitre n'a pas encore introduites (formes canonique et factorisée) :

- **Si tu vois le sommet $S(\alpha;\beta)$** : $f(x)=a(x-\alpha)^2+\beta$. Il ne reste qu'**une** inconnue, $a$, qu'un seul autre point suffit à déterminer.
- **Si tu vois les deux points d'intersection avec l'axe des abscisses**, d'abscisses $x_1$ et $x_2$ : $f(x)=a(x-x_1)(x-x_2)$. Là encore, un seul point supplémentaire suffit.

Ensuite tu développes pour revenir à la forme $ax^2+bx+c$ si l'énoncé la demande.

---

Le piège principal : **ne jamais lire des coordonnées approximatives**. Si un point tombe entre deux carreaux, cherche-en un autre — une erreur de lecture de $0{,}5$ fausse tout le système.

Si tu veux, je peux ajouter cette méthode dans ton chapitre [[Chapitre 1 - Polynomes du 2nd degré]], ou compléter les questions laissées en suspens dans [[Act1]] (Partie B question 5, Partie D) si tu me donnes les points visibles sur les graphiques.
[Timestamp: 2026/09/10 21:22:46]

**user**: j'ai A(0;1)
[Timestamp: 2026/09/10 21:24:56]

**ai**: Avec seulement $A(0;1)$ on ne peut pas conclure : ça ne donne que $c=1$, donc il reste deux inconnues. Mais j'ai regardé ton graphique dans ![[content/images/MA-2.png]] (Partie D) : il y a **trois** points marqués d'une croix, et c'est exactement ce qu'il te faut.

- $A(0;1)$
- $B(1;5)$
- $C(2;3)$

## Résolution complète de la Partie D

**On pose** $f(x)=ax^2+bx+c$.

**Point $A(0;1)$** — il est sur l'axe des ordonnées, donc $c=1$ directement :

$$f(x)=ax^2+bx+1$$

**Point $B(1;5)$** — donc $f(1)=5$ :

$$a\times 1^2+b\times 1+1=5 \quad\Longrightarrow\quad a+b+1=5 \quad\Longrightarrow\quad a+b=4$$

**Point $C(2;3)$** — donc $f(2)=3$ :

$$a\times 2^2+b\times 2+1=3 \quad\Longrightarrow\quad 4a+2b+1=3 \quad\Longrightarrow\quad 4a+2b=2$$

**Le système :**

$$\begin{cases} a+b=4 \\ 4a+2b=2 \end{cases}$$

De la première équation : $b=4-a$. On remplace dans la seconde :

$$\begin{align} 4a+2(4-a)&=2 \\ 4a+8-2a&=2 \\ 2a&=-6 \\ a&=-3 \end{align}$$

Puis $b=4-(-3)=7$.

**Conclusion :**

$$f(x)=-3x^2+7x+1$$

## Vérification

- $f(0)=1$ ✓ (point $A$)
- $f(1)=-3+7+1=5$ ✓ (point $B$)
- $f(2)=-3\times 4+14+1=-12+15=3$ ✓ (point $C$)
- $a=-3<0$, donc les branches sont orientées vers le bas — c'est bien ce qu'on voit sur le graphique ✓

Le sommet se situe légèrement à droite de $x=1$, un peu au-dessus de $5$, ce qui correspond aussi au tracé.

---

Veux-tu que je complète cette Partie D dans ta note [[Act1]] ? Il te reste aussi la question 5 de la Partie B en suspens, et la fin de la question 4 (« son ordonnée est… ») — pour celle-là, avec $f(x)=3x^2-6x-1$ et $x_S=1$, on trouve $f(1)=3-6-1=-4$, donc $S(1;-4)$.
[Timestamp: 2026/09/10 21:24:56]