
def find_missing(a,b):
  if (isinstance(a,list))and (isinstance(b,list)):
    c=sorted(a)
    d=sorted(b)
    
    if len(a)>len(b):
      e=set(a)-set(b)
      return list(e)[0]
      
    elif len(b)>len(a):
      e=set(b)-set(a)
      return list(e)[0]
    elif len(b)==len(a):
       return 0
      
  

