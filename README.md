# DataScience-ImpactLab
## DataScience-ImpactLab is a collection of real world data science projects focused on transforming raw data into actionable business insights.

# String Inbuilt Functions :
**Key concepts and functions covered:**
*********************************************************************************************************************************
String Declaration: Creating a string variable (e.g., s = "Euron").
- upper(): Converts a string to uppercase. It doesn't modify the original string unless reassignment is done (e.g., s = s.upper()).
- lower(): Converts a string to lowercase. Similar to upper(), it requires reassignment to permanently change the string.
- capitalize(): Converts the first character of the string to uppercase and the rest to lowercase.
- title(): Converts the first character of each word in the string to uppercase.
- swapcase(): Swaps the case of each character in the string (uppercase to lowercase and vice versa).
- casefold(): Converts the string to lowercase, performing more aggressive case conversion for case-insensitive matching.
- find(): Returns the index of the first occurrence of a substring within the string. If the substring is not found, it returns -1.
- index(): Similar to find(), but raises a ValueError if the substring is not found.
- count(): Returns the number of times a substring appears in the string.
- is...() functions (e.g., isalpha(), isalnum()): These functions return boolean values (True or False) based on whether the string meets certain criteria.
- isalpha(): Checks if all characters in the string are alphabetic.
- isalnum(): Checks if all characters in the string are alphanumeric (alphabetic or numeric).
- split(): function to split the two number or two inputs into two different variables . e.g : x,y = int(input("Enter two number")).split() ---> x= 500 , y= 500
- reverse():

## 1. String Creation:
Strings can be created using single quotes (' '), double quotes (" "), or triple quotes (''' or """ ).
Triple quotes are useful for multi-line strings or when single/double quotes are present within the string.
If a string contains single quotes, enclose it in double quotes, and vice versa, to avoid syntax errors.

## 2. Indexing:
Python strings are indexed, meaning each character has a position number.
Forward Indexing: Starts from 0 for the first character and increases sequentially.
Backward Indexing: Starts from -1 for the last character and decreases sequentially.
Individual characters can be accessed using their index within square brackets (e.g., string[0] for the first character).

## 3. Slicing:
Slicing extracts a portion (substring) of a string.
The syntax is string[start:end:step].
start: The index to begin the slice (inclusive). If omitted, defaults to the beginning of the string.
end: The index to end the slice (exclusive). The character at this index is not included. If omitted, defaults to the end of the string.
step: The increment between indices (default is 1). A negative step reverses the slice.

## Important: The end index is exclusive. To include a character at a specific index, the end index must be one position beyond it.
**Step Size:**
Determines the jump or step between characters in the slice.
A step of 2 will select every other character.
A negative step reverses the string or a portion of it.

## Reversing a String:
string[::-1] reverses the entire string.
This uses a negative step without specifying start or end indices, effectively reversing the string.

## Conflicts in Direction:
If the start and end indices, combined with the step, create a conflict in direction (e.g., going from a higher index to a lower index with a positive step), the result will be an empty string.

## 4. Key Takeaways:
Understanding forward and backward indexing is crucial for accessing and manipulating string characters.
Slicing provides a powerful way to extract substrings based on index ranges and step sizes.
The step parameter in slicing enables advanced operations like reversing strings or selecting specific character patterns.
Be mindful of the exclusive end index in slicing to ensure the desired characters are included in the result.
When reversing strings with slicing, using [::-1] is the most concise and effective method.

## String Immutability:
Strings in Python are immutable, meaning their values cannot be changed after they are created.

When you perform operations that appear to modify a string (e.g., concatenation), a new string object is created in memory, rather than modifying the original string.
The lecture demonstrates this by showing that the memory address (ID) of a string changes when it's "modified" through concatenation, even if the result is assigned back to the same variable name.

Attempting to modify a string in place (e.g., using item assignment like s[0] = 'new_char') results in a TypeError because strings do not support item assignment.
Reassigning a string variable with a new value also creates a new string object at a different memory address.
String Interning:

# String interning is an optimization technique used by Python to save memory.
When identical string literals are created, Python may store only one copy of the string in memory and have multiple variables refer to the same memory location.
The lecture demonstrates this by creating two variables, a and b, both assigned the same string value "Euron". The id() function reveals that a and b point to the same memory address.

This optimization is particularly effective when dealing with duplicate string data, as it avoids unnecessary memory allocation.
The lecture also shows an example where two strings are created with the same value, one through concatenation and the other directly. Python interns these strings, so they share the same memory address.

**Key Concepts and Takeaways:**
Immutability: Strings cannot be changed in place. Operations that appear to modify strings create new string objects.
Interning: Python may reuse memory for identical string literals to optimize memory usage.
Understanding immutability is crucial for predicting how string operations affect memory and program behavior.
Interning can lead to unexpected behavior when comparing strings using is (identity comparison) versus == (equality comparison).


# Control and Loop
## For loop :
s= "Subash"
for i in s
  print(i)
Here, i is local variable and s will provide the each character each iteration

## Converting the each character to upper case
for i in s
  print(i.upper())

  ## List : List is something which store any type of data . 
  if you want to iterate the list value one by one , we use for loop
  List = [1.2,3,4,56]
  for i in List
     print(i)

  # Range : Range generate the data before upperbound
  Upperbounr will be silent 
  e.g : range(1,40) --> 40 will be silent 
  
  2. range(1,40,3) --> generate till 39 but jump every 3
    for i in range(0,7)
       print (i)

  3. output : subash --> sbs
     s  = "Subash Prasad"
     len = len(s)
     for i in range(len)
       print(i)

  4. for i in range(0,len,2)
       print(i)

  5. output : Reverse the name one by one - hsabus
     range(len{s)-1
     for i in range(9,0,-1)
       print(i)

   6. Pattern Printing
      *
      * *
      *  *  *
      * * *

      for i in range(1,n+1)
       print("*" *i)

      ## Function in Python
      Why we need functions : To increase the reusability
      syntax :
      def test():
        pass  -- nothing will return

      def test1():
         print("My name is sudhansu")
     # Note : in the function you should not use print becuase print will return nonetype , so use return "my name is subash"
       You can return multiple things from the functions

   


      












      
      
         
     
    









  
