### Application de l'algorithme de Dijkstra sur les fonctions

import file_prioritaire as fp

def creerLiens(lig, col) :
    l = []
    n = lig*col
    for i in range(n) :
        l.append([])
        if (i-1)//lig == i//lig :
            l[-1].append(i-1)
        if (i+1)//lig == i//lig :
            l[-1].append(i+1)
        if i-col >= 0 :
            l[-1].append(i-col)
        if i+col < n :
            l[-1].append(i+col)
    return l


def creerFonctions(voisins) :
    n = len(voisins)
    tab = [ [(lambda t : float('inf')) for i in range(n)] for j in range(n)]
    for i in range(n) :
        tab[i][i] = lambda t : 0
        for j in range(len(voisins[i])) :
            b = voisins[i][j]
            tab[i][b] = (lambda t : i*t + b)
    return tab

def voisins(graphe, i) :
    return graphe[1][i]
        
lig, col = 6, 8
vsns = creerLiens(lig, col)
graphe = ([i for i in range(lig*col)], vsns, creerFonctions(vsns))

print(graphe[1])



def pcc(graphe) :
    n = len(graphe[0])
    date_arrivee = graphe[2]
    tab = [ [[int(-1), float('inf')]  for i in range(n)] for j in range(n) ]

    for src in range(n) :

        Q = fp.file_prioritaire(lambda a, b : a[1] <= b[0], [-1, float('inf')])
        Q.enfile([src, 0])
        tab[src][src] = [src, 0]
        F = []

        while not Q.est_vide() :
            (i, t) = Q.defile()
            i = int(i)
            F.append(i)
            for j in voisins(graphe, i) :
                ta = date_arrivee[i][j](tab[src][i][1])
                if ta < tab[src][j][1] :
                    tab[src][j] = [i, ta]
                    Q.enfile([j, ta])
    return tab
                
                            
print(pcc(graphe))        

            
        
                            
                           
        
