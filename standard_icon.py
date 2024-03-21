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


# 示例：绘制图案
draw_pattern(135, 135, 135, 135, 90)
