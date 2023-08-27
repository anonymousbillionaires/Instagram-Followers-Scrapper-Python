import numpy as np
import json

if __name__ == '__main__':
    file = open("following_list_numpy", "rb")
    array = np.load(file)
    print(array)
