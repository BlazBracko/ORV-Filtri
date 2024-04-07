import naloga2

def test_image_loading(self):
        # Preverite, ali se slika pravilno naloži
        image = cv.imread('/lenna.png')
        self.assertIsNotNone(image, "Failed to load image.")
  
def test_filter_dimensions(self):
        # Preverite, ali filtriranje ohranja dimenzije slike
        image = np.zeros((100, 100), dtype=np.uint8)
        sigma = 1.0
        filtered_image = main.filter_with_gaussian_kernel(image, sigma)
        self.assertEqual(image.shape, filtered_image.shape, "Filter changes image dimensions.")

def test_sobel_horizontal(self):
        # Preprost test za preverjanje delovanja Sobelovega filtra
        image = np.zeros((100, 100), dtype=np.uint8)
        image[50, :] = 255  # Ustvari horizontalno črto
        sobel_image = main.filter_with_sobel_horizontal(image)
        # Preverite, ali Sobelov filter zazna spremembo intenzitete
        self.assertTrue(np.any(sobel_image == 255), "Sobel filter failed to detect horizontal edge.")
