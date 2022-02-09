### 安装

最关键的就是安装`moviepy`这个库, 方法是`pip install moviepy`, 但是这个库依赖另外一个工具`IMAGEMAGICK`, 
这个软件需要你从这里下载: https://imagemagick.org/script/download.php

等你安装完`IMAGEMAGICK`, 你需要设置环境变量`IMAGEMAGICK_BINARY`, 例如`G:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe`,
这样你的moviepy就可以找到你的`IMAGEMAGICK`安装位置了.

### 使用

所有代码写在`watermarkauto/__init__.py`,
你只需要修改最后面的代码:

```py
if __name__ == '__main__':
    dir_convert('test/inputs', 'test/outputs', suffix='.ts')
```


`dir_convert`有三个参数: 
    - 第一个参数是输入文件夹, 该文件夹中应该存有你需要添加水印的视频
    - 第二个参数是输出文件夹, 添加水印后的视频会保存到该文件夹中
    - 第三个参数是文件格式的后缀名, 只有你设置的格式的视频文件才会被转换, 其他格式不会被转换

将代码设置完之后, 你就可以运行代码:

`python watermarkauto/__init__.py`