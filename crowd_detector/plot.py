#!/usr/bin/env python

'''
Contain functions to draw Bird Eye View for region of interest(ROI) and draw bounding boxes according to risk factor
for humans in a frame and draw lines between boxes according to risk factor between two humans. 
'''

__title__           = "plot.py"
__Version__         = "1.0"
__copyright__       = "Copyright 2020 , Social Distancing AI"
__license__         = "MIT"
__author__          = "Deepak Birla"
__email__           = "birla.deepak26@gmail.com"
__date__            = "2020/05/29"
__python_version__  = "3.5.2"

# imports
import cv2
import numpy as np

risco = 0
INT_MAX = 100000

# Function to draw Bird Eye View for region of interest(ROI). Red, Yellow, Green points represents risk to human. 
# Red: High Risk
# Yellow: Low Risk
# Green: No Risk
def bird_eye_view(frame, distances_mat, bottom_points, scale_w, scale_h, risk_count):
    h = frame.shape[0]
    w = frame.shape[1]

    red = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (0, 255, 255)
    white = (200, 200, 200)

    blank_image = np.zeros((int(h * scale_h), int(w * scale_w), 3), np.uint8)
    blank_image[:] = white
    warped_pts = []
    r = []
    g = []
    y = []
    for i in range(len(distances_mat)):

        if distances_mat[i][2] == 0:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                r.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                r.append(distances_mat[i][1])

            blank_image = cv2.line(blank_image, (int(distances_mat[i][0][0] * scale_w), int(distances_mat[i][0][1] * scale_h)), (int(distances_mat[i][1][0] * scale_w), int(distances_mat[i][1][1]* scale_h)), red, 2)
            
    for i in range(len(distances_mat)):
                
        if distances_mat[i][2] == 1:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                y.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                y.append(distances_mat[i][1])
        
            blank_image = cv2.line(blank_image, (int(distances_mat[i][0][0] * scale_w), int(distances_mat[i][0][1] * scale_h)), (int(distances_mat[i][1][0] * scale_w), int(distances_mat[i][1][1]* scale_h)), yellow, 2)
            
    for i in range(len(distances_mat)):
        
        if distances_mat[i][2] == 2:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                g.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                g.append(distances_mat[i][1])
    
    for i in bottom_points:
        blank_image = cv2.circle(blank_image, (int(i[0]  * scale_w), int(i[1] * scale_h)), 5, green, 10)
    for i in y:
        blank_image = cv2.circle(blank_image, (int(i[0]  * scale_w), int(i[1] * scale_h)), 5, yellow, 10)
    for i in r:
        blank_image = cv2.circle(blank_image, (int(i[0]  * scale_w), int(i[1] * scale_h)), 5, red, 10)
        
    pad = np.full((100,blank_image.shape[1],3), [110, 110, 100], dtype=np.uint8)
    cv2.putText(pad, "-- HIGH RISK : " + str(risk_count[0]) + " people", (50, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(pad, "-- LOW RISK : " + str(risk_count[1]) + " people", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
    cv2.putText(pad, "-- SAFE : " + str(risk_count[2]) + " people", (50,  80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    blank_image = np.vstack((blank_image,pad))   
        
    return blank_image
    
# Function to draw bounding boxes according to risk factor for humans in a frame and draw lines between
# boxes according to risk factor between two humans.
# Red: High Risk
# Yellow: Low Risk
# Green: No Risk 
def social_distancing_view(frame, distances_mat, boxes, risk_count, polygonX, polygonY):
    
    red = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (0, 255, 255)

    #indexes = []
    realBoxes = boxes    

    #polygon = [ (polygonX[0], polygonY[0]), (polygonX[1], polygonY[1]), (polygonX[2], polygonY[2]), (polygonX[3], polygonY[3]) ]
    
    # for i in range(len(realBoxes)):

    #     x,y,w,h = realBoxes[i][:]
    #     p = (x,y)
    #     if (is_inside_polygon(points = polygon, p = p)):
    #         print('top')
    #     else:
    #         indexes.append(i)
    #         print('zap')
            
    # print('------------')
    # indexes.sort(reverse=True)

    # for i in range(len(indexes)):

    #     del realBoxes[indexes[i]]
    
    # indexes.clear()

    for i in range(len(realBoxes)):

        x,y,w,h = realBoxes[i][:]
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),green,2)
                           
    for i in range(len(distances_mat)):

        per1 = distances_mat[i][0]
        per2 = distances_mat[i][1]
        closeness = distances_mat[i][2]
        
        if closeness == 1:
            x,y,w,h = per1[:]
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),yellow,2)
                
            x1,y1,w1,h1 = per2[:]
            frame = cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),yellow,2)
                
            frame = cv2.line(frame, (int(x+w/2), int(y+h/2)), (int(x1+w1/2), int(y1+h1/2)),yellow, 2) 
            
    for i in range(len(distances_mat)):

        per1 = distances_mat[i][0]
        per2 = distances_mat[i][1]
        closeness = distances_mat[i][2]
        
        if closeness == 0:
            x,y,w,h = per1[:]
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),red,2)
                
            x1,y1,w1,h1 = per2[:]
            frame = cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),red,2)
                
            frame = cv2.line(frame, (int(x+w/2), int(y+h/2)), (int(x1+w1/2), int(y1+h1/2)),red, 2)
            
    pad = np.full((140,frame.shape[1],3), [110, 110, 100], dtype=np.uint8)
    cv2.putText(pad, "Bounding box shows the level of risk to the person.", (50, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 0), 2)
    cv2.putText(pad, "-- HIGH RISK : " + str(risk_count[0]) + " people", (50, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
    cv2.putText(pad, "-- LOW RISK : " + str(risk_count[1]) + " people", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 1)
    cv2.putText(pad, "-- SAFE : " + str(risk_count[2]) + " people", (50,  100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
    frame = np.vstack((frame,pad))
    
    risco = 0
    if risk_count[0] > 1:
        risco = 1       
            
    return frame, risco








# Given three colinear points p, q, r, 
# the function checks if point q lies
# on line segment 'pr'
# def onSegment(p:tuple, q:tuple, r:tuple) -> bool:
     
#     if ((q[0] <= max(p[0], r[0])) &
#         (q[0] >= min(p[0], r[0])) &
#         (q[1] <= max(p[1], r[1])) &
#         (q[1] >= min(p[1], r[1]))):
#         return True
         
#     return False
 
# # To find orientation of ordered triplet (p, q, r).
# # The function returns following values
# # 0 --> p, q and r are colinear
# # 1 --> Clockwise
# # 2 --> Counterclockwise
# def orientation(p:tuple, q:tuple, r:tuple) -> int:
     
#     val = (((q[1] - p[1]) *
#             (r[0] - q[0])) -
#            ((q[0] - p[0]) *
#             (r[1] - q[1])))
            
#     if val == 0:
#         return 0
#     if val > 0:
#         return 1 # Collinear
#     else:
#         return 2 # Clock or counterclock
 
# def doIntersect(p1, q1, p2, q2):
     
#     # Find the four orientations needed for 
#     # general and special cases
#     o1 = orientation(p1, q1, p2)
#     o2 = orientation(p1, q1, q2)
#     o3 = orientation(p2, q2, p1)
#     o4 = orientation(p2, q2, q1)
 
#     # General case
#     if (o1 != o2) and (o3 != o4):
#         return True
     
#     # Special Cases
#     # p1, q1 and p2 are colinear and
#     # p2 lies on segment p1q1
#     if (o1 == 0) and (onSegment(p1, p2, q1)):
#         return True
 
#     # p1, q1 and p2 are colinear and
#     # q2 lies on segment p1q1
#     if (o2 == 0) and (onSegment(p1, q2, q1)):
#         return True
 
#     # p2, q2 and p1 are colinear and
#     # p1 lies on segment p2q2
#     if (o3 == 0) and (onSegment(p2, p1, q2)):
#         return True
 
#     # p2, q2 and q1 are colinear and
#     # q1 lies on segment p2q2
#     if (o4 == 0) and (onSegment(p2, q1, q2)):
#         return True
 
#     return False
 
# # Returns true if the point p lies 
# # inside the polygon[] with n vertices
# def is_inside_polygon(points:list, p:tuple) -> bool:
     
#     n = len(points)
     
#     # There must be at least 3 vertices
#     # in polygon
#     if n < 3:
#         return False
         
#     # Create a point for line segment
#     # from p to infinite
#     extreme = (INT_MAX, p[1])
#     count = i = 0
     
#     while True:
#         next = (i + 1) % n
         
#         # Check if the line segment from 'p' to 
#         # 'extreme' intersects with the line 
#         # segment from 'polygon[i]' to 'polygon[next]'
#         if (doIntersect(points[i],
#                         points[next],
#                         p, extreme)):
                             
#             # If the point 'p' is colinear with line 
#             # segment 'i-next', then check if it lies 
#             # on segment. If it lies, return true, otherwise false
#             if orientation(points[i], p,
#                            points[next]) == 0:
#                 return onSegment(points[i], p,
#                                  points[next])
                                  
#             count += 1
             
#         i = next
         
#         if (i == 0):
#             break
         
#     # Return true if count is odd, false otherwise
#     return (count % 2 == 1)