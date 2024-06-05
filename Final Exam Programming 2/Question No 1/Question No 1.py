#---------------------------------------------Hello Welcome to Question No 1--------------------------------------




print("Questiopn No 2")

def decimal_num_to_binary(decimal_number):

    if decimal_number <= 1:
        return str(decimal_number)
    
    else:
        x = decimal_num_to_binary(decimal_number // 2) + str(decimal_number % 2)
        return x


decimal_num = int(input("Enter any decimal number: "))

binary_number = decimal_num_to_binary(decimal_num)

print("Its Binary number is :", binary_number)


