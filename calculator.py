
print('hi i am a calculator i can do addition,subtraction, multiplication, Floor division, modulus, exponent and division')
for i in range(0, 10):
    if(i==0): 
        number1 = input("enter your first number:")
        operation= input("enter your operation:")
        number2 = input("enter your second number:")
       
        
    else :
        number1 = number3;
        operation= input("enter your operation:")
        number2= input("enter your second number:")
        
    
    if(operation=="+"):
        number3 = int(number1) + int(number2)
    elif(operation=="*"):
        number3 = int(number1) * int(number2)
    elif(operation=="/"):
        number3 = int(number1) / int(number2)
    elif(operation=="-"):
        number3 = int(number1) - int(number2)
    elif(operation =="**"):
        number3 = int(number1) ** int(number2)
    elif(operation == "//"):
        number3 = int(number1) // int(number2)
    elif(operation == "%"):
        number3 = int(number1) % int(number2)
    if int(number1) > 100000000:
        break
    if int(number2)> 100000000:
        break

    print(number3)
   
    gundu=input('do you want to turn off calculator')

    if gundu == "yes" :
        break

    
























