TODO: Reflect on what you learned this week and what is still unclear.

while: a loop that will stop until condition is false 
    e.g. while (x>y) --> this will keep happening until the condition is false
if: a statement that checks true or false for only once 
    e.g. if (x>y) --> this will only happen once

print(): print a text
    e.g. print("hello world!")
input(): print a text and allows the user to input something 
    e.g. age = int(input('how old are you:'))

append: add something to the end of an existing list 
    e.g. string_list = [‘Medium’,’Python’,’Machine Learning’,’Data Science’]
         string_list.append(1)
         --> [‘Medium’,’Python’,’Machine Learning’,’Data Science’, '1']

range: creates a list with specific start, end and step
    e.g. range(1, 10, 2) --> [1, 3, 5, 7, 9]

try: tests a block of code for errors
except: handles the error
finally: execute code, regardless of the result of the try- and except blocks
    e.g. try:
             do_a_dumb()
         except Exception as e:
             print("you did a dumb", e)
         finally:
             print("we still love you")