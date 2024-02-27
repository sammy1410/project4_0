import os 
import shutil

#loc = "./products/images/"
filepath = "./products/images/"
path = "./products/"
files = os.listdir(path)
print(files)
#jpgs = [file for file in files if file.endswith(".jpg")]

for file in files:
#    index = jpg.rfind("_")
#    dot = jpg.rfind(".")
#    name =jpg[:-(len(jpg)-index)]
#    num = int(jpg[(index+1):dot])
#    print(f"File: {filepath}{jpg} to {path}Pid{num}_{name}/image.jpg")
    print(f"File: {path}{file}/image. to {path}{file}/image.jpg")
    shutil.move(f"{path}{file}/image.",f"{path}{file}/image.jpg")

#    os.makedirs(f"{path}/Pid{num}_{name}")
#    with open(f"{path}/Pid{num}_{name}/Pid{num}_{name.lower()}.inf","w") as file_to_write:
#        file_to_write.write(f"""Product Info: {name}
#Quantity: 0
#Color: Clear
#Material: Plastic
#Special_Feature: Stackable, Transparent, transparent
#About this item:
#    -Transparent for ease of use
#    -Complete with clip lock handles
#    -Stackable with the same size Really Useful Box
#    -Perfect for A4 paper, magazines & shoes
#    -Part of a large range of Really Useful Boxes
#""")
#    
#    index = jpg.rfind("_")
#    dot = jpg.rfind(".")
#    name =jpg[:-(len(jpg)-index)]
#    #print(f"{jpg[(index+1):dot]},{name}")
#    x.add(( int(jpg[(index+1):dot]),name))
#    #i+=1
#    #shutil.move(f"{filepath}{jpg}",f"{filepath}{name}.jpg")
#    #print(f"{filepath}{jpg} to {filepath}{name}.jpg")
#sx=sorted(x)
#for i,v in sx:
#    print(f"{i},{v}")


