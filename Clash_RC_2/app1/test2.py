# import os,pathlib,subprocess

# # from django.conf import settings
# # crnt_dir = os.getcwd()
# codeRunnerPath = "Clash_RC_2/Code_Runner"
# # directory = pathlib.Path().cwd()
# # directory = os.path.join(settings.BASE_DIR,crnt_path)
# # print(directory)
# path_fol = os.path.dirname(__file__)
# print(path_fol)         #working


# # print(os.path.dirname(path_fol))   #same
# cn_path = os.path.join(path_fol,codeRunnerPath)
# print(cn_path)


# dire = os.path.abspath(codeRunnerPath)
# print(dire)



import subprocess
import signal,time,os

codeRunnerPath = os.path.abspath("testsubprocess")
# codeRunnerPath="Clash_RC_2/Code_Runner"
runnerPath = os.path.dirname(__file__)
print(codeRunnerPath,"sssssssssssss",runnerPath)

scripts_file_path = f"{runnerPath}/test.py"
ip_file_path = f"{runnerPath}/ip.txt"
with open(ip_file_path, 'r') as f:
    ip_contents = f.read()

op_file_path = f"{runnerPath}/op.txt"

time_limit = 1
memory_limit = 256*1024*1024

def run_code_snippet(code):
    # Define a signal handler to terminate the process when the time limit is reached
    def timeout_handler(signum, frame):
        return TimeoutError('Time limit exceeded1')

    # Set a signal handler for the SIGALRM signal
    signal.signal(signal.SIGALRM, timeout_handler)

    # Start a timer to measure the elapsed time
    signal.setitimer(signal.ITIMER_REAL, time_limit)

    try:
        # Execute the code snippet as a subprocess
        subprocess.run(['python3', '-c', code], check=True, timeout=time_limit)
    except subprocess.TimeoutExpired:
        # The process timed out, so raise a TimeoutError
        return TimeoutError('Time limit exceeded2')
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