# print("Hola Mundo!")
#
# edad = 0
# while edad < 18:
#     edad = edad + 1
#     print("Felicidades, tienes " + str(edad))
#
# while True:
#     entrada = input("> ")
#     if entrada == "adios":
#         break
#     else:
#         print(entrada)

# condicion = True
# while condicion:
#     entrada = input("> ")
#     if entrada == "adios":
#         condicion = False
#     else:
#         print(entrada)

# edad = 0
# while edad < 18:
#     edad = edad + 1
#     if edad % 2 == 0:
#         continue
#     print("Felicidades, tienes " + str(edad))

# l = [99, True, "una lista"]
# mi_var = l[0:2]
# print(mi_var)
# mi_var = l[0:4:2]
# print(mi_var)
# mi_var = l[1:]
# print(mi_var)
# mi_var = l[:2]
# print(mi_var)
# mi_var = l[:]
# print(mi_var)
# mi_var = l[::2]
# print(mi_var)
# l[0:2] = [False]
# print(l)

# t = (1, 2, 3)
# print(type(t))

def varios(param1, param2, *otros):
    for val in otros:
        print(val)
    print("___________________-")

varios(1,2)
varios(1,2,3)
varios(1,2,3,4)
