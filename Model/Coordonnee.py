# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(li: int, co: int) -> tuple:
    """
    Cette fonction inscrit deux parametres 'li' et 'co' dans un tuple de coordonnees que l'on retourne.

    :param li: numero de ligne d'une coordonnee.
    :param co: numero de colonne d'une coordonnee.
    :return: (li, co).
    """
    if not isinstance(li, int) or not isinstance(co, int):
        raise TypeError(f"construireCoordonnee : Le numéro de ligne {type(li)} ou le numéro de colonne {type(co)} "
                        f"ne sont pas des entiers")
    if li < 0 or co < 0:
        raise ValueError(f"construireCoordonnee : Le numéro de ligne ({li}) ou de colonne ({co}) ne sont pas positifs")
    return (li, co)


def getLigneCoordonnee(coord: tuple) -> int:
    """
    Cette fonction retourne le numero de ligne contenu dans la coordonnee passee en parametre.

    :param coord: Tuple contenant les coordonnees (y, x)
    :return: Valeur de ligne de la coordonnee (coord(y))
    """
    if not isinstance(coord, tuple) or (not isinstance(coord[0], int) or not isinstance(coord[1], int)) or \
            (coord[0] < 0 or coord[1] < 0):
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coord[0]


def getColonneCoordonnee(coord: tuple) -> int:
    """
    Cette fonction retourne le numero de colonne contenu dans la coordonnee passee en parametre.

    :param coord: Tuple contenant les coordonnees (y, x)
    :return: Valeur de ligne de la coordonnee (coord(x))
    """
    if not isinstance(coord, tuple) or (not isinstance(coord[0], int) or not isinstance(coord[1], int)) or \
            (coord[0] < 0 or coord[1] < 0):
        raise TypeError("getColonneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coord[1]
