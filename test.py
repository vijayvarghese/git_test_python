a = str()
def Test(a):
    print("Hello, ",a)

def add(b):
    a = int(b)+10
    print("\n","Number : ",a)

def get():
    item = input("Enter Name : ")
    return item
def get2():
    item = input("Enter a Number : ")
    return item

if __name__ == "__main__":
    
    Test(get())
    add(get2())


