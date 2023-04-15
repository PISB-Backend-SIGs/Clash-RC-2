import subprocess
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
scripts_file_path = "./main/test.py"
ip_file_path = "./main/ip.txt"
op_file_path = "./main/op.txt"
cmd = f"python {scripts_file_path} <{ip_file_path}"
op = subprocess.run(cmd,shell=True,text=True,capture_output=True)

print(op)
print(op.stdout)
print(op.stderr)
file_op = open(op_file_path,"w")
file_op.write(op.stdout)
file_op.close()

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

