def is_it_armstrong(num_str):
    #get first, second and third nums seperately
    #use square brackets and the position (index) of the character we want to get 
    first_str = num_str[0]
    second_str = num_str[1]
    third_str = num_str[2]

    #convert each digit from the string into an int and store in a new variable
    first = int(first_str)
    second = int(second_str)
    third = int(third_str)

    #calculate the sum of their cubes, because its a three digit number
    # ** is the mathematical operation for calculating 'to the power of'
    sum = (first**3) + (second**3) + (third**3)

    #convert the original three digit string to a number for comparision 
    num = int(num_str)

    #check if the sum is equal to the original number 
    if num == sum :
        print(f'{num} is an armstrong number')
    else :
        print(f'{num} is not an armstrong number')

#get a three digit number from the user and store it in a variable 
num_str = input('enter a three digit number : ')

#call the function
is_it_armstrong(num_str)