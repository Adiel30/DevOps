# list ייצור טבלה מסוג
myDiet = ['bread', 'chicken', 'fish']
# יתפיס את כל הטבלה
print(myDiet)
# יתפיס את הערך הראשון
print(myDiet[0])
# ישנה את הערך השני בטבלה
myDiet[1] = 'steak'
print(myDiet)

# שימוש ב טבלה בלולאה
for x in myDiet:
    print(x)

# חיפוש
if 'fish' in myDiet:
    print('fish is in your diet')

# מס' ההאיברים בטבלה
print(len(myDiet))
# הוספת איבר לטבלה
myDiet.append('watermalon')
print(myDiet)
print(len(myDiet))
# הוספה של איבר לטבלה במקום ספציפי
myDiet.insert(2, 'milk')
print(myDiet)
print(len(myDiet))
# הסרה של איבר ספציפי
myDiet.remove('milk')
print(myDiet)
print(len(myDiet))

#הסרה של איבר ספציפי או של האיבר האחרון
myDiet.pop()
print(myDiet)
print(len(myDiet))

# מס' ההאיברים בטבלה
print(len(myDiet))
# הוספת איבר לטבלה
myDiet.append('watermalon')
print(myDiet)
print(len(myDiet))
#  מחיקה של אינדקס ספציפי או את כל הטבלה יכול להתבצע גם עם clear
del myDiet[2]
print(myDiet)
# העתקה של הטבלה 2 דרכים
newDiet = myDiet.copy()
print(newDiet)
newDiet = list(myDiet)
print(newDiet)

# הכנה של טבלה חדשה בעזרת LIST
newDiet = list(('pancake', 'fish', 'vegtables'))
print(newDiet)




