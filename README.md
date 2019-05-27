# Digits
Handwritten digits recognition trained with augmented MNIST and USPS dataset.

The practical results of MNIST for digit recognition is poor. So I combined the dataset of MNIST and USPS, modified the datasets by removing some abnormal images, redesigned a new model named 3x3, and trained the model from scratch. The result is promising. 

# Requirements:
caffe

# Procedure:
1, Download the MNIST and USPS datasets.

2, Convert the MNIST dataset to images.
  > python3 convert_mnist.py
  
3, Check the datasets and remove the abnormal digits mannualy, which will harm the accuracy of the results.

4, Convert the USPS images to MNIST format.
  >

5, Image augmentation.
  > python3 run_augmentation.py mnist/train/ mnist/augmented 250000 --rotate_angle=30 --p_mirror=0 --p_hsv=0 --p_gamma=0
  
  > python3 run_augmentation.py usps/train/ usps/augmented 100000 --rotate_angle=30 --p_mirror=0 --p_hsv=0 --p_gamma=0 
  
6, Generate the image and label lists.
  > python3 gen_caffe_imglist.py mnist/train mnist.txt
  
  > python3 gen_caffe_imglist.py mnist/augmented mnist_aug.txt
  
  > python3 gen_caffe_imglist.py usps/train usps.txt
  
  > python3 gen_caffe_imglist.py usps/augmented usps_aug.txt
  
  > cat mnist.txt mnist_aug.txt usps.txt usps_aug.txt> train_mnist_usps.txt
  
7, Convert the images into LMDB with the lists generated in last step.
  > /.../caffe/build/tools/convert_imageset ./ train_mnist_usps.txt train_mnist_usps_lmdb --resize_width=28 --resize_height=28 --gray --shuffle
  
8, Prepare the prototxt files. Different from the well-known LeNet I use another model for the training which i call 3x3.

9, Start training.
  > /.../caffe/build/tools/caffe train -solver 3x3_mnist_usps_solver.prototxt -gpu 0 -log_dir ./train_mnist_usps_Log

The result is very nice.
