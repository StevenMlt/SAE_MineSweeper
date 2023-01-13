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
    if not isinstance(con, int) or ((int(con) < 0 or int(con) > 8) and con != const.ID_MINE):
        isCon = False
    return isCon


def construireCellule(contenu: int = 0, visible: bool = False) -> dict:
    """
    Construi une cellule sous la forme d'un dictionnaire, a partir d'un contenu et d'un etat de visibilite.

    :param con: Contenu de la cellule. (0 par deft)
    :param vis: Etat de la visibilite de la cellule. (False par deft)
    :return: Un dictionnaire representant la cellule.
    """
    if not isContenuCorrect(contenu):
        raise ValueError(f"construireCellule : le contenu {contenu} n’est pas correct")
    elif not isinstance(visible, bool):
        raise TypeError(f"construireCellule : le second paramètre ({type(visible)}) n’est pas un booléen")
    return {const.CONTENU: contenu, const.VISIBLE: visible, const.ANNOTATION: None}


def getContenuCellule(dic: dict) -> int:
    """
    Renvoie le contenu d'un dictionnaire representant une cellule.

    :param dic: Cellule sous la forme d'un dictionnaire
    :return: Renvoie de contenu du dictionnaire (cellule)
    """
    if not type_cellule(dic):
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return dic.get(const.CONTENU)


def isVisibleCellule(dic: dict) -> bool:
    """
    Renvoie l'etat de visibilite de la cellule (dico).

    :param dic: representation de la cellule.
    :return: True si cellule visible, False sinon.
    """
    if not type_cellule(dic):
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return dic.get(const.VISIBLE)


def setContenuCellule(dic: dict, contenu: int) -> None:
    """
    Modifie le contenu de la cellule (dic) avec le contenu passe en parametre.

    :param dic: Representation de la cellule.
    :param contenu: Contenu que l'on veut integrer dans la cellule.
    :return: Rien.
    """
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    elif not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule: la valeur du contenu {contenu} n'est pas correcte.")
    elif not type_cellule(dic):
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    dic[const.CONTENU] = contenu
    return None


def setVisibleCellule(dic: dict, visible: bool) -> None:
    """
    Modifie la visibilite de la cellule (dic) avec la visibilite passee en parametre.

    :param dic: Representation de la cellule.
    :param visible: Visibilite que l'on veut integrer dans la cellule.
    :return: Rien.
    """
    if not type_cellule(dic):
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    elif type(visible) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen")
    dic[const.VISIBLE] = visible
    return None


def contientMineCellule(dic: dict) -> bool:
    """
    Determine si une cellule(dic) contient une mine ou non.

    :param dic: Representation de la cellule.
    :return: True si la cellule contient une mine, False sinon.
    """
    if not type_cellule(dic):
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    return dic.get(const.CONTENU) == const.ID_MINE

def isAnnotationCorrecte(annotation: str) -> bool:
    """
    Verifie si l'annotation passee en parametre est correcte.
    
    :param annotation: str representant l'etat de l'annotation d'une cellule.
    :return: True si l'annotation vaut (None, const.DOUTE ou const.FLAG), False sinon.
    """
    annOK = False
    valide = [None, const.DOUTE, const.FLAG]
    if annotation in valide:
        annOK = True
    return annOK


def getAnnotationCellule(cell: dict) -> str:
    """
    Renvoie l'annotation contenue dans la cellule passee en parametre.

    :param cell: Cellule sous la forme d'un dictionnaire.
    :return: L'annotation contenue dans la cellule. (None, const.DOUTE ou const.FLAG)
    """
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : le paramètre {cell} n’est pas une cellule")
    ann = cell.get(const.ANNOTATION)
    if const.ANNOTATION not in cell.keys():
        ann = None
    return ann
