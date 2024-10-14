from PIL import Image
import numpy as np
import tifffile

def read_tiff(file_path="run5_grphite_image/image"):
    # שימוש בספריית tifffile לטעינת כל התמונות כ-numpy array
    image = tifffile.imread(file_path)
    return image


def group_tiff(image, n=1):
    if n == 1:
        return image.sum(axis=0)
    
    # חישוב מספר התמונות בכל קבוצה
    images_per_group = image.shape[0] // n
    
    # יצירת מערך חדש לאחסון התוצאות
    grouped_images = np.zeros((n,) + image.shape[1:], dtype=image.dtype)
    
    for i in range(n):
        start_idx = i * images_per_group
        end_idx = (i + 1) * images_per_group if i < n - 1 else image.shape[0]
        grouped_images[i] = image[start_idx:end_idx].sum(axis=0)
    
    return grouped_images

