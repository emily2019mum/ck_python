"""
编写一个Python程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来。
"""
file_name = "my_file.txt"
content = "Hello,this is a text file"
# 写入文件
with open(file_name,"w") as file:
    file.write(content)
    print(f"内容已写入文件：{file_name}")
# 读取文件
with open(file_name,"r") as file:
    file_content = file.read()
    print(f"读取到的文件内容：\n{file_content}")