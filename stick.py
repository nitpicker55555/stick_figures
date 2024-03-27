import cenpy
import pandas as pd

# 创建 ACS 实例
acs = cenpy.products.ACS()

# 定义查询的变量
# 注意: 这里仅为示例，你需要根据需要选择合适的变量代码
variables = [
    'B01001_001E',  # 人口总数
    'B19013_001E',  # 家庭收入的中位数
    'B15003_022E',  # 持有学士学位的人口数量
    'B25001_001E',  # 住房单位总数
    'B01001_002E',  # 男性总数
    'B01001_026E',  # 女性总数
    'B25064_001E',  # 租金的中位数
]

# 使用 from_place 方法并指定地区和变量
# 这里，我们将查询的范围设置为 "Illinois"，以获取整个州的数据
data = acs.from_place('Illinois', variables=variables, level='state')

# 查看部分数据
print(data.head())

# 保存为 CSV 文件
# 请替换 '/path/to/your_file.csv' 为你希望保存文件的实际路径
data.to_csv('/path/to/your_file.csv', index=False)
