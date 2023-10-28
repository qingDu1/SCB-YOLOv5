
首先创建python3.8的虚拟环境，请在命令行中执行下列操作：

```bash
conda create -n yolo5 python==3.8.5
conda activate yolo5
```

### pytorch安装（gpu版本和cpu版本的安装）

实际测试情况是YOLOv5在CPU和GPU的情况下均可使用，不过在CPU的条件下训练那个速度会令人发指，所以有条件的小伙伴一定要安装GPU版本的Pytorch，没有条件的小伙伴最好是租服务器来使用。

GPU版本安装的具体步骤可以参考这篇文章：[2021年Windows下安装GPU版本的Tensorflow和Pytorch_dejahu的博客-CSDN博客](https://blog.csdn.net/ECHOSON/article/details/118420968)

需要注意以下几点：

* 安装之前一定要先更新你的显卡驱动，去官网下载对应型号的驱动安装
* 30系显卡只能使用cuda11的版本
* 一定要创建虚拟环境，这样的话各个深度学习框架之间不发生冲突

我这里创建的是python3.8的环境，安装的Pytorch的版本是1.8.0，命令如下：

```cmd
conda install pytorch==1.8.0 torchvision torchaudio cudatoolkit=10.2 # 注意这条命令指定Pytorch的版本和cuda的版本
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cpuonly # CPU的小伙伴直接执行这条命令即可
```

安装完毕之后，我们来测试一下GPU是否

![image-20210726172454406](https://vehicle4cm.oss-cn-beijing.aliyuncs.com/typoraimgs/image-20210726172454406.png)

### pycocotools的安装

<font color='red'>后面我发现了windows下更简单的安装方法，大家可以使用下面这个指令来直接进行安装，不需要下载之后再来安装</font>

```
pip install pycocotools-windows
```

### 其他包的安装

另外的话大家还需要安装程序其他所需的包，包括opencv，matplotlib这些包，不过这些包的安装比较简单，直接通过pip指令执行即可，我们cd到yolov5代码的目录下，直接执行下列指令即可完成包的安装。

```bash
pip install -r requirements.txt
pip install pyqt5
pip install labelme
```

### 测试一下

在yolov5目录下执行下列代码

```bash
python detect.py --source data/images/bus.jpg --weights pretrained/yolov5s.pt
```

执行完毕之后将会输出下列信息

![image-20210610111308496](https://vehicle4cm.oss-cn-beijing.aliyuncs.com/typoraimgs/image-20210610111308496.png)

在runs目录下可以找到检测之后的结果

![image-20210610111426144](https://vehicle4cm.oss-cn-beijing.aliyuncs.com/typoraimgs/image-20210610111426144.png)

按照官方给出的指令，这里的检测代码功能十分强大，是支持对多种图像和视频流进行检测的，具体的使用方法如下：

```bash
 python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```
















