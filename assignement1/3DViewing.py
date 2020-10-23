# import necessary packages 
import os
import pydicom as dicom
import numpy as np
import matplotlib.pyplot as plt

def main():

    # giving the path of dcm images
    path = "/home/yosagaf/devs/medical-biometrics/assignement1/SCD2001_files/"
    
    # let's create a slices list containing a collectiong 
    # the dicom images on a python list passing 
    CT_images = os.listdir(path)
    #print(CT_images)

    slices = [dicom.read_file(path+"/"+s, force=True) for s in CT_images]
    slices = sorted(slices, key=lambda x:x.ImagePositionPatient[2])

    image_shape = []
    image_shape.append(len(slices))
    image_shape.extend(list(slices[0].pixel_array.shape))

    #volume_3D = imageio.volread(dirname, 'DICOM') # this produce shape image of (21, 256, 256)
    
    volume3d = np.zeros(image_shape)

    for i, s in enumerate(slices):
        array2d = s.pixel_array
        volume3d[i:,:,] = array2d

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
        ax.imshow(volume[ax.index])
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

    viewer3D(volume3d)
    plt.show()

    print("")
    print("[INFOS] Type of 2D slices           : ", type(slices))
    print("[INFOS] Shape of 2D array (slice)  :", array2d.shape)
    print("[INFOS] Shape of the 3D volume     :", volume3d.shape)
    print("")

if __name__ == "__main__":
    main()

    