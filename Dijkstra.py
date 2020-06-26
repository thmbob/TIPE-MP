import numpy as np
import file_prioritaire as fp
import Graphe as gr

class chemin :
    def __init__(self) :
        self.__cout = 0
        self.__liste = []

    def ajouter_point(self, point, cout) :
        self.__liste.append(point)
        self.__cout += cout

    def dernier_point(self) :
        return self.__liste[-1]

    def contient(self, point) :
        return point in self.__liste

    def __str__(self) :
        s = ""
        s += "[" + str(self.__cout) + "] " + str(self.__liste)
        return s

    def compare_chemin(c1, c2) :
        return c1.__cout < c2.__cout

    def copy(self) :
        r = chemin()
        r.__cout = self.__cout
        r.__liste = self.__liste.copy()
        return r

def dijkstra(graphe, depart, arrive) :
    file = fp.file_prioritaire(chemin.compare_chemin, etype=chemin)
    c = chemin()
    c.ajouter_point(depart, 0)
    file.enfile(c)
    print(file)
    i = depart
    c = file.defile()
    mat = graphe[2]
    n = gr.ordre(graphe)
    while i != arrive :
        print(i)
        for j in range(n) :
            if mat[i][j] != 0 :
                nc = c.copy()
                if not nc.contient(j) :
                    nc.ajouter_point(j, mat[i][j])
                    file.enfile(nc)
        c = file.defile()
        i = c.dernier_point()
    return c

##tab = np.array([[0, 2, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0
##                [2, 0, 0, 5, 0, 0, 0, 0, 0, 4, 0, 2, 0],#1
##                [4, 0, 0, 0, 6, 1, 0, 0, 0, 3, 0, 0, 0],#2
##                [8, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],#3
##                [0, 0, 6, 0, 0, 2, 4, 0, 0, 0, 0, 0, 1],#4
##                [0, 0, 0, 0, 2, 0, 5, 0, 0, 0, 0, 0, 0],#5
##                [0, 0, 1, 0, 4, 5, 0, 7, 0, 2, 0, 0, 7],#6
##                [0, 0, 0, 0, 0, 0, 7, 0, 1, 0, 0, 0, 0],#7
##                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],#8
##                [0, 4, 3, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0],#9
##                [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 6, 0],#10
##                [0, 2, 0, 4, 0, 0, 0, 0, 0, 0, 6, 0, 0],#11
##                [0, 0, 0, 0, 1, 0, 7, 0, 0, 0, 0, 0, 0],#12
##                ])
##graphe = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [], tab]
##
##print(dijkstra(graphe, 12, 3))
