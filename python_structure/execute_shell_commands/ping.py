import os
import shlex
import subprocess

'''
> cmd_v1
If you save this as a script and run it, you will see the output in the command line. The problem with this 
approach is in its inflexibility since you can’t even get the resulting output as a variable.

> cmd_v2
The os.popen() command opens a pipe from or to the command line. This means that we can access the stream 
within Python. This is useful since you can now get the output as a variable. When you use the .read() function, 
you will get the whole output as one string. You can also use the .readlines() function, which splits each line
( including a trailing \n). Note, that you can run them only once. It is also possible to write to the stream by using 
the mode='w' argument. 

> cmd_v3
The main function you want to keep in mind if you use Python >= 3.5 is subprocess.run().
The subprocess.Popen() class is responsible for the creation and management of the executed process. In contrast to the 
previous functions, this class executes only a single command with arguments as a list. This means that you won’t be 
able to pipe commands.

> cmd_v4
When you run .communicate(), it will wait until the process is complete. However if you have a long program 
that you want to run and you want to continuously check the status in realtime while doing something else, 
you can do it. You can use the .poll() function to check the return code of the process. It will return None while 
the process is still running. To get the output, you can use process.stdout.readline() to read a single line. 
Conversely, when you use process.stdout.readlines(), it reads all lines and it also waits for the process to finish 
if it has not finished yet.

> cmd_v5
Also note, that you won’t need quotations for arguments with spaces in between like '\"More output\"'. If you 
are unsure how to tokenize the arguments from the command, you can use the shlex.split() function.

> cmd_v6
You have also the subprocess.call() function to your disposal which works like the Popen class, but it waits 
until the command completes and gives you the return code as in return_code = subprocess.call(['echo', 'Even more 
output']). The recommended way however is to use subprocess.run() which works since Python 3.5. It has been added as 
a simplification of subprocess.Popen. The function will return a subprocess.CompletedProcess object.


> cmd_v7
Similar to subprocess.call() and the previous .communicate() function, it will wait untill the process is 
completed. Finally, here is a more advanced example on how to access a server with ssh and the subprocess module.
'''


def cmd_v1(command):
    os.system(command)


def cmd_v2(command):
    stream = os.popen(command)
    output = stream.read()
    return output


def cmd_v3():
    process = subprocess.Popen(
        [
            'echo',
            'I am Pit'
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = process.communicate()
    return stdout, stderr


def cmd_v4():
    process = subprocess.Popen(
        ['ping', '-c 5', 'python.org'],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                print(output.strip())
            break


def cmd_v5():
    shlex.split("/bin/prog -i data.txt -o \"more data.txt\"")


def cmd_v6():
    process = subprocess.run(
        ['echo', 'Even more output'],
        stdout=subprocess.PIPE,
        universal_newlines=True)
    return process.stdout


def cmd_v7():
    ssh = subprocess.Popen(
        ["ssh", "-i .ssh/id_rsa", "user@host"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        bufsize=0)

    # Send ssh commands to stdin
    ssh.stdin.write("uname -a\n")
    ssh.stdin.write("uptime\n")
    ssh.stdin.close()

    # Fetch output
    for line in ssh.stdout:
        print(line.strip())


if __name__ == '__main__':
    div = "_______________________________________________"
    cd_ls = 'cd && ls -l'
    cmd_v1(cd_ls)
    print(div)
    print(cmd_v2(cd_ls))
    print(div)
    print(cmd_v3())
    print(div)
    print(cmd_v4())
    print(div)
    print(cmd_v5())
    print(div)
    print(cmd_v6())
    print(div)
    print(cmd_v7())
