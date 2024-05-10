#function is a first class object

def double_decker():
    print("Inside the double decker")

    def inner_fun():
        print("Inside the inner function")
    
    return inner_fun



print(double_decker()())