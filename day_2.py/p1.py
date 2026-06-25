print("hello world")
#hello world



x= 1
x="Python"
print(x)
#Python

l= [1,2,3,4,5]
print(type(l))
print(l)
l.append(6)
print(l)
l.insert(1,0)
print(l)
#<class 'list'>
#[1, 2, 3, 4, 5]
#[1, 2, 3, 4, 5, 6]
#[1, 0, 2, 3, 4, 5, 6]

marks=[30,40,50,45,41,37]
marks[2:4]=[44 , 25]
print(marks)
print(marks[2:4])
#[30, 40, 44, 25, 41, 37]
#[44, 25]