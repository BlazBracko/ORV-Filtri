import cv2 as cv
import numpy as np

def convolution(image, kernel):
    height, width = image.shape
    kernel_height, kernel_width = kernel.shape

    #komentar dodan za test vaje CI/CD
    output = np.zeros_like(image)

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

    return convolution(image, gaussian_kernel)


def filter_with_sobel_horizontal(image):
    sobel_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    return convolution(image, sobel_kernel)


def main():
    colored_photo = cv.imread('.utils/lenna.png')

    if colored_photo is None:
        print("Photo not found.")
    else:
        channels = cv.split(colored_photo)
        filtered_channels = []

        sigma = 3.0
        for channel in channels:
            filtered_channel = filter_with_gaussian_kernel(channel, sigma)
            filtered_channels.append(filtered_channel)

        gaussian_filtered_image = cv.merge(filtered_channels)

        cv.imshow('Original Image', colored_photo)
        cv.imshow('Gaussian Filtered Image', gaussian_filtered_image)

        gray_image = cv.cvtColor(gaussian_filtered_image, cv.COLOR_BGR2GRAY)
        sobel_image = filter_with_sobel_horizontal(gray_image)

        sobel_colored_image = cv.cvtColor(sobel_image, cv.COLOR_GRAY2BGR)

        mask = sobel_image > 120
        sobel_colored_image[mask] = [0, 255, 0]

        cv.imshow('Sobel Filtered Image', sobel_colored_image)

        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == '__main__':   
    main() 

    
