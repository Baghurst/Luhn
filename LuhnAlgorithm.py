
#accountnum = 79927398713
user_number = (input("Enter a number: "))
running_total = 0
count = 0    
odd = 0
even = 0
while account > 0:
    digit = account %10
    account = account // 10
    counter = counter + 1
    if count % 2 == 0:
        digit2=digit*2
        print (digit2)
        print ()
        if digit2>9:
            while digit2>0:
                tmp = digit2 % 10
                print (tmp)
                digit2=digit2 // 10
                even = even + tmp


























