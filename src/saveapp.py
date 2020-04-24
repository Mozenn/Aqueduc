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

            if not(os.path.exists(source["path"])) and not(os.path.isfile(source["path"])):
                print("Error in Plan File. Invalid source")
                sys.exit(1) 

            move(source["path"],source["options"],target_path,1)




#    new_path = [ el for i,el in enumerate(path.split(os.path.sep)) if i > 3]
#    print(os.path.sep.join(new_path))

def move(path,options,target_path,depth) : 

    if os.path.isfile(path) : 

        extension = path.split(".")[-1]

        if extension in options["forbidden_extensions"] : 
            print("forbidden extension")
            return 

        file_size = os.path.getsize(path)
        if options["size_limit"] != -1 and file_size >= options["size_limit"]:
            print("too large")
            return 

        # TODO check last modification time =>os.path.getmtime(path)

        cut_path_list = [ el for i,el in enumerate(path.split(os.path.sep)) if i >= depth ]
        
        if not options["overwrite"] : 
        
            cut_path = os.path.sep.join(cut_path_list)
            
            if os.path.exists(target_path + os.path.sep + cut_path):
                print("not overwrite")
                return  

        cut_path_list_copy = cut_path_list.copy()
        cut_path_list_copy.pop(-1)
        dir_to_create = target_path + os.path.sep + os.path.sep.join(cut_path_list_copy)
        print("CREATED ",dir_to_create)
        os.makedirs(dir_to_create)

        final_target_path = target_path + os.path.sep + os.path.sep.join(cut_path_list)
        print(final_target_path)
        shutil.copy(path,final_target_path) # TODO Fix error 
        
    elif os.path.isdir(path) :

        entries = [path + os.path.sep + x for x in os.listdir(path)]

        for entry in entries : 
            move(entry,options,target_path,depth+1)

def check_parameter() :
    if len(sys.argv) <= 1:
        print("Wrong input. Input should be in form : SaveProgram PlanPath")
        sys.exit(1) 

if __name__== "__main__":
   main()