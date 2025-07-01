
# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("An exception occurred")
    
try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("All is gone wrong")
    
x = -1

if x < 0:
    raise Exception("no numbers below zero")
