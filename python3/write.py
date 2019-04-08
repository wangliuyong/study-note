def save_file(name,count,value):
    file_name = './test/' + name + str(count) + '.txt'
    f = open(file_name,'w',encoding='utf8')
    f.writelines(value)
    f.close()


def split_file(_file):
    f = open(_file,encoding='utf8')
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
            save_file('boy',count,san[count-1:])
            save_file('girl',count,si[count-1:])
            count += 1
    print('san: \n',san,' \n','si: \n',si)
    f.close()

split_file('example.txt')