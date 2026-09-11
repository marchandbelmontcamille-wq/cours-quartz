---
epoch: 1788690476000
mode: agent
backendId: claude
sessionId: "b76a4157-3cb6-495c-973f-b6d82dc0f6d5"
agentLabel: "si deux antécédents ont la mme image que peut on déduire"
usage: '{"usedTokens":33759,"contextWindow":200000,"inputTokens":2,"outputTokens":3,"cacheReadTokens":24711,"cacheWriteTokens":9043,"updatedAt":1788690548926}'
tags:
  - copilot-conversation
---

**user**: si deux antécédents ont la mme image que peut on déduire
[Timestamp: 2026/09/06 12:27:56]

**ai**: Ta question 3 de la Partie B porte sur $f(x)=3x^2-6x-1$, avec $f(0)=-1$ et $f(2)=-1$ (les deux réponses que tu as déjà notées).

## Ce qu'on peut déduire

Deux antécédents **distincts** ont la même image, donc :

1. **La fonction n'est pas injective** : le réel $-1$ admet (au moins) deux antécédents, $0$ et $2$. Une image peut avoir plusieurs antécédents, alors qu'un antécédent n'a qu'une seule image.
2. **Surtout : ces deux points sont symétriques par rapport à l'axe de symétrie de la parabole.** C'est la déduction attendue ici, parce que tu as écrit en Partie A qu'une parabole possède un axe de symétrie passant par le sommet. Cet axe a donc pour équation
$$x=\frac{0+2}{2}=1$$

## Pourquoi ça marche (justification générale)

Si $f(x)=ax^2+bx+c$ et $f(x_1)=f(x_2)$ avec $x_1\neq x_2$ :

$$a(x_1^2-x_2^2)+b(x_1-x_2)=0 \iff (x_1-x_2)\big(a(x_1+x_2)+b\big)=0$$

Comme $x_1\neq x_2$, on obtient $x_1+x_2=-\dfrac{b}{a}$, c'est-à-dire

$$\frac{x_1+x_2}{2}=-\frac{b}{2a}=\alpha \quad(\text{abscisse du sommet})$$

Vérification ici : $-\dfrac{b}{2a}=\dfrac{6}{6}=1$ ✔

## Ce que ça te donne pour la suite

C'est exactement le point de départ de la question 4 : l'abscisse du sommet est $\alpha=1$, donc

$$f(1)=3-6-1=-4 \quad\Rightarrow\quad S(1\,;\,-4)$$

Et comme $a=3>0$, la parabole est tournée vers le haut : $f$ est décroissante sur $]-\infty\,;1]$ puis croissante sur $[1\,;+\infty[$, avec un minimum de $-4$ atteint en $1$ — de quoi remplir le tableau de variations de la question 5.

Veux-tu que j'ajoute la rédaction des questions 3, 4 et 5 dans [[Act1]] ?
[Timestamp: 2026/09/06 12:27:56]