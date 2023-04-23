import subprocess

# r = subprocess.run(['python',"print('hello')"],capture_output = True,shell=True)
# result = subprocess.run(["python", "-c", "t.py"], capture_output=True)
# print(result.stdout)
# print(result.stderr)

# command = ['python', 't.py']

#     # Execute the command in a subprocess
# process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     # Wait for the subprocess to finish and get the output and errors
# output, error = process.communicate()
# print(output)
# print(error)


code_path = "\\t.py"
run = subprocess.run(f"python {code_path} ", text=True, shell=True, capture_output=True)
print(run.stderr)
