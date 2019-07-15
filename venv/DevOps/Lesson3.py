my_file = open('/Users/adiellevy/Documents/1.rtf','a')
my_file.write('AAA')

my_file = open('/Users/adiellevy/Documents/1.rtf','r')
content = my_file.read()
print(content)
my_file.close()

try:
    f = open('/Users/adiellevy/Documents/1.rtf','r')
    f.write('123')
except IOError as e:
    print('Failed')
    print(e)


try:
    f = open('/Users/adiellevy/Documents/1.rtf','r')
    f.write('123')
except:
    print('Failed all')

#soft Error
try:
    t = open('/Users/adiellevy/Documents/Adiel2.rtf','r')
    t.read()
except IOError as e:
    print('Files Doesnt exist')
    print(e)
finally:
    print('Go!!!')

#hard Error

    try:
        f = open('/Users/adiellevy/Documents/1.rtf', 'r')
        f.write('123')
    finally:
        print('Failed all')


