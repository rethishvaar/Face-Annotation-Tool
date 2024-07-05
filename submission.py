import cv2
import numpy as np
import os

# Global variables
drawing = False  # True if the mouse is pressed
ix, iy = -1, -1  # Initial coordinates
ex, ey = -1, -1  # End coordinates

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, ex, ey, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            ex, ey = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        ex, ey = x, y
        cv2.rectangle(img, (ix, iy), (ex, ey), (0, 255, 0), 2)
        # Automatically save the cropped face when the mouse is released
        save_cropped_face(ix, iy, ex, ey)

def save_cropped_face(ix, iy, ex, ey):
    if ix != -1 and iy != -1 and ex != -1 and ey != -1:
        roi = img[iy:ey, ix:ex]
        cv2.imwrite("cropped_face.jpg", roi)
        print("Cropped face saved as cropped_face.jpg")

def main():
    global img
    
    image_path = r"C:\Users\rethi\Downloads\face cut\Ro.jpg"
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found.")
        return

    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load {image_path}.")
        return
    
    cv2.putText(img, 'choose', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2, cv2.LINE_AA)  # Orange color
    cv2.putText(img, ' top left corner', (120, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)  # White color
    cv2.putText(img, ' and drag this', (370, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)  # Green color

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", draw_rectangle)

    while True:
        cv2.imshow("image", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Press 'q' to exit
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
