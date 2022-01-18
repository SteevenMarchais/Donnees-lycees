# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
#"""
import bs4
import urllib
import wget
import shutil
import PyPDF2
   


def get_pdfs_Poitier():
    
    """
    Télécharge et affiche le texte nécessaire du pdf
    
    Entree
    ----------
    my_url:str
    url du site web sur lequel se trouve le pdf
    
    Return
    ---------
    text:str
    texte extrait du pdf
    """
    my_url = "https://www.ac-poitiers.fr/minihome/publications-statistiques-122378"
    links = []
    html = urllib.request.urlopen(my_url).read() #ouvre le site web
    html_page = bs4.BeautifulSoup(html, features="lxml") 
    og_url = html_page.find("meta",  property = "og:url") #cherche les liens dans la page html
    base = urllib.request.urlparse(my_url)
    for link in html_page.find_all('a'): #cherche les balises a
        current_link = link.get('href')#récupere le lien
        if current_link.endswith('download'):#regarde s'il y a download à la fin du lien
            if og_url:
                print("currentLink",current_link)
                links.append("https://www.ac-poitiers.fr" + current_link)#complete l'url
            else:
                links.append(base.scheme + "://" + base.netloc + current_link)

   
    file1 = wget.download(links[3])#télécharge le 4ème pdf
    shutil.move("./" + file1, "../data/" + file1)#envoie le pdf dans le fichier data
    """
    lire et extraire les données du pdf
    """
    pdf1 = open("../data/" + file1, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdf1) 
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)  
    text = pageObj.extractText()
    c = text.index("Terminales")
    for i in range(c, c+38):
        print(text[i])
    pdf1.close() 
    

    
def get_pdfs_Bordeaux():
    """
    Télécharge et affiche le texte nécessaire du pdf
    
    Entree
    ----------
    my_url:str
    url du site web sur lequel se trouve le pdf
    
    Return
    ---------
    text:str
    texte extrait du pdf
    """
    my_url = "https://www.ac-bordeaux.fr/article/second-degre-121965"
    links = []
    html = urllib.request.urlopen(my_url).read()#ouvre le site web
    html_page = bs4.BeautifulSoup(html, features="lxml") 
    og_url = html_page.find("meta",  property = "og:url")#cherche les liens dans la page html
    base = urllib.request.urlparse(my_url)
    for link in html_page.find_all('a'):#cherche les balises a
        current_link = link.get('href')#cherche les balises a
        if current_link.endswith('download'):#regarde s'il y a download à la fin du lien
            if og_url:
                print("currentLink",current_link)
                links.append("https://www.ac-bordeaux.fr" + current_link)#complete l'url
            else:
                links.append(base.scheme + "://" + base.netloc + current_link)

    file1 = wget.download(links[0])#télécharge le 1er pdf
    shutil.move("./" + file1, "../data/" + file1)#envoie le pdf dans le fichier data
    """
    lire et extraire les données du pdf
    """
    pdf1 = open("../data/" + file1, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdf1) 
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(5)  
    text = pageObj.extractText()
    print(text)
    pdf1.close() 

# def main():
    
# if __name__ == "__main__":
#     main()
    

