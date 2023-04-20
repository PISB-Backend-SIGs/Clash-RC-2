import subprocess,os
import time


codeRunnerPath = os.path.abspath("Code_Runner")
# codeRunnerPath="Clash_RC_2/Code_Runner"
runnerPath = os.path.dirname(__file__)
print(codeRunnerPath,"sssssssssssss",runnerPath)

def run_with_popen(language):
    # File path for coderunner
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
    
    # run = subprocess.Popen(cmd,stdin=tc_path,stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True,text=True)
    run = subprocess.Popen(cmd,stdin=tc_path,stderr=er,stdout=out,shell=True,text=True)
    run.wait()
    
    et = time.time()
    print("time foe execution  : ",et-st)
    
    # print(run)
    print(run.returncode)
    """ in popen if we piped stdin out then we not need to communicate op will save at specified place
        if not piped then use communicate"""
    
run_with_popen()