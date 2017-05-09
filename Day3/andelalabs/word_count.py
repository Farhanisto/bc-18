
def words(sentence):
 
  if isinstance(sentence,str):
    
    d=dict()
    l=['1','2','3','4','5','6','7','8','9','0']
    wordss=(' ').join(sentence.split())
    words=wordss.split(" ")
    for word in words:
      if word in l:
        word=int(word)
      value=words.count(str(word))
      d[word]=value
    return d

    
  
