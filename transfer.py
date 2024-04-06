import subprocess,os
# scp -r C:\Users\Morning\Desktop\my_project\stick_figures\ TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\stick
# 定义你想要运行的命令
command = r"scp -r C:\Users\Morning\Desktop\my_project\stick_figures\*.py TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\stick"

# 使用subprocess运行命令
# 这里使用了`shell=True`来允许运行shell命令
# 但请注意，当涉及用户输入时，应小心使用`shell=True`以避免命令注入攻击
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# 输出命令的标准输出
print("Command output:")
print(result.stdout)

# 输出命令的标准错误（如果有的话）
print("Command error (if any):")
print(result.stderr)

# 输出命令的返回码
print("Command return code:")
print(result.returncode)
