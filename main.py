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

				print(info_ligne)

				liste.append(info_ligne)

			else:

				fini = 1

	return liste

test = load_critters("fish2.txt")

print('ici')

print(test[4])


#def nommer_mois(mois):




###############
# Le programme
###############

'''
afficher l'heure actuelle, le nom de chaque joueur et les 
poissons et insectes manquants disponible en ce momant 
pour chacun d'eux.
'''




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





































