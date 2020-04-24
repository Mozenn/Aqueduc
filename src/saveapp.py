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

            limit = len(source["path"].split(os.path.sep)) -1 
            move(source["path"],source["options"],target_path,limit)



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
              
        # get the folder path of the final 
        final_target_path = target_path + os.path.sep + os.path.sep.join(cut_path_list)
        final_target_path_list = [el for el in final_target_path.split(os.path.sep)] 
        final_target_path_list.pop(-1)
        folder_path = os.path.sep.join(final_target_path_list)
  
        if not os.path.exists(folder_path) :
            os.makedirs(folder_path)
        shutil.copy(path,final_target_path)
        
    elif os.path.isdir(path) :

        entries = [path + os.path.sep + x for x in os.listdir(path)]

        for entry in entries : 
            move(entry,options,target_path,depth)

def check_parameter() :
    if len(sys.argv) <= 1:
        print("Wrong input. Input should be in form : SaveProgram PlanPath")
        sys.exit(1) 


if __name__== "__main__":
   main()