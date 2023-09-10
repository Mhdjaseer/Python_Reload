# How TO USE ARRAYS IN PYTHON 
*In order Python arrays , you'll first have to import the array*
module which contains all the necessary functions:

*There are three ways you can import the **array_module** * 
1. By using **import_array** at the top of the file . this includes the module **array**.You would then go on to create an array using **array.array()**

*impor array*
#how you would create an array
*array.array()*

2. Instead of having to type **array.array()** all the time, you could use **import array as arr** at the top of the file , instead of **import array** alone. You  would then create an array by typing **arr.arrayy()** . The **arr** acts as an alias name , with the array constructor then immediately following it .

``` import array as arr ```
#how you would create an array 
```arr.array()```

3. Lastly , you could also **from array import (*)** ,
with **(*)**
importing all the functionalities available , you would then create an array by writing the array () constructor alone .

```from array import ```
#how you would create an array 
```array()```

# How to define arrays in Python 
Once you've  imported the arrray module , you can then go on to define a Python array 

the general syntax for creating an array looks like this :
```variable_name =array(typecode,[element]) ```
### lets break it down :
* **variable_name** would be the name of the array . 
* the **typecode** specifies what kind of elements would be stored in the array , Whenther it would be an array of any other Python data type , Remember that all elements should be of the same data type .


https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods/