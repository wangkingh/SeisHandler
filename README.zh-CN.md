*其他语言版本: [English](README.md), [简体中文](README.zh-CN.md)

# 简单介绍 SeisHandler

SeisHandler是一个用于组织地震数据的Python包。它不会读取文件内的任何数据，而是通过文件名的匹配和组织来进行操作。它是一个利用多个特定标签来组织地震数据的工具。


# 开发的动机和哲学

这一问题长久以来一直困扰着人们，那就是如何组织地震阵列数据。地震阵列是在特定区域部署一段时间，并记录地面运动信号的一组地震仪。地震阵列有时由相同类型的仪器组成，具有相同的特性。

组织地震数据的方式有些像哲学。组织风格描述了用户将如何使用数据。例如，如果数据按照'/data_home/station/time/data'的方式组织，研究者可能会利用这种方式使用单站方法，如接收函数等，来进行一些研究。如果按照'/data_home/time/station/data'的方式组织数据，研究者可能会想要展示不同时间的结果，如速度监测。

因此，在重新组织数据路径之前，所有方法都很难应用到同一数据集上。此外，这个障碍是使用一些非常难以克服的方法。我设计了这个类，以虚拟的方式组织数据，灵感来自于虚拟化的思想。（通过虚拟控制系统，电机可以达到齿轮箱的效果，减少机械部件的使用）在这个包中，开发人员可以通过改变标签的顺序来重塑数据的路径。此外，如果他们基于此设计自己的程序，并且所有的地震开发者都遵循这种风格，那么程序将更加灵活和强大。这将使每个人的方法更容易应用到不同的数据集，而且非常简单。

## 安装

使用者需要提前安装 pandas:

```
pip install pandas
```

Install this package

```
pip install SeisHandler.tar.gz
```

## 使用方法

```
from SeisHandler import SeisArray as sa

array_dir = 'path/to/array/dir'
pattern = '{file}/{path}/{pattern}{with}{label}'

# 根据文件模式匹配文件
my_array = sa(array_dir=array_dir, pattern=pattern)
my_array.match(threads=4)

# 根据准则criteria 筛选文件, 输出是 my_array.filtered_files
# 输出列表是文件信息列表
criteria = { 'label': [label_list],''}
# e.g 
''' 
    criteria = {'component': ['X'], 'time': [
    '2018-01-01 00:00:00', '2018-01-07 00:00:00']}
'''
my_array.filter(criteria=criteria,threads=4)


# 按照标签对数据目录进行分组
# 输出是my_array.files_group。 这是一个字典，字典的键是标签组（比如：台站名-时间）
# 字典的值是列表，每个列表的成员是文件信息字典。
# filtered选项决定是否对已经过滤之后的文件进行分组
my_array.group(['station','time']，filtered=True)

# 按照标签对数据目录进行虚拟重组
# 输出是一个多级虚拟目录。每一级的键是指定标签
my_array.organize(label_order=['station','time'],filtered=True,output_type='path')
for station in my_array.virtual_array:
    for time in my_array.virtual_array[station]:
        print(my_array.virtual_array[station][time])
        print('\n')
```

## 示例
可以下载示例数据 “example_data.zip”

```
from SeisHandler import SeisArray as sa



# matching files
path_to_array_dir = 'abspath/to/demo/data'
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
```

## 更新日志

### v0.1.0 (2023-07-10)

- The First version. 第一版本。

## 联系方式

If you have any questions, issues, or suggestions for improvement,
feel free to open an issue in the repository,
or directly reach out to me at wkh16@mail.ustc.edu.cn.

## 许可证

SeisHandler is licensed under the MIT License. See [LICENSE](LICENSE) file for details.
