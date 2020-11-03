# medical-biometrics
Assignement for medicals biometrics

## Assignement 1 :
### Constructing a 3D volumetric image from 2D Biomedical images :
The objective of this lab is to highlight your skills in terms of computer vision in medical imaging.
For this purpose, we ask you to download the SCD2001_file which contains slices of the chest captured by Computed tomography scans. Read these multiple images to construct  a volumetric (3D) single image.  Finally, you have to visualize the 3D volumetric image.
Programming should be in Python. 
Submit slides, a short report and a short video presentation of your work. 

## Assignement 2 :
## 3D Brain MRI features extraction :
The objective of this lab is to highlight your skills in one of the most important steps in medical image analysis which is feature extracting
For this propose, you will work with a BRAIN 3D MRI absorption is highest in dense tissue, so the resulting should be high.
- To start, you will load the image "BRAIN.nii and check its intensity, Print the image data type, minimum, and maximum intensity, Plot the histogram and CDF cumulative distribution function.
- Then Create a tissue mask by removing all NON-BRAIN tissues , plot the brain mask in grayscale.
- Now, you will have to smooth the Brain , Set each element of the kernel to 0,11 to perform mean filtering then convolve the filter with the image and plot the result.
- Finally, filters can be used as detectors. So create filter weights that detects when intensity changes from the left to right, use only the values 1,0 and -1.convolve the image with the edge detector  and display the result.

## Assignement 3 :
## 3D brain MRI classification: application to Alzheimer diagnosis :
In this lab you will work on 3D MRI obtained from OASIS Database. 5 participants cognitively normal adults and 5 individuals at various stages of cognitive decline aged from 45 to 72 years old. You need to:

- Load these 10 nifty files.
- Segment the gray matter of each one.
- Convert the result to meshes and calculate some morphologic features.
- Run a binary classifier (SVM, LR..) and conclude.
You have to submit a short report including a presentation demo.
Programming should be in Python.
