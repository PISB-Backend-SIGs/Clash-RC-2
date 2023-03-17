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
#         subprocess.run(['python', '-c', code], check=True, timeout=time_limit)
#     except subprocess.TimeoutExpired:
#         # The process timed out, so raise a TimeoutError
#         raise TimeoutError('Time limit exceeded')
#     finally:
#         # Stop the timer
#         signal.setitimer(signal.ITIMER_REAL, 0)

# # Example usage
# code = '''
# import time
# time.sleep(5)
# '''
# time_limit = 3  # Time limit is 3 seconds

# try:
#     run_code_snippet(code, time_limit)
# except TimeoutError:
#     print('Time limit exceeded')


import subprocess
import signal

def run_code_snippet(code, time_limit):
    # Define a signal handler to terminate the process when the time limit is reached
    def timeout_handler(signum, frame):
        raise TimeoutError('Time limit exceeded')

    # Set a signal handler for the SIGTERM signal
    signal.signal(signal.SIGTERM, timeout_handler)

    # Start a timer to measure the elapsed time
    signal.alarm(time_limit)

    try:
        # Execute the code snippet as a subprocess
        subprocess.run(['python', '-c', code], check=True)
    except subprocess.TimeoutExpired:
        # The process timed out, so raise a TimeoutError
        raise TimeoutError('Time limit exceeded')
    finally:
        # Stop the timer
        signal.alarm(0)

# Example usage
code = '''
import time
time.sleep(5)
'''
time_limit = 3  # Time limit is 3 seconds

try:
    run_code_snippet(code, time_limit)
except TimeoutError:
    print('Time limit exceeded')

