#Decorators are when you can pass another function in the function to enhance its functionality
#used to add functionality to functions or methods without modifying their actual code

lst =[5, 7, 9]
#Decorator function func passed as a parameter of other function welcome_msg below:
def welcome_msg(func,lst):
    print("welcome to decorators 1")
    #Decorator function called here
    func(lst)
    print(lst)
    print("end of the decorator calling")

#@welcome_msg    
def square_list(lst):
    print("inside square_list function", lst)
    print(list(map(lambda x:x*2,lst)))


welcome_msg(square_list,lst)
