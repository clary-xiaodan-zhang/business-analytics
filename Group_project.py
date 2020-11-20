#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Created on Fri Nov 20 11:58:15 2020
#@author: xiaodanzhang

import requests
import bs4 
import csv





'''Print All Reviews'''

url = input("Please provide of link of the first page of a website on TrustPilot: ")
pages_to_scrape = int(input("How many pages are there to scrape: "))

def makesoup(url):
    response = requests.get(url) 
    #print('response code is: ', response.status_code)

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print('Issue getting url, Error code: ', response.status_code)
        return None

def print_reviews():
    review_no = 0
    page_no = 1
    while(page_no <= pages_to_scrape):
        scrape_url = str(url)+'?page='+str(page_no)
        print('url:', scrape_url)
        ret_soup = makesoup(scrape_url)
        if ret_soup:   
            for review in ret_soup.find_all('p', class_='review-content__text'): 
                print('review number:', review_no)
                print('review text:',review.text) #We are interested only in the text data, since the reviews are stored as text
                print("\n")
                review_no += 1
        page_no += 1
    print('All reviews successfully printed!')
    print('Total number of reviews scrapped::', review_no-1)
        
print_reviews()






'''Sentiment Analysis'''

def get_reviews():
    review_no = 0
    page_no = 1
    review_list=[]
    while(page_no <= pages_to_scrape):
        # Automatically access subsequent pages
        # 1st page url: https://www.trustpilot.com/review/vivino.com?page=1
        # 2nd page url: https://www.trustpilot.com/review/vivino.com?page=2
        # 3rd page url: https://www.trustpilot.com/review/vivino.com?page=3
        scrape_url = str(url)+'?page='+str(page_no)
        ret_soup = makesoup(scrape_url)
        if ret_soup:   
            for review in ret_soup.find_all('p', class_='review-content__text'): 
                review_list.append(review.text)
                review_no += 1
        page_no += 1
    print('Length of the review list: ',len(review_list))
    return review_list
    


SENTIMENT_CSV = "/Users/xiaodanzhang/Google Drive/1. HEC - M2 - Digital/1. Businss Analytics Using Python/word_sentiment.csv"
'''Updated the path to point to your file. The path provided changes based on your operating system. '''
'''For a windows system the format of the path will be "C:/Users/User/Desktop/word_sentiment.csv" '''

def word_sentiment(word):
    """This function uses the word_sentiment.csv file to find the sentiment of the word 
    entered"""
    with open(SENTIMENT_CSV, 'rt',encoding = 'utf-8') as senti_data:
        sentiment = csv.reader(senti_data)
        for data_row in sentiment:          
            if data_row[0] == word.lower():
                sentiment_val = data_row[1]                
                return sentiment_val
        return 0    
                
def main():
    """This function asks the user to input a sentence and tries to calculate the sentiment 
    of the sentence as the total sentiments of all the words in the sentence"""
    sentiment = 0 
    sentence_in = ' '.join(get_reviews()).lower()
    words_list = sentence_in.split()
    for word in words_list:
        sentiment = sentiment + int(word_sentiment(word))
    print('The sentiment score of all the reviews is: ',sentiment)
    if sentiment > 0: 
        print("The total reviews have a positive sentiment")
    elif sentiment == 0: 
        print("The total reviews have a neutral sentiment")
    else:
        print("The total reviews have a negative sentiment")
              
main()