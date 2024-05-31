name = input("What's your name? ")
match name:
    case "harry" | "harmione" | "ron":
        print("gryffindor")
    case "draco":
        print("slytherin")
    case _:
        print("Who are you")

