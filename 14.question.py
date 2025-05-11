# Print downward Half-Pyramid Pattern with Star (asterisk)
list_asterisk = list("*")

for z in range(0, 6, 1):
    for x in range(z, 6, 1):
        # print(x)
        print("*", end=" ")
    print(" ")

for i in range(6, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=' ')
    print(" ")


print("")
for _ in range(6):
    print("*", end=" ")
print("")
for _ in range(6):
    print("*", end=" ")
print("")

for i in range(3):
    print("* *", end=" ")
    if i == 2: 
        for _ in range(4):
            print("*", end=" ")
            # print("*", end=" ")
    print(" ")

for i in range(3):
    print("* *", end=" ")
    if i == 0: 
        for _ in range(4):
            print("*", end=" ")
    print(" ")

for _ in range(6):
    print("*", end=" ")
print("")
for _ in range(6):
    print("*", end=" ")
print("")

print("")
for _ in range(5):
    print("  * *")


for _ in range(6):
    print("  *", end="")
print("")
for _ in range(6):
    print("  *", end="")
print("")

print("")

for _ in range(6):
    print("    *", end="")
print("")
for _ in range(6):
    print("    *", end="")
print("")

for _ in range(4):
    print("   ", end=" ")
    print("           *  *")
    

for _ in range(6):
    print("    *", end="")
print("")
for _ in range(6):
    print("    *", end="")
print("")