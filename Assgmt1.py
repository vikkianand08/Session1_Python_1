# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 08:22:12 2019

@author: Nutan Anand
"""

print("Asgmt1: Numbers are divisible by 7 but are not a multiple of 5, between 2000 and 3200")
list1=[];
for i in range(200,3201):
	if (i %7 == 0) and (i%5 !=0) :
            list1.append(i)
print(list1)


print("Asgmt1: accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.")
str1=input("Enter 1st Name: %s")
str2=input("Enter 2nd Name: %s") 
str3=str1+' '+str2
print("FirstName and LastName: %s" %(str3))
strb1=str3.split(" ")[0]
strb2=str3.split(" ")[-1]
strb=strb2+' '+strb1
print("LastName and FirstName: %s" %(strb))
str4=strb[::-1]
print("Reverse_LstName and reverse_FirstName: %s" %(str4))


print("volume of a sphere with diameter 12 cm:")
d=24
r=float(d/2)
vol=float((4/3)*(22/7)*(r**3))
print("vol: %s" %vol)