import os,pathlib,subprocess
from django.conf import settings
project_name = "Clash_RC_2"
directory = os.path.join(settings.BASE_DIR,"User_Data")

def make_dir(user):
    print("inside make_dir",directory)
    # project_name = "Clash_RC_2"
    # directory = pathlib.Path(f"./{project_name}/User_Data/{username}")
    # if not directory.exists():
    #     directory.mkdir()
    #     return 1
    user_folder = pathlib.Path(f"{directory}/{user}")  #to check directory is present or not
    #if not it will create it
    if not user_folder.exists():
        user_folder.mkdir()

def make_code_file(language,code,ip_text,user):
    if language == "py":
        code_file = open(f"{directory}/{user}/code.{language}","w")
        code_file.write(code)
        code_file.close()
        text_file = open(f"{directory}/{user}/ip_text_file.txt","w")
        text_file.write(ip_text.replace('\n',""))
        text_file.close()
        return run_code_file(user,language)

def run_code_file(user,language):
    if (language == "py"):
        code_file_path = pathlib.Path(f"{directory}/{user}/code.py")
        text_file = pathlib.Path(f"{directory}/{user}/ip_text_file.txt")
        cmd = f"python {code_file_path} <{text_file}"
        op = subprocess.run(cmd,shell=True,text=True,capture_output=True)
        # print(op)
        # print(op.stdout)
        # print(op.stderr)
        code_op_text_file = open(f"{directory}/{user}/op_text.txt","w")
        if op.returncode !=1:
            code_op_text_file.write(op.stdout)
        else:
            code_op_text_file.write(op.stderr)
            
        code_op_text_file.close()

        if (compare_answer(user)):
            return True
        else:
            return False
        
directory_questions = os.path.join(settings.BASE_DIR,"Question_Data")

def compare_answer(user):
    with open(f'{directory_questions}/question_op/Q1_1_op.txt', 'r') as f1, open(f"{directory}/{user}/op_text.txt", 'r') as f2:
    # Read the contents of each file into memory
        file1_contents = f1.readlines()
        file2_contents = f2.readlines()
        print(file1_contents)
        print(file2_contents)

    # Compare the contents of the files
    if file1_contents == file2_contents:
        print("The files are the same")
        return True
    else:
        print("The files are different")
        return False
    

    # try:
    #     with open(f'{directory_questions}/question_op/Q1_1_op.txt', "r") as correct_output:
    #         x = correct_output.read().strip()
    #         y = f"{directory}/{user}/op_text.txt"
    #         print(x,y)
    #         if y.strip() == x :
    #             print("same file")
    #             return True
    #         else:
    #             print("diff file")
    #             return False
    # except:
    #     return False
        



        
        
    
