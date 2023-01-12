# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(con: int) -> bool:
    """
    Determine si l'entier passe en parametre peut representer le contenu d'une cellule.
    Si oui, renvoie True, False sinon.

    :param con: Entier cense representer le contenu d'une cellule.
    :return: True ou False en fonction de si le param represente un contenu ou non.
    """
    isCon = True
    print(con)
    if not isinstance(con, int):
        isCon = False
    elif (int(con) < 0 or int(con) > 8) and con != const.ID_MINE:
        isCon = False
    return isCon


def construireCellule(con: int = 0, vis: bool = False) -> dict:
    """
    Construi une cellule sous la forme d'un dictionnaire, a partir d'un contenu et d'un etat de visibilite.

    :param con: Contenu de la cellule. (0 par deft)
    :param vis: Etat de la visibilite de la cellule. (False par deft)
    :return: Un dictionnaire representant la cellule.
    """
    if not isContenuCorrect(con):
        raise ValueError(f"construireCellule : le contenu {con} n’est pas correct")
    if not isinstance(vis, bool):
        raise TypeError(f"construireCellule : le second paramètre ({type(vis)}) n’est pas un booléen")
    return {const.CONTENU: con, const.VISIBLE: vis}
