"""list1 = [12,-7,5,64,-14]
for i in list1:
    if i>0:
        print(i, end = "")


list2 = [12,14,-95,3]
for num in list2:
    if num>0:
        print(num, end = "")
"""


a,b = 0,1
n = int(input("Enter number where series should end: "))
while a<n:
    a,b = b,a+b
    print(a)
