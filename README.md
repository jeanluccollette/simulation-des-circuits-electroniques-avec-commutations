# Simulation des circuits électroniques avec commutations

## Problématique

Dans de nombreuses applications en électronique, notamment en électronique de puissance, des composants passifs (inductances, condensateurs, etc.) cohabitent dans un circuit avec d'autres composants (transistors, thyristors, diodes, etc.) qui ont des temps de commutation très petits par rapport aux constantes de temps associées aux composants passifs.

On rencontre alors des difficultés à mettre en oeuvre des méthodes de résolution numérique sur les équations d'état qui modélisent ce type de circuit. Les temps de simulation peuvent alors être très long, notamment si on utilise des méthodes à pas variable, du type [Dormand-Prince](https://en.wikipedia.org/wiki/Dormand%E2%80%93Prince_method), communément utilisées dans les environnements de calcul (Python, Matlab, etc.).

## Exemples

### Oscillateur avec amplificateur opérationnel

![](Data/Diapositive1.PNG)

![](Data/oscillateur_1.png)

![](Data/oscillateur_2.png)

### Convertisseur DC/DC résonnant

![](Data/Diapositive2.PNG)

![](Data/convres_1.png)

![](Data/convres_2.png)

![](Data/convres_3.png)
