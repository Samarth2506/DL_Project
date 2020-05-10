# Using GANs for DeepFake Image Detection

 **_Deep Learning Project - Final Project Code - Team ID: 12_**
 * **Contributors**: Aditya Upadhyayula, Amrit Nidhi, Samarth Marudheri, Shreyash Kumar

 ---

![Fake/Reconstructed images generated from trained autoGAN model.](/imgs/fake_images.png) 

 ---

 * Link for the data : https://drive.google.com/open?id=19tf6fir

 * Accuracy and loss plots for all models are uploaded in the plots folder.

 ---

*  Below is a description of the scripts submitted in the order of workflow of the project:
git a
1. **convert_img.py** : The scripts downsized the .jpg image to a size of 64x64. After resizing, the all images are stored as Numpy arrays.

2. **GAN_train.ipynb** : The script adversarially trains an autoencoder to reconstruct images from real images in the celebA dataset (trains autoGAN model). 

3. **GenerateFakes.ipynb** : The script loads in the trained autoGAN model to generate fake/reconstructed images based on input image (pair-wise generation).

4. **CNN_classifier.ipynb** : The script trains and predicts a simple CNN based classifier as per the workflow described in the report.

5. **DCGAN_classifier.ipynb** : The script trains and predicts using a DCGAN based classifier as per the approach described in the report.