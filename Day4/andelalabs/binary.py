class BinarySearch(list):
  '''a=length of list to create
     b=step or the difference btw consequtive numers'''
  def __init__(self,a,b):
    self.length=a
    
    for i in range(b,(self.length*b)+1,b):
      self.append(i)
      
    
    
    for index, i in enumerate(self):
      if index < self.length - 1:
         self[index+1]-self[index]
         
         
  def search(self,target):
    count=0
    lower = 0
    upper = len(self)-1
    while lower < upper:   
        count+=1
        x = (upper + lower) // 2
        val = self[x]
        if target == val:
            return {'count':count,'index':x}
        elif target > val:
            lower=x+1
            
        elif target < val:
            upper = x-1

a=BinarySearch(100,10)
print a.search(990)
print a


