
#accountnum = 79927398713
user_account = int(input("Enter a number: "))
running_total = 0
counter = 0    
odd = 0
even = 0
while user_account > 0:
    digit = user_account %10 #Gives the remainder of the number which is the very last number
    user_account = user_account // 10 #Double divides the number by 10 taking away the last number, and repeating it with every number after. 
    counter = counter + 1 #Counts all the numbers starting from the first one
    if counter % 2 == 0: #Finds the even number
        digit2=digit*2 #Multiples by 2 all even digits
        print (digit2) #Prints the result of the even numbers multiplied by 2
        print () #Gives a blank space
        if digit2>9: #Checks if the even numbers multiplied by 2 are bigger than 9
            while digit2>1: #Starts a loop if the multiplied numbers are bigger than 9
                print('digit2 is: ', digit2)
                tmp = digit2 % 10 #Finds the remainder of the multiplied number
                print ('first digit from double digit number: ',tmp) #Prints the remainder
                even = even + tmp
                digit2=digit2 // 10 #Changes the value of digit2 by double dividing it by 10
                even = even + digit2 #Changes the value of even by adding it with tmp (the value of the remainder of the multiplied number)
                print('last digiti from double digit number: ', digit2)
                print('Even is: ',even)
        else:
            even = even + digit2
            print('Even is: ', even)
    else:
        odd = odd + digit

print(odd + even)















