# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import pandas as pd
with open('Top_100_Brands _ Comparably.html','r',encoding="utf8") as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    
    #print(soup)
    companies = []
    company_location = []
    industry_type = []
    
    company = soup.find_all('div',class_ = 'companyName')
    company_loc = soup.find_all('li',class_ = 'meta location')
    company_industry = soup.find_all('li',class_ = 'meta industry')
    
    rank = [i for i in range(1,96)]
    for data,loc,indus in zip(company,company_loc,company_industry):
        
        curr_company = data.text.lstrip('0123456789.- Rank')
        companies.append(curr_company)
        
        curr_loc = loc.text
        company_location.append(curr_loc)
        
        curr_ind = indus.text
        industry_type.append(curr_ind)
print(len(companies))
print(len(company_location))
print(len(industry_type))
print(len(rank))

main_data = {'rank' : rank,'company_name' : companies , 'company_location' : company_location ,'company_industry' : industry_type}

data_frame = pd.DataFrame(main_data)
print(data_frame)
data_frame.to_csv(r'C:\Users\katur\Documents\file1.csv')
