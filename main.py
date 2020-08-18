'''
afficher l'heure actuelle, le nom de chaque joueur et les 
poissons et insectes manquants disponible en ce momant 
pour chacun d'eux.
'''

import datetime

heure_actuelle = datetime.datetime.now()

print('**********************', heure_actuelle, '************************')

with open('bugs_p2.txt', 'r') as fichier_bugs:

	number_of_lines = 521#len(fichier_bugs.readlines())

	print(number_of_lines)

	lines_to_read = 9

	compteur_lignes = 0

	nouvelle_ligne = ''

	nouveau_fichier = ''

	while compteur_lignes < number_of_lines:

		compteur_lignes_block = 1

		while compteur_lignes_block < lines_to_read: 

			info_ligne = fichier_bugs.readline()

			print(str(compteur_lignes) + '/' + str(number_of_lines), compteur_lignes_block, info_ligne + '')

			if compteur_lignes_block == 1:

				nouvelle_ligne = info_ligne + ';'

			if compteur_lignes_block == 3:

				nouvelle_ligne = nouvelle_ligne + info_ligne + ';'

			if compteur_lignes_block == 9:

				nouvelle_ligne = nouvelle_ligne + '\n'

			compteur_lignes_block = compteur_lignes_block + 1

			compteur_lignes = compteur_lignes + 1

		nouveau_fichier = nouveau_fichier + nouvelle_ligne
'''
			if compteur_lignes_block == 3:

				nouvelle_ligne = info_ligne

			if compteur_lignes_block == 4:

				nouvelle_ligne = info_ligne

			if compteur_lignes_block == 5:

				nouvelle_ligne = info_ligne

			if compteur_lignes_block == 6:

				nouvelle_ligne = info_ligne

			if compteur_lignes_block == 7:

				nouvelle_ligne = info_ligne
'''





print('-------------------->\n', nouveau_fichier)

'''
Afficher un menu de choix d'opérations
1) inscrire une nouvelle prise
2) annuler une prise inscrite
3) ajouter une créature à la liste officielle
4) enlever une créature à la liste officielle
5) ajouter un joueur
6) effacer un joueur
'''


