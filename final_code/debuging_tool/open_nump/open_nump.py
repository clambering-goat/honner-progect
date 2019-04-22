import numpy
import os


for files in os.listdir("./"):
    if files[-4:len(files)] == ".npy":

        print("file name ",files)
        data=numpy.load(files)
        print()







