num = int(input("Enter the number of rows of stars to print:"))
counter = 0
print("Type 1 to print stars in ascending order.\nType 0 to print stars in descending order.")
bool_val = int(input("Type here:"))

while bool_val == 1:
    counter+=1
    print(counter*"*")
    if counter == num:
       exit("Done")

while bool_val == 0:
    for i in range(num,0,-1):
        print("*"*i)
        if i == 1:
            exit("Done")
