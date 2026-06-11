
Question 8:
  A) False because cv2.imread() loads the images in BGR format but not in RGB format
  B) True.  The rectangle will not appear green because the image is converted to grayscale and basically,
    a grayscale image cannot display colored rectangles.
  C) True.  cv2.waitKey(1) waits for only 1 milisecond which is too short for viewing an image,so the image
    window closes almost immediately. That is why cv2.waitKey(0) should be used to keep the image window
    until any key is pressed.
  D) False because the coordinates (10,10) and (100,100) specify two opposite corners of the rectangle,not the
    center and size of the rectangle.

   Correct Statements: B and C
