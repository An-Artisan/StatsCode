#coding: utf-8
import os
import easygui as g
import  sys
#定义统计变量
source_css_code = 0
source_css_file = 0
source_js_code = 0
source_js_file = 0
source_html_code = 0
source_html_file = 0
source_python_code = 0
source_python_file = 0
source_php_file = 0
source_php_code = 0

def RecursiveFile(dir):
    "递归目录并且打印"

    # 引用全局变量
    global  source_css_code,source_css_file,source_js_code,source_js_file,source_html_code,source_html_file,source_python_code,source_python_file,source_php_file,source_php_code
    # 捕捉异常
    try :
        #打开目录并显示所有目录与文件
        list_dir = os.listdir(dir)
        # 循环所有目录和文件
        for list in list_dir:
            # 拼接路径
            file_path = os.path.join(dir, list)
            # 如果是目录则递归，是文件则打印
            if os.path.isdir(file_path):
                # 开始递归
                RecursiveFile(file_path)
            else:
                # 分离文件名和扩展名
                file_name = os.path.splitext(file_path)[1]
                # 控制台提示
                print("正在分析文件：%s..." % file_path)
                # Python文件统计
                if file_name == ".py":
                    source_python_file += 1
                    source_python_code += fileline(file_path)
                # html文件统计
                elif file_name == '.html':
                    source_html_file += 1
                    source_html_code += fileline(file_path)
                # css文件统计
                elif file_name == '.css':
                    source_css_file += 1
                    source_css_code += fileline(file_path)
                # js文件统计
                elif file_name == '.js':
                    source_js_file += 1
                    source_js_code += fileline(file_path)
                # php文件统计
                elif file_name == '.php':
                    source_php_file += 1
                    source_php_code += fileline(file_path)
    # 权限拒绝的文件，则跳过
    except PermissionError:
        return

def fileline(path):
    "统计文件的行数"

    # 打开文件，默认只读方式打开
    file_content = open(path,'r',encoding='utf-8')
    # 捕捉异常
    try:
        # 获取文件内容，返回值是根据换行组成的列表
        file_line = file_content.readlines()
        # 统计列表的长度也就是多少行
        count = len(file_line)
    #解决编码问题的异常
    except UnicodeDecodeError:
        # 赋值count为0
        count = 0
    finally:
        # 关闭文件
        file_content.close()
        # 返回行数
        return count
#提示用户
g.msgbox("选择你的工作目录，开始统计源文件以及源代码")
# 弹出选择文件夹
file_path =  g.diropenbox("选择你的本地文件夹","统计所有代码行数")
# 递归调用文件目录
RecursiveFile(file_path)
# 目标行数100000行代码
target = 100000
# 获取总的代码行
count = source_css_code + source_php_code + source_html_code + source_js_code + source_python_code
# 如果没有100000行代码则提示继续努力
if target > count:
    residue = target - count
    msg = "你目前共积累编写了 %d 行代码，完成进度：%.2f %%\n离10万行代码还差 %d 行，继续努力吧~" % (count, count / 1000, residue)
# 如果超过100000行代码则提示恭喜
else:
    residue = count - target
    msg = "你目前共积累编写了 %d 行代码，完成进度：%.2f %%\n已经超出10万行代码 %d 行，牛逼啊~~ 恭喜啊~~" % (count, count / 1000, residue)


text = "php源文件 %d 个，源代码 %d 行\n js源文件 %d 个，源代码 %d 行\n html源文件 %d 个，源代码 %d 行\n css源文件 %d 个，源代码 %d 行\n python源文件 %d 个，源代码 %d 行" % (source_php_file,source_php_code,source_js_file,source_js_code,source_html_file,source_html_code,source_css_file,source_css_code,source_python_file,source_python_code)
g.textbox(msg,"统计结束",text)

