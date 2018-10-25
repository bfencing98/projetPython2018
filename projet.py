def Nom(fichier):		#Liste les noms des Prof
    listNom=[]
    f=open(fichier,"r")
    for l in f:
        lsp=l.split('\n')
        nom=lsp[0]
        nomsp=nom.split(';')
        if "DESCRIPTION" in nomsp:
            nomsp=nom.split(':')
            listNom.append(nomsp[3][:-3])
    return listNom
    f.close()

def Salle(fichier):		#Liste les Salles
    listSalle=[]
    f=open(fichier, "r")
    
    for l in f:
        lsp=l.split('\n')
        salle=lsp[0]
        sallesp=salle.split(':')
        if "LOCATION" in sallesp:
           listSalle.append(sallesp[1])
    return listSalle
    f.close()

def Mod(fichier):		#Liste les matières 
    listMod=[]
    f=open(fichier, "r")

    for l in f:
        lsp=l.split('\n')
        module=lsp[0]
        modulesp=module.split(':')
        if "SUMMARY" in modulesp:
          # print(modulesp[1])
          listMod.append(modulesp[1])
    return listMod
    f.close()
    
def Start(fichier):		#Donne la date, horaire du cours
    listStart=[]		#Sous forme : AAAAMMDDTHHMM00Z
    f=open(fichier,"r")
    
    for l in f :
        lsp=l.split('\n')
        Start=lsp[0]
        Startsp=Start.split(':')
        if "DTSTART" in Startsp[0]:
            listStart.append(Startsp[1])
    return listStart
    f.close()


def End(fichier):		#Donne la date, horaire du cours
    listEnd=[]			#Sous forme : AAAAMMDDTHHMM00Z
    f=open(fichier,"r")
    for l in f:
         lsp=l.split("\n")
         End=lsp[0]
         Endsp=End.split(';')
         if "DTEND" in Endsp[0]:
             Endsp=End.split(':')
             listEnd.append(Endsp[1])
    return listEnd
    f.close()
    

listNom=[]
listSalle=[]
listMod=[]
listStart=[]
listEnd=[]
        

listNom.append(Nom("./VCSFiles/GPU_semaine_41_FIL-2.vcs"))
print(listNom)

listSalle.append(Salle("./VCSFiles/GPU_semaine_41_FIL-2.vcs"))
print(listSalle)

listMod.append(Mod("./VCSFiles/GPU_semaine_41_FIL-2.vcs"))
print(listMod)

listStart.append(Start("./VCSFiles/GPU_semaine_41_FIL-2.vcs"))
print(listStart)

listEnd.append(End("./VCSFiles/GPU_semaine_41_FIL-2.vcs"))
print(listEnd)

