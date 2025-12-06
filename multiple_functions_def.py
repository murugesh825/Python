# Create a class and function, and list out the items in the list

class multiple_functions():

    #******************************************************************************
    # Create a class and function, and list out the items in the list
    #******************************************************************************
    
    def Sub_Fields():

        List=('Machine Learning',
          'Neural Networks',
          'Vision',
          'Robotics',
          'Speech Processing',
          'Natural Language Processing')
        
        print('Sub-fields in AI are:')
        for i in List:
            print(i)

    #******************************************************************************
    # Create a function that checks whether the given number is Odd or Even
    #******************************************************************************
    
    def Odd_Even():
        number=int(input('Enter an number : '))
        if (number%2==0):
            print(number, 'is Even number')
        else:
            print(number, 'is Odd number')
        
        print('-'*55)

    #******************************************************************************
    # Create a function that tells elegibility of marriage for male and female 
    # according to their age limit like 21 for male and 18 for female
    #******************************************************************************
    
    def Marriage_Eligible():
        gender=input('Your Gender : ')
        age=int(input('Your Age : '))
        if (gender=='Male' and age>=21):
            print('You are eligible for Marriage')
        elif (gender=='Female' and age>=18):
            print('You are eligible for Marriage')
        else:
            print('You are not eilgible for Marriage')
    
        print('-'*55)

    #******************************************************************************
    # calculate the percentage of your 10th mark
    #******************************************************************************
    
    def percentage():
        Subject1=int(input('Subject1 = '))
        Subject2=int(input('Subject2 = '))
        Subject3=int(input('Subject3 = '))
        Subject4=int(input('Subject4 = '))
        Subject5=int(input('Subject5 = '))
        Total=Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        Percentage=Total/5
        print('Total = ',Total)
        print('Percentage = ',Percentage)

    #******************************************************************************
    # print area and perimeter of triangle using class and functions
    #******************************************************************************
    
    def area_perimeter():
        print('Type A to calculate Area of a Triangle')
        print('Type P to calcuate Perimeter of a Triangle')
        InputType = input()
        if InputType == 'A':
            Height = int(input('Enter Height : '))
            Breadth = int(input('Enter Breadth : '))
            print('Area Formula = (Height*Breadth)/2')
            Area=(Height*Breadth)/2
            print('Area of Triangle',Area)
        elif InputType == 'P':
            Height1 = int(input('Enter Height1 : '))
            Height2 = int(input('Enter Height2 : '))
            Breadth = int(input('Enter Breadth : '))
            print('Perimeter Formula = Height1 + Height2 + Breadth')
            Perimeter = Height1 + Height2 + Breadth
            print('Perimeter of Triangle',Perimeter)
        else:
            print('Invalid Input Type')
    
        print('*'*55)