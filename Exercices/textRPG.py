#!/usr/bin/python2.7
# -*- coding: latin-1 -*-

import sys
from math import *

print "Bienvenue dans donjons et demons quel est le nom de ton perso?"
nom=sys.stdin.readline()
print "Bienvenue "+nom

#Saisie de l'age
age = 0
saisieCorrecte = False
premiereBoucle = True #Necessaire a la premiere execution de la boucle
while not saisieCorrecte: #Tant que la saisie n'est pas correcte
	saisieCorrecte = True #Partons du principe que la saisie est correcte
	age = raw_input("Quel est ton age ?") #Mieux que input ou readline. ne prends pas en compte le \n
	indice = 0
	tailleTableau = len(age)
	#Tant que l'on a pas vérifié tous les caractères saisis par le joueur
	#	ET que tous les caractères sont valides (Il ne sert a rien de continuer
	#	si l'on a detecté un carractère invalide)
	while (indice < tailleTableau) and (saisieCorrecte == True):
		if not age[indice] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			print "Vous avez saisi un caractere incorrect : " + age[indice]
			saisieCorrecte = False	
		indice += 1

if int(age) > 25:
	reponse = str(age) + " ans ? C'est un age vénérable pour un guerrier"
else:
	reponse = "C'est un peu jeune, tu vas payer son insouciance !"
if int(age) == 42:
	reponse = reponse + "\n Et en plus c est le nombre magique !"
	
print(reponse)

#Choix de la porte par entree d'une touche
toucheValide=False
while toucheValide == False:

	print "Un bruit de mécanisme semble emmaner de la pièce de droite."
	print "Tu entends un bruit d'éternuement venant de la porte de gauche."
	direction = raw_input("Quelle porte souhaites-tu emprunter ? Droite (d) ou Gauche (g)\n")

	if direction == "d": 
		print ("A peine tu ouvres la porte qu'une flèche vient se loger dans ton coeur, tu es mort.")
		retry = raw_input("Désires tu revenir au choix de la porte ? o/n \n")
		if retry == "o":
			toucheValide = False #Dans ce cas, il n'a pas vraiment tapé une mauvaise touche,
			# Mais celà permet de relancer la boucle (comme si il avait tappé une mauvaise touche
		else:
			toucheValide = True
	elif direction == "g":
		print ("Alors que tu ouvres la porte, un garde te fait face, il n'a pas l'air commode.")
		toucheValide = True
	else:
		print ("Touche invalide. Veuillez renseigner une touche valide.")

#Combat
pointsDeVieDuGarde = 50
print "le garde a " + str(pointsDeVieDuGarde) +", pv utilise une addition pour reduire ses pv nul!"
m=0
while pointsDeVieDuGarde > 0:
	a = raw_input("a ?\n")
	b = raw_input("b ?\n")
	m = int(a) + int(b)
	print(a + " + " + b + " = " + str(m)) #Affichage de l'addition grace à la concaténation
	reponse = "Tu infliges " + str(m) + " pts de degats"
	pointsDeVieDuGarde = pointsDeVieDuGarde -  m
	if pointsDeVieDuGarde <= 0: 
		reponse = reponse + "\nBien joué ! Tu enfonces ton épée dans les entrailles du garde."
		reponse = reponse + "\nLe garde s'éfondre sur le sol, tu peux maintenant t'echapper !"
	else:
		reponse = reponse + "\nTu y es presque !"
		reponse = reponse + "\nLe garde a ("+str(pointsDeVieDuGarde)+") pv, utilise une nouvelle addition pour reduire ses pv à 0" 
	print(reponse)
