#def tri_recursion(k):
#  if(k>0):
#    result = k+tri_recursion(k-1)
#    print(result)
#  else:
#    result = 0
#  return result

#print("\n\nRecursion Example Results")
#tri_recursion(6)

#colors = ['red', 'green', 'blue', 'purple']
#for i in range (len(colors)):
#  print(colors[3])



#import os
#os.mkdir ('/Users/adiellevy/Documents/test1')
#my_file = open('/Users/adiellevy/Documents/test1/name', 'w').write('Adiel')
#my_file.close

#from docx import Document
#document = Document()
#document.save('/Users/adiellevy/Documents/Newdoc.docx')
#y_file = open('/Users/adiellevy/Documents/Newdoc.docx', 'w').write('Adiel')

def fact(n):
   if n == 1:
      return n
   else:
      return n* fact (n-1)

# accepts input from user
num = int(input("Enter a number: "))
# check whether number is positive or not

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   print("The factorial of " + str(num) +  " is " + str(fact(num)))
