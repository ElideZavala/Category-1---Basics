#  Print multiplication table from 1 to 10

rango = 11

for i in range(1, rango):
    print(f"## Tabla del {i} ##")

    for j in range(1, rango):
        print((f"{j} * {i} = {i * j}" ))
        if (j == 10):
            print("\n")


# EN EL 1 VAN HABER 10, POR QUE ESTA DENTRO DEL BUCLE