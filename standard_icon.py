import matplotlib.pyplot as plt
import numpy as np
from plotly.subplots import make_subplots
def draw_pattern(angle_ac, angle_bc, angle_dc, angle_ec, angle_c_vertical, unit_length=1):
    angle_dc=180-angle_dc
    angle_ec=180-angle_ec
    angle_bc=-angle_bc
    angle_ec=-angle_ec
    # 135, -135, 45, -45, 90
    plt.figure(figsize=(6, 6))

    # 计算线段c的方向
    c_dx = np.cos(np.radians(angle_c_vertical))
    c_dy = np.sin(np.radians(angle_c_vertical))
    c_start = np.array([2, 2])  # 随意设置起点，以保证图案位于图中央
    c_end = c_start + np.array([c_dx * unit_length, c_dy * unit_length])

    # 计算其它线段的终点
    angles = [angle_ac, angle_bc, angle_dc, angle_ec]
    points = [c_start, c_start, c_end, c_end]
    colors = ['r', 'g', 'b', 'm']
    for i, angle in enumerate(angles):
        dx = np.cos(np.radians(angle_c_vertical + angle)) * unit_length
        dy = np.sin(np.radians(angle_c_vertical + angle)) * unit_length
        end_point = points[i] + np.array([dx, dy])
        plt.plot([points[i][0], end_point[0]], [points[i][1], end_point[1]], color=colors[i], lw=2)

    # 绘制线段c
    plt.plot([c_start[0], c_end[0]], [c_start[1], c_end[1]], 'k-', lw=2)

    # 设置图形显示范围并关闭坐标轴
    plt.xlim(0, 4)
    plt.ylim(0, 4)
    plt.axis('off')
    plt.show()


import plotly.graph_objects as go


def draw_pattern_plotly(angle_sets, c_start, angle_rotation,unit_length=0.03):
    data = []
    c_data=[]

    for set_idx, (angles, c_mid) in enumerate(zip(angle_sets, c_start)):


        angle_c_vertical=angles[-1]
        angles=angles[:-1]
        # 计算线段c的方向
        c_dx = np.cos(np.radians(angle_c_vertical))
        c_dy = np.sin(np.radians(angle_c_vertical))
        # c_mid = np.array([2 + 4 * set_idx, 2])  # 设置中点，确保两个图案不重叠
        c_start = c_mid - np.array([c_dx * unit_length / 2, c_dy * unit_length / 2])
        c_end = c_mid + np.array([c_dx * unit_length / 2, c_dy * unit_length / 2])

        # 旋转矩阵
        rotation_matrix = np.array([
            [np.cos(np.radians(angle_rotation)), -np.sin(np.radians(angle_rotation))],
            [np.sin(np.radians(angle_rotation)), np.cos(np.radians(angle_rotation))]
        ])

        # 旋转c的起点和终点
        c_start_rotated = np.dot(rotation_matrix, (c_start - c_mid)) + c_mid
        c_end_rotated = np.dot(rotation_matrix, (c_end - c_mid)) + c_mid
        data.append({'x' : [c_start_rotated[0], c_end_rotated[0]], 'y' : [c_start_rotated[1],
                                                                         c_end_rotated[1]], 'mode' : 'lines',
                                                                                                   'name' : 'Total number of men', 'legendgroup' : 'Total number of men', 'showlegend' : (
                    set_idx == 0)})
        # 绘制线段c
        # 'B15003_022E', # Number of people holding a bachelor's degree
        # 'B25001_001E', # Total number of housing units
        # 'B01001_002E', # Total number of men
        # 'B01001_026E', # Total number of women
        # 'B25064_001E', # Median rent
        # 计算并绘制其它线段
        labels = ["People holding a bachelor's degree", 'Housing units', 'Total number of women', 'Median rent']
        points = [c_start, c_start, c_end, c_end]

        for i, angle in enumerate(angles):
            dx = np.cos(np.radians(angle_c_vertical + angle)) * unit_length
            dy = np.sin(np.radians(angle_c_vertical + angle)) * unit_length
            end_point = points[i] + np.array([dx, dy])
            # 旋转
            end_point_rotated = np.dot(rotation_matrix, (end_point - c_mid)) + c_mid
            point_rotated = np.dot(rotation_matrix, (points[i] - c_mid)) + c_mid
            data.append({'x': [point_rotated[0], end_point_rotated[0]], 'y': [point_rotated[1], end_point_rotated[1]],
                         'mode': 'lines', 'name': labels[i], 'legendgroup': labels[i], 'showlegend': (set_idx == 0)})


    return data



# 设置两组角度参数以及c线段的角度
angle_sets = [
[38.0, 117.0, 70.0, 153.0,60]
    # [45, 45, 135, 135],  # 第一组图案的角度参数
    # [135, 135, 135, 135]   # 第二组图案的角度参数
]
c_start = [[0.38968731792581085, 0.3179088738450779], [0.5365119440668091, 0.21254391572551784], [0.4899980578753156, 0.1902295365012758]]  # c线段相对于垂直线的角度
def data_input(angle_sets,c_start):
# 绘制图案
    for angle in angle_sets:

        angle[2] = 180 - angle[2]
        angle[3] = 180 - (angle[3])

        angle[1] = -(angle[1])
        # angles[2] = abs(angles[2])
        # angles[0] = abs(angles[0])
        angle[3] = -(angle[3])
    data=draw_pattern_plotly(angle_sets,c_start,0)
    fig = go.Figure()
    # fig.add_trace(
    #     go.Scatter(c_data))

    for i in data:
        fig.add_trace(
            go.Scatter(i))

    fig.update_layout(title="Chicago, IL acs data 2019", xaxis=dict(title='Total population'), # 设置横轴标签
    yaxis=dict(title='Median household income'),
                      plot_bgcolor='white')

    fig.update_layout(
        sliders=[dict(
            steps=[dict(method='animate',
                        args=[[f'frame{k}'],
                              dict(mode='immediate',
                                   frame=dict(duration=500, redraw=True),
                                   transition=dict(duration=0))],
                        label=f'{k}') for k in range(0, 360, 10)],
            active=0,
            currentvalue={"prefix": "Rotation angle: "},
            pad={"t": 50})],
        updatemenus=[dict(
            type="buttons",
            direction="left",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)])])])

    frames = []
    for angle in range(0, 360, 10):
        frames.append(go.Frame(data=draw_pattern_plotly(angle_sets,c_start,angle),
                               name=f'frame{angle}'))

    fig.frames = frames

    fig.show()
# data_input(angle_sets,c_start)
# 示例：绘制图案
# draw_pattern(135, 135, 135, 135, 90)
