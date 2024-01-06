# this challenge is about finding the zip , zip file ? or zip what ? let's see
from zipfile import ZipFile
import urllib.request, urllib.error, urllib.parse
import re
webpage = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/channel.html')
print (webpage.read().decode())

webpage2 = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')
# the webpage2 is in fact a zip file and we download it to try to open it with python
file_name = 'channel.zip'
all_files = [] 
with ZipFile(file_name,'r') as zip:
    # this line prints all the content of the zip file file_name / in this case 'channel.zip'
    zip.printdir()
    
    # below code extracts all the content of the zip file
    # all_files = zip.extractall()
    
    
    # let's get the list of the files inside the zip file
    list_zip_files = zip.namelist()
    # print ('list of files = ', list_zip_files)
    
    # let's open one by one
    status = True
    x = '90052'
    while status == True:
        
        opened_file = zip.read(x+'.txt')
        new_result = opened_file.decode('utf-8')  # this will return str result instead of byte type
        print ('new result = ',new_result)
        x = re.findall('\d+',new_result)[0]
        print ('new x = ',x)
        print ('type of x = ', type(x))
        
        try:
            x = int (x)
            x  = str(x)
            continue
        except :
            print ('there is exception')
            status = False
            # the result show : 'collect the comments'
            # meaning : we should retreive the comments related to the files inside the zip file (using zipfile module)
      


