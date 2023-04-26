# Exercices crypto

## Cheat sheet RSA
### Création de la paire de clé
On prend **p** **q** premiers.  
$n=pq$  
$\phi(n)=(p-1)(q-1)$  
On choisis e tel que e et $\phi(n)$ soient premiers entre eux  
$d=e^{-1}\ mod(\phi(n))$

**Clé publique**: $(n,e)$  
**Clé privée**: $d$

### (dé)chiffrement
**m** est le message en clair et **c** le chiffré  
$c=m^e\ mod(n)$  
$m=c^d\ mod(n)$

## Exercices RSA
- Clé factorisable  
Cette clé paraît très petite... est-ce qu'on peut brute-force ?
- Module commun  
Un message a été chiffré deux fois avec deux paire de clés différentes.  
Cependant, les deux clés ont le même **n**...  
Est-ce un problème ??
- Oracles
    - Oracle chosen ciphertext  
    Vous pouvez déchiffrer ce que vous voulez !  
    Sauf le flag biensûr
    - Oracle sans n