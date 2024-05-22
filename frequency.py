def freq(string):
    dictionary = {}             #empty dictionary created
    for i in string:             #iterate througth the string
        if(i != " "):           
            if (i in dictionary.keys()):       #check whether the character already present in the dictionary          
                value = dictionary[i] + 1    #increment the value 
                dictionary[i] = value          # elements added to dictionary
            else:                           
                key = i
                dictionary[key] = 1             
                
    print(dictionary)

if __name__ == '__main__':
    string=input("enter the string:")
    freq(string)