##1
# print("hello world")

##2
# for i in range(int(input())):
#     print("i =",i,"sum =",i+10)

##3
# for i in range(int(input())):
#     print("i =",i,"sum =",i+10)


##4
# def count_vowels(s):

#     count = 0

#     for char in s:

#         if char.lower() in ['a', 'e', 'i', 'o', 'u']:

#             count += 1

#     print(count)

# count_vowels(input())



###6
# import signal
# timeout_limit = 1
# import time,resource,os,subprocess
# def set_time_limit(time_limit):
#     def signal_handler(signum, frame):
#         raise TimeoutError
#     signal.signal(signal.SIGALRM, signal_handler)
#     signal.alarm(timeout_limit)
# # tracemalloc.start()
# set_time_limit(timeout_limit)

# MEM_LIMIT = 256*1024*1024
# def set_memory_limit():
#     resource.setrlimit(resource.RLIMIT_CPU, (timeout_limit, timeout_limit))
#     resource.setrlimit(resource.RLIMIT_AS, (MEM_LIMIT, MEM_LIMIT))

# code="while(1):\n\tprint('hello')"

# st = time.time()
# p = subprocess.run(f"python3 {code}",shell=True,text=True,preexec_fn=set_memory_limit)
# et = time.time()
# print("timessssssssssssssssssssssssssssssssss ",et-st)
# print(p)


# # # import resource
# print("dffffffffffffffffffff")
# print(6/0)

#runtime err
# print(n)

# list = [2]
# print(list[1])
# print("dddddddddddd")




#value rer
# s = int("val")

#keyerr
# dict={"d":2}
# print(dict["s"])
# s="dfsdfs"
# i = input()
# print(i)
# displaying the memory
#  (current, peak),

while(1):
    print("Dd")
# t=10000000000000000000000000000000000000000000000
# while(t>0):
#     print(t)
#     t -=1

# while(True):
#     print("ff") 

#type error
# my_list = [1, 2, 3]
# result = my_list / 2
# print(result)

# process_memory_usage = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss 
# print(process_memory_usage,"meemor")

# import  os
# codeRunnerPath = os.path.abspath("testsubprocess")
# # codeRunnerPath="Clash_RC_2/Code_Runner"
# runnerPath = os.path.dirname(__file__)
# print(codeRunnerPath,"sssssssssssss",runnerPath)

# scripts_file_path = f"{runnerPath}/test.py"
# ip_file_path = f"{runnerPath}/ip.txt"
# with open(ip_file_path, 'r') as f:
#     ip_contents = f.read()

# op_file_path = f"{runnerPath}/op.txt"

# filename = f"{scripts_file_path}"
# size_in_bytes = os.path.getsize(filename)
# size_in_mb = size_in_bytes / (1024 * 1024)

# print(f"Size of {filename}: {size_in_mb} MB")


# m =tracemalloc.get_traced_memory()
# print("memry usage",m,"bytes")
 
# # stopping the library
# tracemalloc.stop()




# import numpy as np
# import norm
# # from scipy.stats import norm


# # Generate some random data
# np.random.seed(123)
# data = np.random.normal(0, 1, size=100)

# # Define the log-likelihood function
# def log_likelihood(theta, data):
#     mu, sigma = theta
#     ll = np.sum(norm.logpdf(data, mu, sigma))
#     return ll

# # Perform maximum likelihood estimation
# from scipy.optimize import minimize

# mle = minimize(lambda x: -log_likelihood(x, data), x0=[0, 1])
# print(mle)
 
# # stopping the library
# tracemalloc.stop()
