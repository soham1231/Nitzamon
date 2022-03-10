import random


def make_world(width, height, world_name):
    f = open(world_name + ".txt", 'w')
    for i in range(height):
        for j in range(width):
            if j == width - 1:
                f.write("G")
            else:
                if random.randint(1, 10) >= 5:
                    f.write("G ")
                else:
                    f.write("G2 ")
        if i != height - 1:
            f.write("\n")
    f.close()


def read_world(world_path):
    world = []
    f = open(world_path, 'r')
    for line in f:
        line = line.replace("\n", "")
        world.append(line.split(" "))
    return world


if __name__ == "__main__":
    make_world(250, 250, "World1")
