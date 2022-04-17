from typing import Dict
from alphabet import to_nbr
from random import randint


def name_num(name: str) -> int:
    nbr: int = 0
    place: int = 0
    for char in name[::-1]:
        nbr += to_nbr(char) * (26 ** place)
        place += 1
    return nbr


def main(silly=True) -> None:
    name: str = input("What is your name flesh bag?\n")
    bag_nbr: int = name_num(name)

    if name.lower() in {"violet"}: # wifey only
        roll: int = randint(1, 20)
        print("" + str(roll) + "")
        if roll in {"20"}:
            print("Hai cutie, you have a nice ass ;3 *headpats*")
        elif roll in {"10"}:
            print("Horny levels over 100% detected, please go fuck yourself")
        print("Hai cutie <3 *headpats*")

    elif name.lower() in {"ashlee"}:  # ashlee only
        print("Hai cutie <3 *headpats*")

    elif bag_nbr % 50 == 1:  # overcompensation
        print("Hello " + name + ", I love your name, apologies for calling you flesh bag!")
    elif bag_nbr % 5 == 1:  # disapproval
        print("Hello flesh bag #" + str(bag_nbr) + " otherwise known as \"" + name + "\" which is a stupid name by the way!")
    else:  # approval
        print("Hello flesh bag #" + str(bag_nbr) + " otherwise known as \"" + name + "\"!")

    if silly:
        dbl_name: str = name * 2
        name_len: int = len(name)
        print("Name go rotate!")
        for index in range(0, name_len):
            print(dbl_name[index : index + name_len])

if __name__ == '__main__':
    main(silly=False)
