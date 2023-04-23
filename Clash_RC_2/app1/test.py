import uuid


# t =uuid.uuid4
# print(t)
# uuid.uuid4()
# s=0
# if (!s):
    # pr/int("hello")

# if not(False):
#     print("Hello")



# import subprocess
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
#         subprocess.run(['python3', '-c', code], check=True)
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


import subprocess
import signal,time

def run_code_snippet(code, time_limit):
    # Define a signal handler to terminate the process when the time limit is reached
    def timeout_handler(signum, frame):
        raise TimeoutError('Time limit exceeded1')

    # Set a signal handler for the SIGALRM signal
    signal.signal(signal.SIGALRM, timeout_handler)

    # Start a timer to measure the elapsed time
    signal.setitimer(signal.ITIMER_REAL, time_limit)

    try:
        # Execute the code snippet as a subprocess
        subprocess.run(['python3', '-c', code], check=True, timeout=time_limit)
    except subprocess.TimeoutExpired:
        # The process timed out, so raise a TimeoutError
        raise TimeoutError('Time limit exceeded2')
    finally:
        # Stop the timer
        signal.setitimer(signal.ITIMER_REAL, 0)

# Example usage
code = '''
while(1):
    print("hello")
'''
time_limit = 1  # Time limit is 3 seconds
st =time.time()
try:
    run_code_snippet(code, time_limit)
except TimeoutError:
    print('Time limit exceeded3')
    # print()
et =time.time()
print(et-st)

# import subprocess
# import signal

# def run_code_snippet(code, time_limit):
#     # Define a signal handler to terminate the process when the time limit is reached
#     def timeout_handler(signum, frame):
#         raise TimeoutError('Time limit exceeded')

#     # Set a signal handler for the SIGTERM signal
#     signal.signal(signal.SIGTERM, timeout_handler)

#     # Start a timer to measure the elapsed time
#     signal.alarm(time_limit)

#     try:
#         # Execute the code snippet as a subprocess
#         d=subprocess.run(['python3', '-c', code], check=True)
#     except subprocess.TimeoutExpired:
#         # The process timed out, so raise a TimeoutError
#         raise TimeoutError('Time limit exceeded')
#     finally:
#         # Stop the timer
#         signal.alarm(0)

# # Example usage
# code = '''
# import time
# time.sleep(5)
# '''
# time_limit = 1  # Time limit is 3 seconds

# try:
#     run_code_snippet(code, time_limit)
# except TimeoutError:
#     print('Time limit exceeded')



# import subprocess
# import resource

# def run_with_limits(command, cpu_limit, memory_limit):
#     # Set CPU time limit (in seconds)
#     resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit, cpu_limit))
    
#     # Set memory limit (in bytes)
#     resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit))
    
#     # Start the subprocess
#     process = subprocess.Popen(['python3','-c',f'{command}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
#     # Wait for the subprocess to finish
#     stdout, stderr = process.communicate()
    
#     # Return the stdout and stderr
#     return stdout, stderr ,process.returncode
# # # Example usage
# code = '''
# import time
# time.sleep(2)
# print("helo")
# '''
# time_limit = 1  # Time limit is 3 seconds
# memory_limit = 256 * 1024 * 1024
# # code = ["python3",f"{code}"]
# try:
#     r,l,s=run_with_limits(code, time_limit,memory_limit)
#     print(r,l,s)
# except TimeoutError:
#     print('Time limit exceeded')

