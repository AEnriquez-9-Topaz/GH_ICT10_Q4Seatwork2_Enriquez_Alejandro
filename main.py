#SW 2 Creation of a Classmate in a Class
from pyscript import document, display

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name #Attribute
        self.section = section #Attribute
        self.favorite_subject = favorite_subject #Attribute

    def introduce(self):
        return f'Hi, my name is {self.name}! I am in the section {self.section} and my favorite subject is {self.favorite_subject}.'

#Initial Objects
Classmate1 = Classmate('Ryker', 'Topaz', 'Math')
Classmate2 = Classmate('Xiangling', 'Ruby', 'Science')
Classmate3 = Classmate('Surose', 'Emerald', 'Art')
Classmate4 = Classmate('Xingqiu', 'Sapphire', 'PE')
Classmate5 = Classmate('Kaeya', 'Sapphire', 'TLE')

classmates = [Classmate1, Classmate2, Classmate3, Classmate4, Classmate5]

def Show(e):
    document.getElementById('output2').innerHTML = ''

    for i, classmate in enumerate(classmates): 
        display(classmate.introduce(), target=f'output2')

def New_Classmate(e):  #Allow user to add new classmates

    name = document.getElementById('input1').value
    section = document.getElementById('input2').value
    favorite_subject = document.getElementById('input3').value

    Classmate6 = Classmate(name, section, favorite_subject)
   
    classmates.append(Classmate6) #Append global list
    display(f'New Classmate has been added', target='output') #Show that a new classmate has been added

    
