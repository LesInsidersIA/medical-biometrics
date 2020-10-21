

import glob
import sys
import os
import pydicom as dicom
import numpy as np
import matplotlib.pyplot as plt

def main():

    path = "/home/yosagaf/devs/medical-biometrics/assignement1/data/"
    
    # let's save the dicom images on a python list
    CT_images = os.listdir(path)
    print(CT_images)

    slices = [dicom.read_file(path+"/"+s, force=True) for s in CT_images]
    slices = sorted(slices, key=lambda x:x.ImagePositionPatient[2])

    pixel_spacing = slices[0].PixelSpacing
    slice_thickness = slices[0].SliceThickness
     
    axial_aspect_ratio = pixel_spacing[1]/pixel_spacing[0]
    sagital_aspect_ratio = pixel_spacing[1]/slice_thickness
    coronal_aspect_ratio = slice_thickness/pixel_spacing[0]

    print("Pixel spacing         :", pixel_spacing)
    print("Slice thickness       :", slice_thickness)
    print("Pixel spacing         :", axial_aspect_ratio)
    print("Sagital aspect ratio  :", sagital_aspect_ratio)
    print("Coronal aspect ratio  :", coronal_aspect_ratio)

    image_shape = []
    image_shape.append(len(slices))
    image_shape.extend(list(slices[0].pixel_array.shape))
    
    print(image_shape)
    
    volume3d = np.zeros(image_shape)

    for i, s in enumerate(slices):
        array2d = s.pixel_array
        volume3d[i:,:,] = array2d

    print("Array 2D shape        :", array2d.shape)
    print("Volume 3D shape       :", volume3d.shape)

    def remove_keymap_conflicts(new_keys_set):
        for prop in plt.rcParams:
            if prop.startswith('keymap.'):
                keys = plt.rcParams[prop]
                remove_list = set(keys) & new_keys_set
                for key in remove_list:
                    keys.remove(key)

    def multi_slice_viewer(volume):
        remove_keymap_conflicts({'j', 'k'})
        fig, ax = plt.subplots()
        ax.volume = volume
        ax.index = volume.shape[0] // 2
        ax.imshow(volume[ax.index])
        fig.canvas.mpl_connect('key_press_event', process_key)

    def process_key(event):
        fig = event.canvas.figure
        ax = fig.axes[0]
        if event.key == 'j':
            previous_slice(ax)
        elif event.key == 'k':
            next_slice(ax)
        fig.canvas.draw()

    def previous_slice(ax):
        volume = ax.volume
        ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
        ax.images[0].set_array(volume[ax.index])

    def next_slice(ax):
        volume = ax.volume
        ax.index = (ax.index + 1) % volume.shape[0]
        ax.images[0].set_array(volume[ax.index])

    multi_slice_viewer(volume3d)
    plt.show()

if __name__ == "__main__":
    main()

    