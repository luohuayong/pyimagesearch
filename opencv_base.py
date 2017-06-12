# -*- coding:utf-8 -*-
# 导入需要的包
import cv2

# 载入图像并显示
image = cv2.imread("jurassic-park-tour-jeep.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

# 输出图像尺寸
print image.shape

# 保持图片的宽高等比例缩放，以保证图片显示不变形
# 计算新图片相对于旧图片的比例
r = 100.0/image.shape[1]
dim = (100, int(image.shape[0]*r))

# 执行图片缩放，并显示
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)

# 获取图片尺寸并计算图片中心点
(h, w) = image.shape[:2]
center = (w/2, h/2)

# 将图像旋转180度
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated", rotated)
cv2.waitKey(0)

# 使用numpy数组切片对图像进行剪裁
cropped = image[70:170, 440:540]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)

# 将剪切后的图片以PNG格式保存至磁盘
cv2.imwrite("thumbnail.png", cropped)

