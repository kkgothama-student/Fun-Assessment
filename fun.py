from string import digits


def dog_years():
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """

    #enter your code here
def dog_years():
    if human_years > 20:
        human_years = 20

    if human_years<= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + (human_years -2) * 4

    return int(dog_years) 
try:
    human_years =float(input("input a dog age in human years"))
    if human_years< 0:
        print("age cannot be negative")
    else:
        print("the dog age in dog year is")    
except ValueError:
    print("please enter a vaild number.")



def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """

    #enter your code here
def Fizzbuzz(num):
    result = []
    for i in range(1,num + i): 
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
         result.append("Fizz")               
        elif i % 5 == 0:
            result.append("Buzz")
    else:
        result.append(str(1))

    return "  ".join((15))  
    print(Fizzbuzz(15))  
        
        


    

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazi"
    Output: {'Aunty': 5, 'ngYankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    
    #enter your code here
def word_lengths(sentence):
    words = sentence.split(" ")
    word_lengths_dict ={word: len(word)for word in words} 
    return word_lengths_dict 

word_lengths("Aunty Yankho is amazi")

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    
    #enter your code here
def cube_sum(numbers):
    digits = [int(digits) for digit in str(num)]
    cube_sum =sum(digits ** 3 for digits in digits)

print(cube_sum(123))   