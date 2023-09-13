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


* inside square brackets you mention the **elements** that would be stored in the array , with each element being seperated by a comma . You can also created an *empty* array by just writing  *variable_name=array(typecode )* alone, without any elements. 

below is a typecode table, with the different typecodes that can be used with the different data types when defining Python array 


Tying everything together, here is an example how you would define an array in Python::

```import array as arr```
```numbers=arr.array('i',[10,20,30])```
```print(number)```
#output 
#array('i',[10,20,30])


# LINKED LIST  >
*Linked_list* directory >
===========================================

# What is Linked List in Python
-----------------------------------
    A linked list is a type of linear data structure similar to arrays. it is a collection of nodes that are linked with each other . A node 
    contains two things first is data and second is a link that connects it with four nodes and each node contains charecter data and a link to another node. Our first node is where **head** points and we can access all the elements of teh linked list using the head . 

## Creating a linked list in Python 

In this LinkedList class , we will use the Node class to create a linked list . in this class, we have an __init__ method that initializes the linked list with an empty head , Next , we have created an **insertAtBrgin()** method to insert a node at the given index of the linked list , and **insertEnd** method inserts a node at the end of the linked list. After that we have the **remove_node** method which takes the data as an argument to delete that node . In the **remove_node** method we traverse the linked list if a not is present equal to data then we delete that node from the linked list . Then we have the **sizeOfLL()** method to get the current size of the linked list and the last method of the LinkedList class is **PrintLL()** which traverse the linked list and print the data of each node. 

### Creating a Node Class 

we have created a Node class in which we have defined a __init__ function to initialize the node with the data passed as an argument and a reference with None because if we have only one node then there is nothing in its reference . 

-------------------------
```class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
```

### Insertion in Linked List 
#### Insertion at Beginning in Linked List 

This method inserts the node at the beginning of the linked list. in this method, we create a **new_node** with the given **data** and check if the head is an empty node or not if th ehead is empty then we make the **new_node** as head and return else we insert the head at the next **new_node** and make the **head** equal to **new_node**.

--------
```
def insertAtBegin(self,data):
    new_node=Node(data)
    if self.head is None:
        self.head= new_node
        return
    else:
    new_node.next= self.head
    self.head=new_node
```
### Insert a Node at specific Positon in a Linked List 

This method inserts the node at the given index in the linked list. In this method , we create a **new_node** with given data, a current_node that equals to the head, and a counter **'position'** initializes with **0** . Now , if the index is equal to zero it means the node is to be inserted at begin so we called **insertAtBegin()** else we run a while loop until the **current_node** is not equal to **None** or **(postion+1)** is not equal to the index we have to at the one position back to insert at a given position to make the linking of nodes and in each iteration , we increament the position by 1 and make the **current_node** next of it . when the loop breaks and if current_node  is not equal to None we insert new_node at after to the current_node. if current_node is equal to None it means that the index is not present in the list and we print **"Index not present"**

-----------------------------------------------------
```
def insertAtIndex(self, data, index):
    new_node=Node(data)
    current_node=self.head
    position=0
    if position == index:
        self.insertAtBegin(data)
    else:
        while(current_node !=None and position+1 !=index):
            position=postion+1
            current_node=current_node.next
            
        if current_node != None:
            
            new_node.next=current_node.next
            current_node.next=new_node
        else:
            print("index not present")
```

### INSERTION IN LINKED LIST AT END 

this method inserts the node at the end of the linked list . in this method , we create a **new_node** with the given data and chdck if teh head is an empty node or not if the head is empty then we make the **new_node** as head and return **else** we make a **current_node equal**  to **the_head** traverse to the last **node** of the linked lsit and when we get **none** after the curernt_node the while loop breaks and insert the **new_node** in the next of **current_node** in the next of **current_node** which is the last node of linked list . 

```
def inserAtEnd(self,data):
    new_node=Node(data)
    if self.head is None:
        self.head=new_node
        return 

    current_node=self.head
    while(current_node.next):
        current_node=current_node.next

    current_node.next=new_node
```

## Update the Node of a Linked List 

this code defines a method called updateNode in a linked list class. it is uded to upload the value of a node at a given  position in the linked list.


#