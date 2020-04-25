import sys 
import os.path
import os
import json
import time 
import datetime
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
    s_time = datetime.datetime.strptime("30 Nov 2010 12", "%d %b %Y %H").timestamp() 
    epoch = datetime.datetime.utcfromtimestamp(0)
    # print(s_time - epoch)
    
    time_file = os.path.getmtime("test.py") 
    t = time.strftime("%a %d %b %Y %H:%M:%S GMT", time.gmtime(time_file))
    print(s_time)
    print(time_file)
    # milliseconds_since_epoch = datetime.datetime.now().timestamp() * 1000
    # print(time_file - milliseconds_since_epoch)
    # print(s_time - milliseconds_since_epoch)
    # print(s_time)
   #main()
#    path = "C:\\Users\\Gauthier\\Downloads\\Music"
   
#    new_path = [ el for i,el in enumerate(path.split(os.path.sep)) if i > 2]
#    print(os.path.sep.join(new_path))
#    child_paths = os.listdir(path)
#    [print(path + os.path.sep + x) for x in child_paths]
#    [print(x.split(".")[-1]) for x in child_paths]
