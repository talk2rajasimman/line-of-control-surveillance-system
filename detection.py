import cv2
import argparse
import orien_lines
import datetime
from utils import detector_utils as detector_utils
from datetime import date
import numpy as np
from imutils.video import FPS


lst1 = []
lst2 = []
ap = argparse.ArgumentParser()
ap.add_argument('-d', '--display', dest='display', type=int,
                default=1, help='Display the detected images using OpenCV. This reduces FPS')

# ap.add_argument('-d', '--orientation', dest='display', type=int,
#                 default='lr', help='help to draw line right or left')

# ap.add_argument('-d', '--line_position', dest='display', type=int,
#                 default=35, help='help to draw line right or left')

args = vars(ap.parse_args())

detection_graph, sess = detector_utils.load_inference_graph()


if __name__ == '__main__':

    score_thresh = 0.60

    Orientation = 'lr'

    # 'video/VID_20211223_142032.mp4'
    cap = cv2.VideoCapture('video/video_2021-12-28_12-01-00.mp4')

    Line_Perc = float(35)

    # Used to calculate fps
    start_time = datetime.datetime.now()
    num_frames = 0

    im_height, im_width = (None, None)

    fps = cap.get(cv2.CAP_PROP_FPS)
    print('video fps :', fps)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print('total frames :', length)

    count = 0
    skip = 1

    # We need to set resolutions.
    # so, convert them from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    size = (frame_width, frame_height)

    # Below VideoWriter object will create
    # a frame of above defined The output
    # is stored in 'filename.avi' file.
    result = cv2.VideoWriter('filename.avi',
                             cv2.VideoWriter_fourcc(*'MJPG'),
                             10, size)

    while True:

        ret, frame = cap.read()
        frame = np.array(frame)

        if count % skip == 0:
            print(count)

            if im_height == None:
                im_height, im_width = frame.shape[:2]

            boxes, scores, classes = detector_utils.detect_objects(
                frame, detection_graph, sess)

            Line_Position = orien_lines.drawsafelines(
                frame, Orientation, Line_Perc)

            detector_utils.draw_box_on_image(
                2, score_thresh, scores, boxes, classes, im_width, im_height, frame, Line_Position, Orientation)

            num_frames += 1
            elapsed_time = (datetime.datetime.now() -
                            start_time).total_seconds()
            fps = num_frames / elapsed_time

            detector_utils.draw_text_on_image(
                "FPS : " + str("{0:.2f}".format(fps)), frame)

            result.write(frame)

            cv2.imshow('Detection', frame)
            # cv2.resizeWindow(win_name, width, height)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        count += 1

    cap.release()
