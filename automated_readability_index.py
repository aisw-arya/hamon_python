from sys import argv  #Importing argv module.
script, fileName = argv  

data = open(fileName)  #Opening the file in 'r' mode. 

word = data.read().split() #Spliting each word in the file.
word_count = len(word)  #Counting number of words.

data.seek(0)  #Changing the file pointer position. 
import re   #Importing re module.
data1 = data.read() #Reading the data
sentences = re.split(r'[.!?]',data1)# Finding all sentences.
sentence_count = len(sentences)  #Counting number of sentences.


data.seek(0)#Changing the file file pointer position
character = (data.read())
character_count = len(character)#Counting number of characters.
print('Number of words=',word_count,'\n','Number of sentences=',sentence_count,'\n','Number of characters=',character_count)

#automated readability index calculation
automated_readability_index = 4.71 * (character_count/word_count) + 0.5 * (word_count/sentence_count) - 21.43
print(automated_readability_index)
ari=int(automated_readability_index)  #converting floating point number to integer 

#creating chart of automated readability index using dictionary
chart={1:"Kindergarten",2:"First Grade",3:"Second Grade",4:"Third Grade",5:"Fourth Grade",6:"Fifth Grade",7:"Sixth Grade",8:"Seventh Grade",9:"Eighth Grade",10:"Ninth Grade",11:"Tenth Grade",12:"Eleventh Grade",13:"Twelfth Grade ",14:"College student"}


#to check and print the automated readability index and grade level
if ari in chart.keys():
    print(chart[ari])














#to print the automated readability index
# if(automated_readability_index >= 1 and automated_readability_index < 2):
#     print("Kindergarten")
# elif(automated_readability_index >= 2 and automated_readability_index < 3):
#     print("First Grade")
# elif(automated_readability_index >= 3 and automated_readability_index < 4):
#     print("Second Grade")
# elif(automated_readability_index >= 4 and automated_readability_index < 5):
#     print("Third Grade")
# elif(automated_readability_index >= 5 and automated_readability_index < 6):
#     print("Fourth Grade")
# elif(automated_readability_index >= 6 and automated_readability_index < 7):
#     print("Fifth Grade")
# elif(automated_readability_index >= 7 and automated_readability_index < 8):
#     print("Sixth Grade")
# elif(automated_readability_index >= 8 and automated_readability_index < 9):
#     print("Seventh Grade")
# elif(automated_readability_index >= 9 and automated_readability_index < 10):
#     print("Eighth Grade")
# elif(automated_readability_index >= 10 and automated_readability_index < 11):
#     print("Ninth Grade")
# elif(automated_readability_index >= 11 and automated_readability_index < 12):
#     print("Tenth Grade")
# elif(automated_readability_index >= 12 and automated_readability_index < 13):
#     print("Eleventh Grade")
# elif(automated_readability_index >= 13 and automated_readability_index < 14):
#     print("Twelfth Grade")
# elif(automated_readability_index >= 14 and automated_readability_index < 15):
#     print("College student")
# else:
#     pass