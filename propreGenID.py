#!/usr/bin/python3
import csv

x=input('entrer un chemin de fichier CSV : ')
f=open(x, 'r')
t=csv.reader(f,delimiter=';')
tab=[]
dicoLogin = {}
res=[]

for l in t:
    tab.append(l)

def multiLogin(loginExiste, login):
    if loginExiste > 0:
        login = login[:-1]+str(loginExiste)
    return login

def loginExiste(dicoLogin, login):
    if login in dicoLogin:
        dicoLogin[login] = +1
    else:
        dicoLogin[login] = 0
    return dicoLogin[login]

def nettoyeTout(chaine):
    chaine=chaine.replace(" ","")
    chaine=chaine.replace("-","")
    return chaine

def creerLogin(nom, prenom):
    c=[prenom[0],nom[:7]]
    login="".join(c)
    return login

def creerLogin2(login, prenom, nom):
    c=[nom,prenom]
    login,np=login, "-".join(c)
    return login,np
                           
fichier = open("listLogin-result.html", 'a') 

for i in range(len(tab)):
    nom=tab[i][0]
    prenom=tab[i][1]
    login=creerLogin(nettoyeTout(nom), nettoyeTout(prenom))
    login=multiLogin(loginExiste(dicoLogin, login), login)
    login,np=creerLogin2(login, prenom, nom)
    result=login,np
    fichier.write(result) 
    print(login,np)

fichier.close()
