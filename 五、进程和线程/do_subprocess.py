# -*- coding:UTF-8 -*-

# 子进程演示

import subprocess

print('$ nslookup www.python.org')

r = subprocess.call(['nslookup', 'www.python.org'])

print('Exit done:', r)

# communicate() 方法输入

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)