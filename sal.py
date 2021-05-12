"""
print("Hello World!")
ename="adi"
eid=25
esal=2.36

print(ename)


a,b=10,25
a,b=b,a
print(a,b)





# date types declarations whcih data is application 

a="adi narayana"
b=25
c=20.36252142124
d=True
e=1+3j


print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))



# diffret  ways to print the data

num=30+25*36    
print(num)




num1,num2,num3=25,36,2502
num1
print(num3)






a=10
print(a)
a=100
print(a)


print(id(a))





import sys
v,v21,v3='adi',25,23.6
print(sys.getsizeof(v21))






# python comments in singile line or thriple cotestion singile or thriple cottestions





eid,ename,esal=10,'rajesh',2563.25
print(eid)
print(ename)
print(esal)


print(eid,ename,esal)

print("Empleid=", eid,"Emplename=",ename,"Emplesal=",esal)

print("emplid=",ename,"emplesal=",esal,"emplid=",eid)
print("Empeid=",eid)




eid,ename,esal=10,'rajesh',2563.25

print("emp ename={0} emp ename={1} emp esal={2}".format(eid,ename,esal))

print(f"emp eid={eid} empname ename={ename} esal={esal}")








# escape sequence character.

print("hello narayana sir and ratna sir garu")
print("hello \anarayana sir and ratna sir\ garu")
print("hello \as\narayana\dd\ sir and ratna sir garu")
print("hello narayana sir and ratna sir garu")

print("hello \n\narayana sir and ratna sir \n\garu")


ename,esal,eid="adi",25.36,25
print("empid =",id)
print("empid ={0} ,\t\nempesal={1}".format(eid ,esal))



ename,esal,eid="adi",25.36,25

#print(eid="&&&")
print(ename,esal,eid,sep="**")
print(ename,esal,sep="++++")



n=input('enter a number 1:')
n2=input('enter number2:')
c=n+n2
print(c)


n=str(input('enter a number 1:'))
n2=str(input('enter number2:'))
c=n+n2
print(c)



val=253635.25
print("val=%f"%(val))





a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=int(input('enter 3rd number:'))

d=a+b+c
print("hi ratan your total marks is ",d,"and your persentage is 89.4%")


mathes=int(input('enter 1st number:'))
science=int(input('enter 2nd number:'))
social=int(input('enter 3rd number:'))

c=mathes+science+social
totalmarks=c
a=totalmarks
print("hi ratan your total marks is ",a,"and your persentage is 89.4%")



"""

import keyword
print(keyword.kwlist)

# direcory in python 
import keyword
print(dir(keyword))


import abc
print(dir(abc))
