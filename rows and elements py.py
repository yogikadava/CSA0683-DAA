n = int(input("Enter the number of rows to print: "))

for i in range(n):
    coef = 1
    for j in range(n - i):
        print(" ", end="")
    
    for j in range(i + 1):
        print(" ", coef, end="")
        coef = coef * (i - j) // (j + 1)
    
    print()

row_number = int(input("Enter row number: "))
if 1 <= row_number <= n:
    row_elements = [1]
    for i in range(1, row_number):
        row_elements.append(row_elements[i - 1] * (row_number - i) // i)
    
    sum_of_elements = sum(row_elements)
    print(f"The sum of elements in row ",sum_of_elements)
else:
    print("Row number out of bounds.")
