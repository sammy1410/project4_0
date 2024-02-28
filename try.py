import pickle

from utility.fileHandler import USER_DB,PRODUCT_DB,PRODUCT_PATH

with open(USER_DB,"w") as file:
    while True:
        try:
            break
            pass
            #this = pickle.load(file)
            #print(this)
            #print(this["Email"])
        except EOFError:
            break
