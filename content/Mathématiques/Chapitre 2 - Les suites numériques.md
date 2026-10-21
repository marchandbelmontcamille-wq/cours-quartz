## I- Mode de génération d'une suite
### 1) Définition et notation
>[!INFO] Définition
>Une suite numérique $u$ est une fonction définie pour tout entier naturel $n$, tel que n$\ge n_0$ avec $n_0$ un entier naturel donné. Cette fonction est à valeurs réelles
>Pour chaque entier $n\ge n_0$, on associe le nombre $u(n)$, noté $u_n$
>$$u:n\mapsto u(n)=u_n$$
>Le réel $u_n$ se lit "u indice n" est le terme de rang $n$ de la suite
>Le réel $u_{n_{0}}$ est le premier terme de la suite
>La suite se nomme $(u_n)$ ou $(u_n)_{n\ge n_0}$

>[!EXAMPLE] Exemple Thème 1
>$n$ : nb de points
>$s_n$ : nb de segments constructibles avec $n$ points
>$s_1=0$
>$s_2=1$
>$s_3=3$

>[!EXAMPLE] Exemple
>$u_0=50$
>$u_1=25$
>$u_2=12,5$
>$u_3=6,25$

### 2) Formule explicite
>[!INFO] Définition
>Une suite est définie par une formule explicite lorsque $u_n$ s'exprime en fonction de $n$. Dans ce cas, on peut calculer chaque terme en remplaçant directement la valeur de $n$

## 3) Formule de récurrence
>[!INFO] Définition 
>Une suite est définie par une relation de récurrence lorsque $(u_n)$ est définie par la donnée de son premier terme et d'une relation permettant de calculer un terme à partir de son (ses) terme(s) précédent(s).
>Dans ce cas, pour calculer un terme, il faut connaitre tous les termes précédents
## II- Etude d'une suite
### 1) Représentation graphique d'une suite
>[!TIP] Méthode
>Ici on a $u_{n+1}=f(u_n)$
>Pour construire les termes de la suite sur l'axe des abcisses
>-> On place le premier terme $u_0$
>-> On sait que $u_1=f(u_0)$. On va représenter graphiquement $u_1$ comme l'image de $u_0$
>$u_0$-> Courbe de f -> axe des ordonnées=$u_1$
>On bascule ensuite $u_1$, ainsi construit sur l'axe (Ox)
>$u_1$=axe des ordonnées-> droite $y=x$ -> axe des abscisses

### 2) Sens de variation d'une suite
>[!NOTE] Définition
>Etudier le sens de variation d'une suite c'est préciser si elle est croissante, décroissante ou constante
>- La suite $(u_n)$ est dite croissante à partir du rang p si pour tout entier naturel $n$ : $n\ge p => u_n>u_p$ 
>- La suite $(u_n)$ est dite décroissante à partir du rang p si pour tout entier naturel $n$ : $n\le p => u_n+1<u_n$
>- La suite $(u_n)$ est dite monotone si elle est croissante (ou décroissante) sur tout son ensemble de définition. Elle ne change pas de variation

>[!NOTE] Propriété
>- $(u_n)$ est strictement croissante à partir du rang p $<=>$ Pour tout entier naturel $n$, $n\ge p$ : $u{n+1}-u_n>0$ 
>- $(u_n)$ est strictement décroissante à partir du rang p $<=>$ Pour tout entier naturel $n$, $n\ge p$ : $u_{n+1}-u_n<0$
>- $(u_n)$ est constante à partir du rang p $<=>$ Pour tout entier naturel $n$, $n\ge p$ : $u_{n-1}-u_n=0$

>[!TIP] Méthode
>Pour étudier la variation d'une suite $(U_n)$
>1) On calcule : $\forall n\in\mathbb{N}$ : $u_{n+1}-u_n$
>2) On cherche son signe : Strict. positif -> Strict. croissant / strict. négatif -> strict. décroissant

>[!NOTE] Propriété
>- $(u_n)$ est strictement croissante à partir du rang p $<=>$ Pour tout entier naturel $n$, $n\ge p$ : $\frac {u_{n+1}}{u_n}>1$
>- $(u_n)$ est strictement croissante à partir du rang p $<=>$ Pour tout entier naturel $n$, $n\ge p$ : $\frac {u_{n+1}}{u_n}<1$

>[!TIP]
>Pour étudier la variation d'une suite $(u_n)$ strictement positive :
>1) On calcule : $\forall n \in \mathbb{N}$ : $\frac {u_{n+1}} {u_n}$
>2) On compare le résultat à 1 : $\frac {u_{n+1}} {u_n}>1$<=> strict. croissant / $\frac {u_{n+1}} {u_n}<1$<=> strict. décroissante
### 3) Notion intuitive de limite
>[!INFO] Définition
>Soit $(u_n)$ une suite.
>La suite $(u_n)$ a pour limite le nombre $l$ quand n tend $+\infty$, si les termes $u_n$ deviennent tous aussi proches de $l$ que l'on veut, en prenant $n$ suffisamentgrand.
>On dit que $u_n$ converge vers $l$ et on note $\lim_{n \to +\infty}=l$

