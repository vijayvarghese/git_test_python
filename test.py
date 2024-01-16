a = str()
def Test(a):
<<<<<<< HEAD
<<<<<<< HEAD
    print(a+10)


def get():
    item = input("Enter any Number : ")
=======
    print("Hello, ",a,"Welcome !")
=======
    print("Hello, ",a)
>>>>>>> parent of 0bea603 (new greeting)

def add(b):
    a = int(b)+10
    print("\n","Number : ",a)

def get():
    item = input("Enter Name : ")
>>>>>>> New_Feature
    return item
def get2():
    item = input("Enter a Number 1-10 : ")
    return item

if __name__ == "__main__":
    
    Test(get())
    add(get2())


