from PIL import Image
import numpy as np

def flip_image(np_img):
    return np.fliplr(np_img), np.flipud(np_img)

def add_noise(np_img, noise_level=30):
    noise = np.random.randint(-noise_level, noise_level + 1, np_img.shape, dtype=int)
    noisy = np_img.astype(int) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def brighten_channels(np_img, increment=40):
    bright = np_img.astype(int) + increment
    return np.clip(bright, 0, 255).astype(np.uint8)

def apply_mask(np_img, mask_size=(100, 100)):
    masked = np_img.copy()
    h, w = masked.shape[:2]
    mh, mw = mask_size
    y1 = (h - mh) // 2
    x1 = (w - mw) // 2
    masked[y1:y1+mh, x1:x1+mw] = [0, 0, 0]
    return masked

img = Image.open("images/birds.jpg")
np_img = np.array(img)

h_flip, v_flip = flip_image(np_img)
Image.fromarray(h_flip).save("flip_horizontal.jpg")
Image.fromarray(v_flip).save("flip_vertical.jpg")

noisy_img = add_noise(np_img)
Image.fromarray(noisy_img).save("noisy.jpg")

bright_img = brighten_channels(np_img, 40)
Image.fromarray(bright_img).save("bright.jpg")

masked_img = apply_mask(np_img, (100, 100))
Image.fromarray(masked_img).save("masked.jpg")
