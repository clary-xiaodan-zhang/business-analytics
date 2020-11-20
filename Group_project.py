#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:58:15 2020

@author: xiaodanzhang
"""

import requests
import bs4 

#url = "https://www.airbnb.com/experiences/1677350?currentTab=experience_tab&federatedSearchId=99f5bcea-d8eb-40bc-9798-421a39b67923&searchId=6b41c597-8221-4c8a-80ad-629609de194d&sectionId=badc9767-3385-4288-9882-09a2e2d30289&source=p2&modal=REVIEWS"
url = "https://www.trustpilot.com/review/vivino.com?page=1"

def scrapecontent(url):
    response = requests.get(url) 
    print('response code is: ', response.status_code)

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print('Issue getting url, Error code: ', response.status_code)
        return None

'''def rating_n(text):
    if text == '1 star: Bad':
        return 1
    elif text == '2 stars: Poor':
        return 2
    elif text == '3 stars: Average':
        return 3
    elif text == '4 stars: Great':
        return 4
    else:
        return 5'''

def main():
    review_no = 0
    page_no = 1
    while(page_no <= 1):
        # Automatically access subsequent pages
        # 1st page url: https://www.trustpilot.com/review/vivino.com?page=1
        # 2nd page url: https://www.trustpilot.com/review/vivino.com?page=2
        # 3rd page url: https://www.trustpilot.com/review/vivino.com?page=3
        scrape_url = 'https://www.trustpilot.com/review/vivino.com?page='+str(page_no)
        print('url:', scrape_url)
        ret_soup = scrapecontent(scrape_url)
    
        rating = ret_soup.find('div', class_='star-rating star-rating--medium').find('img', alt=True)
        rating_text = rating['alt']
            
        if ret_soup:   
            for review in ret_soup.find_all('p', class_='review-content__text'): 
            #for review in ret_soup.find_all('article', class_='review'): 
                #comment = review.find('p', class_='review-content__text')
                #title = review.find('p', class_='review-content__title')
                print('review number:', review_no)
                #print('review rating:',rating_n(rating_text))
                #print('review title:',title.text)
                print('review text:',review.text) #We are interested only in the text data, since the reviews are stored as text
                print("\n")
                review_no += 1
        page_no += 1
        print('Success!!!')
        print('Total number of reviews scrapped::', review_no-1)
        
main()



'''
if response.status_code == 200:
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    
    #usernames = soup.find_all('div', class_='_1lc9bb6')
    #dates = soup.find_all('div', class_='_1ixuu7m')
    #reviews = soup.find_all('div', class_='_1y6fhhr')
    reviews = soup.find_all('p', class_='review-content__text')
    
    count = 0
    while count < len(reviews):
        print('review number:', count+1)
        #print('review user:', usernames[count].div.text)
        #print('review date:', dates[count].contents[0][9:])
        print('review text:', reviews[count].text)
        print('\n')
        count += 1
        
    print('Total number of reviews scrapped:', len(reviews))
    
else:
    print('Issue getting url, Error code: ', response.status_code)
'''