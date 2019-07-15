# טבלה מסוג Dictionary היא ללא סדר בעלת יכול עריכ =ה ובעלת אינדקס
myWorkout = {'back': 'sunday',
             'chest': 'monday',
             'legs': 'wednesday'}
print(myWorkout)

# לקרוא לערך
x = myWorkout['back']
print(x)
x = myWorkout.get('chest')
print(x)

# עדכון ערך
myWorkout['legs'] = 'friday'
print(myWorkout)
myWorkout['abs'] = 'thursday'
print(myWorkout)

# מדפיס רק את הKEY
for x in myWorkout:
    print(x)

# להדפיס רק את ה-values
for x in myWorkout:
    print(myWorkout[x])
for x in myWorkout.values():
    print(x)

# להדפיס גם וגם
for x,y in myWorkout.items():
    print(x,y)


if 'chest' in myWorkout:
    print('chest is exist')

# מחיקה של ערכים
myWorkout.pop('abs')
print(myWorkout)
myWorkout['abs'] = 'thursday'
print(myWorkout)
del myWorkout['abs']
print(myWorkout)
myWorkout['abs'] = 'thursday'
print(myWorkout)
#   ב 3.7 מוחק את הערך האחרון לפני מחק רנדומלית
myWorkout.popitem()
print(myWorkout)
myWorkout['abs'] = 'thursday'
print(myWorkout)
# מחיקה של הטבלה
# עם DEL או CLEAN ללא תוספת

