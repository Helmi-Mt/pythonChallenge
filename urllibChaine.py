# this is the 4th challenge in pythonchallenges
# urllib may help you (this was written on the source code of the html of this challenge)
import urllib.request
import codecs

# below do : open the url 
requested_url = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=2")
print (requested_url.read())
list0 = [15,16]
list1 = []
list1.append(list0[0])
print (list1)
list1.append(list0[0])
print (list1)

# print (dir(list1))