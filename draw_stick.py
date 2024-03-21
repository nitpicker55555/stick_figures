import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 加载数据
df = pd.read_csv('chicago_acs_data.csv')

# 转换数据类型确保数据是数值类型
for column in df.columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')
for col in ['B15003_022E', 'B12001_001E', 'B01001_002E', 'B01001_026E','B01001_001E','B19013_001E']:
    # df[col] = (df[col] - df[col].mean()) / df[col].std()
    column_min = df[col].min()
    column_max = df[col].max()
    df[col] = (df[col] - column_min) / (column_max - column_min)

# 函数：根据角度和长度绘制单个 Stick Figure
# def create_stick_figure(angles, lengths, origin):
#     # 计算各个点的坐标
#     x0, y0 = origin
#     points_x = [x0]
#     points_y = [y0]
#     for angle, length in zip(angles, lengths):
#         x = points_x[-1] + length * np.cos(angle)
#         y = points_y[-1] + length * np.sin(angle)
#         points_x.append(x)
#         points_y.append(y)
#     return points_x, points_y
#
# # 定义长度和角度
# lengths = [0.1, 0.1, 0.1, 0.1]  # 示例长度
# angles = np.linspace(0, 2 * np.pi, 5)[:-1]  # 示例起始角度
#
# # 初始绘制每个 Stick Figure
# figures_data = []
c_start_list=[]
angles_list=[]

for index, row in df.iterrows():
    if not np.isnan(row['B01001_001E']) and not np.isnan(row['B19013_001E']):
        origin = [(row['B01001_001E']),( row['B19013_001E'])]
        angles = [round((360 * z),0) for z in row[['B15003_022E', 'B12001_001E', 'B01001_002E', 'B01001_026E']]]
        angles_list.append(angles)
        c_start_list.append(origin)
print(angles_list)
print(c_start_list)
from standard_icon import data_input
data_input(angles_list,c_start_list)
    # fig_x, fig_y = create_stick_figure(angles, lengths, origin)
    # figures_data.append(go.Scatter(x=fig_x, y=fig_y, mode='lines+markers'))

# # 创建滑块
# steps = []
# for i in range(0, 360, 15):
#     step = {
#         'method': 'update',
#         'args': [{'visible': [True] * len(figures_data)}],
#         'label': f'{i} degrees'
#     }
#     steps.append(step)
#
# sliders = [{
#     'active': 0,
#     'currentvalue': {"prefix": "Rotation Angle: "},
#     'pad': {"t": 50},
#     'steps': steps
# }]
#
# # 初始图表布局
# fig = go.Figure(data=figures_data)
# fig.update_layout(sliders=sliders)
#
# # 滑块响应函数
# def rotate(angle, lengths, origin):
#     rad_angle = np.deg2rad(angle)
#     rotated_angles = angles + rad_angle
#     return create_stick_figure(rotated_angles, lengths, origin)
#
# for i, step in enumerate(steps):
#     angle = i * 15
#     # 计算新的角度和长度
#     for j, row in df.iterrows():
#         origin = [row['B01001_001E'], row['B19013_001E']]
#         fig_x, fig_y = rotate(angle, lengths, origin)
#         fig.add_trace(go.Scatter(x=fig_x, y=fig_y, mode='lines+markers', visible=False))
#
# # 显示图表
# fig.show()
