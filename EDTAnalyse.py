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
		print ("Aucun fichier CVS n'a été trouvé dans ce dossier, veuillez rentrer un chemin de dossier valide")
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
	for x in files:
		fileToRead = open(x, "r")
		content.append(fileToRead.read())
	cpt = 0
	for i in content:
		content[cpt] = i.split("BEGIN:VEVENT")
	print(content)
		
		

		
############# MAIN ###############

path = input("Veuillez entrer le chemin du dossier contenant les fichiers VCS : ")
path = path.replace('/', '')

vcs_parser(find_files(path))
