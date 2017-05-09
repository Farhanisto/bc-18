
def find_max_min(li):
  if isinstance(li,list):
    
    if(min(li)==max(li)):
      return [len(li)]
    
    return [min(li),max(li)]
