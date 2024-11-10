#------Diccionarios------
persona = ['Grover', 40, 1.72, 'Masculino', True]

person = {
    'id': 123,
    'nombre':'Grover',
    'edad': 40,
    'estatura': 1.72, 
    'género': 'Masculino',
    'estado': True,
    'gadgets': ['iPhone', 'PS4', 'Audífonos']
}
lista = person['gadgets']
#print(person.get('direccion', 'Lima'))
#print(person.keys())
#print(person.values())
#for k,v in person.items():
#    print(k,":",v)
#person.clear()
#person.pop("estado")
#person.update({'direccion':'Lima'})
#print(person)

#------Conjuntos (Set)---
frutas = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
#print(frutas)

letras = {'a', 'b', 'c'}
#print(letras)

conja = set('abracadabra')
conjb = set('alacazam')
print(conja)
print(conjb)
print(conja - conjb)
print(conja | conjb)
print(conja & conjb)
print(conja ^ conjb)

