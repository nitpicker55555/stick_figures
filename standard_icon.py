import matplotlib.pyplot as plt
import numpy as np

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


def draw_pattern_plotly(angle_sets, c_start, unit_length=1):

    fig = go.Figure()

    for set_idx, (angles, c_start) in enumerate(zip(angle_sets, c_start)):
        angles[2] = 180 - angles[2]
        angles[3] = 180 - angles[3]
        angles[1] = -angles[1]
        angles[3] = -angles[3]
        angle_c_vertical=90
        # 计算线段c的方向
        c_dx = np.cos(np.radians(angle_c_vertical))
        c_dy = np.sin(np.radians(angle_c_vertical))
        # c_start = np.array([2 + 4 * set_idx, 2])  # 设置起点，确保两个图案不重叠
        print(c_start)
        c_end = c_start + np.array([c_dx * unit_length, c_dy * unit_length])

        # 绘制线段c
        fig.add_trace(
            go.Scatter(x=[c_start[0], c_end[0]], y=[c_start[1], c_end[1]], mode='lines', name='c', legendgroup='c',
                       showlegend=(set_idx == 0)))

        # 计算并绘制其它线段
        labels = ['a', 'b', 'd', 'e']
        points = [c_start, c_start, c_end, c_end]
        for i, angle in enumerate(angles):
            dx = np.cos(np.radians(angle_c_vertical + angle)) * unit_length
            dy = np.sin(np.radians(angle_c_vertical + angle)) * unit_length
            end_point = points[i] + np.array([dx, dy])
            fig.add_trace(
                go.Scatter(x=[points[i][0], end_point[0]], y=[points[i][1], end_point[1]], mode='lines', name=labels[i],
                           legendgroup=labels[i], showlegend=(set_idx == 0)))

    fig.update_layout(title="Different Patterns with Varied Angles", xaxis_showgrid=False, yaxis_showgrid=False,
                      plot_bgcolor='white')
    fig.show()


# 设置两组角度参数以及c线段的角度
angle_sets = [
    [45, 45, 135, 135],  # 第一组图案的角度参数
    [135, 135, 135, 135]   # 第二组图案的角度参数
]
c_start = [(1,2), (2,4)]  # c线段相对于垂直线的角度
# 绘制图案
draw_pattern_plotly(angle_sets,c_start)

# 示例：绘制图案
# draw_pattern(135, 135, 135, 135, 90)
