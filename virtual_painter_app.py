import cv2
import numpy as np


class VirtualPainter:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.setup_camera()

        self.colors_list_detect = [['blue', 94, 253, 60, 120, 255, 255],
                                   ['pink', 54, 99, 182, 173, 251, 255],
                                   ['green', 59, 94, 107, 101, 251, 255]]

        self.colors_list_paint = [[196, 77, 77],  # blue
                                  [178, 102, 255],  # pink
                                  [76, 153, 0]]  # green

        self.points_to_draw = []  # [x, y, color index]
        self.img = None
        self.img_result = np.zeros((480, 640, 3), dtype=np.uint8)

    def setup_camera(self):
        frame_width = 640
        frame_height = 480
        brightness_level = 150
        self.cap.set(3, frame_width)
        self.cap.set(4, frame_height)
        self.cap.set(10, brightness_level)

    @staticmethod
    def get_contours(image, color):
        contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        x, y, w, h = 0, 0, 0, 0

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:
                cnt_lng = cv2.arcLength(curve=contour, closed=True)
                approx = cv2.approxPolyDP(curve=contour, epsilon=0.02*cnt_lng, closed=True)

                x, y, w, h = cv2.boundingRect(array=approx)

        return x+w//2, y

    def color_detect(self, image):
        # convert the image to HSV
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        new_points = []

        for i, color in enumerate(self.colors_list_detect):
            # create a numpy array for the minimum values and the max values of h,s,v
            lower = np.array(color[1:4])  # [hue_min, sat_min, val_min]
            upper = np.array(color[4:7])  # [hue_max, sat_max, val_max]
            mask = cv2.inRange(img_hsv, lower, upper)
            x, y = self.get_contours(mask, color)

            # draw a circle at the top of the contour that we detected
            cv2.circle(img=self.img_result, center=(x, y), radius=7, color=self.colors_list_paint[i],
                       thickness=cv2.FILLED)
            # cv2.imshow(str(color[0]), mask)

            if x != 0 and y != 0:
                new_points.append([x, y, i])

        return new_points

    def draw_on_screen(self, ):
        for point in self.points_to_draw:
            cv2.circle(img=self.img_result, center=(point[0], point[1]), radius=7,
                       color=self.colors_list_paint[point[2]], thickness=cv2.FILLED)

    def clear_screen(self):
        self.points_to_draw = []
        self.img_result = self.img.copy()

    def run(self):
        while True:
            success, self.img = self.cap.read()
            self.img = cv2.flip(self.img, 1)
            self.img_result = self.img.copy()

            points = self.color_detect(image=self.img)
            if points:
                self.points_to_draw.extend(points)

            if self.points_to_draw:
                self.draw_on_screen()

            cv2.imshow("Virtual Painter", self.img_result)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c'):
                self.clear_screen()

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    painter = VirtualPainter()
    painter.run()
