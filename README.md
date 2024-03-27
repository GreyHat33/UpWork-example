# Fixing a current error on the code

So I have found a github repository:

- https://github.com/peduajo/geetest-slice-captcha-solver?tab=readme-ov-file 

that can get you a distance between a board that is missing a puzzle and the missing puzzle:

![image](https://github.com/FraneCal/UpWork-example/assets/90317417/578ddd75-ad4f-489a-88e4-9b31df9df9a6)

I have copied the file solver.py from the given link, and added it to my code scraper.py. So my codes gets the two images and saves them, as desbriced in the function solver_captcha_slider. After it has save them (as shown in the next images)

![image](https://github.com/FraneCal/UpWork-example/assets/90317417/df21c782-f160-4c7e-a3dc-96efac76ad02) ![image](https://github.com/FraneCal/UpWork-example/assets/90317417/c54a3374-272d-4142-a865-68397fcd5437)

I would like to use the PuzleSolver class from the solver.py to get the distance (under the variable solution) between them, and later on use that distance to move the missing piece to the board. But when it runs the code I get the following error message: 

File "c:\Users\xxxxx\OneDrive - xxxxx SA\Documents\German site\solver.py", line 17, in get_position
res = cv2.matchTemplate(background, template, cv2.TM_CCOEFF_NORMED)
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
cv2.error: OpenCV(4.9.0) D:\a\opencv-python\opencv-python\opencv\modules\imgproc\src\templmatch.cpp:588: error: (-215:Assertion failed) corr.rows <= img.rows + templ.rows - 1 && corr.cols <= img.cols + templ.cols - 1 in function 'cv::crossCorr'

for the function (in solver.py):

def get_position(self):
        template, x_inf, y_sup, y_inf = self.__piece_preprocessing()
        background = self.__background_preprocessing(y_sup, y_inf)

        res = cv2.matchTemplate(background, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc

        origin = x_inf
        end = top_left[0] + PIXELS_EXTENSION

        return end - origin


How can I fix this issue so that I get the distance between them?

P.S. The puzzle captcha does not appear always, so you will need to run the program a couple of times.



