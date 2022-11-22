#importing required libraries
from bs4 import BeautifulSoup 
import pandas as pd
with open('Top_100_Brands _ Comparably.html','r',encoding="utf8") as html_file:
    
    content = html_file.read() #reading content from the html file
    
    soup = BeautifulSoup(content,'lxml') #setting in a perfect format
    
    #variables to store data
    companies = []
    company_location = []
    industry_type = []
    rank = [i for i in range(1,96)]
    
    #collecting data
    company = soup.find_all('div',class_ = 'companyName')
    company_loc = soup.find_all('li',class_ = 'meta location')
    company_industry = soup.find_all('li',class_ = 'meta industry')
    
    
    for data,loc,indus in zip(company,company_loc,company_industry):
        
        curr_company = data.text.lstrip('0123456789.- Rank')
        companies.append(curr_company)
        
        curr_loc = loc.text
        company_location.append(curr_loc)
        
        curr_ind = indus.text
        industry_type.append(curr_ind)

main_data = {'rank' : rank,'company_name' : companies , 'company_location' : company_location ,'company_industry' : industry_type}

#converting data into a csv file
data_frame = pd.DataFrame(main_data)
print(data_frame)
data_frame.to_csv(r'C:\Use\t\Doc\file1.csv')
