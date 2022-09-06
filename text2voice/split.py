from nnsplit import NNSplit
import re
import time
from datetime import datetime




def parseline(line):
    fmt = '<p begin="(.+)" end="(.+)" style=".+">(.+)</p>'
    match = re.match(fmt, line)
    if match is None:
        return None
    begin, end, content = match.groups(0)
    content = content.replace('&#39;', "'")
    datefmt = '%H:%M:%S.%f'
    begin = datetime.strptime(begin, datefmt)
    end = datetime.strptime(end, datefmt)
    perworddur = (end-begin)/len(content.split(' '))
    return (begin, end, content, perworddur)

def format(path: str):
    content = ''
    timedata = []
    with open(path, 'r', encoding='utf8') as f:
        for line in f.read().split('\n'):
            parsed = parseline(line)
            print(parsed)
            if parsed is not None:
                timedata.append(parsed)
                if content:
                    content += ' '
                content += parsed[2]
    return content, timedata


def split(path: str):
    splitter = NNSplit(r"G:\python3.9\Lib\site-packages\nnsplit-0.5.8_post0.dist-info\models\en\model.onnx")
    content, timedata = format(path)
    print(content, timedata)
    splits = splitter.split([content, ])[0]
    segcontent = '\n'.join([str(s) for s in splits])
    with open('{}.segs.txt'.format(path), 'w', encoding='utf8') as f:
        f.write(segcontent)



if __name__ == '__main__':
    print(parseline('<p begin="00:00:05.120" end="00:00:08.880" style="s2">in this video</p>'))
    split(r'D:\mysites\watermarkauto\text2voice\test.subtitles.xml')

