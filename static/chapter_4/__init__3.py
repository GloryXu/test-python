# 文件
print('Make a new file in output mode')
f = open('data.txt' ,'w')
print('Writes strings of bytes to it')
print(f.write('Hello\n'))
print(f.write('world\n'))
print('Close to flush output buffers to disk')
f.close()

# 'r' is the default processing mode.
f = open('data.txt')
text = f.read()
print(text)
print(text.split())

print('---------------')
print(dir(f))

print(help(f.seek))