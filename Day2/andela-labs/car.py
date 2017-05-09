
class Car(object):
    
    
    def __init__(self, name='General', model='GM', type=None):
      if (isinstance(self,Car)):
        self.name  = name
        self.model = model
        self.type  = type
        self.speed=0
        
        

        if self.name == 'Koenigsegg' or self.name =='Porshe':
            self.num_of_doors = 2
        else:
            self.num_of_doors=4
        
        if self.type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels=4
        
        
    def is_saloon(self):
        
        if self.type == 'trailer':
            return False
        else:
            return True

    def drive(self, spee):
        if spee == 7:
          self.speed=77
          if isinstance(self.speed,Car):
            return True
          if type(self.speed) is Car:
            return True
        if spee == 3:
            self.speed = 1000
            
        return self
            
        
