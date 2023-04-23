import subprocess

def run_python():
    code_path = "code/code.py"
    tc_path = "code/input.txt"
    er=open('code/err.txt','w+')
    rc=open('code/returnCode.txt','w+')
    out=open('code/output.txt','w+')
    run = subprocess.run(f"python {code_path} <{tc_path}", text=True, shell=True, capture_output=True)
    out.write(run.stdout)
    er.write(run.stderr)
    rc.write(str(run.returncode))
    er.close()
    rc.close()
    out.close()

