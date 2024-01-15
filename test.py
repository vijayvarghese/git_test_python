a = str()
def Test(a):
<<<<<<< HEAD
    print(a+10)


def get():
    item = input("Enter any Number : ")
=======
    print("Hello, ",a,"Welcome !")


def get():
    item = input("Enter Name : ")
>>>>>>> New_Feature
    return item

if __name__ == "__main__":
    
    Test(get())

