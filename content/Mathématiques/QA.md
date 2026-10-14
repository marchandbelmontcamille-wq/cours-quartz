## I- Fonction polynôme du second degré
### 1) Définition
>[!INFO] Définition
>On appelle fonction polynôme du second degré toute fonction définie sur $]-\infty;+\infty[$ pour laquelle il existe des réels a, b et c, avec $a\ne 0$, tels que $f(x)=ax^2+bx+c$. Cette epression s'appelle forme développée

>[!TIP] Remarque
>Si $a=0$ : $f(x)=bx+c$ est un polynôme du premier degré (=fonction affine)

>[!EXAMPLE] Exemple
>$f(x)=2x^2+x+3$
>$a=2\text {   } b=1\text {   } c=3$
>
>$g(x)=3x^2-2x-5$
>$a=3\text {   } b=-2\text {   } c=-5$
>
>$h(x)=\frac {1} {3}x^2-6x$
>$a=\frac{1} {3}\text {   } b=-6\text {   } c=0$
>
>$k(x)=x^2$
>$a=1 b=0 c=0$

>[!CITE] Vocabulaire
>- $a$, $b$ et $c$ sont appelés les coefficients du polynôme
>- $a$ est le coefficient dominant
>- $c$ est le coefficient constant


### 2) Courbe représentative
>[!INFO] Définition
>La courbe représentative d'une fonction trinôme est une parabole
>Le "point le plus haut" ou "le point le plus bas" de la parabole est appelé sommet

>[!NOTE] Propriété
>- Lorsque le coefficient dominant $a$ est positif : Les branches de la parabole sont orientées vers le haut et le sommet est le point le plus bas de la parabole
>- Lorsque le coefficient dominant $a$ est négatif : Les branches de la parabole sont orientées vers le bas et le sommet est le point le plus haut de la parabole

>[!TIP] Remarque
>- La parabole a un arc de symétrie qui est vertical / parallèle à l'axe (0y)
>- Plus le coef dominant $a$ s'éloigne de 0, plus les branches se rapprochent de l'axe de symétrie
>- Plus le coef dominant $a$ s'approche de 0, plus les branches s'éloignent de l'axe de symétrie

>[!NOTE] Propriété
>La parabole coupe l'axe des ordonnées à l'ordonnée $c$
>>[!EXAMPLE] Exemple
>>On calcule l'image de 0 par f
>>$f(x)=ax^2+bx+c$
>>$f(x0)=a\times 0^2+b\times 0+c=c$
>>Ainsi la parabole passe par le point $(0;c)$

### 3) Forme canonique
>[!NOTE] Propriété
>Toute fonction $f$ du polynôme du second degré, dont la forme développée est $ax^2+bx+c$ peut s'écrire : 
>$$f(x)=a(x-\alpha)^2+\beta$$
>avec $\alpha=........$ et $\beta=f(\alpha)$
>Cette expression s'appelle forme canonique de $f$
>>[!TIP] Méthode
>>1) Factoriser par a dans les deux premiers membres de $f(x)$
>>2) Identifier le facteur au début d'une identité remarquable
>>3) Remplace le facteur par l'identité remarquable
>>4) Calculer et réduire pour trouver la forme canonique
>
>>[!EXAMPLE] Exemple
>>$\begin {align}f(x)&=3x^2-24x+10\\&=3(x^2-8x)+10\\&=3[(x-4)^2-4^2]+10\\&=3[(x-4)^2-16]+10\\&=3(x-4)^2-3\times 16+10\\&=3(x-4)^2-38\end {align}$ avec $\alpha=4$ et $\beta=-38$

>[!EXAMPLE] Exemple :
>$$
>\begin {align} g(x)&=3x^2+6x+1\\&=3(x^2+2x)+1\\&x^2+2xy\\&=3[(x+1)^2-1^2]+1\\&=3(x+1)^2-3+1\\&=3(x+1)^2-2\\&\alpha=-1\\&\beta=-2\end {align}
>$$

>[!TIP] Demonstration 
>$$\begin {align}&=\boxed {ax^2+bx+c}\\&=a(x^2+\frac {b} {a}x)+c\\&=(x^2+2\times\frac {b} {2a}x)+c\\&x^2+2yx=(x+y)^2-y\\&=a[(x+\frac {b} {2a})^2-\frac {b} {2a}]+c\\&=a(x+\frac {b} {2a})^2-a(\frac {b} {2a})+c\\&=a(x+\frac {b} {2a})^2-a\times\frac {b^2}{2^2\times a^2}+c\\&=a(x+\frac{b} {2a})^2-\frac {b^2}{4a}+c\\&=a(x-(-\frac {b} {2a}))^2-\frac {b^2} {4a}+c\\&=\boxed {a(x-\alpha)^2+\beta}\end {align}
$$

>[!NOTE] Propriété
>La parabole représentative de $f(x)=a(x-\alpha)^2+\beta$ a pour axe de symétrie la droite d'équation $\boxed {x=\alpha}$

>[!TIP] Démonstration
>Soit $f(x)=a(x-\alpha)^2+\beta$
>Soit $M$ et $N$ deux points tels que (avec $\epsilon>0$) :
>$x_M=\alpha-\epsilon$ et $x_N=\alpha+\epsilon$
>$M$ et $N$ sont sur la parabole donc
>$\begin {align} y_M&=f(x_M) \\&=a(x_M-\alpha)^2+\beta\\&=a(\alpha-\epsilon-\alpha)^2+\beta\\&=a(\epsilon)^2+\beta\\&=a\epsilon^2+\beta\\ \\y_N&=f(x_N)\\&=a(x_N-\alpha)^2+\beta\\&=a(\alpha+\epsilon-\alpha)^2+\beta\\&=a\epsilon^2+\beta\end {align}$
>Ainsi $y_M=y_N$ donc $M$ et $N$ sont symétriques l'un de l'autre sur la parabole. L'axe de symétrie passe alors par le milieu de $[MN]$. Donc l'axe de symétrie a pour équation $\boxed {x=\alpha}$

>[!NOTE] Propriété
>Le sommet de la parabole a pour coordonnées $\boxed{S(\alpha;\beta)}$

>[!TIP] Démonstration
>Le sommet S se trouve sur l'axe de symétrie donc $x_S=\alpha$. Et, il se trouve sur la parabole, donc $y_S=f(x_S)=f(\alpha)=a(\alpha-\alpha)^2+\beta=\beta$

>[!EXAMPLE] Exemples :
>$f(x)=-2(x+3)^2+5$
>1) $S(-3;5)$
>2) $-2x^2-12x-18+5$

### 4) Variations
>[!NOTE] Théorème
>Soit f une fonction trinôme telle que $f(x)=ax^2+bx+c=a(x+\alpha)^2+\beta$
>- Si $a<0$ : Les branches pointent vers le bas
>- Si $a>0$ : Les branches pointent vers le haut

## II- Factorisation d'équation
### 1) Forme factorisée
>[!NOTE] Définition :
>Soit $f$ une fonction polynôme du second degré de forme développée $f(x)=ax^2+bx+c$. On appelle discriminant de $f$le réel noté $\triangle$ : $\boxed {\triangle=b^2-4ac}$

>[!EXAMPLE] Exemple :
>$f(x)=6x^2-5x+3$
>Calculer le discriminant :
>$\begin {align}\triangle&=5^2+4\times6\times3 \\&=97\end {align}$

>[!NOTE] Théorème de factorisation
>Soit $f$ un trinôme de forme développée $f(x)=ax^2+bx+c$ et $\triangle$ son discriminant
>- Si $\triangle >0$ alors $f$ est factorisable et on a $f(x)=a\times(x-x_1)\times(x-x_2)$ avec $x_1=\frac {-b-\sqrt {\triangle}} {2a}$ et $x_2=\frac {-b+\sqrt {\triangle}} {2a}$
>- Si $\triangle=0$ alors f est factorisable et on a $f(x)=a\times(x-x_0)^2$ avec $x_0=\frac {-b} {2a}$
>- C'est la forme factorisée de $f$
>- Si $\triangle<0$ alors $f$ n'est pas factorisable dans $R$

>[!EXAMPLE] Exemple :
>$f(x)=2x^2-4x-6$
>1) Calculer le discriminant
>$\triangle=b^2-4ac=(-4)^2-4\times 2\times(-6)=64$
>2) Déterminer la F.F de $f$
>$f(x)=a(x-x_1)(x-x_2)$ avec $x_1=\frac{-(-4)-\sqrt {64}} {2\times 2}=\frac{4-8} {4}=-1$ et $x_2=\frac {4+8} {4}=\frac {12} {4}=4$ 
>Donc $f(x)=2(x+1)(x-3)$
>
>$g(x)=3x^2-3x+\frac {3} {4}$
>1) Calculer le discriminant
>$\triangle=b^2-4ac=(-3)^2-4\times3\times\frac{3} {4}=9-9=0$ 
>2) Déterminer la F.F
>Le discriminant est nul donc
>$g(x)=a(x-x_0)=(x-\frac {-b}{2a})^2=3(x-\frac {1} {2})^2$

>[!NOTE] A quoi sert la F.F
>Si on a $f(x)=a(x-x_1)(x-x_2)$
>$x_1$ et $x_2$ sont les antécédents de 0 par $f$

>[!EXAMPLE] Exemple
>$f(x)=2x^2-4x-6=2(x+1)(x-3)$
>$x=x_1=-1$
>$f(-1)=2(-1+1)(-1+3)=2\times 0\times (-4)$
>$x=x_2=3$
>$f(3=)$
>demander le cours

### 2) Résolution d'équations du second degré
>[!NOTE] Théorème
>Soit $a$, $b$, $c$ trois réels, $a\ne0$
>L'équation $ax^2+bx+c=0$ est une équation du second degré
>- Si $\triangle>0$ alors l'équation admet deux solutions réelles et distinctes :
>$x_1=\frac {-b-\sqrt {\triangle}} {2a}$ et $x_2=\frac {-b+\sqrt {\triangle}} {2a}$
>- Si $\triangle=0$ alors l'équation admet une solution réelle "double" :
>$x_0=-\frac {b} {2a}$
>- Si $\triangle<0$, alors l'équation n'a pas de solution réelle

>[!TIP] Méthode
>$f(x)=ax^2+bx+c$
>1) On calcule le discriminant $\triangle=b^2-4ac$
>2) 
>- Si $\triangle>0$ : deux solutions réelles distinctes $x_1=\frac {-b-\sqrt {\triangle}} {2a}$ et $x_2=\frac {-b+\sqrt {\triangle}} {2a}$
>- Si $\triangle=0$ : une unique solution $x_0=\frac {-b}{2a}$
>- Si $\triangle<0$ : L'équation n'a pas de solution réelle

### 3) Somme et produit de racine
>[!NOTE] Définition
>On appelle racine du trinôme $ax^2+bx+c$ la ou les solutions de l'équation $ax^2+bx+c=0$.
>Les racines sont les antécédents de 0 par le trinôme $ax^2+bx+c$

>[!NOTE] Propriété
>Soit $ax^2+bx+c$ un trinôme dont les racines réelles sont $x_1$ et $x_2$
>Alors :
>$x_1+x_2^=$
>$x_1\times x_2=$

>[!TIP] Démonstration
>$$
\begin {align}x_1+x_2&=\frac {-b-\sqrt {\triangle}} {2a}+\frac {-b+\sqrt {\triangle}} {2a}\\&=\frac {-b-\sqrt {\triangle}-b+\sqrt {\triangle}} {2a}\\&=\frac {-2b} {2a}\\&=-\frac {b} {a} \end {align}
>$$
>$$
\begin {align}x_1\times x_2&=(\frac {-b-\sqrt {\triangle}} {2a})\times(\frac {-b+\sqrt {\triangle}} {2a})\\&=\frac {(-b-\sqrt {\triangle})\times(-b+\sqrt {\triangle})}{4a^2}\\&=\frac {(-b)^2-\sqrt {\triangle}^2} {4a^2}\\&=\frac {b^2-\triangle} {4a^2}\\&=...\\&=\boxed{\frac {c} {a}} \end {align}
>$$
## III- Signe du trinôme
![[Fichier a mettre.png]]
- $\triangle>0$ :
$$
\begin {align}f(x)&=ax^2+bx+c\\&=a(x-\alpha)+\beta\\&=a(x-x_1)(x-x_2)\\&\text{avec }x_1<x_2 \end {align}
$$
![[Pasted image 20260925100011.png]]
- $\triangle=0$ :
$$
\begin {align}f(x)&=ax^2+bx+c\\&=a(x-x_0)^2 \end {align}
$$
![[Pasted image 20260925100358.png]]
- $\triangle<0$ :
$$
\begin {align}f(x)&=ax^2+bx+c\\&=a(x-\alpha)+\beta\end {align}
$$
![[Pasted image 20260925100456.png]]

>[!NOTE] Théorème
>Soit $f(x)=ax^2+bx+c$ un trinôme, $\triangle=b^2-4ac$ son discriminant
>- Si $\triangle>0$ : **Le trinôme est du signe de son coeff dominant $a$ à l'extérieur des racine**s : De $-\infty$ à $x_1$, c'est le signe de $a$, de $x_1$ à $x_2$, c'est le signe de $-a$ et de $x_2$ à $+\infty$, c'est le signe de a
>- Si $\triangle=0$ : **Le trinôme est du signe du coefficient dominant $a$ et s'annule en $x_0$** : de $-\infty$ à $x_0$ et de $x_0$ à $+\infty$, c'est le signe de $a$
>- Si $\triangle<0$ : **le trinôme est du signe de son coefficient dominant** $a$ : De $-\infty$ à $+\infty$, c'est le signe de $a$

>[!TIP] Méthode
>Résoudre une inéquation du 2nd degré
>1° Ramener l'équation à 0
>2° Calculer le discriminant $\triangle=b^2-4ac$
>3° Selon le discriminant :
>- $\triangle>0$ : On calcule les racines +tableau de signes justifié
>- $\triangle=0$ : On calcule la racine + tableau de signes justifié
>- $\triangle<0$ : Tableau de signes justifié
>
>4° Répondre à la question !

---
**$-2x^2+x+3\ge0$**
On calcule le discriminant
$$
\begin {align}\triangle&=b^2-4ac\\&=1^2-4\times-2\times3\\&=25 \end {align}
$$
$\triangle>0$ : Le trinôme a deux racines réelles distinctes  
$$
\begin{align}x_1&=\frac {-b-\sqrt {\triangle}}{2a}\\&=\frac {-1-\sqrt {25}} {-4}\\&=1,5\\x_2&=\frac {-b+\sqrt {\triangle}}{2a}\\&=-1 \end {align}
$$
D'ou le tableau :
Le trinôme est du signe de son coeff dominant $a$ à l'extérieur des racines
-|+|-
Les solutions sont $S=[-1;-1,5]$

---
$$
\begin {align}&x^2-4x\ge5\\<=>\text { }&x^2-4x-5\ge0 \end {align}
$$
On calcule le discriminant
$$
\begin {align}\triangle&=b^2-4ac\\&=-4^2-4\times1\times-5\\&=36 \end {align}
$$
$\triangle>0$, donc le trinôme à deux racines réelles et distinctes
$$
\begin {align}x_1&=\frac {-b-\sqrt {\triangle}} {2a}\\&=\frac {4-\sqrt{36}} {2}\\&=-1\\x_2&=\frac {-b+\sqrt {\triangle}} {2a} \\&=5\end {align}
$$
D'ou le tableau :
Le trinôme est du signe de son coeff dominant $a$ à l'extérieur des racines
+|-|+
Les solutions sont $S=[-1;5]$

---
$$
\begin {align}&x^2+x<1\\<=>\text{ }&x^2+x-1<0 \end {align}
$$
On calcule le discriminant
$$
\begin {align}\triangle&=b^2-4ac\\&=1^2-4\times1\times-1\\&=1+4\\&=5 \end {align}
$$
$\triangle>0$  : le trinome a deux racines réelles distinctes
$$
\begin {align}x_1&=\frac {-b-\sqrt{\triangle}} {2a}\\&=\frac{-1-\sqrt {5}} {2}\\x_2&=\frac{-1+\sqrt{\triangle}} {2a}\\&=\frac {-1+\sqrt {5}} {2} \end {align}
$$

D'ou le tableau :
Le trinôme est du signe de son coeff dominant $a$ à l'extérieur des racines
+|-|+
Les solutions sont $S=[\frac{-1-\sqrt {5}} {2};\frac{-1+\sqrt {5}} {2}]$ 

---
$$
\begin {align}&x^2<x-2\\<=>\text { }&x^2-x+2<0\end {align}
$$
On calcule le discriminant
$$
\begin {align}\triangle&=b^2-4ac\\&=1-4\times1\times2\\&=-7 \end {align}
$$
$\triangle<0$ : Le trinome n'a pas de racine
D'ou le tableau
Le trinome est le signe de son coeff dominant
+