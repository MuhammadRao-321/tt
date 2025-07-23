#function 1
def fun1(n):
 return n*(n+1)/2
print(fun1(4))
#time complexity = 1
#more effecient

def fun2(n):
 sum = 0
 for i in range(1, n+1):
  sum += i
 return sum
print(fun2(4))
 #time complexity = n
 #average effecient

def fun3(n):
  sum = 0
  for i in range(1, n+1):
   for i in range(1, i+1):
    sum += 1
  return sum
print(fun3(4))
   #time complexity = n^2
   #less effecient

def printnumber(n):
  iteration = 0
  print("the total number entered my user is", n)


def myfunction1(n):
 if(n>0):
  return

  print("Codingal")
  myfunction1(n/2)
  myfunction1(n/3)
#recurrence relation
#T(n)=T(n/2)+T(n/3)+0(1)
#0(lognbase2 + lognbase3)

#function1
def sum(n):
 return n*(n+1)/2
print(sum(10))
#time complexity = 0(1)
#sc = inputspace + auxiliary space
#space somplexity = 0(1)
#best case sceanrio
#more effecient

#function2
def arraysum(a):
 sum=0
 for i in a:
  sum = sum + i
  return(sum)
 
a = [12, 3, 4, 15]
print(arraysum(a))
#time complexity = 0(a)
#sc = inputspace + auxiliary space
#space complexity will increase due to array size
#space complexity = 0(n) n is the size of array
#average case sceanrio
#less effecient