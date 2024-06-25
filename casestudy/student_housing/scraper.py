import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def api_call(url):
  payload = {'api_key': '#########', 'url': url}
  try:
    response = requests.get('http://api.scraperapi.com', params=payload)
  except ConnectionError:
    print("Connection Error")
    exit(0)
  
  return response


page_amount = 50

url_first_part = 'https://www.wg-gesucht.de/wg-zimmer-in-Muenchen.90.0.1.'
url_second_part = '.html'                                                                       #complete url => first part + page_number + second part

total_link_list = []

for page_number in range(1, page_amount):

    response = api_call(url_first_part + str(page_number) + url_second_part)
    soup = BeautifulSoup(response.content, "html.parser")

    relevant_page_content = soup.find("div", attrs={'class': 'col-xs-12 col-md-8 col-md-push-4'})
    links = relevant_page_content.find_all("a", attrs={'class': 'detailansicht'})

    even = True
    for link in links[1:]:
        intern_link = link.get("href")
        if even:
            if "sort_column" not in intern_link:
                total_link_list.append("https://www.wg-gesucht.de/" + intern_link)
            even = False
        else:
            even = True

print(total_link_list)


def get_page_content(page_content, Url):
    try:
        title = page_content.find("h1", attrs={'class': 'headline headline-detailed-view-title'}).text.strip()             # get title String
        
        size = page_content.find_all("b", attrs={'class': 'key_fact_value'})[0].text.strip()             # get size String

        price_total = page_content.find_all("b", attrs={'class': 'key_fact_value'})[1].text.strip()             # get price_total String

        price = page_content.find_all("span", attrs={'class': 'section_panel_value'})[0].text.strip()             # get price String

        extra_costs = page_content.find_all("span", attrs={'class': 'section_panel_value'})[1].text.strip()             # get extra_costs String

        other_costs = page_content.find_all("span", attrs={'class': 'section_panel_value'})[2].text.strip()             # get other_costs String

        deposit = page_content.find_all("span", attrs={'class': 'section_panel_value'})[3].text.strip()             # get deposit String

        redemption_agreement = page_content.find_all("span", attrs={'class': 'section_panel_value'})[4].text.strip()             # get redemption_agreement String

        date_free = page_content.find_all("span", attrs={'class': 'section_panel_value'})[5].text.strip()             # get date_free String

        date_free_till= "n.a."
        if len(page_content.find_all("span", attrs={'class': 'section_panel_value'})) > 6:
            date_free_till = page_content.find_all("span", attrs={'class': 'section_panel_value'})[6].text.strip()             # get date_free_till String
               
        online_since =  page_content.find("b", attrs={'class': 'noprint'}).text.strip()             # get online_since String
        
        adress = page_content.find_all("span", attrs={'class': 'section_panel_detail'})[5].text.strip()             # get adress String

        details = ""
        for detail in page_content.find_all("ul", attrs={'class': 'pl15'})[0].find_all("span", attrs={'class': 'section_panel_detail'}):              #get Details String
            details += detail.text.strip() + '\n'

        looking_for = ""
        for looking_for_element in page_content.find_all("ul", attrs={'class': 'pl15'})[1].find_all("span", attrs={'class': 'section_panel_detail'}):              #get looking_for String
            looking_for += looking_for_element.text.strip() + '\n'

        amount_of_icons = "n.a. "
        if len(page_content.find_all("div", attrs={'class': 'utility_icons'})) > 0:
            amount_of_icons = len(page_content.find_all("div", attrs={'class': 'utility_icons'})[0].find_all("div", attrs={'class': 'text-center'}))         # get amount_of_icons String
        
        amount_of_icons_needed = "n.a."
        if len(page_content.find_all("div", attrs={'class': 'utility_icons'})) > 1:
            counter = 0
            counter += len(page_content.find_all("div", attrs={'class': 'utility_icons'})[1].find_all("div", attrs={'class': 'text-center'}))         # get amount_of_icons String
            counter += len(page_content.find_all("div", attrs={'class': 'utility_icons'})[1].find_all("a", attrs={'class': 'text-center campaign_click'}))
            amount_of_icons_needed = counter

        description_room_div = page_content.find("div", attrs={'id': 'freitext_0'})
        description_room = 'n.a.'
        if description_room_div:
            description_room = description_room_div.text.strip()
                    
        description_location_div = page_content.find("div", attrs={'id': 'freitext_1'})
        description_location = 'n.a.'
        if description_location_div:
            description_location = description_location_div.text.strip()
      
        # Check and get description_life if it exists
        description_life_div = page_content.find("div", attrs={'id': 'freitext_2'})
        description_life = 'n.a.'
        if description_life_div:
            description_life = description_life_div.text.strip()
       
        # Check and get description_other if it exists
        description_other_div = page_content.find("div", attrs={'id': 'freitext_3'})
        description_other = 'n.a.'
        if description_other_div:
            description_other = description_other_div.text.strip()
                    

        return {'Url': Url, 'Title': title, 'Size': size, 'PriceTotal': price_total, 'Price': price, 'ExtraCosts': extra_costs, 'OtherCosts': other_costs, 'Deposit': deposit, 'RedemptionAgreement': redemption_agreement, 'DateFree': date_free, 'DateFreeTill': date_free_till, 'OnlineSince': online_since, 'Adress': adress, 'Details': details, 'LookingFor': looking_for, 'AmountofIcons': amount_of_icons, 'AmountofIconsNeeded': amount_of_icons_needed, 'DescriptionRoom': description_room, 'DescriptionLocation': description_location, 'DescriptionLife': description_life, 'description_other': description_other}
    except (AttributeError, IndexError) as e:
        return "error"



main_dict = {'Url': [], 'Title': [], 'Size': [], 'PriceTotal': [], 'Price': [], 'ExtraCosts': [], 'OtherCosts': [], 'Deposit': [], 'RedemptionAgreement': [], 'DateFree': [], 'DateFreeTill': [], 'OnlineSince': [], 'Adress': [], 'Details': [], 'LookingFor': [], 'AmountofIcons': [], 'AmountofIconsNeeded': [], 'DescriptionRoom': [], 'DescriptionLocation': [], 'DescriptionLife': [], 'description_other': []}

for link in total_link_list:
    
    response = api_call(link)
    soup = BeautifulSoup(response.content, "html.parser")
    temp_dict = get_page_content(soup, link)
    if temp_dict == "error":
        continue    
    for key, value in temp_dict.items():
        if key in main_dict:
            main_dict[key].append(value) 
        else:
            main_dict[key] = [value]  

    
result_dataframe = pd.DataFrame(main_dict)

print(result_dataframe.size)
display(result_dataframe)

# Save DataFrame to CSV without the index
result_dataframe.to_csv('wggesucht_scraped_22_05.csv', index=False)   