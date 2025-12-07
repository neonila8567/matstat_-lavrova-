with open('file.txt', 'w') as file:
    for i in range(1,10):
        file.write("a" * i + "\n")
with open('file.txt', 'r') as file:
    text = file.read()
print(text)