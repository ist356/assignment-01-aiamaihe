'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''

def order_numbers():
    numbers = {'odd': [], 'even': []}

    while True:
        try:
            num = int(input("Enter an integer (0 to stop): "))
            if num == 0:
                break
            elif num % 2 == 0:
                numbers['even'].append(num)
            else:
                numbers['odd'].append(num)
        except ValueError:
            print("Please enter a valid integer.")
    
    print("Ordered numbers:", numbers)

order_numbers()
