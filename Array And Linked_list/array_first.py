import array as arr 

numbers=arr.array('i',[10,20,30])

print(numbers)

'''
#lets break it down :
    * first we included the array module, in this case with 'import array as arr'
    * Then , we created a 'numbers' array.
    * we used 'arr.array() because of 'import  array as arr',
    * Inside the array() constructor, we first included 'i' , for signed integer . Signed 
      integer means that the array can include positive and negative values . 
      Unsigned integer , with 'H' for example , would mean that no negative values are allowed . 
    * Lastly , we included the values to be stored in the array in square brackets . 

    #keep in mind included the values that were not of 'i' typecode, meaning they were not integer values , you would get an error 

'''

'''
=================================================
    in the example above, i tried to include a floating point number in the array . I got an error because this is meant to be an integer array only . 

    another way to create an array is the following . 
=================================================

'''

from array import * 

number=array('d',[10.0,20.0,30.0])
print(number)

'''
the example above imported the 'array module' via from array 
'import * ' and created an array 'number' of float data type. This means that 
it holds only floating point numbers, which is specified with the 'd' typecode . 

'''

'''
## HOw to find the length og an array in python 
    ===========================================
   To find the exact number of elements contained in an array , 
   use the built-in 'len()' method.

   it will return the integer number that is equal to the total number of elements in the 
   array you specify  

'''
import array as arr 

numbers= arr.array('i',[10,20,30])
print(len(numbers))


'''
Array Indexing and How to access individual items in an array in Python 
=====================================================================
Each item in an array has a specific address. Individual items are accessed 
by referencing their index number . 

indexing in Python , and in all programming languages and computing 
in general, starts at '0' . it is important to remember that counting 
starting at '0' and not at '1'

To access an element , you first write the name of the array followed by 
square brackets . Inside the square brackets you include the item's 
index number . 

The general syntax would look something like this :
"array_name[index_value_of_item]
'''

# Here is how you would access each individual element in an array :

import array as arr 

numbers=arr.array('i',[10,20,30])

print(number[0])#gets the 1st element
print(number[1])
print(number[2])



'''
How to search  Through an array in python 
=======================================
You can find out an element's index 
'''