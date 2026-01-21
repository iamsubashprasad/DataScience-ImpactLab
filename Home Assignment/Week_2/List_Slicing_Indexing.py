'''
Perform the following operations using list slicing and indexing techniques:
a) Extract the middle five primes: Create a new list containing the five primes in the middle
of the original list.
b) Get every second prime: Create a new list containing every second number from the
original list, starting from the beginning.
c) Use negative indexing: Create a new list containing the last three primes of the list.
d) Reverse the list: Create a new list that contains all the elements of the original list in
reverse order.
e) Descending Order: Sort the list in descending order and store it in a new list.
'''
#prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

prime_list = [ 3, 5, 7, 11, 13, 17, 19, 23, 29]

#xtract the middle five primes: Create a new list containing the five primes in the middle
#of the original list.

list_len = int(len(prime_list)/2)
print(list_len)

new_middle_list = prime_list[list_len-2:list_len+3:]
print("New list containing the five primes in the middle", new_middle_list)


# Get every second prime: Create a new list containing every second number from the
#original list, starting from the beginning.
new_list_middle = prime_list[1::2]
print("new list containing every second number", new_list_middle)


#Use negative indexing: Create a new list containing the last three primes of the list.
new_negative_list = prime_list[-1:-4:-1]
print("new list containing the last three primes of the list", new_negative_list)


#Reverse the list: Create a new list that contains all the elements of the original list in
#reverse order.

new_reverse_list = prime_list[::-1]
print("Reverse the list", new_reverse_list)

# Descending Order: Sort the list in descending order and store it in a new list.
Descending_List = sorted(prime_list, reverse=True)
print("Descending Order", Descending_List)


