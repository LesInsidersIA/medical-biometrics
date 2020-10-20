

import glob
import sys
import pydicom
import numpy as np

def main():

    dir = "/home/yosagaf/devs/medical-biometrics/assignement1/data/*"
    
    files=[]
    print('[INFO] : DICOM data file : {}'.format(dir))
    for fname in glob.glob(dir, recursive=False):
        print("loading: {}".format(fname))
        files.append(pydicom.dcmread(fname))

    print("[INFO] File count: {}".format(len(files)))

    # skip files with no SliceLocation (eg scout views)
    slices = []
    skipcount = 0
    
    for f in files:
        if hasattr(f, 'SliceLocation'):
            slices.append(f)
        else:
            skipcount = skipcount + 1

    print("[INFO] Skipped, no SliceLocation: {}".format(skipcount))

    # ensure they are in the correct order
    slices = sorted(slices, key=lambda s: s.SliceLocation)

    # pixel aspects, assuming all slices are the same
    ps = slices[0].PixelSpacing
    ss = slices[0].SliceThickness
    ax_aspect = ps[1]/ps[0]
    sag_aspect = ps[1]/ss
    cor_aspect = ss/ps[0]

    # create 3D array
    img_shape = list(slices[0].pixel_array.shape)
    img_shape.append(len(slices))
    img3d = np.zeros(img_shape)

    # fill 3D array with the images from the files
    for i, s in enumerate(slices):
        img2d = s.pixel_array
        img3d[:, :, i] = img2d

    print("[INFO] Shape of 3D image", img3d.shape)

if __name__ == "__main__":
    main()