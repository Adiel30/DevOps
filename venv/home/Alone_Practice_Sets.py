# יצירת טבלה מסוג SET הטבלה היא לא לפי סדר ולא לפי אינדקס.
myGym = {'chest', 'back', 'legs'}
print(myGym)

# לא ניתן להגיע לערך ספציפי בטבלה מסוג set משום שהיא לא יוצרת סדר או אינדקס

# ניתן ליצור לולאת for
for x in myGym:
    print(x)

# ניתן לבדוק האם ערך ספציפי קיים בset
print('chest' in myGym)

# לא ניתן לערוך ערך אבל ניתן להוסיף
# להוסיף בעזרת ADD יכול להוסיף רק ערך אחד למס' ערכים משתמשים ב-update
myGym.add('shoulders')
print(myGym)
myGym.update(['bicep', 'forhand', 'abs'])
print(myGym)

# ניתן למחוק ערכים עם הפקודות remove or discard והערך המדויק
# מחיקה בעזרת POP אתה לא תדע איזה ערך נמחק
# ניתן למחוק את הכל בעזרת clean or del
