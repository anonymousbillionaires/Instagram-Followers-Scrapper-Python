import numpy as np


def read_following_list():
    file = open("following_list_numpy", "rb")
    return np.load(file)
