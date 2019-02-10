import cv2


def one_contour_xy_direction(contours):
    """
    compute the center of one contour and send x and y directions back
    """
    if contours is not None:
        moment = cv2.moments(contours[0])
        target_x = int(moment["m10"] / moment["m00"])
        target_y = int(moment["m01"] / moment["m00"])
        return "direction", str(target_x) + ' ' + str(target_y)
    else:
        return "direction", "9999"


def two_contour_xy_direction(contours):
    """
    compute the center of two contours and send x and y directions back
    """
    if len(contours) == 2:
        moment1 = cv2.moments(contours[0])
        moment2 = cv2.moments(contours[1])
        target_x = (int(moment1["m10"] / moment1["m00"]) + int(moment2["m10"] / moment2["m00"])) / 2
        target_y = (int(moment1["m01"] / moment1["m00"] + int(moment1["m01"] / moment1["m00"]))) / 2
        return "direction", str(target_x) + ' ' + str(target_y)
    elif len(contours) == 1:
        return one_contour_xy_direction(contours)
    else:
        return "direction", "9999"
