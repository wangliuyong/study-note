

f = open('./example.txt',encoding='utf8')

san = []
si = []
count = 1
for each_line in f:
    
    if each_line[:6] != '======':
        lineArr = each_line.split('：')
        print(lineArr)
        name = lineArr[0]
        say = lineArr[1].rstrip()
        if name == '张三':
            san.append(say)
        elif name == '李四':
            si.append(say)
    else:
        boy = './test/boy' + str(count) + '.txt'
        girl = './test/girl' + str(count) + '.txt'
        save_boy = open(boy,'w',encoding='utf8')
        save_boy.writelines(san[count-1:])
        save_boy.close()
        save_girl = open(girl,'w',encoding='utf8')
        save_girl.writelines(si[count-1:])
        count += 1
        save_girl.close()

print('san: \n',san,' \n','si: \n',si)

f.close()













f.close()