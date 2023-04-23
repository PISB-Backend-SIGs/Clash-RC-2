# import subprocess
##1
# scripts_file_path = "testsubprocess/main/test.py"
# scripts_file_path = "main/test.py"
# cmd = f"python {scripts_file_path}"
# op = subprocess.run(cmd,shell=True,text=True,capture_output=True)
# print(op)
# # print(type(op.stdout))
# print(op.stderr)
# print(op.stdout)

# op = subprocess.call(cmd,shell=True,text=True)
# print(op)
# print(op.stdout)
# print(op.stderr)
# op = subprocess.check_call(cmd,shell=True,text=True,capture_output=True)



##2
# scripts_file_path = "./testsubprocess/main/test.py"
# ip_file_path = "./testsubprocess/main/ip.txt"
# cmd = f"python {scripts_file_path} <{ip_file_path}"
# op = subprocess.run(cmd,shell=True,text=True,capture_output=True)

# print(op)
# print(op.stdout)
# print(op.stderr)

##3
# scripts_file_path = "./testsubprocess/main/test.py"
# ip_file_path = "./testsubprocess/main/ip.txt"
# op_file_path = "./testsubprocess/main/op.txt"
# cmd = f"python {scripts_file_path} <{ip_file_path}"
# op = subprocess.run(cmd,shell=True,text=True,capture_output=True)

# # print(op)
# # print(op.stdout)
# # print(op.stderr)
# file_op = open(op_file_path,"w")
# file_op.write(op.stdout)
# file_op.close()

# ##4
# scripts_file_path = "./main/test.py"
# ip_file_path = "./main/ip.txt"
# op_file_path = "./main/op.txt"
# cmd = f"python {scripts_file_path} <{ip_file_path}"
# op = subprocess.run(cmd,shell=True,text=True,capture_output=True)

# print(op)
# print(op.stdout)
# print(op.stderr)
# file_op = open(op_file_path,"w")
# file_op.write(op.stdout)
# file_op.close()

##5

# import signal
# def run_code_snippet(code, time_limit):
    
#     # Define a signal handler to terminate the process when the time limit is reached
#     def timeout_handler(signum, frame):
#         raise TimeoutError('Time limit exceeded')

#     # Set a signal handler for the SIGALRM signal
#     signal.signal(signal.SIGALRM, timeout_handler)

#     # Start a timer to measure the elapsed time
#     signal.setitimer(signal.ITIMER_REAL, time_limit)

#     try:
#         # Execute the code snippet as a subprocess
#         subprocess.run(['python', '-c', code], check=True)
#     except subprocess.TimeoutExpired:
#         # The process timed out, so raise a TimeoutError
#         raise TimeoutError('Time limit exceeded')
#     finally:
#         # Stop the timer
#         signal.setitimer(signal.ITIMER_REAL, 0)

# code = "while True: pass"
# time_limit = 1  # Time limit is 1 second

# try:
#     run_code_snippet(code, time_limit)
# except TimeoutError:
#     print('Time limit exceeded')



# # ###6
# import subprocess
# import resource,os,signal
# codeRunnerPath = os.path.abspath("testsubprocess")
# # codeRunnerPath="Clash_RC_2/Code_Runner"
# FilePath = os.path.dirname(__file__)
# print(codeRunnerPath,"sssssssssssss",FilePath)


# # set the CPU time limit to 1 second
# resource.setrlimit(resource.RLIMIT_CPU, (1, 1))


# # set the memory limit to 10 MB
# resource.setrlimit(resource.RLIMIT_AS, (1 * 1024 * 1024, 1 * 1024 * 1024))

# # execute the user's code
# scripts_file_path = f"{FilePath}/test.py"
# ip_file_path = f"{FilePath}/ip.txt"
# with open(ip_file_path, 'r') as f:
#     ip_contents = f.read()

# op_file_path = f"{FilePath}/op.txt"




# process = subprocess.Popen(['python3', f'{scripts_file_path}'],stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# process.communicate(input=ip_contents.encode())

# # print(op)
# # print(op.stdout)
# # print(op.stderr)
# # file_op = open(op_file_path,"w")
# # file_op.write(process.stdout)
# # file_op.close()
# # process = subprocess.Popen(['python', 'user_code.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  #by gpt

# # wait for the process to finish
# try:
#     stdout, stderr = process.communicate(timeout=1)
# except subprocess.TimeoutExpired:
#     # process exceeded the CPU time limit
#     process.kill()
#     print('TLE')
#     exit()

# # check the maximum memory usage of the process
# usage = resource.getrusage(resource.RUSAGE_CHILDREN)
# memory_usage = usage.ru_maxrss * 1024
# if memory_usage > 1 * 1024 * 1024:
#     # process exceeded the memory limit
#     print('MLE')
#     print(stderr.decode())
#     print(process.returncode)
#     exit()

# # check the stderr for any other errors
# if stderr:
#     print(stderr.decode())
#     print(process.returncode)
#     exit()

# # print the stdout if everything is okay
# print(stdout.decode())
# print(process.returncode)




###7
# import subprocess
# import signal,os
# resource_limits = {
#     'memory': 256000,  # 100 MB
#     'time': 1,  # 1 second
# }
# # set the timeout limit to 1 second
# # timeout = 1

# # define a function to handle the timeout
# def handle_timeout(signum, frame):
#     raise TimeoutError

# # execute the user's code
# codeRunnerPath = os.path.abspath("testsubprocess")
# # codeRunnerPath="Clash_RC_2/Code_Runner"
# FilePath = os.path.dirname(__file__)
# print(codeRunnerPath,"sssssssssssss",FilePath)

# scripts_file_path = f"{FilePath}/test.py"
# ip_file_path = f"{FilePath}/ip.txt"
# with open(ip_file_path, 'r') as f:
#     ip_contents = f.read()

# op_file_path = f"{FilePath}/op.txt"
# process = subprocess.Popen(['python3', f'{scripts_file_path}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# # set the signal handler for the timeout
# signal.signal(signal.SIGALRM, handle_timeout)
# signal.alarm(resource_limits["time"])

# # wait for the process to finish
# try:
#     stdout, stderr = process.communicate()
#     signal.alarm(0)
# except TimeoutError:
#     # process exceeded the timeout limit
#     process.kill()
#     print('TLE')
#     exit()
# print(stdout,stderr)
# # check the stderr for any other errors
# if stderr:
#     print(stderr.decode())
#     exit()

# # print the stdout if everything is okay
# print("sss",stdout.decode())




import os
codeRunnerPath = os.path.abspath("testsubprocess")
# codeRunnerPath="Clash_RC_2/Code_Runner"

#It will give current file path 
#And our other files are in same folder
FilePath = os.path.dirname(__file__)
print("File Path ",FilePath)

#File in which users code is present
scripts_file_path = f"{FilePath}/test.py"
#File in which ip testcase is present
tc_path = open(f'{FilePath}/ip.txt','r')
# with open(ip_file_path, 'r') as f:
#     ip_contents = f.read()

op_file_path = open(f"{FilePath}/op.txt","w+")

####8
import subprocess
import signal,resource

ceErrors = [ "SyntaxError:","NameError:","TypeError:","ImportError:","IndentationError:","LogicError:"]
reErrors = ["ZeroDivisionError:","IndexError:","KeyError:","AttributeError:","ValueError:","RuntimeError","StopIteration","RecursionError","OSError"]
#"MemoryError"

# # define a timeout limit for the user's code
TimeoutLimit = 1
def set_time_limit(time_limit):
    def signal_handler(signum, frame):
        raise TimeoutError
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(TimeoutLimit)

# signal.signal(signal.SIGALRM, handle_timeout)
# signal.alarm(timeout_limit)


# # define a function to handle timeouts
# def handle_timeout(signum, frame):
#     raise TimeoutError
import time
MemoryLimit = 256 * 1024 * 1024   #on 17 mle
def set_memory_limit():
    resource.setrlimit(resource.RLIMIT_CPU, (TimeoutLimit, TimeoutLimit))
    # resource.setrlimit(resource.RLIMIT_AS, (MemoryLimit, MemoryLimit))
    resource.setrlimit(resource.RLIMIT_AS, (MemoryLimit, MemoryLimit))
# define a function to execute the user's code and detect errors

def RunByLang():
    # process = subprocess.Popen(command,stdin=tc_path,stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
    process = subprocess.Popen(['g++', '-o', f"{FilePath}/code", f"{FilePath}/test.cpp"], capture_output=True, text=True)
    return process
   


def execute_user_code(command):
    try:
        # set_time_limit(TimeoutLimit)
        process = subprocess.Popen(command,stdin=tc_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
        # process = RunByLang()
        # process2 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit)
            
        #Cpp 
        # process = subprocess.Popen(['g++', '-o', f"{FilePath}/code", f"{FilePath}/test.cpp"],stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit )
        # print(process)
        # process = subprocess.Popen([f"{FilePath}/./code"],stdin=tc_path,stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=set_memory_limit )
        # print(process)
        # # wait for the command to finish and get the stdout and stderr
        stdout, stderr = process.communicate()
        print("\nstdeerr : ",stderr )
        op_file_path.write(stdout.decode().strip())
        # stdout2, stderr2 = process2.communicate()
        # print(stderr2,stdout2)
        # print(stderr.decode())
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
                print(process.returncode)
                return "TLE"

            # print(process.returncode)
            # print(stderr.decode())
            # print(stdout.decode())
            # print(ZeroDivisionError in str(stderr.decode()))
            # print(str(stderr.decode()).split())
            # print( "SyntaxError:" in str(stderr.decode()).split())
            # print( "ZeroDivisionError:" in str(stderr.decode()).split())
            # # print((stderr).find("ZeroDivisionError"))
            # s =list((stderr.decode().strip()).split())
            # # s[s.index("File")] = "ddddd"
            # print("index ",s)
            # return "CE"
        else:
            if (process.returncode == 0):
                print("ac")
                return 
            else:
                return "WA"
            
            # no errors detected, return the output
            # print(stdout)
            # print(stdout.decode())
            # print(stdout.decode().strip())
            # print(process.returncode)
            # print(ZeroDivisionError in str(stderr.decode()))
            # return stdout.decode().strip()
    
    except TimeoutError:
        # handle timeout error
        process.kill()
        stdout, stderr = process.communicate()
        CopyFilesToTxt(stdout,stderr)

        # stderr = process.stderr.read()
        ListOfReturn =stderr.decode().strip().split()
        print(ListOfReturn)
        # s[s.index("File")] = "ddddd"
        # print("index ",ListOfReturn)
        # print("inside 1timeout ",str(stderr.decode()).split())
        if ("MemoryError" in ListOfReturn):
            print("present MLE")
            return "MLE"
        
        return "TLE"

def CopyFilesToTxt(stdout,stderr):
    er=open(f'{FilePath}/error.txt','w+')
    out=open(f'{FilePath}/output.txt','w+')

    out.write(stdout.decode().strip())
    er.write(stderr.decode().strip())

# test the function with a sample command
command = ['python3', f'{scripts_file_path}']
result = execute_user_code(command)
print("result   ",result)

 
# starting the monitoring


# import subprocess
# import resource
# import signal
ErrorCodes={
  "AC": 0, 
  "WA": 1, 
  "MLE":2, 
  "TLE":3, 
  "CE": 4, 
  "RE": 5, 
}

# Define a function to set memory limit for the subprocess
# def set_memory_limit(memory_limit):
#     soft_limit = hard_limit = memory_limit
#     resource.setrlimit(resource.RLIMIT_AS, (soft_limit, hard_limit))

# # Define a function to set time limit for the subprocess
# time_limit = 1
# def set_time_limit(time_limit):
#     def signal_handler(signum, frame):
#         raise TimeoutError
#         # raise TimeoutError("Subprocess exceeded time limit")
#     signal.signal(signal.SIGALRM, signal_handler)
#     signal.alarm(time_limit)


# MEM_LIMIT = 2 * 1024 * 1024  # 256 mb
# # TIME_LIMIT = 10  # 1 s


# # Define a function to run the subprocess with memory and time limits
# def run_subprocess_with_limits(command):
#     # set_memory_limit(memory_limit)
#     # set_time_limit(TIME_LIMIT)
#     try:
#         result = subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,preexec_fn=resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit)))
#         # result = subprocess.run(command,preexec_fn=set_limit_resource)
#         # op ,er = result.communicate()
#         result.wait()
#     except TimeoutError:
#         print("timeout")
#     except Exception as e:
#         print("dasdas")
#     # except TimeoutError as e:
#     #     print("timeout",e,result.returncode)
#     #     signal.alarm(0)
#     # except subprocess.CalledProcessError as e:
#     #     print("error",e.returncode)
#     # else:
#     #     print("code ",result.returncode)
#     #     print("op",op)
#     #     print("ercod",er)


# run_subprocess_with_limits(['python3', f'{scripts_file_path}'])
# # run_subprocess_with_limits(['python3', f'{scripts_file_path}'], memory_limit=1*1024*1024, time_limit=2)











# import subprocess,os
# codeRunnerPath = os.path.abspath("testsubprocess")
# # codeRunnerPath="Clash_RC_2/Code_Runner"
# FilePath = os.path.dirname(__file__)
# print(codeRunnerPath,"sssssssssssss",FilePath)

# scripts_file_path = f"{FilePath}/test.py"
# ip_file_path = f"{FilePath}/ip.txt"
# with open(ip_file_path, 'r') as f:
#     ip_contents = f.read()

# op_file_path = f"{FilePath}/op.txt"

# # set resource limits
# resource_limits = {
#     'memory': 1000,  # 100 MB
#     'cpu': 1,  # 1 second
# }

# # command to run the user's code
# command = ['python3', f'{scripts_file_path}']

# # run the command as a subprocess and capture its output and error messages
# result = subprocess.run(
#     command,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     timeout=resource_limits['cpu'],
#     check=False,
#     shell=False,
#     env=None,
#     cwd=None,
#     start_new_session=True,
#     preexec_fn=None,
#     close_fds=True,
#     text=True,
#     universal_newlines=True
# )
# print(result)
# # check if the error message contains MLE error
# if 'MemoryError' in result.stderr:
#     print('MLE error')
# else:
#     print(result.stdout)
