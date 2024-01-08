# 7th challenge / i have no idea what is about
import urllib.request, urllib.parse, urllib.error
# import requests


webpage = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')
print (webpage)
# data = requests.get(url).content 

# after looking for a hint on the internet, i found the library Pillow (pil)
# to install the library : pip3 install pil



url = "http://www.pythonchallenge.com/pc/def/oxygen.png" # the URL of the image
filename = "oxygen.png" # the name of the file to save the image

urllib.request.urlretrieve(url, "oxygen.png") # download the image and save it as filename
 
#  no solution found !!