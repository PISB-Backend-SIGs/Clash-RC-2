import subprocess
import shutil
import os
from . models import Question, Testcase
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