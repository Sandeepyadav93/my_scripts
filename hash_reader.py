import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines:
    if 'baseurl' in line:
        my_list = line.split('/')
        ref_index = my_list.index('component')
        print(f"{my_list[ref_index+1]} {'/'.join(my_list[ref_index+2:])}", end ='')
