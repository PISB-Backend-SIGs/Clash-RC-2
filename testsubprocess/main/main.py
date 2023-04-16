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
# runnerPath = os.path.dirname(__file__)
# print(codeRunnerPath,"sssssssssssss",runnerPath)


# # set the CPU time limit to 1 second
# resource.setrlimit(resource.RLIMIT_CPU, (1, 1))


# # set the memory limit to 10 MB
# resource.setrlimit(resource.RLIMIT_AS, (1 * 1024 * 1024, 1 * 1024 * 1024))

# # execute the user's code
# scripts_file_path = f"{runnerPath}/test.py"
# ip_file_path = f"{runnerPath}/ip.txt"
# with open(ip_file_path, 'r') as f:
#     ip_contents = f.read()

# op_file_path = f"{runnerPath}/op.txt"




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

# # set the timeout limit to 1 second
# timeout = 1

# # define a function to handle the timeout
# def handle_timeout(signum, frame):
#     raise TimeoutError

# # execute the user's code
# codeRunnerPath = os.path.abspath("testsubprocess")
# # codeRunnerPath="Clash_RC_2/Code_Runner"
# runnerPath = os.path.dirname(__file__)
# print(codeRunnerPath,"sssssssssssss",runnerPath)

# scripts_file_path = f"{runnerPath}/test.py"
# ip_file_path = f"{runnerPath}/ip.txt"
# with open(ip_file_path, 'r') as f:
#     ip_contents = f.read()

# op_file_path = f"{runnerPath}/op.txt"
# process = subprocess.Popen(['python3', f'{scripts_file_path}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# # set the signal handler for the timeout
# signal.signal(signal.SIGALRM, handle_timeout)
# signal.alarm(timeout)

# # wait for the process to finish
# try:
#     stdout, stderr = process.communicate()
#     signal.alarm(0)
# except TimeoutError:
#     # process exceeded the timeout limit
#     process.kill()
#     print('TLE')
#     exit()

# # check the stderr for any other errors
# if stderr:
#     print(stderr.decode())
#     exit()

# # print the stdout if everything is okay
# print(stdout.decode())





####8
import subprocess
import signal,resource
import psutil,re
import os
# set resource limits
resource_limits = {
    'memory': 10000,  # 100 MB
    'cpu': 1,  # 1 second
}

codeRunnerPath = os.path.abspath("testsubprocess")
# codeRunnerPath="Clash_RC_2/Code_Runner"
runnerPath = os.path.dirname(__file__)
print(codeRunnerPath,"sssssssssssss",runnerPath)

scripts_file_path = f"{runnerPath}/test.py"
ip_file_path = f"{runnerPath}/ip.txt"
with open(ip_file_path, 'r') as f:
    ip_contents = f.read()

op_file_path = f"{runnerPath}/op.txt"
# define a timeout limit for the user's code
timeout_limit = 5

# define a function to handle timeouts
def handle_timeout(signum, frame):
    raise TimeoutError

# define a function to execute the user's code and detect errors
def execute_user_code(command):
    try:
        # execute the command and get stdout and stderr
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pid = process.pid
        print(pid)
        # process.wait()
        # stdout, stderr = process.communicate()
        process_memory_usage = psutil.Process(pid).memory_info().rss
    
        
        # set a timer for the command execution
        signal.signal(signal.SIGALRM, handle_timeout)
        signal.alarm(timeout_limit)

        # wait for the command to finish and get the stdout and stderr
        stdout, stderr = process.communicate()
        signal.alarm(0)

        # check for any errors in stderr

        # process_memory_usage = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss 
        print(process_memory_usage,"mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        # check if the memory usage exceeds the limit
        if process_memory_usage > resource_limits['memory']:
            # kill the subprocess if it exceeds the memory limit
            print(process.returncode)
            process.kill()
            print('MLE error')
        if process.returncode != 0:
            return "CE"
        else:
            # no errors detected, return the output
            return stdout.decode().strip()

    except TimeoutError:
        # handle timeout error
        process.kill()
        return "TLE"


# test the function with a sample command
command = ['python3', f'{scripts_file_path}']
result = execute_user_code(command)
print("result   ",result)












# import subprocess,os
# codeRunnerPath = os.path.abspath("testsubprocess")
# # codeRunnerPath="Clash_RC_2/Code_Runner"
# runnerPath = os.path.dirname(__file__)
# print(codeRunnerPath,"sssssssssssss",runnerPath)

# scripts_file_path = f"{runnerPath}/test.py"
# ip_file_path = f"{runnerPath}/ip.txt"
# with open(ip_file_path, 'r') as f:
#     ip_contents = f.read()

# op_file_path = f"{runnerPath}/op.txt"

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
