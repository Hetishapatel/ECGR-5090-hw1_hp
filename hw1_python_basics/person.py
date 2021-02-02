#[C]

class person :
    def __init__(self, name, age, height):
        self.name=name
        self.age=age
        self.height=height
#[D]       
    def __repr__(self):
        return'{:} is {:} years old and is {:} cm tall'.format(self.name, self.age, self.height)
    
new_person1=person('Roger',23,175)

#[C]
print('\n\nC')
print('{:} is {:} years old'.format(new_person1.name,new_person1.age))

#[D]
print('\n\nD')
print (new_person1)
