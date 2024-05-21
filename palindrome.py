def palindrome(s):
    st=s.lower()
    if (st == st[::-1]):                   #check if the string and reverse of the string are same 
        print(s,"is palindrome")
    else:
        print(s,"is not a palindrome")




if __name__ =='__main__':
    s=(input("enter the string:"))
    palindrome(s)