import random
import string

def password_generator(cantidad=0):
    
    str1 = string.ascii_uppercase
    str2 = string.ascii_lowercase
    str3 = string.digits
    str4 = string.punctuation
    
    s =[]
    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))
    
    random.shuffle(s)
    
    password = ("".join(s[0:cantidad]))
    return password    

cantidad = int(input("Ingrese la cantidad de letras del Password:"))
print(password_generator(cantidad))