import random


def make_world(width, height, world_name):
    f = open(world_name + ".txt", 'w')
    for i in range(height):
        for j in range(width):
            if j == 0:
                f.write("B ")
            elif j == width - 1:
                f.write("B")
            else:
                if i == 0 or i == height - 1:
                    f.write("B ")

                elif random.randint(1, 10) >= 5:
                    f.write("G ")
                else:
                    f.write("g ")
        if i != height - 1:
            f.write("\n")
    f.close()


rock = "R"
grass = "G"
tallgrass = "B"  # B for bush
water = "W"
leaf = "L"
wood = "T"
border = "X"


def main():
    HEIGHT = 100
    WIDTH = 100
    world = []
    # file = open("World1.txt" ,"w")

    for i in range(HEIGHT):
        world.append([])
        for j in range(WIDTH):
            if (j == 0 or j == WIDTH - 1) or (i == 0 or i == HEIGHT - 1):
                node = border
            else:
                chance = random.randint(1, 100)
                if chance >= 96:
                    tree(world, i, j)
                elif chance >= 95:
                    node = water
                elif chance >= 90:
                    node = tallgrass

                elif chance >= 50:
                    node = grass
                else:
                    node = grass

            world[i].append(node)

    tree(world, 50, 50)
    return world

    # file.close()


def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end="")
        print()


def tree(mat, x, y):  # note: y >= 4, x >= 3 for a tree
    if (x < 3 or y < 4) or (x > len(mat) - 3 or y > len(mat) - 4):
        return
    else:
        mat[x][y] = leaf
        mat[x + 1][y + 1] = leaf
        mat[x + 1][y - 1] = leaf
        mat[x + 1][y] = leaf
        mat[x + 2][y] = wood
        mat[x + 3][y] = wood


def read_world(world_path):
    world = []
    f = open(world_path, 'r')
    for line in f:
        line = line.replace("\n", "")
        world.append(line.split(" "))
    f.close()
    return world


if __name__ == "__main__":
    make_world(100, 100, "World1")
    # world = main()
    # file = open("World1.txt", "w")
    # for line in world:
    #     file.write(' '.join(line) + "\n")
    # file.close()