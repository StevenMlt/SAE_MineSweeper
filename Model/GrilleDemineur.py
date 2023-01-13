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
    :param coord: Coordonnees supposees d'une cellule, sous la forme d'un tuple.
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
    :param coord: Coordonnees supposees d'une cellule, sous la forme d'un tuple.
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
    :param coord: Coordonnees supposees d'une cellule, sous la forme d'un tuple.
    :return: Contenu de la cellule passee en parametre.
    """
    return getCelluleGrilleDemineur(grille, coord).get(const.CONTENU)


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    """
    Modifie le contenu de la cellule se trouvant a la coordonnee passee en parametre dans la grille passee en
    parametre avec le nouveau contenu.


    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnees supposees d'une cellule, sous la forme d'un tuple.
    :param contenu: Nouveau contenu a attribuer dans la cellule designee par les coord.
    :return: Rien.
    """
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Verifie si la cellule de la grille passee en parametre est visible ou non.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnees supposees d'une cellule, sous la forme d'un tuple.
    :return: Renvoie True si la cellule est visible, False sinon.
    """
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    """
    Modifie la visibilite de la cellule se trouvant a la coordonnee passee en parametre dans la grille passee en
    parametre avec la nouvelle visibilite.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnees supposees d'une cellule, sous la forme d'un tuple.
    :param visible: Nouvel etat de visibilite de la cellule designee.
    :return: Rien.
    """
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)
    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Vérifie si la cellule designee en parametre contient une mine ou non.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnees supposees d'une cellule, sous la forme d'un tuple.
    :return: True si la cellule contient une mine, False sinon.
    """
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    """
    Retourne dans une liste la liste des coordonnees des cellules voisines de la cellule designee en params.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnees supposees d'une cellule, sous la forme d'un tuple.
    :return: Liste des coordonnees des cellules voisines.
    """
    if not type_grille_demineur(grille) or type(coord) != tuple:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type")
    elif not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    voisins = []
    for line in range(-1, 2):
        for column in range(-1, 2):
            temp = (coord[0] + line, coord[1] + column)
            if (temp[0] >= 0 and temp[1] >= 0) and (temp[0] < getNbLignesGrilleDemineur(grille) and temp[1] < getNbColonnesGrilleDemineur(grille)) and temp != coord:
                voisins.append(temp)
    return voisins


def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    """
    Place exactement nb mines dans nb cellules de la grille en evitant celle dont la coordonnee est passee en parametre.

    :param grille: Liste de listes representant une grille de demineur.
    :param nb: Nombre de mines à placer.
    :param coord: Coordonnees de la premiere cellule cliquee, ne doit pas contenir de mines.
    :return: Rien.
    """
    dimensionsGrille = (getNbLignesGrilleDemineur(grille), getNbColonnesGrilleDemineur(grille))
    nbCasesGrille = dimensionsGrille[0] * dimensionsGrille[1]
    if nb < 0 or nb > (nbCasesGrille - 1):
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    elif not isCoordonneeCorrecte(grille, coord):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    while nb > 0:
        coordMine = (randint(0, dimensionsGrille[0]-1), randint(0, dimensionsGrille[1]-1))
        if coordMine != coord and not contientMineGrilleDemineur(grille, coordMine):
            setContenuGrilleDemineur(grille, coordMine, const.ID_MINE)
            nb -= 1
    compterMinesVoisinesGrilleDemineur(grille)
    return None


def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    """
    Pour chaque case ne contenant pas de mine, compte le nombre de mines voisines de cette case et affecte ce nombre au
    contenu de la case.

    :param grille: Liste de listes representant une grille de demineur.
    :return: Rien.
    """
    dimensionsGrille = (getNbLignesGrilleDemineur(grille), getNbColonnesGrilleDemineur(grille))
    for line in range(dimensionsGrille[0]):
        for column in range(dimensionsGrille[1]):
            if not contientMineGrilleDemineur(grille, (line, column)):
                cptMinesVoisines = 0
                for voisin in getCoordonneeVoisinsGrilleDemineur(grille, (line, column)):
                    if contientMineGrilleDemineur(grille, voisin):
                        cptMinesVoisines += 1
                setContenuGrilleDemineur(grille, (line, column), cptMinesVoisines)
    return None


def getNbMinesGrilleDemineur(grille: list) -> int:
    """
    Compte et renvoie le nombre de mines contenues dans la grille.

    :param grille: Liste de listes representant une grille de demineur.
    :return: Nombre de mines de la grille.
    """
    if not type_grille_demineur(grille):
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    cptMines = 0
    dimensionsGrille = (getNbLignesGrilleDemineur(grille), getNbColonnesGrilleDemineur(grille))
    for line in range(dimensionsGrille[0]):
        for column in range(dimensionsGrille[1]):
            if contientMineGrilleDemineur(grille, (line, column)):
                cptMines += 1
    return cptMines


def getAnnotationGrilleDemineur(grille: list, coord: tuple) -> str:
    """
    Retourne l'annotation de la cellule dont les coordonnees sont passees en parametre.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnees de la cellule selectionnee.
    :return: L'annotation de la cellule.
    """
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """
    Compte le nombre de mines restantes a marquer.

    :param grille: Liste de listes representant une grille de demineur.
    :return: Le nombre (nb) de mines.
    """
    nb = 0
    dimensionsGrille = (getNbLignesGrilleDemineur(grille), getNbColonnesGrilleDemineur(grille))
    for line in range(dimensionsGrille[0]):
        for column in range(dimensionsGrille[1]):
            if grille[line][column].get(const.ANNOTATION) == const.FLAG:
                nb += 1
    return getNbMinesGrilleDemineur(grille) - nb


def gagneGrilleDemineur(grille: list) -> bool:
    """
    Determine si la partie est gagnee en fonction de si toutes les cases ne contenant pas de mines sont decouvertes.

    :param grille: Liste de listes representant une grille de demineur.
    :return: True si toutes les cases vides ont ete decouvertes, False sinon.
    """
    gagne = True
    dimensionsGrille = (getNbLignesGrilleDemineur(grille), getNbColonnesGrilleDemineur(grille))
    for line in range(dimensionsGrille[0]):
        for column in range(dimensionsGrille[1]):
            cell = grille[line][column]
            if not contientMineCellule(cell) and not isVisibleCellule(cell):
                gagne = False
            elif contientMineCellule(cell) and isVisibleCellule(cell):
                gagne = False
            elif contientMineCellule(cell) and getAnnotationCellule(cell) != const.FLAG:
                gagne = False
    return gagne


def perduGrilleDemineur(grille: list) -> bool:
    """
    Determine si la partie a ete perdue ou non.

    :param grille: Liste de listes representant une grille de demineur.
    :return: True si une cellule contenant une mine est visible, False sinon.
    """
    perdu = False
    dimensionsGrille = (getNbLignesGrilleDemineur(grille), getNbColonnesGrilleDemineur(grille))
    for line in range(dimensionsGrille[0]):
        for column in range(dimensionsGrille[1]):
            cell = grille[line][column]
            if contientMineCellule(cell) and isVisibleCellule(cell):
                perdu = True
    return perdu


def reinitialiserGrilleDemineur(grille: list) -> None:
    """
    Reinitialise toutes les cellules de la grille de Demineur.

    :param grille: Liste de listes representant une grille de demineur.
    :return: Rien.
    """
    dimensionsGrille = (getNbLignesGrilleDemineur(grille), getNbColonnesGrilleDemineur(grille))
    for line in range(dimensionsGrille[0]):
        for column in range(dimensionsGrille[1]):
            cell = grille[line][column]
            reinitialiserCellule(cell)
    return None


def decouvrirGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Decouvre (rend visible) la cellule correspondant a la coordonnee passee en parametre.
    Si cette cellule contient 0 mines dans le voisinage, la fonction decouvre les cellules dans le voisinage.
    Si une des cellules du voisinage contient 0 mine, on relance le processus.

    :param grille: Liste de listes representant une grille de demineur.
    :param coord: Coordonnees de la premiere cellule decouverte par l'utilisateur.
    :return: L’ensemble des coordonnees des cellules rendues visibles.
    """
    setVisibleGrilleDemineur(grille, coord, True)
    cellDecouvertes = set()
    cellDecouvertes.add(coord)
    if getContenuGrilleDemineur(grille, coord) == 0:
        cellAVerifier = []
        voisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
        for voisin in voisins:
            if voisin not in cellAVerifier:
                cellAVerifier.append(voisin)
        while cellAVerifier != []:
            temp = cellAVerifier.pop()
            setVisibleGrilleDemineur(grille, temp, True)
            cellDecouvertes.add(temp)
            if getContenuGrilleDemineur(grille, temp) == 0:
                voisins = getCoordonneeVoisinsGrilleDemineur(grille, temp)
                for voisin in voisins:
                    if voisin not in cellAVerifier and voisin not in cellDecouvertes:
                        cellAVerifier.append(voisin)
    return cellDecouvertes
