def hello():
    print("Hello")
hello()

def pack(a, b, c):
    return(a, b, c)
print(pack("A", "B", "C"))

def eat_lunch(lunch_box):
    if len(lunch_box) == 0:
        print("My lunch box is empty")
    else:
        for i in range(len(lunch_box)):
            if i == 0:
                print(f"First I eat", {lunch_box[0]})
            else:
                print(f"Next I eat", {lunch_box[i]})
print(eat_lunch(["apple", "sandwich", "chips"]))