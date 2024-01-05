# this challenge is the number 5 on the http://www.pythonchallenge.com
# i took a hint and it's about some href inside the webpage / let's discover !?
#  on the first page html , "peack hell, sounds familiar ?" WTF ?
# it turns out they mean the - pickle module in python for serialisation and deserialisation of data
import urllib.request
import re
import pickle

page = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/peak.html")
print ('this the retreived url =',page)
# print ((page.read().decode()))
# print (type(page.read().decode())) # as you can see, this is an str value, we easily extract src values from it
strHtml = page.read().decode()
print ('strHtml = ', strHtml) # page.read().decode() should be put in a variable the first time it's executed or else it will not give a the result !!!
result = re.findall('src="(\S+)"',strHtml) # the ( ) delimits the extraction edges
print ('resuslt = ', result)
for r in result :
    if (r[-3:] != 'p'):
        result.remove(r) # removing the src for image and keep the other one / banner.p
# print ('result update = ', result)
        
nexpage = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/"+result[-1])
# strH = nexpage.read() #  this gives a byte type  of data
# strHtml2 = nexpage.read().decode()
strHtml2 = nexpage.read()

print ('next page strHtml2 = ', strHtml2)
print (type(strHtml2))
# i search the meaning of this pattern using chat gbt
deserialised_data = pickle.loads(strHtml2)
# print (deserialised_data) # it is all # & spaces and i thinck we should draw this list to the result
for i in deserialised_data:
    # print ('**'+i[0][0]+'**',end='')
    # print (i[0][1])
    # print (i)
    for tup in i:
        print (tup[0]*tup[1],end='') # this will print without adding newline break
    print ('-')
print ('the result = channel')
    
# the result after drawing this pattern is : Channel 
    