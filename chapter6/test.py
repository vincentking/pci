import re

# print dict([('a',1),('a',1),('a',2),('a',1),('b',1),('b',1),('b',10),(1,1),(1,1)])
# print [('a',1),('a',1),('a',2),('a',1),('b',1),('b',1),('b',10),(1,1),(1,1)]

# print
cc = {"a" : 1, "b" : 2, "g" : 3, "o" : 4}
print cc.keys()
print cc.values()
print sum(cc.values())
# dict["w"] = "watermelon"
# del(dict["a"])
# dict["g"] = "grapefruit"
# print dict.pop("b")
# dict[1] = 1
# dict['1'] = 1
# print dict
# dict.clear()
# print dict

# dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
# for k in dict:
#     print "dict[%s] = " % k,dict[k]


def getwords(doc):
  splitter=re.compile('\\W*')
  print doc
  words=[s.lower() for s in splitter.split(doc) 
          if len(s)>2 and len(s)<20]
  return dict([(w,1) for w in words])

features = getwords('the quick a  rabbit jumps fences')    
for k in features:
  print 'key is %s and value is %s' %  (k , features[k])
