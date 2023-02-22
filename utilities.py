import matplotlib.pyplot as plt
import cv2

orb = cv2.ORB_create(nfeatures=1000)

#############################################################################
# The following article was referred to for writing the below lines of code.
# https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html

def find_top_matches(ip1,ip2, top_n =4):

  '''
  Given 2 input image paths, and a number top_n, returns a list of tuples with
  each tuple containing 2 more tuples with the coordinates of the top top_n matched 
  feature points in image 1 and 2 respectively.
  '''

  #Get Descriptors for image 1
  img1 = cv2.imread(ip1, cv2.IMREAD_GRAYSCALE)

  # detect features 
  (keypoints1, descriptors1) = orb.detectAndCompute(img1, None)

  #Get Descriptors for image 2
  img2 = cv2.imread(ip2, cv2.IMREAD_GRAYSCALE)

  # detect features 
  (keypoints2, descriptors2) = orb.detectAndCompute(img2, None)

  import cv2 as cv
  # create BFMatcher object
  bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
  # Match descriptors.
  matches = bf.match(descriptors1,descriptors2)
  # Sort them in the order of their distance.
  matches = sorted(matches, key = lambda x:x.distance)

  #TO DRAW LINES BETWEEN THE MATCHING POINTS IN BOTH THE IMAGES
  # # Draw first 10 matches.
  # img3 = cv.drawMatches(img1,keypoints1,img2,keypoints2,matches[:top_n],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

  # # img3 = cv.drawMatches(img1,keypoints1,img2,keypoints2,matches,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
  # plt.imshow(img3)
  # plt.show()

  matches = matches[:top_n]
  match_coordinates = [(keypoints1[match.queryIdx].pt,keypoints2[match.trainIdx].pt) for match in matches]

  #TO PLOT THE MATCHING POINTS IN THE IMAGES
  # for mc1, mc2 in match_coordinates:
  #   for j in range(-30, 30):
  #     img1[int(mc1[1])+j, int(mc1[0])+j] = 0 
  #     img1[int(mc1[1])-j, int(mc1[0])+j] = 255 

  #     img2[int(mc2[1])+j, int(mc2[0])+j] = 0 
  #     img2[int(mc2[1])-j, int(mc2[0])+j] = 255 

  #     # img2[int(k1.pt[1])+j, int(k1.pt[0])+j] = 0 
  #     # img2[int(k1.pt[1])-j, int(k1.pt[0])+j] = 255 

  # plt.imshow(img1)
  # plt.show()
  # plt.imshow(img2)
  # plt.show()

  return match_coordinates

# The following article was referred to for writing the above lines of code.
# https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html
#############################################################################
