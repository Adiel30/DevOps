# מכניס משתנה לתוך הפונקציה
def my_name(enterName):
    print(enterName + 'Ref')

my_name('alon')

# להכניס משתנה קבועה לתוך הפונקיצה
def my_football_team(favTeam = 'real madrid'):
    print('i love ' + favTeam)

my_football_team('city')
my_football_team('juve')
my_football_team()

def my_calc (x):
   return (x * 5 % 10)

def my_check (n):
    if (n>0):
        result = n + my_check(n - 10)
        print(result)
    else:
        result = 0
    return result
print(my_check(100))



