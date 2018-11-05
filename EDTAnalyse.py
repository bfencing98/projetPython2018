"""
+----------------------------------------------+
|         Python Project main response         |
|  Made by Baptiste Bonnaudet, Tom Lepore and  |
|            and Leo Leffy in 2018             |
+----------------------------------------------+
"""
#!/usr/bin/python

import os
import sys
import time

def find_files(path):
	os.system("ls "+path+" | grep .*.vcs > ./tmpFilesNames.txt")
	tmpFilesNames = open("tmpFilesNames.txt", "r")
	filesNames = tmpFilesNames.read()
	tmpFilesNames.close()

	if len(filesNames) == 0:
		print("Aucun fichier CVS n'a été trouvé dans ce dossier, veuillez rentrer un chemin de dossier valide")
		sys.exit()

	files = []
	files = filesNames.split("\n")
	files = [i for i in files if i != '']
	path = path+"/"

	cpt = 0
	for x in files:
		files[cpt] = path+x
		cpt = cpt+1
	return files

def vcs_parser(files):
	content = []
	listNom=[]
	listSalle=[]
	listMod=[]
	listStart=[]
	listEnd=[]

	for x in files:
		content = open(x, "r")
		for l in content:
			lsp=l.split('\n')
			nom=lsp[0]
			nomsp=nom.split(';')
			if "DESCRIPTION" in nomsp:
				nomsp=nom.split(':')
				listNom.append(nomsp[3][:-3])

		content = open(x, "r")
		for l in content:
			lsp=l.split('\n')
			salle=lsp[0]
			sallesp=salle.split(':')
			if "LOCATION" in sallesp:
				listSalle.append(sallesp[1])

		content = open(x, "r")
		for l in content:
			lsp=l.split('\n')
			module=lsp[0]
			modulesp=module.split(':')
			if "SUMMARY" in modulesp:
				listMod.append(modulesp[1])

		content = open(x, "r")
		for l in content :
			lsp=l.split('\n')
			Start=lsp[0]
			Startsp=Start.split(':')
			if "DTSTART" in Startsp[0]:
				listStart.append(Startsp[1])

		content = open(x, "r")
		for l in content:
			lsp=l.split("\n")
			End=lsp[0]
			Endsp=End.split(';')
			if "DTEND" in Endsp[0]:
				Endsp=End.split(':')
				listEnd.append(Endsp[1])

	parsedContent = []
	parsedContent.append(listNom)
	parsedContent.append(listSalle)
	parsedContent.append(listMod)
	parsedContent.append(listStart)
	parsedContent.append(listEnd)
	print(parsedContent)
	
	return parsedContent


############# MAIN ###############

path = input("Veuillez entrer le chemin du dossier contenant les fichiers VCS : ")
path = path.replace('/', '')

vcs_parser(find_files(path))
