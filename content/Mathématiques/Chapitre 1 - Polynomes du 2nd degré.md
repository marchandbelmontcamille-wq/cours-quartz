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