import plotly.graph_objects as go
import numpy as np

# 定义线段的起点和终点
a_start = [0, 0]
a_end = [1, 1]
b_start = a_end
b_end = [2, 1]
c_start = b_end
c_end = [3, 0]

# 计算b线段的中点，作为旋转中心
# b_mid = [(b_start[0] + b_end[0]) / 2, (b_start[1] + b_end[1]) / 2]

# 绘制初始图形
fig = go.Figure()

# 添加线段
fig.add_trace(go.Scatter(x=[a_start[0], a_end[0]], y=[a_start[1], a_end[1]], mode='lines', name='a'))
fig.add_trace(go.Scatter(x=[b_start[0], b_end[0]], y=[b_start[1], b_end[1]], mode='lines', name='b'))
fig.add_trace(go.Scatter(x=[c_start[0], c_end[0]], y=[c_start[1], c_end[1]], mode='lines', name='c'))

# 添加滑块
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
def calculate_rotated_data(angle):
    """
    根据给定的角度和线段起始点，计算旋转后的线段数据。

    Parameters:
    - angle: 旋转的角度（度）
    - a_start, a_end: 线段a的起点和终点坐标
    - b_start, b_end: 线段b的起点和终点坐标
    - c_start, c_end: 线段c的起点和终点坐标

    Returns:
    - data: 包含旋转后的三个线段数据的列表
    """
    # 计算b线段的中点，作为旋转中心
    b_mid = [(b_start[0]+b_end[0])/2, (b_start[1]+b_end[1])/2]

    # 将角度转换为弧度
    rad = np.radians(angle)
    cos_a, sin_a = np.cos(rad), np.sin(rad)

    # 定义旋转函数
    def rotate_point(p):
        return [cos_a * (p[0]-b_mid[0]) - sin_a * (p[1]-b_mid[1]) + b_mid[0],
                sin_a * (p[0]-b_mid[0]) + cos_a * (p[1]-b_mid[1]) + b_mid[1]]

    # 计算旋转后的线段坐标
    ra_start, ra_end = rotate_point(a_start), rotate_point(a_end)
    rb_start, rb_end = rotate_point(b_start), rotate_point(b_end)
    rc_start, rc_end = rotate_point(c_start), rotate_point(c_end)

    # 准备数据用于更新图形
    data = [
        {'x': [ra_start[0], ra_end[0]], 'y': [ra_start[1], ra_end[1]], 'mode': 'lines', 'name': 'a'},
        {'x': [rb_start[0], rb_end[0]], 'y': [rb_start[1], rb_end[1]], 'mode': 'lines', 'name': 'b'},
        {'x': [rc_start[0], rc_end[0]], 'y': [rc_start[1], rc_end[1]], 'mode': 'lines', 'name': 'c'}
    ]

    return data
for angle in range(0, 360, 10):
    frames.append(go.Frame(data=calculate_rotated_data(angle),
                           name=f'frame{angle}'))

fig.frames = frames

fig.show()
