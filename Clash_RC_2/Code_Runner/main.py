import subprocess,os
import time
# codeRunnerPath = os.path.abspath("Code_Runner")
# print(codeRunnerPath,"dddddddddddddddddddddkkkkkkkkkkkkkkkkkkkkkkkk")
codeRunnerPath = os.path.dirname(__file__)
print("File Path ",codeRunnerPath)
def run_with_run():
    code_path = f"{codeRunnerPath}/code.py"
    tc_path = f"{codeRunnerPath}/input.txt"
    # x = open(tc_path,"r")
    # y = open(code_path,"r")
    # print(x.read(),y.read())
    er=open(f'{codeRunnerPath}/error.txt','w+')
    rc=open(f'{codeRunnerPath}/returncode.txt','w+')
    out=open(f'{codeRunnerPath}/output.txt','w+')
    # run = subprocess.run(f"python {code_path} <{tc_path}", text=True, shell=True, capture_output=True,timeout=1)
    st =time.time()
    cmd =f"python3 {code_path} <{tc_path}"
    try:
        run = subprocess.run(cmd, text=True, shell=True, capture_output=True,timeout=1)
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

# run_with_run()


def run_with_popen():
    # File path for coderunner
    # code_path = f"{codeRunnerPath}/test.py"
    code_path = f"{codeRunnerPath}/code.py"
    # tc_path = f"{codeRunnerPath}/input.txt" 

    # Location for ip.txt file
    tc_path = open(f'{codeRunnerPath}/input.txt','r')

    #Locations for error output file
    er=open(f'{codeRunnerPath}/error.txt','w+')
    rc=open(f'{codeRunnerPath}/status.txt','w+')
    out=open(f'{codeRunnerPath}/output.txt','w+')
    
    st =time.time()
    cmd = f"python3 {code_path}"
    
    run = subprocess.Popen(cmd,stdin=tc_path,stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True,text=True)
    # run = subprocess.Popen(cmd,stdin=tc_path,stderr=er,stdout=out,shell=True,text=True)
    run.wait()
    
    et = time.time()
    print("time foe execution  : ",et-st)
    stdout , stderr = run.communicate()
    print("stdout : ",stdout,"\nstderr : ",stderr)
    print(stderr.encode())
    # print(run)
    print(run.returncode)

    """ in popen if we piped stdin out then we not need to communicate op will save at specified place
        if not piped then use communicate"""
    

run_with_popen()