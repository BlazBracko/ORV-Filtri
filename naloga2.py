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

def filter_with_gaussian_kernel(image, sigma):
    kernel_size = int(2 * np.ceil(2 * sigma) + 1)

    x = np.arange(-kernel_size // 2, kernel_size // 2 + 1)
    y = np.arange(-kernel_size // 2, kernel_size // 2 + 1)
    xx, yy = np.meshgrid(x, y)

    gaussian_kernel = np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))
    gaussian_kernel /= (2 * np.pi * sigma ** 2)
    gaussian_kernel /= gaussian_kernel.sum()

    # Padding to handle edges
    padded_image = np.pad(image, [(kernel_size//2, kernel_size//2), (kernel_size//2, kernel_size//2)], mode='constant')

    # Convolution
    filtered_image = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            filtered_image[i, j] = np.sum(padded_image[i:i+kernel_size, j:j+kernel_size] * gaussian_kernel)

    return filtered_image

def filter_with_sobel_horizontal(image):
    sobel_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    return convolution(image, sobel_kernel)

if __name__ == '__main__':    
    pass
