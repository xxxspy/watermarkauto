from moviepy.editor import *
import random
from pathlib import Path


fonts = TextClip.list('font')

rmd_txts = ['water marker txt']


def read_txt():
    txts = []
    fpath = Path(__file__).absolute().parent / 'markers.txt'
    if fpath.exists():
        txts = fpath.read_text(encoding='utf8').split('\n')
    return txts

def convert(fpath=r"test\inputs\test.ts", topath=None):
    fpath = Path(fpath)
    print('convert:', fpath)
    if topath is None:
        topath = fpath.parent / 'mark-{}'.format(fpath.name)
    font = random.choice(fonts[-9:])
    txtcontent = random.choice(read_txt() or rmd_txts)
    print(font, txtcontent)
    my_clip = VideoFileClip(str(fpath), audio=True)  #  The video file with audio enabled
    w,h = my_clip.size  # size of the clip
    txt = TextClip(txtcontent, font=font,
                    color='black',fontsize=24)
    txt_col = txt.on_color(size=(int(txt.w*1.2), txt.h-10),
                    color=(0,0,0), pos=(6,'center'), col_opacity=0.4)
    def move(t):
        left = t*20 % ((w+h)*2)
        if left < w - txt.w:
            x = left
            y = 0
        elif left < w + h - txt.w - txt.h:
            x = w-txt.w*1.2
            y = left-w
        elif left < w*2+h - txt.w*2 - txt.h:
            x = 2*w + h - left - txt.w*1.2
            y = h-txt.h
        else:
            x = 0
            y = 2*h+2*w-left
        return x,y
    txt_mov = txt_col.set_pos( move)
    final = CompositeVideoClip([my_clip,txt_mov])
    final.duration = my_clip.duration
    final.write_videofile(str(topath), fps=24, codec='libx264')


def dir_convert(fromdir, todir=None, suffix='.ts'):
    for fpath in Path(fromdir).iterdir():
        if fpath.suffix == suffix:
            if todir is None:
                topath = None
            else:
                topath = Path(todir) / fpath.name
            convert(fpath, topath)



if __name__ == '__main__':
    # dir_convert(r'D:\notebooks\数据分析\结构方程模型\视频教程', suffix='.mp4')
    convert(
        r'D:\notebooks\数据分析\结构方程模型\视频教程\mplus多组分析分类变量的调节效应.mp4',
        r'D:\notebooks\数据分析\结构方程模型\视频教程\mark-mplus多组分析分类变量的调节效应.mp4',
        )
