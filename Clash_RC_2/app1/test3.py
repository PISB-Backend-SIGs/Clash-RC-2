import os
codeRunnerPath = os.path.abspath("testsubprocess")
# codeRunnerPath="Clash_RC_2/Code_Runner"

#It will give current file path 
#And our other files are in same folder
FilePath = os.path.dirname(__file__)
print("File Path ",FilePath)

#File in which users code is present
PythonFile = f"{FilePath}/code.py"
CppFile = f"{FilePath}/code.cpp"
CFile = f"{FilePath}/code.c"
#File in which ip testcase is present
ip_file_path = f"{FilePath}/input.txt"
with open(ip_file_path, 'r') as f:
    ip_contents = f.read()

import subprocess
import signal,resource
import psutil,re

ceErrors = [ "SyntaxError:","NameError:","TypeError:","ImportError:","IndentationError:","LogicError:"]
reErrors = ["ZeroDivisionError:","IndexError:","KeyError:","AttributeError:","ValueError:","RuntimeError","StopIteration","RecursionError","OSError"]
#"MemoryError"

#Timeout Signal
TimeoutLimit = 1
def set_time_limit(time_limit):
    def signal_handler(signum, frame):
        raise TimeoutError
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(TimeoutLimit)

MemoryLimit = 256 * 1024 * 1024   
def set_memory_limit():
    # resource.setrlimit(resource.RLIMIT_CPU, (TimeoutLimit, TimeoutLimit))
    resource.setrlimit(resource.RLIMIT_AS, (MemoryLimit, MemoryLimit))

def execute_user_code(lang):
    try:
        set_time_limit(TimeoutLimit)

        process = RunByLang(lang)
            
        # # wait for the command to finish and get the stdout and stderr
        stdout, stderr = process.communicate()
        CopyFilesToTxt(stdout,stderr)
        ListOfReturn =stderr.decode().strip().split()
        print(ListOfReturn)
        # signal.alarm(0)

        # check for any errors in stderr
        if process.returncode != 0:
            process.kill()
            if any(error in ListOfReturn for error in ceErrors):
                return "CE"
            elif any(error in ListOfReturn for error in reErrors):
                return "RE"
            elif "MemoryError" in ListOfReturn:
                return "MLE"
            else:
                return "WA"
        else:
            if (process.returncode == 0):
                return "AC"
            else:
                return "WA"    
    except TimeoutError:
        # handle timeout error
        process.kill()
        stdout, stderr = process.communicate()
        CopyFilesToTxt(stdout,stderr)

        # stderr = process.stderr.read()
        ListOfReturn =stderr.decode().strip().split()
        # s[s.index("File")] = "ddddd"
        # print("index ",ListOfReturn)
        # print("inside 1timeout ",str(stderr.decode()).split())
        if ("MemoryError" in ListOfReturn):
            print("present MLE")
            return "MLE"
        
        return "TLE"

def CopyFilesToTxt(stdout,stderr,rCode):
    err=open(f'{FilePath}/error.txt','w+')
    out=open(f'{FilePath}/output.txt','w+')
    # rCode=open(f'{FilePath}/status.txt','w+')

    out.write(stdout.decode().strip())
    err.write(stderr.decode().strip())
    # rCode.write(rCode)

def RunByLang(lang):
    if (lang == "py"):
        process = subprocess.Popen(['python3', f'{PythonFile}'],stdin=ip_contents,stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
        return process
    elif (lang == "cpp"):
        process = subprocess.Popen(['g++', '-o', f"{FilePath}/code", f"{CppFile}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit )
        if (process.returncode != 0):
            return process
        process = subprocess.Popen([f"{FilePath}/./code"],stdin=tc_path,stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit )
        return process
    
# test the function with a sample command
command = ['python3', f'{PythonFile}']
result = execute_user_code(command)
print("result   ",result)