#ans1
a=int(input('Number 1:'))
b=int(input('Number 2:'))
c=int(input('Number 3:'))
x=a+b+c/3
print(x)

#ans2
a=int(input('Please enter your Gross Income:-'))
print(a)
b=int(input('No. of dependents:-'))
print(b)
S=10000
D=3000
x=D*b
c=S+x
T=a-c
t=T*0.2
print(t)

#ans3
a=int(input("Number of Seconds:-"))
print("The time in minutes and seconds is: ",(a//60),"Minutes and",(a%60),"Seconds")

#ans4
x = int('25')
result = 25 + x + 25.0
result_str = str(result)
print(result_str)
result = round(25 + x + 25.0)
result_str = str(result)
print(result_str)