import os
import imageio
result = os.listdir ("homework8")
print (result)

file_list = sorted(os.listdir ("homework8/image"))
print (file_list)
IMAGES =[]
for file_name in file_list :
    #print (file_name)
    file_path = "homework8/image/"+ file_name
    #print (file_path)
    image =imageio.imread (file_path)
    IMAGES.append (image)
print (IMAGES)
imageio.mimsave("homework8/output.gif",IMAGES)