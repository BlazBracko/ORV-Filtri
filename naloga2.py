import cv2 as cv
import numpy as np

def convolution(image, kernel):
    height, width = image.shape
    kernel_height, kernel_width = kernel.shape

    output = null

    padding_v = kernel_height // 2
    padding_s = kernel_width // 2

    padded_image = np.pad(image, ((padding_v, padding_v), (padding_s, padding_s)), mode='constant', constant_values=0)

    for x in range(height):
        for y in range(width):
            patch = padded_image[x:x + kernel_height, y:y + kernel_width]
            output[x, y] = np.sum(patch * kernel)

    return output

def filtriraj_z_gaussovim_jedrom(slika,sigma):
    '''Filtrira sliko z Gaussovim jedrom..'''
    pass

def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''
    pass

if __name__ == '__main__':    
    pass
