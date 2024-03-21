import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 加载数据
df = pd.read_csv('chicago_acs_data.csv')

# 确保数据是数值类型
for column in df.columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# 标准化数据，使之适用于定义角度和长度
# 这里我们仅将数据转换为它们在各自列中的 z-scores
for col in ['B15003_022E', 'B12001_001E', 'B01001_002E', 'B01001_026E','B19013_001E','B01001_001E']:
    df[col] = (df[col] - df[col].mean()) / df[col].std()

# 定义绘制 Stick Figure 的函数
def draw_stick_figure(ax, origin, angles, lengths=(0.1,0.1, 0.1, 0.1), head_radius=0.001):
    # 定义肢体的结束点
    points = np.array([origin])

    for angle, length in zip(angles, lengths):
        # 计算新点的坐标
        dx = length * np.cos(angle)
        dy = length * np.sin(angle)
        new_point = points[-1] + np.array([dx, dy])
        points = np.vstack([points, new_point])

    # 绘制身体
    body_parts = [(0, 1), (1, 2), (1, 3), (1, 4)]
    for start, end in body_parts:
        ax.plot([points[start][0], points[end][0]], [points[start][1], points[end][1]], 'k-')

    # 绘制头部
    head = plt.Circle(points[1], head_radius, color='k', fill=False)
    ax.add_artist(head)

# 设置坐标轴的范围
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, aspect='equal')
plt.xlim(df['B01001_001E'].min(), df['B01001_001E'].max())
plt.ylim(df['B19013_001E'].min(), df['B19013_001E'].max())

# 对于每一行数据，绘制一个 Stick Figure
for index, row in df.iterrows():
    # 定义 Stick Figure 的起点（根据 B01001_001E 和 B19013_001E）
    origin = (row['B01001_001E'], row['B19013_001E'])

    # 获取其他变量以定义角度（这里使用的是弧度）
    angles = [np.deg2rad(360 * z) for z in row[['B15003_022E', 'B12001_001E', 'B01001_002E', 'B01001_026E']]]

    # 绘制 Stick Figure（这里假设所有长度相同，你可以根据需要进行调整）
    draw_stick_figure(ax, origin, angles)

plt.xlabel('B01001_001E')
plt.ylabel('B19013_001E')
plt.title('Stick Figures Representation of Data')
plt.show()
