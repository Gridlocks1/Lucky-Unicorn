show_instructions = input("Have you played this game before? ") .lower()

if show_instructions == "yes" or show_instructions == "y":
    print ("program continues" )

elif show_instructions == "no" or show_instructions == "n":
    print("Display instructions ")

else:
    print ("Please answer with yes / no" )

