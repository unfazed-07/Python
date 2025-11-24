class Justnotcoolerror(Exception):
    pass
x=2
try:
    raise Justnotcoolerror("This is just not cool, man")
    
    raise Exception("I'm a custom excpetion")
   # print(x)
    if not type(x) is str:
        raise TypeError("")
except NameError:
    print("Name Error means something is probabily undefined")
except ZeroDivisionError:
    print("PLease donot divide by zero.")
except Exception as error:
    print(error)
else:
    print("No error!")
finally:
    print("I'm going to print with or wihtout an error")