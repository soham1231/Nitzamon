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
