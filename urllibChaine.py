# this is the 4th challenge in pythonchallenges
# urllib may help you (this was written on the source code of the html of this challenge)

# urllib : Urllib is a Python module that provides a simple interface for making HTTP requests to
# web pages and retrieving data from them. It is used to open URLs and read their contents.
# It can be used to send GET and POST requests, among others.

# urllib.request  is a Python module that provides functions and classes to 
# help in opening URLs (mostly HTTP) in a complex world, with basic and digest authentication, redirections, cookies and more.
# It also provides an OpenerDirector class to 
# install and manage different handlers for different protocols and scenarios1.
import urllib.request, urllib.parse, urllib.error
import re


# # below do : open the url 
# requested_url = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+'2')
# try to extract the result number using regex
# requested_to_str = requested_url.read().decode() # this will transform the resul in str by decode()
# print ('req.read.decode variable = ',requested_to_str)
# number = re.findall("\d+",requested_to_str)
# 
number = 63579
while type(number is int):
    req_url = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(number))
    req_to_str = req_url.read().decode()  
    number_list = re.findall("\d+",req_to_str)  # check for number in the the opened html file
    if (len(number_list) == 0):
        break # break when there is a html page with no numbers
    number = number_list[0]
    print (req_to_str)
    print (number)
print('las req_to_str = ', req_to_str)
# result = peak.html

