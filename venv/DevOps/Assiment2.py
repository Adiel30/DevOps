#y = 67
#x = 30

#if x >= y:
#    print ('Bigger')
#elif x <= y:
#    print ('Smaller')


#for x in range(5):
#    print (x)

#Season = 2

#if Season == 1:
#    print ('`now is Summer')
#elif Season == 2:
#    print ('The Winter is coming')
#elif Season == 3:
#    print ('Now is Fallen')
#elif Season == 4:
#    print ('Winds of spring')

#MyAge = 230
#Surname = 'L'
#Currency = 3.58
#ApartmentNumber = 29

#print (MyAge)
#print (Surname)
#print (Currency)
#print (ApartmentNumber)
#print (Currency+MyAge)

#My_Phone_Number = input('My_Number_Is ')
#print ('Adiel_Number: ', My_Phone_Number)

#def printhello():
#    print ('Hello')
#def calculate():
#    print (3.52+5)
#if __name__ == '__main__':
#    print (printhello())
#    print (calculate())

#def My_Name (Name):
#    print (Name)
#if __name__ == '__main__':
#    print (My_Name(Name='Adiel'))
#
#def Divide(num):
#    print (num/2)

#if __name__ == '__main__':
#    print (Divide(num=6))

#def Sum(x,a):
#    return x+a
#if __name__ == '__main__':
#    print (Sum(4,8))

#def String(X,Y):
#    return X + " " + Y

#if __name__ == '__main__':
#    print (String(X='Real_Madrid',Y='Champion'))

#import array as arr
#if __name__ == '__main__':
# Table = arr.array("i",[33,44,55])
# for number in Table:
#     print (number)


# Pyramde
for i in range(0, 5):
    for j in range(0, i + 1):
        print("#", end=' ')

    print("\r")

#Reverse Pyramde
for x in range(0 , 5):
    for y in range(0, 5-x):
        print ("* ", end=' ')

    print ("\r")


# Paint X
B = 0
D = 6
for r in range(7):
    for c in range (7):
        if r==B and c==D:
            print ('#' , end='')
            B = B+1
            D = D-1
        elif r==c:
            print ('#' , end='')
        else:
            print (end=' ')
    print ()

def Enter_Number():
    Num = input('Please Enter Number')
    return (Num)


def Sum_Number():
    Num2= int(Enter_Number())
    sum=0
    while Num2/10>0:
        sum += Num2%10
        Num2 = int(Num2/10)
    return int(sum)

if __name__ == '__main__':
    print (Sum_Number())





#if __name__ == '__main__':
#    print (Enter_Number())
#    print Sum_Number()




