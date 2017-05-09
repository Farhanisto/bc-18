
'''a real world application showing the sale of vehicles'''
class Vehicle(object): 
    '''take a vehicle object and return the price of the vehicle based on the name

    '''
    def __init__(self,name):
        self.name=name

    # method to check the name of the car and return the price

    def sale(self):
        if self.name=='lambo':
            return 500000
        elif self.name=='nissan':
            return 300000
        else:
            return 'out of stock'


# inheritance - This is where a class i.e a child class inherites the methods and atributes of a parent class

class lambo(Vehicle):
    wheels=4 #Encampsulation is data hidding to a given method or a class this data is private to that class. now this data,wheels is private to this class
    def __init__(self,name):
        self.name=name

class nissan(Vehicle):
    wheels=3
    def __init__(self,name):
        self.name=name

lm=lambo('lambo')
print lm.sale()  # this shows inheritance---

ns=nissan('nissan')
print ns.sale()      # this similarly shows inheritance and as well POLYMORPHISM in that we use the same function to get differnt price of carss

 





