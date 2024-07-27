n=eval(input("enter the word"))

result = ""
for word in n:
    if word == word[::-1]:  
        result = word
        break

print(result)  
