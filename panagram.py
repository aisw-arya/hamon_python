def panagram(s):
    st = s.lower()  
    for i in range(97,123):
        if chr(i) in st:
            pass
        else:
            print(s," not a panagram")
            break;
    else:
        print(s," is panagram")

if __name__ == '__main__':
    s=input("enter the string:")
    panagram(s)