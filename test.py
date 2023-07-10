import sys
sys.path.append('/mnt/c/Users/think8/Desktop/临时/')
from SeisHandler import SeisArray as sa



# matching files
path_to_array_dir = '/mnt/c/Users/think8/Desktop/wjxArray'
seis_file_pattern = '{home}/{*}/{station}.{YYYY}.{JJJ}.{HH}{MI}.{component}.{suffix}'
my_array = sa(array_dir=path_to_array_dir, pattern=seis_file_pattern)
my_array.match(threads=20)

'''
for file in my_array.files:
    print(file)
'''

criteria = {'component': ['X'], 'time': [
    '2018-01-01 00:00:00', '2018-01-07 00:00:00']}
my_array.filter(criteria=criteria, threads=20)

my_array.group(labels=['station', 'time'], filtered=True)

'''
for station_time in my_array.files_group:
    print(my_array.files_group[station_time])
    print('\n')
'''

# generate a multi-level dictionary for virtual array
my_array.organize(label_order=['station','time'],filtered=True,output_type='path')
for station in my_array.virtual_array:
    for time in my_array.virtual_array[station]:
        print(my_array.virtual_array[station][time])
        print('\n')
# filtering files
