# decipher the input / key : K→M , O→Q , E→G
inputText = '''g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''

# key indicates that every character is moved two character forward, so we should move two character backward
print (dir(inputText)) # dislay all the method linked to the string 
# print (inputText.index('f'))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print ('This is the alphabet = ',alphabet,' alphabet length = ',len(alphabet))
str = ''
for i in inputText:
    # print ('this is i = ', i)
    # print ('this is i index in alphabet = ', alphabet.index(i))
    try :
        indexAlphabet = alphabet.index(i)
        newI = alphabet[(indexAlphabet+2)%26]
        str += newI
        # print ('this new str = ', str)
    except :
        str += i
        # print ('there is a problem with the code')
    
print ('New line : \n', str)
inputText.maketrans()
  
