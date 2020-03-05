import sys 
import os.path
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
   main()