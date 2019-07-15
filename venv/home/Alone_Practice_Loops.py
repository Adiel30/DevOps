# שבירת הלולאה בעזרת break
num = 3
while num < 30:
    print(num)
    if num == 10:
        break
    num += 1

# שימוש בcontinue מאפשר להמשיך למרות שתנאי מתקיים
num2 = 12
while num2 < 50:
    num2 += 1
    if num2 == 20:
        continue
    elif num2 < 30:
        num2 += 3
    print(num2)

myWorkout = {'back': 'sunday',
             'chest': 'monday',
             'legs': 'wednesday'}

# שימוש ב-break לעצור לולאת for
for workout in myWorkout:
    print(workout)
    if workout == 'chest':
        break
    print(workout)

# שימוש ב RANGE
for num in range(100):
    print(num)
# לקבוע מאיזה מספר יתחיל
for num in range(50, 100):
    print(num)
# לקבוע מקדם לקפיצה
for num in  range(30, 100, 5):
    print(num)

myDiet = ['bread', 'chicken', 'fish']
myHours = [6, 13, 16]
for d in  myDiet:
    for h in myHours:
        print(d,h)
