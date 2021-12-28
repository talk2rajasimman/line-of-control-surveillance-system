import cv2
# from mailer import Mailer
from telegram import Telegram


def drawboxtosafeline(image_np, p1, p2, Line_Position2, Orientation):

    #global crossed
    if(Orientation == "bt"):
        bounding_mid = (int((p1[0]+p2[0])/2), int(p1[1]))
        if(bounding_mid):
            cv2.line(img=image_np, pt1=bounding_mid, pt2=(bounding_mid[0], Line_Position2), color=(
                255, 0, 0), thickness=1, lineType=8, shift=0)
            distance_from_line = bounding_mid[1]-Line_Position2
    elif(Orientation == "tb"):
        bounding_mid = (int((p1[0]+p2[0])/2), int(p2[1]))
        if(bounding_mid):
            cv2.line(img=image_np, pt1=bounding_mid, pt2=(bounding_mid[0], Line_Position2), color=(
                255, 0, 0), thickness=1, lineType=8, shift=0)
            distance_from_line = Line_Position2-bounding_mid[1]
    elif(Orientation == "lr"):
        bounding_mid = (int(p2[0]), int((p1[1]+p2[1])/2))
        if(bounding_mid):
            cv2.line(img=image_np, pt1=bounding_mid, pt2=(Line_Position2, bounding_mid[1]), color=(
                255, 0, 0), thickness=1, lineType=8, shift=0)
            distance_from_line = Line_Position2-bounding_mid[0]
    elif(Orientation == "rl"):
        bounding_mid = (int(p1[0]), int((p1[1]+p2[1])/2))
        if(bounding_mid):
            cv2.line(img=image_np, pt1=bounding_mid, pt2=(Line_Position2, bounding_mid[1]), color=(
                255, 0, 0), thickness=1, lineType=8, shift=0)
            distance_from_line = bounding_mid[1]-Line_Position2

    # print(distance_from_line)
    if (distance_from_line <= 0):

        # crossed+=1
        # print("[INFO] Sending email alert..")
        # Telegram().send('+918883140975')
        # print("[INFO] Alert sent")

        posii = int(image_np.shape[1]/2)
        cv2.putText(image_np, "WARNING!!!!!", (posii, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        return 1
    else:
        return 0
