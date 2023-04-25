largest = None
smallest = None

while True:
    num_in = input("Enter a number: ")
    if num_in == "done":
        break
    try:
        num = int(float(num_in))    #necessary to accept both int and float values
        if largest is None or smallest is None:
            largest = num
            smallest = num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    except:
        print("Invalid input")

print("Maximum is",largest)
print("Minimum is",smallest)