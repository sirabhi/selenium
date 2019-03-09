# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:34:50 2018

@author: admin
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from docx import Document
from selenium.webdriver.firefox.options import Options

options=Options()
options.set_headless(True)
driver=webdriver.Firefox(options=options,executable_path="D:\\abhishek\\geckodriver.exe")


driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("quick sort")

time.sleep(10)
driver.find_element_by_name("btnK").click()
time.sleep(10)
links=[]

urls=driver.find_elements_by_xpath("//div[@class='r']/a")

for l in urls:
    links.append(l.get_attribute('href'))
    
print links

#a=driver.find_element_by_partial_link_text('GeeksforGeeks').click();
#time.sleep(10)
#my_url=driver.current_url
my_url=links[0]

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
word=page_soup.find('h1').findNext("p").get_text()
print("Overview")
print word

a=driver.find_element_by_partial_link_text('Wikipedia').click();
time.sleep(10)
my_url=driver.current_url
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
print("\n")

word=page_soup.find(text="History").findNext("p").get_text()
print("History")
print word

word3=page_soup.find('h1').findNext("p").get_text()
print("Description")
print word3

word1=page_soup.find('span',{'id':'Algorithm'}).findNext("p").get_text()
word2=page_soup.find('span',{'id':'Algorithm'}).findNext("pre").get_text()
print("Algorithm")
print word1
print word2

"""
Important
uClient1=uReq(links[0])

page_html=uClient1.read()
uClient1.close()
page_soup1=soup(page_html,"html.parser")

def fun():
    if page_soup1.find('pre') :
         return 1
    else:
   
        return 2
x=fun()

if x==1 :
     word=page_soup1.find('pre').get_text()
     print word
    
"""         




"""

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
print("\n")
#word=page_soup.find('h1').findNext("p").get_text()
#print word
#print("\n")
#word=page_soup.find(text="Quick Sort Pivot Algorithm").findNext("p").get_text()
#print word
s=page_soup.get_text()
print s

"""



