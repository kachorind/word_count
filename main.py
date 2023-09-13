# Devina Kachorin
# 13 septembre 2023
# TP1 - word_count


def count_word(chaine):
    # En utilisant split(), je divise le nombre de chaîne de caractères en utilisant les espaces comme séparateurs
    mots = chaine.split()

    # Je compte le nombre de mots dans la liste à l’aide de la fonction len()
    mot_nbr = len(mots)

    return mot_nbr

print("Bonjour!\nVous pouvez écrire des mots en lettres minuscules et je vous dirai combien de mots vous avez écrit.")

# Je demande à l’utilisateur de m’écrire une chaîne de caractère avec l’aide de la fonction input()
chaine2 = input("Entrez votre chaîne de caractères en lettres minuscules: ").lower()

# Affiche le nombre de mots
combien_mots = count_word(chaine2)
print("Votre nombre de mots est de: ", combien_mots)
