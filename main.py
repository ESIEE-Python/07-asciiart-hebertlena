#### Imports et définition des variables globales
"""fonction"""
import sys

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    n = len(s)
    print(n)
    c = [s[0]]
    o = [1]
    k = 1
    while k < n:
        if s[k] == s[k-1] :
            o[-1] += 1
        else :
            c.append(s[k])
            o.append(1)
        k+=1
    return list(zip(c,o))

sys.setrecursionlimit(2000)

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    if not s :
        return []
    k = 0
    for c in s:
        if c != s[0] :
            break
        k += 1
    return [(s[0],k)] + artcode_r(s[k:])

#### Fonction principale


def main():
    """fonction principal"""
    #print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('bmmma'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
