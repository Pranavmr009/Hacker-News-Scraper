import requests
from bs4 import BeautifulSoup
from colorama import Fore
from termcolor import colored
import sys
from os import system

urls = ['https://thehackernews.com/', 
'https://thehackernews.com/search/label/data%20breach', 
'https://thehackernews.com/search/label/Cyber%20Attack', 
'https://thehackernews.com/search/label/Vulnerability', 
'https://thehackernews.com/search/label/Malware']


for url in urls:
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'lxml')
    headlines = soup.find_all(attrs={'class':'story-link'})

    print(colored(Fore.LIGHTBLUE_EX + "Today's News main".center(60) ,attrs=['bold']) + '\n')
    for headline in headlines[:5]:
        
        date_published = headline.find('div', class_='item-label')   
        title = headline.find('h2', class_='home-title')

        headline = headline.get('href')

        print(Fore.MAGENTA + f"Title: {title.text}")
        print(Fore.LIGHTGREEN_EX + f"Url: {headline}")
        print(Fore.LIGHTBLUE_EX + f"Date/Author: {date_published.text}")

        print(Fore.CYAN + "\n=============================================================================================\n")

    continue_or_not = input("Would you like to continue (Y or N): ")

    if continue_or_not.lower() == "y":
        system('clear')

    elif continue_or_not.lower() == "n":
        sys.exit()

    else:

        print("Invalid Input")


