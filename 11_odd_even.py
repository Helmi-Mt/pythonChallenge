# 11 th challenge, and as usual , i have no clue what is about
import urllib.request, urllib.error, urllib.parse

# webpage = urllib.request.urlopen("http://www.pythonchallenge.com/pc/return/5808.html")
# print ('the page requested is open :\n ',webpage.read())
try: 
    webpage = urllib.request.urlopen("http://www.pythonchallenge.com/pc/return/5808.html") 
    print(webpage.read()) 
  
# Catching the exception generated      
except Exception as e : 
    print(str(e)) 
    
import requests
from requests.auth import HTTPBasicAuth

response = requests.get('http://www.pythonchallenge.com/pc/return/5808.html')

if response.status_code == 401:    
    response = requests.get('http://www.pythonchallenge.com/pc/return/5808.html', auth=HTTPBasicAuth('huge', 'file'))
    print ('this is respoonse = ', response.text) # this is how you read the get response

if response.status_code != 200:
    # Definitely something's wrong
    print ('there is something wrong !!')

# not a clue what thre result is