import subprocess
import shutil
import os
# from . models import Question, Testcase
from subprocess import STDOUT, check_output
from celery import shared_task

def execute(code, tc, language):
    copy_run_py(language)
    copy_code(code)
    copy_input(tc)
    run = subprocess.run("python code/run.py", shell=True)

    return get_output_files()


def runCode(que, code, language):
    TCs = Testcase.objects.filter(que=que).order_by('pk')
    TC_Status = []
    outputList = []
    for tc in TCs:
        output, err, rc = execute(code, tc, language)
        if rc != 0:
            TC_Status.append("RE")
        elif compare(output, tc):
            TC_Status.append("AC")
        else:
            TC_Status.append("WA")

    return TC_Status

def compare(output, tc):
    try:
        with open(tc.tc_output.path, "r") as correct_output:
            x = correct_output.read().strip()
            return output.strip() == x
    except:
        return False

def create_containers():
    for i in range(6):
        try:
            os.makedirs(f"containers/container_{i}/")
        except:
            pass
    for i in range(6):
        container_path = f"{os.getcwd()}\\containers\\container_{i}"
        subprocess.run(f"docker run --name container_{i} -v {container_path}:src\ python", shell=True)

def copy_run_py(language):
    src = "run.py"
    dst = f"code/run.py"
    shutil.copyfile(src, dst)
    file1 = open(dst, "a")  # append mode
    file1.write(f"\nrun_{language}()")
    file1.close()

def copy_code(code):
    file_path = "code/code.py"
    with open(file_path, 'w+') as file:
        file.write(code)
        file.close()

def copy_input(tc):
    dst = "code/input.txt"
    src = tc.tc_input.path
    shutil.copy(src, dst)

def get_output_files():
    output = open("code/output.txt").read()
    err = open("code/err.txt").read()
    rc = open("code/returnCode.txt").read()
    return output, err, int(rc)

#my
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
        



        
        
    





#dev

import subprocess,os
import time
codeRunnerPath = os.path.abspath("Code_Runner")
print(codeRunnerPath,"dddddddddddddddddddddkkkkkkkkkkkkkkkkkkkkkkkk")
def run_python():
    code_path = f"{codeRunnerPath}/code.py"
    tc_path = f"{codeRunnerPath}/input.txt"
    # x = open(tc_path,"r")
    # y = open(code_path,"r")
    # print(x.read(),y.read())
    er=open(f'{codeRunnerPath}/error.txt','w+')
    rc=open(f'{codeRunnerPath}/status.txt','w+')
    out=open(f'{codeRunnerPath}/output.txt','w+')
    # run = subprocess.run(f"python {code_path} <{tc_path}", text=True, shell=True, capture_output=True,timeout=1)
    st =time.time()
    try:
        run = subprocess.run(f"python {code_path} <{tc_path}", text=True, shell=True, capture_output=True,timeout=1)
    except subprocess.TimeoutExpired:
        print("enter in exept blockhhhhhhhhhhhhhhhhhhhkkhk")
    et = time.time()
    print("time foe execution  : ",et-st)
    
    # print(run)
    # print(run.stdout)
    # print(run.stderr)
    # print(run.returncode)
    
    out.write(run.stdout)
    er.write(run.stderr)
    rc.write(str(run.returncode))
    er.close()
    rc.close()
    out.close()

def run_cpp():
    code_path = f"{codeRunnerPath}/code.cpp"
    tc_path = f"{codeRunnerPath}/input.txt"
    # x = open(tc_path,"r")
    # y = open(code_path,"r")
    # print(x.read(),y.read())
    er=open(f'{codeRunnerPath}/error.txt','w+')
    rc=open(f'{codeRunnerPath}/status.txt','w+')
    out=open(f'{codeRunnerPath}/output.txt','w+')
    # run = subprocess.run(f"python {code_path} <{tc_path}", text=True, shell=True, capture_output=True)
    run = subprocess.run(['g++', '-o', f"{codeRunnerPath}/code", f"{code_path}"], capture_output=True, text=True)
    # print(run)
    if run.returncode != 0:
        rc.write(str(run.returncode))
        rc.close()
        er.write(run.stderr)
        er.close()
        print('Compilation failed. Errors written to errors.txt.')
    else:
        with open(f"{tc_path}", "r") as input_file:
            program_result = subprocess.run([f"{codeRunnerPath}/./code"],stdin=input_file, capture_output=True, text=True)
            out.write(program_result.stdout)
            er.write(program_result.stderr)
            rc.write(str(run.returncode))
            rc.close()
            er.close()
            out.close()



def run_c():
    code_path = f"{codeRunnerPath}/code.c"
    tc_path = f"{codeRunnerPath}/input.txt"
    # x = open(tc_path,"r")
    # y = open(code_path,"r")
    # print(x.read(),y.read())
    er=open(f'{codeRunnerPath}/error.txt','w+')
    rc=open(f'{codeRunnerPath}/status.txt','w+')
    out=open(f'{codeRunnerPath}/output.txt','w+')
    # run = subprocess.run(f"python {code_path} <{tc_path}", text=True, shell=True, capture_output=True)
    run = subprocess.run(['gcc', '-o', f"{codeRunnerPath}/code", f"{code_path}"], capture_output=True, text=True)
    # print(run)
    if run.returncode != 0:
        rc.write(str(run.returncode))
        rc.close()
        er.write(run.stderr)
        er.close()
        print('Compilation failed. Errors written to errors.txt.')
    else:
        with open(f"{tc_path}", "r") as input_file:
            program_result = subprocess.run([f"{codeRunnerPath}/./code "],stdin=input_file, capture_output=True, text=True)
            out.write(program_result.stdout)
            er.write(program_result.stderr)
            rc.write(str(run.returncode))
            rc.close()
            er.close()
            out.close()



