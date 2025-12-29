import cv2
import numpy as np
import os
import PIL.Image as Image
import PIL.ImageEnhance as IE
import PIL.ImageFilter as IF


degradation_levels = ['mild', 'moderate', 'severe']
class_names = ['01_palm', '02_l', '03_fist', '04_fist_moved', '05_thumb', '06_index', '07_ok', '08_palm_moved', '09_c', '10_down']


def apply_degradation(image, output_folder, level):
    img = cv2.imread(image)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(img_rgb)

    if level == 'mild':
        # pil_image = pil_image.filter(IF.GaussianBlur(radius=1))
        enhancer = IE.Contrast(pil_image)
        pil_image = enhancer.enhance(0.8)
    elif level == 'moderate':
        # pil_image = pil_image.filter(IF.GaussianBlur(radius=2))
        enhancer = IE.Contrast(pil_image)
        pil_image = enhancer.enhance(0.5)
    elif level == 'severe':
        # pil_image = pil_image.filter(IF.GaussianBlur(radius=3))
        enhancer = IE.Contrast(pil_image)
        pil_image = enhancer.enhance(0.25)

    degraded_img_rgb = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    degraded_img_bgr = cv2.cvtColor(degraded_img_rgb, cv2.COLOR_RGB2BGR)

    name = os.path.basename(image)
    name1, ext = os.path.splitext(name)
    name2 = f"{name1}_{level}{ext}"
    output_path = os.path.join(output_folder, name2)
    cv2.imwrite(output_path, degraded_img_bgr)

    return output_path

def process_folder(input_folder, output_folder, level):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for name in os.listdir(input_folder):
        if name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(input_folder, name)
            apply_degradation(image_path, output_folder, level)


# Example usage:
if __name__ == "__main__":
    input_folder = 'D:/prototype/data/leapGestRecog/test'
    for level in degradation_levels:
        for classes in class_names:
            input_folder = f'D:/prototype/data/leapGestRecog/test/{classes}'
            output_folder = f'D:/prototype/degradation/test/{level}/{classes}'
            process_folder(input_folder, output_folder, level)        