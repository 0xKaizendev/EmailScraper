try:
    from importlib.util import spec_from_file_location
    import re
    import requests.exceptions
    from googlesearch import search
except ImportError:
	print("Un ou plusieurs modules necessaires manquants")

# Creating an empty list.
tab_Site=[]

# Asking the user to input a theme.
recherche = str(input("Entrez une thematique : "))

# Asking the user to input a language.
langue= str(input("Entrez le langage de la recherche : "))

# Asking the user to input a number of results to generate.
search_Count= int(input("Donnez un nombre de resultat à generer : "))
# Asking the user to input a country.
search_Country= str(input("Entrez le pays cible : "))

# Searching for the user input and appending the results to the tab_Site list.
for url in search(recherche,num=15,start=0,stop=search_Count,country=search_Country,tld='com',lang="en"):
    tab_Site.append(url)

# Creating an empty list.
emails = []

def listToString(tab):
    """
    It takes a list of strings and returns a string with each element of the list on a new line
    
    :param tab: the list of strings to be converted to a single string
    :return: A string of the elements in the list, separated by newlines.
    """
    spef=""
    for e in tab:
        spef+="\r\n"+e
    return spef
# A for loop that iterates through the tab_Site list and appends the results to the emails list.
for x in tab_Site:
    url = x
    print("Exploration de l'URL %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue
    new_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
    pretty_new=listToString(new_emails)
    print(pretty_new)
    emails.append(pretty_new)
final=listToString(emails)
# Writing the final list to a text file.
with open('Email_scraper.txt', 'w') as f:
            f.write(final)
            f.close()