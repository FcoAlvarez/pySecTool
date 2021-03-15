import os

p = os.popen('ls -la')
print(p.read())