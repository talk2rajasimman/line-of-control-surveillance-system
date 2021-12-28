import cv2


def drawsafelines(image_np, Orientation, Line_Perc):

    print(Line_Perc/100)

    posii = int(image_np.shape[1]-(image_np.shape[1]/3))
    cv2.putText(image_np, 'Blue Line : Safety Line',
                (posii, 30),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    if(Orientation == "lr"):

        Line_Position = int(
            image_np.shape[1]-(image_np.shape[1]*(Line_Perc/100)))

        cv2.line(img=image_np, pt1=(Line_Position, 0), pt2=(Line_Position,
                 image_np.shape[0]), color=(255, 0, 0), thickness=2, lineType=8, shift=0)

        return Line_Position

    elif(Orientation == "rl"):

        Line_Position = int(image_np.shape[1]*(Line_Perc/100))

        cv2.line(img=image_np, pt1=(Line_Position, 0), pt2=(Line_Position,
                 image_np.shape[0]), color=(255, 0, 0), thickness=2, lineType=8, shift=0)

        return Line_Position
