import pathlib,subprocess,os
username = "prasad"

# lang = "py"
# user_code = "print('user code')"

lang = "cpp"
user_code = """#include <iostream>
using namespace std;
int main(){
    cout<<"isede cpp"
}"""

code_folder = pathlib.Path(f"./testsubprocess/test/user/{username}")  #to check directory is present or not
#if not it will create it
if not code_folder.exists():
    code_folder.mkdir()


code_op_text_file = open(f"{code_folder}/test.txt","w")

bin_file = pathlib.Path(f"{code_folder}/./bin")
if not bin_file.exists():
    bin_file.mkdir()

if (lang=="py"):
    #to store user code in testing file
    code_file_path = open(f"{code_folder}/test.py","w")
    code_file_path.write(user_code)
    code_file_path.close()
    code_file_path = pathlib.Path(f"{code_folder}/test.py")
    cmd = f"python {code_file_path} "
    op = subprocess.run(cmd,shell=True,text=True,capture_output=True)
    # print(op)
    # print(op.stdout)
    # print(op.stderr)
    if op.returncode !=1:
        code_op_text_file.write(op.stdout)
    else:
        code_op_text_file.write(op.stderr)
elif (lang=="cpp"):
    #to store user code in testing file
    code_file_path = open(f"{code_folder}/test.cpp","w")
    code_file_path.write(user_code)
    code_file_path.close()

    code_file_path = pathlib.Path(f"{code_folder}/test.cpp")
    cmd = f"g++ {code_file_path} -o {bin_file}/out"
    subprocess.run(cmd)
    # final_op = subprocess.run(f"{bin_file}/./out",capture_output=True)    #use stdout.decode()
    # final_op = subprocess.run(f"{bin_file}/./out",text=True,capture_output=True)
    # print(final_op)
    # print(final_op.stdout)
    # print(final_op.stderr)

    exe_file_path = [f"{bin_file}/./out"]
    ojh = subprocess.check_output(code_file_path,text=True)
    print(ojh.decode())
    # code_op_text_file.write(out.decode())

    # exe_file_path = [f"{bin_file}/./out"]
    # out ,err = subprocess.Popen(exe_file_path,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    # print(out)
    # print(err)
    # code_op_text_file.write(out.decode())
    # the stdout of the C++ program is captured using subprocess.PIPE and stored in the stdout attribute of the result object. The decode() method is used to convert the binary data to a string, which can then be printed to the console.

    # if final_op.returncode !=1:
    #     code_op_text_file.write(final_op.stdout.decode("utf-8"))
    # else:
    #     code_op_text_file.write(final_op.stderr.decode("utf-8"))

