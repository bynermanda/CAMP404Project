## BYAN ERMANDA - LET YOUR COMPUTER GUESS THE NUMBER 1-10 ##

low = 1
high = 10
middle = 5

def LowerThan5(): ##FUNCTION IF NUMBER LOWER THAN 5
    Q2 = input(str('Your number greater equal than 3 (number >= 3)? y/n: '))
    ## QUETION 2
    if Q2 == 'y':
        Q3_1 = input(str('Your number is even? y/n: '))
        ## QUETION 3
        if Q3_1 == 'y':
                for a in range(3,middle+1):
                    if (a%2) == 0:
                        print(a,end=" ")
        elif Q3_1 == 'n':
                Q4 = input(str('Your number is 5? y/n: '))
                ## QUETION 4
                if Q4 == 'y':
                    print('YOUR NUMBER IS 5', end =" ")
                elif Q4 == 'n':
                    ## QUETION 4 IF QUETION 4 IS 'NO'
                    print('YOUR NUMBER IS 3', end =" ")
                else:
                    print('SORRY YOUR TYPO')
        else:
                print('SORRY YOUR TYPO')
    elif Q2 == 'n':
        ## QUETION 2 IF QUETION 2 IS 'NO'
        Q3_2= input(str('Your number is even? y/n: '))
        if Q3_2 == 'y':
            ## QUETION 3 IF QUETION 3 IS 'NO'
            for x in range(low,middle-2):
                if (x%2) == 0:
                        print('YOUR NUMBER IS',x,end=" ")
        elif Q3_2 == 'n':
            for z in range(low,middle-2):
                if(z%2)!=0:
                        print('YOUR NUMBER IS', z, end=" ")
        else:
            print('SORRY YOUR TYPO')
    else:
        print('SORRY YOUR TYPO')


def GreatThan5(): ##FUNCTION IF NUMBER GREATER THAN 5
    Q2 = input(str('Your number higher equal than 8 (number >= 8)? y/n: '))
    ## QUETION 2
    if Q2 == 'y':
        Q3_1 = input(str('Your number is even? y/n: '))
        ## QUETION 3
        if Q3_1 == 'y':
                Q4 = input(str('Your number is 8? y/n: '))
                ## QUETION 4
                if Q4 == 'y':
                    print('YOUR NUMBER IS 8', end =" ")
                elif Q4 == 'n':
                    print('YOUR NUMBER IS 10', end =" ")
                else:
                    print('SORRY YOUR TYPO')
        elif Q3_1 == 'n':
            ## QUETION 3 IF QUETION 3 IS 'NO'
            for a in range(8,high+1):
                if (a%2) != 0:
                    print(a,end=" ")
        else:
                print('SORRY YOUR TYPO')
    elif Q2 == 'n':
        ## QUETION 2 IF QUETION 2 IS 'NOT'
        Q3_2= input(str('Your number is even? y/n: '))
        for a in range(middle+1,8):
             if (a%2) == 0:
                        print('YOUR NUMBER IS', a,end=" ")
        if Q3_2 == 'y':
            for x in range(middle+1,8):
                if (x%2) == 0:
                        print('YOUR NUMBER IS', x,end=" ")
        else:
            print('SORRY YOUR TYPO')
    else:
        print('SORRY YOUR TYPO')


print('chose number 1 to 10 and let the computer guess your number')
input('PRESS ENTER')
start = input(str('WHAT IS YOURN NUMBER LOWER THAN 5? y/n: '))
## QUETION 1
if start == 'y':
    LowerThan5()
elif start == 'n':
    GreatThan5()

