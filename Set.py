
'''A set in Python is an unordered collection of unique items. It is a data type that acts like a mathematical set.
It is defined by enclosing the items within curly braces {} and each item seperated by (,).'''


mycolors = {'sky','pink','yellow','green'}
print(mycolors)


mycolor = {'orange','sky','pink','sky','green','sky','sky'}
print(mycolor)



mycolors = {'orange','sky','pink','sky','green'}
print("Before adding Value : ",mycolors)
mycolors.add('white')
print("After adding Value : ",mycolors)