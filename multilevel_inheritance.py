class grandpa:
    name="xyz"
    surname='Purbia'

class Papa(grandpa):
    name='pqr'                  #name is over write

class Me(Papa):
    name="Sanjana"

me=Me()
print(me.name,me.surname)