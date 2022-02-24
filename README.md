# prjTut_TSP

# <div align="center">  Le problème du voyageur de commerce</div>
## <div align="center">  TSP : Travelling Salesman Problem</div>


### 1 Introduction

Un problème d’optimisation combinatoire repose sur la donnée d’un ensemble _E_ et d’une fonction _f : E 7 → R_. Il s’agit de déterminer l’élément _e_ de _E_ qui optimise _f(e)_. Un algorithme, dit de force brute, consiste à énumérer tous les éléments _e_ de _E_ et à calculer _f(e)_ pour chacun d’eux. Mais cet algorithme devient vite inutilisable en pratique, à cause de la taille de l’ensemble _E_. On a alors recours à des algorithmes appelés heuristiques. Une heuristique est un algorithme qui permet de déterminer rapidement une solution acceptable : la vitesse d’exécution est privilégiée à la qualité de la solution.

### 2 Le problème

Un voyageur de commerce doit visiter _n_ villes. Il s’agit de déterminer la tournée la plus courte qui passe une et une seule fois par chacune des villes et se termine par la ville d’origine. La situation peut être représenté par un graphe pondéré non orienté _G = (S, A, ω)_ où chaque sommet de _S_ représente une ville et où chaque arête de _A_ représente une liaison entre 2 villes. Le poids _ω(x, y)_ d’une arête _xy_ est égal à la distance (en km) entre les villes représentées par les sommets _x_ et _y_. Une tournée correspond alors à un cycle Hamiltonien et le problème consiste à déterminer un cycle Hamiltonien de poids minimum.

Pour simplifier le problème, on considère que les distances entre villes sont des distances à vol d’oiseau et que _G_ est un graphe complet d’ordre _n_ et de taille _n(n − 1)/2_. Dans ce cas, toute permutation de l’ensemble des sommets représente une tournée possible : il y a _n!_ permutations. Cependant, une tournée donnée est représentée par _2n_ permutations. En effet, une tournée étant un cycle, tout sommet de ce cycle peut être un point de départ. De plus, comme le graphe est non orienté, un cycle peut être parcouru dans un sens comme dans l’autre. Au final, il existe exactement _(n − 1)!/2_ tournées distinctes. Considérons par exemple un graphe de 4 sommets _S = {a, b, c, d}_ : les tournées _abcda_, _bcdab_, _cdabc_ et _dabcd_ sont de même poids (il reste _(4!)/4 = 3!_ permutations possibles) ; les 2 tournées _abcda_ et _adcba_ sont aussi de même poids (il reste alors _3!/2 = 3_ tournées).

Le problème du voyageur de commerce est donc un problème d’optimisation combinatoire : l’ensemble _E_ est un ensemble de _(n − 1)!/2_ tournée et la fonction objectif que l’on souhaite ici minimiser correspond au poids (en km) d’une tournée. 

### 3 Heuristiques recherchant une tournée acceptable

L’objectif est d’obtenir rapidement une solution qui soit la plus proche possible de la solution optimale.

#### [3.1 Heuristique aléatoire](https://github.com/ChorbaDev/prjTut_TSP/issues/1)

Cette heuristique consiste à générer aléatoirement un grand nombre de permutations en espérant en trouver une de bonne qualité. En pratique, on se fixe une limite de temps (à vous de la définir) et on ne retient que la meilleure solution obtenue.

#### [3.2 Heuristique du plus proche voisin](https://github.com/ChorbaDev/prjTut_TSP/issues/2)

On démarre avec une tournée _T_ ne contenant qu’une seule ville. Puis, à chaque itération, on ajoute à _T_ la ville la plus proche de la dernière ville visitée de _T_ . Le processus se termine quand toutes les villes ont été ajoutées à la tournée.

Il s’agit d’une heuristique dite _gloutonne_ (_greedy heuristic_) : à chaque itération une nouvelle ville est ajoutée à la tournée sans jamais remettre en cause les ajouts précédents. A vous de voir comment exploiter au mieux cette heuristique.

#### 3.3 Votre proposition

Faire des recherches et proposer au moins une autre heuristique.

### 4 Heuristiques d’amélioration

Ces heuristiques ont pour objectif d’améliorer une solution existante. En pratique, on recherche une solution en utilisant l’une des heuristiques présentées dans le paragraphe [§3](#3-heuristiques-recherchant-une-tournée-acceptable) et on essaie d’obtenir une meilleure solution à l’aide d’une heuristique d’amélioration.

#### [4.1 Heuristique d’échange de 2 sommets](https://github.com/ChorbaDev/prjTut_TSP/issues/3)

Étant donnée une tournée _T_ , on regarde si l’échange de 2 villes dans _T_ produit une tournée de meilleure qualité que _T_ . Par exemple, si on échange _b_ et _d_ dans la tournée _T = abcde_ on obtient une nouvelle tournée _T ′ = adcbe_. En pratique, on effectue des améliorations successives jusqu’à ce qu’il ne soit plus possible d’améliorer la solution courante. On peut aussi arrêter le processus quand une limite de temps fixée au préalable est dépassée.

#### [4.2 Heuristique de (dé)croisement de deux arêtes](https://github.com/ChorbaDev/prjTut_TSP/issues/4)

Soit une tournée _T = · · · ab · · · cd · · ·_ . On (dé)croise les deux arêtes _ab_ et _cd_ pour obtenir la nouvelle tournée _T ′ = · · · ad · · · bc · · ·_ . Il suffit ensuite de comparer _T_ et _T ′_ et de conserver la meilleure des deux. En pratique, on procède comme pour l’heuristique précédente.

### [5 Algorithme de force brute](https://github.com/ChorbaDev/prjTut_TSP/issues/5)

Ce type d’algorithme énumère toutes les tournées possibles, calcule le poids de chacune d’elles et fournit la solution optimale. On testera cet algorithme sur des graphes d’ordre 10 à 20 au plus (à vous de voir). Il s’agit ici d’analyser l’évolution du temps d’exécution en fonction du nombre de villes.

Indication : utiliser le parcours en profondeur d’abord (dfs) et améliorer son usage (par exemple en évitant de poursuivre les visites à partir d’un sommet si cela ne
permet pas d’améliorer la solution courante).

### 6 Les instances

Sur Arche, vous trouverez différentes instances à résoudre. La plus simple est l’instance [communes_10.txt](https://github.com/ChorbaDev/prjTut_TSP/tree/main/communes/communes/communes_10.txt) qui contient la liste des arêtes et leur poids pour un ensemble de 10 villes. La plus grande instance est [communes_777.txt](https://github.com/ChorbaDev/prjTut_TSP/tree/main/communes/communes/communes_777.txt) pour un ensemble de 777 villes. Notez que les sommets sont identifiés par les entiers allant de _0_ à _n − 1_.

Toutes les instances respectent un même format : la première ligne contient le nombre de sommets _n_ et le nombre d’arêtes _m = n(n − 1)/2_. Puis suivent _m_ lignes, chaque ligne décrivant une arête sous la forme : _x y ω(x, y)_ où _x < y_ et où _ω(x, y)_ est la distance en kilomètres séparant les villes _x_ et _y_ (distance à vol d’oiseau).

### 7 Travail demandé

Dans un premier temps, il s’agit de programmer les 5 heuristiques et l’algorithme de force brute en langage C/C++ ou en Python. Vous devrez ensuite utiliser vos programmes pour résoudre au mieux les différentes instances proposées. Une analyse et un bilan des résultats devra être ensuite présenté.

### [8 Question bonus](https://github.com/ChorbaDev/prjTut_TSP/issues/6)

Visualiser les tournées sur une carte de France. Le fichier [communes.xlsx](https://github.com/ChorbaDev/prjTut_TSP/tree/main/communes/communes.xlsx) contient diverses information concernant les communes. On y trouvera les coordonnées GPS des 777 communes mais aussi les _coordonnées cartésiennes_ (obtenues par projection sur un plan). Le graphique (nuage de points) se trouvant dans ce fichier est obtenu
à l’aide de ces coordonnées cartésiennes.


# <div align="center">  Pre-requis </div>

## intaller les paquets suivant:

- plotly
- pandas
- random
- sys
- numpy
- time
- 