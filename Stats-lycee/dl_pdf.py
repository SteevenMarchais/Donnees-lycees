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
    my_url = "https://www.ac-poitiers.fr/minihome/publications-statistiques-122378"
    links = []
    html = urllib.request.urlopen(my_url).read()
    html_page = bs4.BeautifulSoup(html, features="lxml") 
    og_url = html_page.find("meta",  property = "og:url")
    base = urllib.request.urlparse(my_url)
    for link in html_page.find_all('a'):
        current_link = link.get('href')
        if current_link.endswith('download'):
            if og_url:
                print("currentLink",current_link)
                links.append("https://www.ac-poitiers.fr" + current_link)
            else:
                links.append(base.scheme + "://" + base.netloc + current_link)

   
    file1 = wget.download(links[3])
    shutil.move("./" + file1, "../data/" + file1)
    pdf1 = open("../data/" + file1, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdf1) 
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)  
    test = pageObj.extractText()
    c = test.index("Terminales")
    for i in range(c, c+38):
        print(test[i])
    pdf1.close() 
    

    
def get_pdfs_Bordeaux():
    my_url = "https://www.ac-bordeaux.fr/article/second-degre-121965"
    links = []
    html = urllib.request.urlopen(my_url).read()
    html_page = bs4.BeautifulSoup(html, features="lxml") 
    og_url = html_page.find("meta",  property = "og:url")
    base = urllib.request.urlparse(my_url)
    for link in html_page.find_all('a'):
        current_link = link.get('href')
        if current_link.endswith('download'):
            if og_url:
                print("currentLink",current_link)
                links.append("https://www.ac-bordeaux.fr" + current_link)
            else:
                links.append(base.scheme + "://" + base.netloc + current_link)

    file1 = wget.download(links[0])
    shutil.move("./" + file1, "../data/" + file1)
    pdf1 = open("../data/" + file1, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdf1) 
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(5)  
    test = pageObj.extractText()
    print(test)
    pdf1.close() 


# def get_pdfs_Limoges():
#     my_url = "https://www.ac-bordeaux.fr/article/second-degre-121965"
#     links = []
#     html = urllib.request.urlopen(my_url).read()
#     html_page = bs4.BeautifulSoup(html, features="lxml") 
#     og_url = html_page.find("meta",  property = "og:url")
#     base = urllib.request.urlparse(my_url)
#     for link in html_page.find_all('a'):
#         current_link = link.get('href')
#         if current_link.endswith('download'):
#             if og_url:
#                 print("currentLink",current_link)
#                 links.append("https://www.ac-bordeaux.fr" + current_link)
#             else:
#                 links.append(base.scheme + "://" + base.netloc + current_link)

   
    
#     file2 = wget.download(links[0])
#     shutil.move("./" + file2, "../data/" + file2)


    

