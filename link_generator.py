import requests, bs4, webbrowser, re, string, random, urllib.request, validators, repeat, ptimer
from selenium import webdriver

for i in range(0,500):
    try:
        # Generate URL
        letters = string.ascii_lowercase
        digits = string.digits
        random_code = ( ''.join(random.choice(letters + digits) for i in range(16)) )
        url = ('https://wi.to/' + random_code)

        # Print URL and validate it
        print(url)
        print (validators.url(url))
        print(urllib.request.urlopen(url).getcode())
    except:
        # If URL is dead repeat until working URL is found
        repeat
