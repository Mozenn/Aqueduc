import sys 
import os.path
import os 
import json 
import shutil

def main():

    check_parameter() 

    plan_path = sys.argv[1]
    
    if not(os.path.exists(plan_path)) or not(os.path.isfile(plan_path)):
        print("Wrong input. Invalid Plan File")
        sys.exit(1) 


    with open(plan_path) as plan_file: 
        
        plan = json.load(plan_file)
        target_path = plan["target"]

        if not(os.path.exists(target_path)) or not(os.path.isdir(target_path)):
            print("Error in Plan File. Invalid target")
            sys.exit(1) 

        for source in plan["sources"]:

            if not(os.path.exists(source["path"])) or not(os.path.isfile(source["path"])):
                print("Error in Plan File. Invalid source")
                sys.exit(1) 

            move(source["path"],source["options"])




if not(source["overwrite"]):
    source_name = source["path"].split(os.path.sep)[-1]

    if os.path.exists(target_path + os.path.sep + source_name):
        continue 

def move(path,options) : 

    if os.path.isfile(path) : 

        extension = path.split(".")[-1]

        if extension in options["forbidden_extensions"] : 
            return 
        # TODO check size => search how to 
        # TODO check extension => use split 
        
        # TODO check overwrite => tweak above code 

        shutil.copy(path,target_path)
        
    elif os.path.isdir(source["path"]) :

        entries = [path + os.path.sep + x) for x in os.listdir(path)]

        for entry in entries : 
            move(entry,options)

def check_parameter() :
        if len(sys.argv) <= 1:
        print("Wrong input. Input should be in form : SaveProgram PlanPath")
        sys.exit(1) 

if __name__== "__main__":
   main()