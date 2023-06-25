bottels = 99
while bottels > 0:
    if bottels != 1:
        print(f"{bottels} bottels of beer on the wall.")
        print(f"{bottels} bottels of beer.")
        print(f"Take one down, pass it around, {bottels -1 } bottels of beer on the wall.")
        print("*********************************************************************")
        bottels -= 1
    else:
        print(f"{bottels} of beer on the wall.")
        print(f"{bottels} of beer.")
        print(f"Take one down, pass it around, no more bottels of beer on the wall.")
        print("*********************************************************************")
        bottels -= 1
