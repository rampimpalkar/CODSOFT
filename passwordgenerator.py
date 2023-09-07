import random
import string

print("Welcome to our Random Password Generator")

def main():
    length=input("Enter Your Name")
    length=int(input("Enter the length of password you want:"))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolD=string.punctuation
    combine=lowerD+upperD+digitD+symbolD
    x=random.sample(combine,length)
    Password="".join(x)
    print(Password)
    main()
main()

