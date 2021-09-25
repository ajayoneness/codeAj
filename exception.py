a=2
b=0

try:
    print("open resource ")
    print(2/0)
    k= int(input("enter a value : "))
    print (k)

except ZeroDivisionError as e:
    print("you cannt divide by zero : ")
except Exception as e:
    print(e)
except ValueError as e:
    print("hi",e)
finally:
    print("close resource")