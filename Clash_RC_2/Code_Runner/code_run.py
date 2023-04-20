"""currently we are not using this insted of this we are using codeRun.py"""

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




run_python()