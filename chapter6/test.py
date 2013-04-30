import re

print dict([('a',1),('a',1),('a',2),('a',1),('b',1),('b',1),('b',10),(1,1),(1,1)])
print [('a',1),('a',1),('a',2),('a',1),('b',1),('b',1),('b',10),(1,1),(1,1)]

print
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
dict["w"] = "watermelon"
del(dict["a"])
dict["g"] = "grapefruit"
print dict.pop("b")
dict[1] = 1
dict['1'] = 1
print dict
dict.clear()
print dict

dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
for k in dict:
    print "dict[%s] = " % k,dict[k]


def getwords(doc):
  splitter=re.compile('\\W*')
  print doc
  # Split the words by non-alpha characters
  words=[s.lower() for s in splitter.split(doc) 
          if len(s)>2 and len(s)<20]
  print dict([(w,1) for w in words])
  # Return the unique set of words only
  return dict([(w,1) for w in words])

features = getwords('the quick rabbit jumps fences')    
for k in f:
	print f[k]
