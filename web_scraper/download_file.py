import requests
import time


def download(url, write_sim=False):
    file = requests.get(url)
    print('Status code: ', file.status_code)
    # raise an exception if an error occurs and do nothing if th file was successfully downloaded
    file.raise_for_status()
    print('___ File content ___\n')
    if write_sim:
        write_simulation(file)
    else:
        print(file.text)
    exit(0)


def write_simulation(file):
    row = ''
    for i in range(len(file.text)):
        row += file.text[i]
        if file.text[i] == '\n':
            for j in row:
                print(j, end='')
                time.sleep(0.1)
            # print(row, end='')
            row = ''


if __name__ == '__main__':
    download('https://raw.githubusercontent.com/PitPietro/python-structure/master/execute_shell_commands/ping.py')
    exit(0)
