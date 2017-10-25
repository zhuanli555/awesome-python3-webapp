import os.path

def match_line(path):#一个文件的行数
    count = 0
    pattern = r'[^\s]'
    with open(path,'rb') as f:
        for line in f.readlines():
            if line != b'\r\n':
                count = count + 1
        return count

def match_line_white(path):#一个文件的行数include space
    pattern = r'[^\s]'
    with open(path,'rb') as f:
        return len(f.readlines())

def main():
    count = 0
    count_white = 0
    for rt,dirs,files in os.walk('.'):#可以是任意目录
        for file in files:
            base,suffix = os.path.splitext(file)
            if suffix != '.py' and suffix != '.java' and suffix != '.c' and suffix != '.cpp':
                continue;
            filepath = os.path.join(rt,file)
            count = count + match_line(filepath)
            count_white = count_white + match_line_white(filepath)
        output = 'line count is %d,line count with space is %d' %(count,count_white)
    print(output)
    return output

if __name__ == '__main__':
    main()