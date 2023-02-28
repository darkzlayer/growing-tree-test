n = int(input("How many years does the tree grow? "))
def cycle(s, height):
    height *= 2
    height += 1
    s -= 1
    if s != 0:
        cycle(s, height)
    else:
        print("Your tree was", height, "meters.")
cycle(n, 1)