import requests, bs4, webbrowser, re, string, random
from selenium import webdriver

letters = string.ascii_lowercase
digits = string.digits
random_code = ( ''.join(random.choice(letters + digits) for i in range(16)) )
url = ('https://wi.to/' + random_code)

print(url)
