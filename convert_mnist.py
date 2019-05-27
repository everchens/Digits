import os
import gzip
import pickle
from matplotlib import pyplot

# Load the dataset， 从压缩文件读取MNIST数据集：
print('Loading data from mnist.pkl.gz ...')
with gzip.open('mnist.pkl.gz', 'rb') as f:
    train_set, valid_set, test_set = pickle.load(f, encoding='bytes')
 
#在当前路径下生成mnist文件夹
imgs_dir = 'mnist'
os.system('mkdir -p {}'.format(imgs_dir))
 
#datasets是个字典 键-值对 dataname-dataset 对
datasets = {'train': train_set, 'val': valid_set, 'test': test_set}
for dataname, dataset in datasets.items():
    print('Converting {} dataset ...'.format(dataname))
    data_dir = os.sep.join([imgs_dir, dataname])    #字符串拼接
    os.system('mkdir -p {}'.format(data_dir))       #生成对应的文件夹
    
    # i代表数据的序号，用zip()函数读取对应的位置的图片和标签
    for i, (img, label) in enumerate(zip(*dataset)):
        filename = '{:0>6d}_{}.jpg'.format(i, label)
        filepath = os.sep.join([data_dir, filename])
        img = img.reshape((28, 28)) #将一维数组还原成二维数组
        #用pyplot保存可以自动归一化生成像素值在[0,255]之间的灰度图
        pyplot.imsave(filepath, img, cmap='gray')
        if (i+1) % 10000 == 0:
            print('{} images converted!'.format(i+1))
