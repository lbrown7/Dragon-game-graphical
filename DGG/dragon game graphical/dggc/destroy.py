import time
import sys

print('loading destroy files...')
time.sleep(0.2)

print('ready!')
time.sleep(1)

print('destroying...')

file1 = "E:/dragon game graphical/dggc/admin/dragon game graphical/dragon game graphical test.py"
file2 = "E:/dragon game graphical/dggc/admin/dragon game graphical/Gideon.py"
file3 = "E:/dragon game graphical/dggc/admin/dragon game graphical/settings.py"
file4 = "E:/dragon game graphical/dggc/admin/dragon game graphical/Tree.py"
file5 = "E:/dragon game graphical/dggc/admin/dragon game graphical/orc.py"
with open(file1, 'w+') as f:
    f.write('')
    f.close()


with open(file2, 'w+') as f2:
    f2.write('')
    f2.close()

with open(file3, 'w+') as f3:
    f3.write('')
    f3.close()

with open(file4, 'w+') as f4:
    f4.write('')
    f4.close()

time.sleep(1)
print('almost done!!!')

with open(file5, 'w+') as f5:
    f5.write('')
    f5.close()

time.sleep(2)

print('done!!!')

file6 = "E/:dragon game graphical/dggc/admin/dragon game graphical"
with open(file6) as pd:
    pd.del()

time.sleep(1)

exit()
quit()
sys.exit()