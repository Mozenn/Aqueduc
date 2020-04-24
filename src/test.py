import sys 
import os.path
import os
import json
sys.path.append('src/')

def main():

    print(os.getcwd())
    with open("test.json") as file:
        data = json.load(file)

        print(data["target"]) 

        for source in data["sources"]:
            print(source["path"])
        print("done")  
    

if __name__== "__main__":
   #main()
   path = "C:\\Users\\Gauthier\\Downloads\\Music"
   
   new_path = [ el for i,el in enumerate(path.split(os.path.sep)) if i > 2]
   print(os.path.sep.join(new_path))
   child_paths = os.listdir(path)
#    [print(path + os.path.sep + x) for x in child_paths]
#    [print(x.split(".")[-1]) for x in child_paths]
