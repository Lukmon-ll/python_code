#
x = "Lukmon"
y = input("Enter the lucky word and win great prizes ")
y = y.title()
if(x == y):
    print("You have won for yourself a gold chain")
else:
    print("Try again next time")

# Lotto code
a = [42, 80, 4]
b = input("Enter first number ")
c = input("Enter 2nd number diff from first ")
d = input("Enter 3rd number diff from first and 2nd ")
        
# if got 2 numbers out of 3, you win some prizes - multiply the drop money by 20
# if you got the 3 numbers correctly, you win the greatest prize - multiply the drop money by 100

b = int(b)
c = int(c)
d = int(d)

if(b in a and c in a and d in a):
    print("You have won the greatest prize")
elif(b in a and c in a):
    print("You have won some prizes")
elif(b in a and d in a):
    print("You have won some prizes")
elif(c in a and d in a):
    print("You have won some prizes")
else:
    print("Try again next time")