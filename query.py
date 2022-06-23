import subprocess
import json
import re
import random

def check_output(cmd):
    return [line for line in re.split('\\r?\\n', subprocess.check_output(cmd).decode('utf-8')) if line != '']

def main():
    versions = []
    for line in check_output('aqt list-qt windows desktop'):
        for v in line.split(' '):
            versions.append(v)
    #print(versions)
    
    debug = 0
    if debug:
        random.shuffle(versions)
        versions = versions[:3]

    arch = dict()
    for v in versions:
        a = []
        for line in check_output('aqt list-qt windows desktop --arch {}'.format(v)):
            a = a + line.split(' ')
        arch[v] = a

    tools_list = []
    for line in check_output('aqt list-tool windows desktop'):
        tools_list += line.split(' ')

    tools = dict()
    for t in ['tools_mingw', 'tools_mingw90', 'tools_ninja', 'tools_cmake', 'tools_qtcreator', 'tools_vcredist']:
        tools[t] = []
        for line in check_output('aqt list-tool windows desktop {}'.format(t)):
            tools[t] += line.split(' ')
        if debug:
            break

    data = {'versions': versions, 'arch': arch, 'tools_list': tools_list, 'tools': tools}
    with open('aqt.json','w',encoding='utf-8') as f:
        json.dump(data, f)
    

if __name__ == "__main__":
    main()