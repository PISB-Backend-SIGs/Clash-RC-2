import os
import subprocess
import signal,resource


codeRunnerPath = os.path.abspath("testsubprocess")
# codeRunnerPath="Clash_RC_2/Code_Runner"

#It will give current file path 
#And our other files are in same folder
FilePath = os.path.dirname(__file__)
# print("File Path ",FilePath)

#File in which users code is present
PythonFile = f"{FilePath}/code.py"
CppFile = f"{FilePath}/code.cpp"
CFile = f"{FilePath}/code.c"
#File in which ip testcase is present
# ip_file_path = f"{FilePath}/input.txt"
ip_file_path = open(f'{FilePath}/input.txt','r')
# open(f'{FilePath}/ip.txt','r')


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
    resource.setrlimit(resource.RLIMIT_CPU, (TimeoutLimit, TimeoutLimit))
    resource.setrlimit(resource.RLIMIT_AS, (MemoryLimit, MemoryLimit))

def execute_python_code():
    try:
        # set_time_limit(TimeoutLimit)

        process = subprocess.Popen(['python3', f'{PythonFile}'],stdin=ip_file_path,stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
            
        # # wait for the command to finish and get the stdout and stderr
        stdout, stderr = process.communicate()
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        # print("stout : ",stdout," stderr ",stderr)
        ListOfReturn =stderr.decode().strip().split()
        # try:
        #    ListOfReturn[1] = "<string>"
        #    print("after change listorerrors : ",ListOfReturn)
        # except:
        #     pass

        # print("list of errors : ",ListOfReturn)
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
                CopyReturnCode(stderr,ErrorCodes["TLE"])
                print("TLE")
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
    print("errrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    # print(err,"  fdsf  ",rcode)
    err.write(stderr.decode().strip())
    rcode.write(str(rCode))

def CopyOpFile(stdout,rCode):
    out=open(f'{FilePath}/output.txt','w+')
    rcode=open(f'{FilePath}/returncode.txt','w+')

    out.write(stdout.decode().strip())
    rcode.write(str(rCode))
    # rCode.write(rCode)

def RunByLang(lang):
    if (lang == "python"):
        process = subprocess.Popen(['python3', f'{PythonFile}'],stdin=ip_file_path,stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
        return process
    elif (lang == "cpp"):
        args = ['g++', '-o', f'{FilePath}/code', CppFile] # compile the file and generate an output executable
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
        print("llllllllllllllllllllllllllllllllllll")
        # print(process.returncode)
        output, error = process.communicate() # get the output and error messages
        # print(output,error)
        if not error:
            executable = f'{FilePath}/./code'
            process = subprocess.Popen(executable, stdin=ip_file_path,stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit,shell=False)
            output, error = process.communicate()
            print("llllllllllllllllllllllllllllllllllll")
            # print(process.returncode)
            return process
        else:
            return process
    
# test the function with a sample command


def execute_cpp_code():
    args = ['g++', '-o', f'{FilePath}/code', CppFile] # compile the file and generate an output executable

    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
    output, error = process.communicate()
    # error = process.stderr
    print("executable file ",error)

    if error:
        CopyReturnCode(error,ErrorCodes["CE"])
        print("Compile Error:")
        # print(error.decode('utf-8'))
    else:
        executable = f'{FilePath}/./code'
        try:
            process = subprocess.Popen(executable, stdin=ip_file_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=set_memory_limit,shell=False)
            # print(process.returncode)

            out, err = process.communicate(timeout=1) # timeout after 5 seconds
            # print("try block err : ",err.decode().split())
            print("try block err : ")
        except subprocess.TimeoutExpired:
            process.kill()    # terminate the process if it exceeds the timeout
            CopyReturnCode(err,ErrorCodes["TLE"])
            print("Time Limit Exceeded")
            exit()
        except subprocess.CalledProcessError:
            CopyReturnCode(err,ErrorCodes["MLE"])
            print("inside 3rd except : ")

        if err:
            CopyReturnCode(err,ErrorCodes["RE"])
            print("Runtime Error1:")
            # print(err.decode('utf-8'))
        elif process.returncode != 0:
            CopyReturnCode(err,ErrorCodes["TLE"])
            print("Runtime Error2: TLE ")
            # print(out.decode('utf-8'))
        else:
            print("outtttttttttttt ",out)
            CopyOpFile(out,ErrorCodes["AC"])
            print("AC CPP")
            # print(out.decode('utf-8'))




def execute_c_code():
    args = ['gcc', '-o', f'{FilePath}/ccode', CFile] # compile the file and generate an output executable

    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
    output, error = process.communicate()
    # error = process.stderr
    print("executable file ",error)

    if error:
        CopyReturnCode(error,ErrorCodes["CE"])
        print("Compile Error:")
        # print(error.decode('utf-8'))
    else:
        executable = f'{FilePath}/./ccode'
        try:
            process = subprocess.Popen(executable, stdin=ip_file_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=set_memory_limit,shell=False)
            # print(process.returncode)

            out, err = process.communicate(timeout=1) # timeout after 5 seconds
            # print("try block err : ",err.decode().split())
            print("try block err : ")
        except subprocess.TimeoutExpired:
            process.kill()    # terminate the process if it exceeds the timeout
            CopyReturnCode(err,ErrorCodes["TLE"])
            print("Time Limit Exceeded")
            exit()
        except subprocess.CalledProcessError:
            CopyReturnCode(err,ErrorCodes["MLE"])
            print("inside 3rd except : ")

        if err:
            CopyReturnCode(err,ErrorCodes["RE"])
            print("Runtime Error1:")
            # print(err.decode('utf-8'))
        elif process.returncode != 0:
            CopyReturnCode(err,ErrorCodes["TLE"])
            print("Runtime Error2: TLE ")
            # print(out.decode('utf-8'))
        else:
            print("outtttttttttttt ",out)
            CopyOpFile(out,ErrorCodes["AC"])
            print("AC CPP")
            # print(out.decode('utf-8'))







