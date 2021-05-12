name1="adi"
name2="chinna"
name3="web developer"

print(id(name1))
print(id(name2))

print(id(name3))

print(name1 is name2)
print(name2 is name1)
print((name1 is name1))

print("a" in name1)
print("a" not in name1)

# %d %s  %f,%g

eid,ename,esal =1111,"chinna",420.00
print(eid)

print("emp id=eid,emp ename=ename,emp esal=esal")
print("emp id=%d,emp ename=%s,emp esal=%f"%(eid,ename,esal))


print("emp id=%d, emp ename=%s, emp esal=%f"%(eid,ename,esal))

print("emp id=%d, emp ename=%s, emp esal=%f"%(eid,ename,esal))

print("emp id={0}, emp emp={1}, emp sal={2}".format(eid,ename,esal))



# concatination

s1="adi"
s2="chinna"
s3="web developer"
s4 = s1+s2+s3 
print(s4)



# mulitiplication

a1= "chinna"
a2="web developer"

a3 = a1*100 
print(a3)

a5=a2*30

print(a5)


# relational data


print("adi">"chinna")

print("chinna">"chinna")
print("chinna"=="chinna")

print("chinna"!="adi")

### founctions

# capitalise
a="chinna"
a.capitalize()
print(a)


# assignment

# interviw question

a = "web developer"
print(a.count('w'))


count=0
for x in a:
    if x=='e':
        count=count+1
print(count)



# assignment 2

s = "ratan rantan ratna "
print(s)

words = s.split()
for z in words:
    if z==words:
        
        count=count+1
print(count)



##

my = "developer jobs"

ss = my.split()

ss.sort()
for sss in ss:
    
    print(sss)

word="adi"
words.sort(reverse=True)
for word in words:
    print(word)
