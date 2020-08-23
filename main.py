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

heures_24 = {
	'1PM': 13,
	'2PM': 14,
	'3PM': 15,
	'4PM': 16,
	'5PM': 17,
	'6PM': 18,
	'7PM': 19,
	'8PM': 20,
	'9PM': 21,
	'10PM': 22,
	'11PM': 23,
	'12PM': 0
}

critters = ['fish', 'bugs']

listes_critters = {} # listes_critters["fish"] pour la liste complète ou listes_critters["fish"][3] pour le Barbel Steed

traduction = {
	'fish': 'poisson',
	'bugs': 'insecte'
}

les_joueurs = ['david', 'aurelie', 'marianne', 'florence']


###############
# Les fonctions
###############

def load_critters(nom_fichier):

	liste = []

	fini = 0

	with open(nom_fichier, 'r') as fichier:

		while fini != 1:

			info_ligne = fichier.readline()

			info_ligne = info_ligne.replace('\n', '') # enlever le symbole de nouvelle ligne

			if info_ligne != '':

				info_ligne = info_ligne.split(";")

				#print(info_ligne)

				liste.append(info_ligne)

			else:

				fini = 1

	return liste



def nommer_mois(mois):

	return noms_mois[mois]


def heures_explicites(heures_texte):

	#print(heures_texte)

	if heures_texte == 'All Day':

		return [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]]

	# separer les morceaux (d'abord les blocs, ensuites les premier et derniers mois)

	heures_texte = heures_texte.replace(" ", "") # enlever les espaces inutiles

	heures_texte = heures_texte.replace("AM", "") # enlever les AM inutiles

	blocs = heures_texte.split(",") # certaines créatures ont plusieurs blocs d'heures de présences

	# determiner la première et dernière heure en chiffre et compléter la séquence (remplir les mois entre deux)

	i = 0

	for bloc in blocs:

		fin = -1 # sera remplacé si la période est plus longue que une heure

		deux_heures_lettres = bloc.split("-")

		#print(deux_heures_lettres[0])

		if 'PM' in deux_heures_lettres[0]:

			deux_heures_lettres[0] = heures_24[deux_heures_lettres[0]]

		debut = deux_heures_lettres[0]

		if len(deux_heures_lettres) > 1:

			if 'PM' in deux_heures_lettres[1]:

				deux_heures_lettres[1] = heures_24[deux_heures_lettres[1]]

			fin = int(deux_heures_lettres[1])

		#print(premier_mois)

		gauche = int(debut)

		liste_temp = [gauche]

		if fin != -1: # il a plus d'une heure dans le bloc

			# vérifier que ça ne passe pas à travers minuit

			if gauche > fin: # le bloc commence avant minuit et continue

				while gauche < 23: # remplir la liste jusqu'au mois décembre

					gauche += 1

					liste_temp.append(gauche)

				gauche = -1 # changer à minuit

				while gauche + 1 < fin:

					gauche += 1

					liste_temp.append(gauche)								

			if gauche < fin:

				while gauche + 1 < fin:

					gauche += 1

					liste_temp.append(gauche)

			#liste_temp.append(fin) # ne pas inclure l'heure de la fin puisque ça fini au début de l'heure...

		blocs[i] = liste_temp

		i += 1

	#print(blocs)

	# retourner la liste complète

	return blocs

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

		if len(deux_mois_lettres) > 1: # il a plus d'un mois dans le bloc

			deuxieme_mois = mois_numerique[deux_mois_lettres[1]]

			#print(deuxieme_mois)

			# vérifier que ça ne passe pas à travers décembre

			if gauche > deuxieme_mois: # le bloc commence avant décembre et continue dans la nouvelle année

				while gauche < 12: # remplir la liste jusqu'au mois décembre

					gauche += 1

					liste_temp.append(gauche)

				gauche = 0 # changer à janvier

				while gauche + 1 < deuxieme_mois:

					gauche += 1

					liste_temp.append(gauche)								

			if gauche < deuxieme_mois:

				while gauche + 1 < deuxieme_mois:

					gauche += 1

					liste_temp.append(gauche)

			liste_temp.append(deuxieme_mois)

		blocs[i] = liste_temp

		i += 1

	#print(blocs)

	# retourner la liste complète

	return blocs


def creatures_maintenant(mois_demande, heure_demande, joueur='', exhaustive=0):

	# Retourne une liste des créatures présente. Si aucun joueur n'est spécifié, c'est la liste complète pour le moment présent.

	# Si "exhaustive" est 1, c'est la liste la plus total qui est retourné.

	index_mois = {'fish':5, 'bugs':4} # les poissons ont un champs d'information supplémentaire (taille de l'ombre)

	index_heures = {'fish':6, 'bugs':5} # les poissons ont un champs d'information supplémentaire (taille de l'ombre)

	mois_present_texte = ''

	liste_creatures_presentes = []

	if joueur != '':

		creature_deja_capture = deja_capture(joueur)

	for type_creature in critters: # poisson et insecte ('fish' et 'bugs')

		for creature in listes_critters[type_creature]:

			mois_present_texte = creature[index_mois[type_creature]]

			heures_present_texte = creature[index_heures[type_creature]]

			blocs_mois_present_numerique = mois_explicites(mois_present_texte)

			blocs_heures_present_numerique = heures_explicites(heures_present_texte)

			#print(creature[0], blocs_mois_present_numerique)

			for bloc_mois in blocs_mois_present_numerique:

				if mois_demande in bloc_mois: # la créature est disponible ce mois-ci

					for bloc_heure in blocs_heures_present_numerique:

						#print(heure_demande, bloc_heure)

						if heure_demande in bloc_heure: # la créature est disponible ce mois-ci

							if joueur == '':

								creature.insert(0, type_creature) # réarrange l'ordre de l'information.

								liste_creatures_presentes.append(creature)

							else:

								if creature[0] not in creature_deja_capture:

									creature.insert(0, type_creature) # réarrange l'ordre de l'information.

									liste_creatures_presentes.append(creature)

	return liste_creatures_presentes


def ajouter_creature_capture(joueur):

	nom_fichier = joueur + '.txt'

	# Afficher la liste des créatures qui peuvent être ajouté:

	# Lister les créatures déjà capturé.

	acquis = deja_capture(joueur)

	with open(nom_fichier, 'a+') as fichier:
	

		# Afficher les créatures restantes



		info = 'test'

		# Enregistrer l'information dans le fichier.

		fichier.write(info)


def tous_creatures_du_moment(joueur=''):

	# Formarter et lister les créatures à afficher

	index_mois = {'fish':6, 'bugs':5} # les poissons ont un champs d'information supplémentaire (taille de l'ombre)

	index_heures = {'fish':7, 'bugs':6} # les poissons ont un champs d'information supplémentaire (taille de l'ombre)

	creatures_du_moment = []

	creatures_dispo_maintenant = creatures_maintenant(mois_format_12, heure_format_24, joueur)

	#print(creatures_dispo_maintenant)

	for creature in creatures_dispo_maintenant:

		nom = creature[1]

		le_type = traduction[creature[0]]

		endroit = creature[4]

		heure = creature[index_heures[creature[0]]]

		mois = creature[index_mois[creature[0]]]

		a_ajouter = le_type + ' - ' + nom + ': ' + endroit + ', ' + heure + ', ' + mois

		creatures_du_moment.append(a_ajouter)

	return creatures_du_moment


def deja_capture(joueur):

	nom_fichier = joueur + '.txt'

	liste = []

	try:

		with open(nom_fichier, 'r') as fichier:

			info = fichier.read()

			info = info.replace('\n', '') # enlever le symbole de nouvelle ligne

			if info != '':

				info = info.split(";")

				#print(info_ligne)

				liste = info

	except:

		print('\nLe fichier "' + nom_fichier + '" n\'existait pas. Il a donc été créé.')

		fichier = open(nom_fichier, 'w+') 

		fichier.close()

	return liste


def afficher_liste_demande(joueur=''):

	creatures_maintenants = tous_creatures_du_moment(joueur)

	type_affiche = ''

	if joueur == '':

		print('\n -- Liste complète: --')

	else:

		print('\n -- Liste personalisé pour ' + joueur + ': --')

	for creature in creatures_maintenants:

		type_de_la_creature = creature[:7]

		if type_de_la_creature != type_affiche:

			print('\nLes ' + type_de_la_creature + 's:\n')

			type_affiche = type_de_la_creature

		print(creature)



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


print('\n\n\n**********************', jour_format_30, noms_mois[mois_format_12], heure_format_long, '************************')

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

#test = mois_explicites(listes_critters["fish"][12][5])

#print(listes_critters["fish"][12])

#print(test)
'''
creatures_dispo_maintenant = creatures_maintenant(mois_format_12, heure_format_24)

print(creatures_dispo_maintenant)

for creature in creatures_dispo_maintenant:

	nom = creature[1]

	le_type = traduction[creature[0]]

	endroit = creature[4]

	#heure = 

	print(le_type, '-', nom + ':', endroit)


'''


afficher_liste_demande('david')

ajouter_creature_capture('grosjambon')























