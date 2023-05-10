import numpy as np


def Gaussian_distribution(m, std):
    return m + std * (sum(np.random.uniform(0, 1, 12)) - 6)


def main():
    f = open("data/input.data")
    lines = f.readlines()
    x_list = []
    y_list = []
    for line in lines:
        sp = line[:-1].split(' ')
        x_list.append(sp[0])
        y_list.append(sp[1])

    beta = 5
    print(x_list[0] + Gaussian_distribution(0, 3))
    
    


if __name__ == "__main__":
    main()
