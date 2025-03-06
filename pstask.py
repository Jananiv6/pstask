# A biometric security system needs to generate a secure PIN from a user's fingerprint data. Each scanned fingerprint is converted into a unique number, and the system extracts the smallest prime digit from this number to enhance security checks. If no prime digits exist, it alerts the user.
# Your task is to write a program that finds the smallest prime digit (2, 3, 5, or 7) in a given number.
def find_smallest_prime_digit(number):
    num_str = str(number)
    prime_digits = [2, 3, 5, 7]
    smallest_prime = None
    for digit in num_str:
        digit_int = int(digit) 
        if digit_int in prime_digits:   
            if smallest_prime is None or digit_int < smallest_prime:
                smallest_prime = digit_int

    if smallest_prime is None:
        print("No prime digits found.")
    else:
        print(f"The smallest prime digit is: {smallest_prime}")
  
number = int(input("Enter a number: "))
find_smallest_prime_digit(number)


# Programme to print the sum of odd digits in a number. 

def sum_of_odd_digits(number):
    num_str = str(number)
    odd_sum = 0
    for digit in num_str:
        digit_int = int(digit)
        if digit_int % 2 != 0:   
            odd_sum += digit_int
    
    print(f"The sum of odd digits is: {odd_sum}")
number = int(input("Enter a number: "))
sum_of_odd_digits(number)
