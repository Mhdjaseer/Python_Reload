x="awesome"

def myFunction():
    print("python is "+x)


myFunction()


def My_second_fun():
    global y
    y="this is global"

    print( "this is from inside of the function "+ y)

My_second_fun()

print("this is  from main page global value "+y)