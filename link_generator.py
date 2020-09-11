import requests, bs4, webbrowser, re, string, random, urllib.request, validators, repeat, ptimer
from selenium import webdriver

# Variables
letters = string.ascii_lowercase
digits = string.digits

for i in range(500):
    while True:
        try:
            # Generate URL
            random_code = ( ''.join(random.choice(letters + digits) for i in range(16)) )
            url = ('https://wi.to/' + random_code)
        
            # Print URL and validate it
            print(url)
            print (validators.url(url))
            print(urllib.request.urlopen('https://google.com').getcode())
            
        except Exception: # Replace Exception with something more specific.
            continue
        else:
            break
