# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
#"""
import bs4
import sys
import urllib
import wget
import webbrowser
   
def check_validity(my_url):
    try:
        urllib.request.urlopen(my_url)
        print("Valid URL")
    except IOError:
        print ("Invalid URL")
        sys.exit()


def get_pdfs(my_url):
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

   
    try:
        file = wget.download(links[0])
    except:
            print(" \n \n Unable to Download A File \n")
    print(file)

def lire():
    webbrowser.open_new(r'file:./m-mentos---rentr-e-2021-18745.pdf')