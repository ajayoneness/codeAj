for i in range(1,16):
    
    if i%3 ==0 and i%5==0:
        print ("FizzBuzz")
        continue
    
    if i%3==0 and i%5 != 0:
        print("Fizz")
        continue
    
    elif i%5==0 and 3 != 0:
        print("Buzz")
        continue
    
    elif i%3 !=0 and i%5 != 0:
        print(i)
        continue
            
