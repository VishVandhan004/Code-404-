# String Slicing, Indexing and Methods
ch = "ENGINEERING" 
a = 'hello world'
print(ch[0])
print(ch[-1])
print(ch[4])
print(ch[1:12:2])
print(ch[2:])
print(ch[:3])
print(ch[3:6])
print(ch.lower())
print(a.split())
print(a.split('o'))

#String Concatenation
name = 'sam'
ll = name[1:]
print('p' + ll)
print(name + '5')

# Dictionaries
my_dict = {'key1':'value1','key2':'values2'}
print(my_dict['key1'])
d = {'k1':123,'k2':[0,1,2],'k3':{'inside':100}}
print(d['k2'])
print(d['k2'][2])
print(d['k3'])
print(d['k3']['inside'])
d['k4'] = 400 # adding a new element to the dictionary
print(d)
d1 = {'k1':['a','b','c']}
print(d1['k1'])
print(d1['k1'][2])






