# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

#   Ingredientes vegetarianos: Pimiento y tofu.
#   Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y 
# todos los ingredientes que lleva.

# Declaracion de variables
tipoPizza = input("Quieres una pizza Vegetariana? S/N ")

# declaracion de funciones:
def choose(pizza):
    ingrediente = ""
    pizza = pizza.lower()
    if pizza == "s":
        print("""
        Los ingredientes son\n:
        PIMIENTO Y TOFU
        P = PIMIENTO , T = TOFU\n
        SOLO PUEDES ELEJIR UN INGREDIENTE \n """
        )
        ingrediente = input("Escoje tu Ingrediente \n")
        ingrediente = ingrediente.lower()
        if ingrediente == "p":
            print("""    Tu pizza es Vegetariana con los siguientes ingredientes:
                PIMIENTOS CON TOMATE Y MOZZARELLA
            """)
        elif ingrediente == "t":
            print("""    Tu pizza es Vegetariana con los siguientes ingredientes:
                TOFU CON TOMATE Y MOZZARELLA
            """)
        else:
            print("Elije un ingrediente correcto ")

    elif pizza == "n" :
        print("""
        los ingredientes son\n:
        PEPERONI JAMON Y SALMON
        PE = PEPERONI , J = JAMON , S = SALMON\n
        SOLO PUEDES ELEJIR UN INGREDIENTE\n """
        )
        ingrediente = input("Escoje tu Ingrediente\n ")
        ingrediente = ingrediente.lower()
        if ingrediente == "pe":
            print("""   Tu pizza NO es Vegetariana con los siguientes ingredientes:
                PEPERONI CON TOMATE Y MOZZARELLA
            """)
        elif ingrediente == "J" or ingrediente == "j":
            print("""    Tu pizza NO es Vegetariana con los siguientes ingredientes:
                JAMON CON TOMATE Y MOZZARELLA
            """)
        elif ingrediente == "S" or ingrediente == "s":
            print("""    Tu pizza NO es Vegetariana con los siguientes ingredientes:
                SALMON CON TOMATE Y MOZZARELLA
            """)
        else:
            print("Elije un ingrediente correcto")
choose(tipoPizza)