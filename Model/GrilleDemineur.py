# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(li: int, co: int) -> list:
    """
    Cree une liste de listes representant la grille du demineur, remplie de cellules.

    :param li: Nombre de lignes de la grille.
    :param co: Nombre de colonnes de la grille.
    :return: La grille sous forme de liste de listes.
    """
    if type(li) != int or type(co) != int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes ({type(li)}) ou de colonnes ({type(co)}) "
                        f"n’est pas un entier.")
    elif li <= 0 or co <= 0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes ({li}) ou de colonnes ({co}) est "
                         f"négatif ou nul.")
    grille = []
    for line in range(li):
        grille.append([])
        for column in range(co):
            grille[line].append(construireCellule())
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    """
    Determine le nombre de lignes d'une grille de demineur passee en parametre.

    :param grille: Liste de listes representant une grille de demineur.
    :return: Le nombre de lignes de la grille.
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """
    Determine le nombre de colonnes d'une grille de demineur passee en parametre.

    :param grille: Liste de listes representant une grille de demineur.
    :return: Le nombre de colonnes de la grille.
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    """
    Verifie si la coordonnee passee en parametre est contenue dans la grille aussi passee en parametre.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnee supposees d'une cellule, sous la forme d'un tuple.
    :return: True si les coordonnees correspondent a une cellule, False sinon.
    """
    if type(grille) != list or not type_grille_demineur(grille) or type(coord) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    presCell = False
    if coord[0] <= getNbLignesGrilleDemineur(grille)-1 and coord[1] <= getNbColonnesGrilleDemineur(grille)-1:
        presCell = type_cellule(grille[coord[0]][coord[1]])
    return presCell


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    """
    Retourne la cellule se trouvant a la coordonnee passee en parametre dans la grille egalement passee en parametre.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnee supposees d'une cellule, sous la forme d'un tuple.
    :return: Cellule(dict) designee par les coordonnees passees en parametre.
    """
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    elif type(grille) != list or not type_grille_demineur(grille) or type(coord) != tuple:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    """
    Retourne le contenu de la cellule se trouvant a la coordonnee passee en parametre dans la grille passee en
    parametre.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnee supposees d'une cellule, sous la forme d'un tuple.
    :return: Contenu de la cellule passee en parametre.
    """
    return getCelluleGrilleDemineur(grille, coord).get(const.CONTENU)


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    """
    Modifie le contenu de la cellule se trouvant a la coordonnee passee en parametre dans la grille passee en
    parametre avec le nouveau contenu.


    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnee supposees d'une cellule, sous la forme d'un tuple.
    :param contenu: Nouveau contenu a attribuer dans la cellule designee par les coord.
    :return: Rien.
    """
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Verifie si la cellule de la grille passee en parametre est visible ou non.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnee supposees d'une cellule, sous la forme d'un tuple.
    :return: Renvoie True si la cellule est visible, False sinon.
    """
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    """
    Modifie la visibilite de la cellule se trouvant a la coordonnee passee en parametre dans la grille passee en
    parametre avec la nouvelle visibilite.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnee supposees d'une cellule, sous la forme d'un tuple.
    :param visible: Nouvel etat de visibilite de la cellule designee.
    :return: Rien.
    """
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)
    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Vérifie si la cellule designee en parametre contient une mine ou non.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnee supposees d'une cellule, sous la forme d'un tuple.
    :return: True si la cellule contient une mine, False sinon.
    """
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))
