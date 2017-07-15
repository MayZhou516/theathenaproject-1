''' 
Most of the code taken from 
http://hanzratech.in/2015/02/24/handwritten-digit-recognition-using-opencv-sklearn-and-python.html
'''

# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

# Load the classifier
clf = joblib.load("digits_cls.pkl")


def readNum(im):
    # Convert to grayscale and apply Gaussian filtering
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

    # Threshold the image
    ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the image
    _, ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get rectangles contains each contour
    rects = [cv2.boundingRect(ctr) for ctr in ctrs]


    # For each rectangular region, calculate HOG features and predict
    # the digit using Linear SVM.
    nums = []
    for rect in rects:
        # Draw the rectangles
        cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
        # Make the rectangular region around the digit
        leng = int(rect[3] * 1.6)
        pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
        pt2 = int(rect[0] + rect[2] // 2 - leng // 2)

        # i'm pretty sure I mixed up the x and y axes
        rightmost, bottommost = im_th.shape
        left = max(pt1, 0)
        right = min(pt1+leng, rightmost)
        top = max(pt2, 0)
        bottom = min(pt2+leng, bottommost)

        roi = im_th[left:right, top:bottom]
        # Resize the image

        if(min(roi.shape) < 1):
            continue
        roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
        roi = cv2.dilate(roi, (3, 3))
        # Calculate the HOG features
        roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
        nbr = clf.predict(np.array([roi_hog_fd], 'float64'))

        # should be sorting by left, but I think I mixed up the axes. this at least works
        nums.append((top, nbr))
        #cv2.putText(im, str(int(nbr[0])), (rect[0], rect[1]+50),cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 3)

    nums.sort()
    return ''.join([str(int(x[1][0])) for x in nums])

'''
# Read the input image 
im = cv2.imread("test_ocr/test_ocr_8.png")
print(readNum(im))
'''
