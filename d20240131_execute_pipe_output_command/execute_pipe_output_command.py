import subprocess
import shlex

def run_command(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    output = ''
    while True:
        assert process.stdout is not None
        line = process.stdout.readline()
        if not line:
            break
        print(line, end='')  # 標準出力に出力
        output += line

    process.wait()

    return output

cmd = ['ls']
cmd = ["qmk", "compile", f"-kb=sparrow60c", f"-km=default"]

print("$", shlex.join(cmd))
output = run_command(cmd)
