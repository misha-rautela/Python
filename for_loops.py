for i, v in enumerate (['A','B','C']):
	print i, v
ques = ['name','age','sex']
ans = ['Misha', 21, 'F']

for i, j in zip(ques, ans):
	print 'what is your {0}? It is {1}' .format(i,j)

for i in reversed(xrange(0,100,5)):
	print i

set_ex = ['D','E','ZA','AA','AB','AE','AC']
for i in sorted(set(set_ex)):
	print i

dic_ex = {'a':'1', 'b':'2','c':3}
for i, j in dic_ex.iteritems():
	print i,j

words = ['1','22','333','4444','55555','666666','7777777']
for i in words[:]:
	if len(i)>3:
		 words.insert(0,i)
print(words)
		
