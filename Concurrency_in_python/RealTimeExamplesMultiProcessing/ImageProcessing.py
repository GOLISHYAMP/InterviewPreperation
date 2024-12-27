from multiprocessing import Pool
import cv2

def process_image(image_path):
    image = cv2.imread(image_path)
    return cv2.GaussianBlur(image, (5,5), 0)

if __name__ == "__main__":
    image_paths = ["images/image1.jpg", "images/image2.jpg", "images/image3.jpg"]
    with Pool(processes=4) as pool:
        results = pool.map(process_image, image_paths)
    
    for result in results:
        cv2.imshow('image', result)
        cv2.waitKey(0)
