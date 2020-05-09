import os
import matplotlib.pyplot as plt
from skimage import transform

# root path depends on your computer
root = '/home/sk002/Downloads/Nvidia_fake/1m_faces_01/1m_faces_01/'
save_root = '/home/sk002/Downloads/Nvidia_fake/'
resize_size = 256

if not os.path.isdir(save_root):
    os.mkdir(save_root)
if not os.path.isdir(save_root + 'fake1'):
    os.mkdir(save_root + 'fake1')

img_list = os.listdir(root)

# ten_percent = len(img_list) // 10
count=0
for i in range(len(img_list)):
    # print(count)
    # count+=1
    img = plt.imread(root + img_list[i])
    try:
        img = transform.resize(img, (resize_size, resize_size))
    except (ValueError):
        continue
    plt.imsave(fname=save_root + 'fake1/2_' + img_list[i], arr=img)

    if (i % 1000) == 0:
        print('%d images complete' % i)
