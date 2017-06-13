# -*- coding:utf-8 -*-
# 导入需要的包
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# 构造参数解析器并解析参数
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="图片路径")
args = vars(ap.parse_args())

# 载入并显示图片
image = cv2.imread(args["image"])
cv2.imshow("image", image)
# cv2.waitKey(0)

# 将图片转化为灰度图，并建立直方图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
# cv2.waitKey(0)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
# plt.show()

# 获取图像通道，初始化颜色数组，展平特征向量
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
features = []

# 循环图像的颜色通道
for (chan, color) in zip(chans, colors):
    # 建立当前颜色通道的直方图并将全部直方图串联起来
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    features.extend(hist)

    # 显示直方图
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
# plt.show()

# 这里我们只是简单的将每个颜色通道的直方图维度相加
# 256 × 3 = 768 ，在实践中，通常不会为每个通道设置
# 256个bins,一般是选择32-96个bins,具体值取决于应用需要
print "flattened feature vector size: %d" % (np.array(features).flatten().shape)

# 我们来看下2D直方图，现在我把直方图的数量从256减少至32，
# 这让我们可以更好的查看结果
fig = plt.figure()

# 呈现绿色和蓝色的2D颜色直方图
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for Green and Blue")
plt.colorbar(p)

# 呈现绿色和红色的2D颜色直方图
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None,
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for Green and Red")
plt.colorbar(p)

# 呈现蓝色和红色的2D颜色直方图
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for Blue and Red")
plt.colorbar(p)

# 最后，我们来检查2D直方图的维度
print "2D histogram shape: %s, with %d values" % (
    hist.shape, hist.flatten().shape[0])

plt.show()
cv2.waitKey(0)
