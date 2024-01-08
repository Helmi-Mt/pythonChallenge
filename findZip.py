# this challenge is about finding the zip , zip file ? or zip what ? let's see
from zipfile import ZipFile
import urllib.request, urllib.error, urllib.parse
import re



file_name = 'channel.zip'
all_files = [] 
with ZipFile(file_name,'r') as zip:
    # this line prints all the content of the zip file file_name / in this case 'channel.zip'
    zip.printdir()
    # let's get the list of the files inside the zip file
    list_zip_files = zip.namelist()
    # another code for the list of files inside the zip file
    extra_list = zip.infolist()
    # print ('extra list = ', extra_list)
    status = True
    x = '90052'
    names_list = ['90052.txt']
    while status == True:
        opened_file = zip.read(x+'.txt')
        new_result = opened_file.decode('utf-8')  # this will return str result instead of byte type
        try:
            x = re.findall('\d+',new_result)[0]
            print ('new x = ',x,end='')
            names_list.append(x+'.txt')
            x = int (x)
            x  = str(x)
            continue
        except :
            print ('there is exception')
            print ('last result = ', new_result)
            status = False
            # the result show : 'collect the comments'
            # meaning : we should retreive the comments related to the files inside the zip file (using zipfile module)
    list_comment = []
    for fl in extra_list:
        # print ('this is fl = ', fl)
        if fl.filename in names_list:
            
            # print ('decoding the fl time = ', fl)
            # print ('extracting the file name = ',fl.filename, 'file name type = ',type(fl.filename) ) 
            print ('comment on this file = ', fl.comment.decode())
            if fl.comment.decode() != ' ' and fl.comment.decode() != '*':
                
                list_comment.append(fl.comment.decode()) 
            


print ('name list length = ',len(names_list))
print ('extra list length =', len(extra_list))
print ('comment list = ', list_comment)


# the result is: oxygen (i didn't find it)