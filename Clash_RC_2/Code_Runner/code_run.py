import os
import subprocess
import signal,resource


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


ErrorCodes={
  "AC": 0, 
  "WA": 1, 
  "MLE":2, 
  "TLE":3, 
  "CE": 4, 
  "RE": 5, 
}

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
        ListOfReturn =stderr.decode().strip().split()
        print(ListOfReturn)
        # signal.alarm(0)

        # check for any errors in stderr
        if process.returncode != 0:
            process.kill()
            if any(error in ListOfReturn for error in ceErrors):
                CopyReturnCode(stderr,ErrorCodes["CE"])
                print("CE")
                # return "CE"
            elif any(error in ListOfReturn for error in reErrors):
                CopyReturnCode(stderr,ErrorCodes["RE"])
                print("RE")
                # return "RE"
            elif "MemoryError" in ListOfReturn:
                CopyReturnCode(stderr,ErrorCodes["MLE"])
                print("MLE")
                # return "MLE"
            else:
                CopyReturnCode(stderr,ErrorCodes["WA"])
                print("WA")
                # return "WA"
        else:
            if (process.returncode == 0):
                CopyOpFile(stdout,ErrorCodes["AC"])
                print("AC")
                # return "AC"
            else:
                CopyReturnCode(stderr,ErrorCodes["WA"])
                print("WA")
                # return "WA"    
    except TimeoutError:
        # handle timeout error
        process.kill()
        stdout, stderr = process.communicate()
        CopyOpFile(stdout,stderr)

        # stderr = process.stderr.read()
        ListOfReturn =stderr.decode().strip().split()
        # s[s.index("File")] = "ddddd"
        # print("index ",ListOfReturn)
        # print("inside 1timeout ",str(stderr.decode()).split())
        if ("MemoryError" in ListOfReturn):
            CopyReturnCode(stderr,ErrorCodes["MLE"])
            print("MLE")
            # return "MLE"
        else:
            CopyReturnCode(stderr,ErrorCodes["TLE"])
            print("TLE")
            # return "TLE"

def CopyReturnCode(stderr,rCode):
    err=open(f'{FilePath}/error.txt','w+')
    rcode=open(f'{FilePath}/returncode.txt','w+')
    err.write(stderr.decode().strip())
    rcode.write(rCode)

def CopyOpFile(stdout,rCode):
    out=open(f'{FilePath}/output.txt','w+')
    rcode=open(f'{FilePath}/returncode.txt','w+')

    out.write(stdout.decode().strip())
    rcode.write(rCode)
    # rCode.write(rCode)

def RunByLang(lang):
    if (lang == "py"):
        process = subprocess.Popen(['python3', f'{PythonFile}'],stdin=ip_contents,stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
        return process
    elif (lang == "cpp"):
        process = subprocess.Popen(['g++', '-o', f"{FilePath}/code", f"{CppFile}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit )
        if (process.returncode != 0):
            return process
        process = subprocess.Popen([f"{FilePath}/./code"],stdin=ip_contents,stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit )
        return process
    
# test the function with a sample command









run_python()