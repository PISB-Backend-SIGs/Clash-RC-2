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
# while(1):
#     print("hello")

import resource
print("dffffffffffffffffffff")



# print("dddddddddddd")
# s="dfsdfs"
# i = input()
# print(i)

# a simple program that keeps allocating memory until the process runs out of memory
# inner psutil function
import psutil,os
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss
 
# decorator function
def profile(func):
    def wrapper(*args, **kwargs):
 
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before))
 
        return result
    return wrapper
 
# instantiation of decorator function

import numpy as np

# Generate some sample data from a normal distribution
mu = 3.0
sigma = 2.0
n = 100
data = np.random.normal(mu, sigma, n)

# Define the likelihood function for a normal distribution
# @profile
def normal_likelihood(theta, data):
    mu, sigma = theta
    n = len(data)
    log_likelihood = -n/2 * np.log(2*np.pi) - n*np.log(sigma) \
        - np.sum((data-mu)**2)/(2*sigma**2)
    return -log_likelihood

# Find the maximum likelihood estimate by grid search
mu_range = np.linspace(0.0, 6.0, 100)
sigma_range = np.linspace(0.1, 4.0, 100)
mu_mle = None
sigma_mle = None
max_log_likelihood = -np.inf
for mu_candidate in mu_range:
    for sigma_candidate in sigma_range:
        log_likelihood = normal_likelihood([mu_candidate, sigma_candidate], data)
        if log_likelihood > max_log_likelihood:
            max_log_likelihood = log_likelihood
            mu_mle = mu_candidate
            sigma_mle = sigma_candidate

print("MLE for mu:", mu_mle)
print("MLE for sigma:", sigma_mle)

# process_memory_usage = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss 
# print(process_memory_usage)
