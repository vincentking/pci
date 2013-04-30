def getAll():
    a = []
    a.append('11')
    a.append('111')
    return a

a = []
a.append('1')
a.append('2')
for item in getAll():
    a.append(item)
a.append('3')

a += getAll()
print a
print list(set(a))

a.append(getAll())
print a

s = 'a|b|||          |||||||c '
ss = s.split('|')
print ss
for item in ss:
    if item.strip()!='':
        a.append(item.strip())
a.append('4')            
print a

def gen():
    print 'enter'
    yield 1
    print 'next'
    # return
    print 'next 2'
    yield 2
    print 'next 3'
for i in gen():
	print i
g = gen()
print g
print g.next()

print '---------------------------'
for i in range(1,3):
    print i