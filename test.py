a = str()
def Test(a):
    print("Hello, ",a)


def get():
    item = input("Enter Name : ")
    return item

if __name__ == "__main__":
    
    Test(get())

