import requests
from bs4 import BeautifulSoup
import re
import argparse

def scrapeDetails(prediction):
    result = requests.get("https://www.medicinenet.com/search/mni/"+prediction)
    c = result.content
    soup = BeautifulSoup(c, features="lxml")
    samples = soup.find_all("div", "spotlight")
    disease = soup.find_all("div", "searchresults main")
    medication = soup.find_all("div", "searchresults medication")
    procedures = soup.find_all("div", "searchresults proc")
    return (samples[0].get_text().split('.')[0], disease[0].get_text().split('.')[0], medication[0].get_text().split('.')[0], procedures[0].get_text().split('.')[0])

def scrapeDoctors():    
    results = requests.get("https://www.practo.com/search?results_type=doctor&q=%5B%7B%22word%22%3A%22General%20Physician%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=Chennai")
    cc = results.content
    soup = BeautifulSoup(cc, features="lxml")
    docimage = soup.find_all("div", "u-spacer--right c-card__left c-card__photo")
    docname = soup.find_all("h2", "u-title-font u-c-pointer u-bold")
    docdetails = soup.find_all("span", "u-color--green u-bold")
    patientexp = soup.find_all("a", "c-card-list__item")
    #details = soup.find_all("h3", "u-t-ellipsis")
    return (docname[0].get_text(), docdetails[0].get_text(), patientexp[0].get_text(), docname[1].get_text(), docdetails[1].get_text(), patientexp[1].get_text(), docname[2].get_text(), docdetails[2].get_text(), patientexp[2].get_text())