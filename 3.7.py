#!/usr/bin/env python
# coding: utf-8

# In[1]:


code = {' ': '_',"'": '.----.','(': '-.--.-',')': '-.--.-',',': '--..--','-': '-....-','.': '.-.-.-','/': '-..-.','a':'.-'  ,'b':'-...','c':'-.-.','d':'-..'  ,'e':'.'   ,
         'f':'..-.','g':'--.' ,'h':'....','i':'..'  ,'j':'.---',
         'k':'-.-' ,'l':'.-..','m':'--'  ,'n':'-.'  ,'o':'---' ,
         'p':'.--.','q':'--.-','r':'.-.' ,'s':'...' ,'t':'-'   ,
         'u':'..-' ,'v':'...-','w':'.--' ,'x':'-..-','y':'-.--','z':'--..',
         'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','0':'-----' ,'1':'.----' ,'2':'..---' ,'3': '...--','4': '....-' ,
         '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.' }

def to_morse_code(sentence):
    morse_code = ""
    for letters in sentence:
        morse_code += code [letters] +""
    return morse_code
   
        
    return morse_code
    
text = input('Enter text:')
print(to_morse_code(text))


# In[2]:


# Python exercise-1 (3.7)


# In[3]:


# Python exercise-6 (3.7)


# In[1]:


from datetime import datetime
import time

def date_passed(td, sd):
    td_new= td.replace("rd","").replace("th","").replace("st","")
    sd_new= sd.replace("rd","").replace("th","").replace("st","")

    if datetime.strptime(td_new, '%d %B') < datetime.strptime(sd_new, '%d %B'):
        return False
    else:
        return True

d1 = '21st February'
d2 = '3rd March'

date_passed(d1,d2)


# In[2]:


from datetime import datetime
import time

def date_passed(td, sd):
    td_new= td.replace("rd","").replace("th","").replace("st","")
    sd_new= sd.replace("rd","").replace("th","").replace("st","")

    if datetime.strptime(td_new, '%d %B') < datetime.strptime(sd_new, '%d %B'):
        return False
    else:
        return True

d1 = '4th April'
d2 = '3rd March'

date_passed(d1,d2)


# In[ ]:




