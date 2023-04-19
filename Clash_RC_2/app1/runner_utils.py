import subprocess
import shutil
import os
from .models import Question, Testcases
from subprocess import STDOUT, check_output
# from celery import shared_task

def execute(code, tc, language):
    copy_run_py(language)
    copy_code(code,language)
    copy_input(tc)
    run = subprocess.run("docker exec test_container python3 src/code_run.py", shell=True)

    return get_output_files()



def runCode(que_num, code, language,btn_click_status,user_test):             #btn_click_status true = submit and false = run
    TC_Status = []
    # print("fffffffffff",user_test)
    if (btn_click_status==0):
        output, err, rc = execute_run(code, user_test, language)
        if int(rc) !=0:
            TC_Status.append(err)
        else:
            TC_Status.append(output)
        return TC_Status
    
    TCs = Testcases.objects.filter(q_id=que_num).order_by('t_id')
    # print("TEst casesinside runcode ",TCs)
    outputList = []
    for tc in TCs:
        
        output, err, rc = execute(code, tc, language)
        # print("op",output,"err",err,"status",rc,"value of compare",compare(output, tc))
        if int(rc) != 0:
            TC_Status.append("RE")
        elif compare(output, tc):
            TC_Status.append("AC")
        else:
            TC_Status.append("WA")
    print("see list of status ",TC_Status)
    return TC_Status

def compare(output, tc):
    try:
        with open(tc.t_op.path, "r") as correct_output:
            x = correct_output.read().strip()
            # print("actual : ",x,"user : ",output)
            return output.strip() == x
    except:
        return False


def copy_run_py(language):
    src = "app1/runner.py"
    dst = f"Code_Runner/code_run.py"
    shutil.copyfile(src, dst)
    file1 = open(dst, "a")  # append mode
    file1.write(f"\nrun_{language}()")
    file1.close()

def copy_code(code,language):
    if (language=="python"):
        file_path = f"Code_Runner/code.py"
    elif (language=="cpp"):
        file_path = f"Code_Runner/code.cpp"
    elif (language=="c"):
        file_path = f"Code_Runner/code.c"
    with open(file_path, 'w+') as file:
        file.write(code)
        file.close()

def copy_input(tc):
    dst = "Code_Runner/input.txt"
    src = tc.t_ip.path
    shutil.copy(src, dst)

def get_output_files():
    output = open("Code_Runner/output.txt").read()
    err = open("Code_Runner/error.txt").read()
    rc = open("Code_Runner/status.txt").read()
    # print("ddddddddddd",rc,"type ",type(rc))
    return output, err, rc


#when run clicke
def copy_test_input(tc):
    # print("dfddddddddd",tc)
    dst = open("Code_Runner/input.txt","w")
    dst.write(tc)
    dst.close()

def execute_run(code, tc, language):
    copy_run_py(language)
    copy_code(code,language)
    copy_test_input(tc)
    run = subprocess.run("python Code_Runner/code_run.py", shell=True)

    return get_output_files()