try:
    from importlib.util import spec_from_file_location
    import re
    import requests.exceptions
    from googlesearch import search
except ImportError:
	print("Un ou plusieurs modules necessaires manquants")


#Un tableau pour la liste de site
tab_Site=[]
# Pour le theme à rechercher
recherche = str(input("Entrez une thematique : "))
#Le nombre de resultat à generer à partir du theme
nbre= int(input("Donnez un nombre de resultat à generer compris entre 10 et 100 : "))
#On parcourt les liens issues de la recherche
for url in search(recherche,num_results=nbre):
    tab_Site.append(url)
# Un tableau pour l'ensemble des mails trouvés pendant l'excecution
emails = []
##Fonction pour la conversion de type Tableau en string histoire d'avoir un output lisible dans le fichier resultat
def listToString(tab):
    #chaine vide...
    spef=""
    for e in tab:
        #pour chaque element de la liste on a un retour à la ligne et une incrementation de la chaine de caratere
        spef+="\r\n"+e
    return spef
#Le parcours de la liste de site
for x in tab_Site:
    url = x
    print("Exploration de l'URL %s" % url)
    #une requete vers l'url x du tableau
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        # ignore les pages avec des erreurs et continue
        continue
    #new_emails pour les emails trouvé dans le response.text de x
    new_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
    #Ici j'en ai bavé 😂😂😂😂il faut faire une double conversion le re.findall retourne de base un tableau so voici la premiere conversion
    #avec la fonction ListToString
    pretty_new=listToString(new_emails)
    print(pretty_new)
    #emails reçoit les nouveaux emails
    emails.append(pretty_new)
    #reconversion emails to string
final=listToString(emails)
#Et ecriture du resulat dans un fichier txt
with open('Email_scraper.txt', 'w') as f:
           #"Appended line %d\r\n" % (e+1)
            f.write(final)
            f.close()