###################
# Les importations:
###################

import datetime
'''
with open('fish.txt', 'r') as fichier_bugs:

	total_number_of_lines = 521 #len(fichier_bugs.readlines())

	#print(total_number_of_lines)

	lines_to_read = 9

	compteur_lignes = 0

	nouveau_fichier = ''

	while compteur_lignes < total_number_of_lines:

		compteur_lignes_block = 0

		nouvelle_ligne = ''

		while compteur_lignes_block < lines_to_read: 

			info_ligne = fichier_bugs.readline()

			info_ligne = info_ligne.replace("\n", "")

			#print(str(compteur_lignes) + '/' + str(total_number_of_lines), compteur_lignes_block, info_ligne + '')

			if compteur_lignes_block < 7:

				nouvelle_ligne = nouvelle_ligne + info_ligne + ';'

			if compteur_lignes_block == 7:

				if info_ligne != '': # il y a un commentaire

					nouvelle_ligne = nouvelle_ligne + info_ligne + ";\n"

				else: #fin du bloc parce qu'il n'y a pas de commentaires

					nouvelle_ligne = nouvelle_ligne + ";\n"

					break;

			compteur_lignes_block = compteur_lignes_block + 1

			compteur_lignes = compteur_lignes + 1

		nouveau_fichier = nouveau_fichier + nouvelle_ligne

		#print('nouvelle ligne: ' + nouvelle_ligne)
'''


########################
# Les variables globales
########################

heure_actuelle_raw = datetime.datetime.now()

heure_format_24 = heure_actuelle_raw.hour

mois_format_12 = heure_actuelle_raw.month

jour_format_30 = heure_actuelle_raw.day

jour_format_long = heure_actuelle_raw.strftime("%A")

heure_format_long = heure_actuelle_raw.strftime("%X")[:-3]

noms_mois = {
	1: "janvier",
	2: "février",
	3: "mars",
	4: "avril",
	5: "mai",
	6: "juin",
	7: "juillet",
	8: "août",
	9: "septembre",
	10: "octobre",
	11: "novembre",
	12: "décembre"
}

mois_numerique = {
	"January": 1,
	"February": 2,
	"March": 3,
	"April": 4,
	"May": 5,
	"June": 6,
	"July": 7,
	"August": 8,
	"September": 9,
	"October": 10,
	"November": 11,
	"December": 12
}

critters = ['fish', 'bugs']

listes_critters = {} # listes_critters["fish"] pour la liste complète ou listes_critters["fish"][3] pour le Barbel Steed


###############
# Les fonctions
###############

def load_critters(nom_fichier):

	liste = []

	fini = 0

	with open(nom_fichier, 'r') as fichier:

		while fini != 1:

			info_ligne = fichier.readline()

			if info_ligne != '':

				info_ligne = info_ligne.split(";")

				#print(info_ligne)

				liste.append(info_ligne)

			else:

				fini = 1

	return liste



def nommer_mois(mois):

	return noms_mois[mois]


def mois_explicites(mois_texte):

	if mois_texte == 'All year':

		return [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]

	# separer les morceaux (d'abord les blocs, ensuites les premier et derniers mois)

	mois_texte = mois_texte.replace(" ", "") # enlever les espaces inutiles

	blocs = mois_texte.split(",") # certaines créatures ont plusieurs blocs de mois de présences

	# print(liste_mois)

	# determiner le premier et dernier mois en chiffre et compléter la séquence (remplir les mois entre deux)

	i = 0

	for bloc in blocs:

		deux_mois_lettres = bloc.split("-")

		#print(deux_mois_lettres[0])

		premier_mois = mois_numerique[deux_mois_lettres[0]]

		#print(premier_mois)

		gauche = premier_mois

		liste_temp = [gauche]

		if len(deux_mois_lettres) > 1:

			deuxieme_mois = mois_numerique[deux_mois_lettres[1]]

			#print(deuxieme_mois)

			while gauche + 1 < deuxieme_mois:

				gauche += 1

				liste_temp.append(gauche)

			liste_temp.append(deuxieme_mois)

		blocs[i] = liste_temp

		i += 1

	#print(blocs)

	# retourner la liste complète

	return blocs


def creatures_maintenant(mois_demande, heure_demande):

	index_mois = {'fish':5, 'bugs':4} # les poissons ont un champs d'information supplémentaire (taille de l'ombre)

	mois_present_texte = ''

	liste_creatures_presentes = []

	for type_creature in critters: # poisson et insecte

		for creature in listes_critters[type_creature]:

			mois_present_texte = creature[index_mois[type_creature]]

			blocs_mois_present_numerique = mois_explicites(mois_present_texte)

			print(creature[0], blocs_mois_present_numerique)

			for bloc in blocs_mois_present_numerique:

				if mois_demande in bloc:

					liste_creatures_presentes.append(creature[0])

	return liste_creatures_presentes


###############
# Le programme
###############

'''
afficher l'heure actuelle, le nom de chaque joueur et les 
poissons et insectes manquants disponible en ce momant 
pour chacun d'eux.
'''

for critter in critters:

	ficher_critter = critter + '2.txt'

	listes_critters[critter] = load_critters(ficher_critter)


print('**********************', jour_format_30, noms_mois[mois_format_12], heure_format_long, '************************')

'''
Afficher un menu de choix d'opérations
1) inscrire une nouvelle prise
2) annuler une prise inscrite
3) ajouter une créature à la liste officielle
4) enlever une créature à la liste officielle
5) ajouter un joueur
6) effacer un joueur
'''

#print(listes_critters["fish"][3])

test = mois_explicites(listes_critters["fish"][12][5])

print(listes_critters["fish"][12])

print(test)

creatures_maintenant(mois_format_12, heure_format_24)



































