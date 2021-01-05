#Kenneth Otis
#Python Passowrd Generator
import random

def PasswordGenerator():
    reason=str(input("What would you like the password for? "))
    length=int(input("How long would you like your password to be? "))
    low=['a',"b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upp=['A',"B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers=[0,1,2,3,4,5,6,7,8,9,0]
    Special=["$","%","&"]
    alls=low+upp+numbers+Special
    password=random.sample(alls,length)
    print ("Your new ",reason, " password: ",*password,sep="")
PasswordGenerator()

    


