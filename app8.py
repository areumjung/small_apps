
# coding: utf-8

# In[69]:


import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

c = r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.findAll("div", {"class":"propertyRow"})

#len(all)

all[0].find("h4",{"class":"propPrice"}).text.replace("\n","")

page_nr = soup.findAll("a",{"class":"Page"})[-1].text
#print(page_nr)


# In[75]:


l = []
base_url = "https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,30,10):
    print(base_url + str(page) + ".html")
    r = requests.get(base_url + str(page) + ".html")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.findAll("div", {"class":"propertyRow"})
    
    for item in all:
        d = {}
        d["Price"] = item.find("h4",{"class":"propPrice"}).text.replace("\n","")
        d["Address"] = item.findAll("span",{"class":"propAddressCollapse"})[0].text
        
        try:
            d["Locality"] = item.findAll("span",{"class":"propAddressCollapse"})[1].text
        except:
            d["Locality"] = None
            
        try:
            d["beds"] = item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["beds"] = None

        try:
            d["Area"] = item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"] = None

        try:
            d["Full Baths"] = item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None

        try:
            d["Half Baths"] = item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None

        for column_group in item.findAll("div", {"class":"columnGroup"}):
            #print(column_group)
            for feature_group, feature_name in zip(column_group.findAll("span", {"class":"featureGroup"}), 
                                                   column_group.findAll("span", {"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)


# In[76]:


import pandas as pd
df = pd.DataFrame(l)

df.to_csv("output.csv")

