with open('C:\\Users\\andri\\OneDrive\\Робочий стіл\\proj\\text') as f:
    content = f.read().split("\n")

me_value = 0
while me_value <= 0 or me_value > 1000:
    me_value = int(input("Your result [1-1000] ---> "))
    if(me_value <= 0 or me_value > 1000): 
        print("\nWrong input, Right[1-1000]")

for line in content:
    parts = line.split(" ")
    if(int(parts[1]) > me_value):
        print(line)

   