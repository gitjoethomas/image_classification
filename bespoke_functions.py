import os
import cv2


def import_data(folder):
        
    """
    reads in all images for files in either datafiles/train/ or datafiles/test/, and applies the correct label for the 
    relevant folder
    """
    
    label_dict = {'buildings':0, 'forest':1, 'glacier':2, 'mountain':3, 'sea':4, 'street':5}
    image_list = []
    label_list = []
    
    for image_category in os.listdir(f'datafiles/{folder}'):
#         label = label_dict.get(image_category)
        
        for image in os.listdir(f'datafiles/{folder}/{image_category}'):
            
            img = cv2.imread(f'datafiles/{folder}/{image_category}/{image}')
            img = cv2.resize(img, (150, 150))
            
            image_list.append(img)
            label_list.append(image_category)
            
    return image_list, label_list