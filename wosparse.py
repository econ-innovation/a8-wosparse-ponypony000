import pandas as pd

# 读取原始数据
file_path = '/Users/mawenting/Documents/Bigdata_econ/mypython/wosparse/qje2014_2023.txt'
data = pd.read_csv(file_path, sep='\t', encoding='utf-8')
#sep='\t': 这是 pd.read_csv 函数的一个参数，指定了数据文件中列之间的分隔符。\t 表明数据文件是以制表符分隔的。

# 提取基本信息的列
basic_info = data[['UT', 'PY', 'SO', 'SN', 'DI', 'IS', 'VL']]
# 保存基本信息表格
basic_info.to_csv('/Users/mawenting/Documents/Bigdata_econ/mypython/wosparse/qje_basic_info.csv', index=False)

# 提取摘要信息的列
abstract_info = data[['UT', 'AB']]

# 保存摘要信息表格
abstract_info.to_csv('/Users/mawenting/Documents/Bigdata_econ/mypython/wosparse/qje_abstract_info.csv', index=False)

# 提取题目信息的列
title_info = data[['UT', 'TI']]

# 保存题目信息表格
title_info.to_csv('/Users/mawenting/Documents/Bigdata_econ/mypython/wosparse/qje_title_info.csv', index=False)

# 提取作者信息的列
author_info = data[['UT', 'AU', 'AF']]

# 保存作者信息表格
author_info.to_csv('/Users/mawenting/Documents/Bigdata_econ/mypython/wosparse/qje_author_info.csv', index=False)

# 提取作者与单位信息的列
author_affiliation_info = data[['UT', 'AU', 'AF', 'C1']]

# 保存作者与单位信息表格
author_affiliation_info.to_csv('/Users/mawenting/Documents/Bigdata_econ/mypython/wosparse/qje_author_affiliation_info.csv', index=False)

# 提取参考文献信息的列
citation_info = data[['UT', 'CR']]

# 保存参考文献信息表格
citation_info.to_csv('/Users/mawenting/Documents/Bigdata_econ/mypython/wosparse/qje_citation_info.csv', index=False)

