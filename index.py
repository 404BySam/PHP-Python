prenom = "Jean"
nom = "Dupont"

age = 26

taille = 1.75

est_developpeyeur = True

print(type(prenom))
print(type(nom))
print(type(age))
print(type(taille))
print(type(est_developpeyeur))

# Concaténation sans f-string

print("Je m'appelle " + prenom + " et j'ai " + str(age) + " ans.")

# Concaténation avec f-string
# Une f-string (ou formatted string literal) -Elle a été introduite avec Python 3.6-
# est une façon rapide et lisible d’insérer des variables dans une chaîne de caractères.

print(f"Je m'appelle {prenom} et j'ai {age} ans. je mesure {taille} m.")
print(f"est_developpeyeur : {est_developpeyeur}" )

x = "Bonjour"
y = "python"
z = "c'est cool"

print(x, y, z)
demobool = True
demobool = False

#          0    1   2   3
demotbl = [10, 20, 30, "40"]


test = demotbl[3] + "3"

test = 3


#           0        1     0         1       0  1   3    2   3   0  1
notes = ["Bonjour", 18,["Salut", "Super !", [1, 2, 3]], 20, 14, [0, 5]]

print(notes[2][0])