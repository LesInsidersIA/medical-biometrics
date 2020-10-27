# import necessary packages

import imageio
import scipy.ndimage as ndi
import numpy as np
import SimpleITK as sitk
import matplotlib.pyplot as plt

# the path of a T1-weighted brain .nii image
path = "data/BRAIN.nii"


# read the .nii image containing the volume with the SimpleITK 
sitk_f = sitk.ReadImage(path)

# access to the numpy array
slices = sitk.GetArrayFromImage(sitk_f)
print("[INFOS] 2D Array slice data type :", type(slices)) #-> numpy array
print("[INFOS] 3D sitk object type      :", type(sitk_f)) #-> numpy array
print("[INFOS] Shape of 3D image array  :", slices.shape)
print("[INFOS] Shape of 2D slice array  :", slices[0].shape)
print("[INFOS] Number of slices         :", slices.shape[0])

def removeKeymapConflicts(new_keys_set):
    for prop in plt.rcParams:
        if prop.startswith('keymap.'):
            keys = plt.rcParams[prop]
            remove_list = set(keys) & new_keys_set
            for key in remove_list: 
                keys.remove(key)

def viewer3D(volume):
    removeKeymapConflicts({'n', 'l'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index], cmap='gray')
    fig.canvas.mpl_connect('key_press_event', processKey)

def processKey(event):
    fig = event.canvas.figure
    ax = fig.axes[0]
    if event.key == 'n':
        lSlice(ax)
    elif event.key == 'l':
        nSlice(ax)
    fig.canvas.draw()

def lSlice(ax):
    volume = ax.volume
    ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
    ax.images[0].set_array(volume[ax.index])

def nSlice(ax):
    volume = ax.volume
    ax.index = (ax.index + 1) % volume.shape[0]
    ax.images[0].set_array(volume[ax.index])


mask3d_array = slices > 900
mask3d_array = ndi.binary_dilation(mask3d_array, iterations=8)
mask3d_array = ndi.binary_closing(mask3d_array, iterations=8)

weights_edge = [[[1, 1, 1],
                 [0, 0, 0], 
                 [1, -1, -1]],
           
                [[1, 1, 1],
                 [0, 0, 0], 
                 [-1, -1, -1]],
           
                [[1, 1, 1],
                 [0, 0, 0], 
                 [-1, -1, -1]]]

im3d_edge = ndi.convolve(slices, weights_edge)

#viewer3D(mask_array)
#viewer3D(slices)
viewer3D(im3d_edge)
plt.show()
