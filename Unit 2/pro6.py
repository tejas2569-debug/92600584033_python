# . Write a program to iterate over lists strings and dictionaries using loops.
num =[10,20,30,40,50]
print(num)
for i in num:
    print(i)

name ="Tejas"
print(name)
for ch in name:
    print(ch)
    
student = {
    "name":"vasu",
    "age":21,
    "Course":"Python"
    
}
for key,value in student.items():
    print(key,":",value)
    
'''output :
    [10, 20, 30, 40, 50]
10
20
30
40
50
Tejas
T
e
j
a
s
name : tejas
age : 21
Course : Python'''
