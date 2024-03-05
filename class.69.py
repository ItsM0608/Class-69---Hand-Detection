import cv2
from cvzone.HandTrackingModule import HandDetector



video=cv2.VideoCapture(0)

detector= HandDetector(detectionCon=0.9)

while True:
    try:
        dummy,cameraFeedImage=video.read()
        cameraFeedImage_flipped=cv2.flip(cameraFeedImage, 1)
        handsDetector=detector.findHands(cameraFeedImage_flipped, flipType = False)
        hands=handsDetector[0]           #boolean value to check hand detected
        cameraFeedImage_flipped=handsDetector[1]   #1 index gets all landmark values

        if hands:
            hand1=hands[0]
            lmlist1=hand1["lmList"]
            handType1=hand1["type"]
            #print(handType1)
        #print(handsDetector)
            
            current_fingersup=""
            
            fingers1=detector.fingersUp(hand1)
            if fingers1[0] == 1:
                current_fingersup="Thumb"
                
            elif fingers1[1] == 1:
                current_fingersup="Index Finger"
                
            elif fingers1[2] == 1:
                current_fingersup="Middle Finger"
    
            elif fingers1[3] == 1:
                current_fingersup="Ring Finger"
              
            elif fingers1[4] == 1:
                current_fingersup="Little Finger"
                
            else:
                current_fingersup=""
            
            cv2.putText(cameraFeedImage_flipped, handType1 + " : "+current_fingersup,(350,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)

            hand1=hands[1]
            lmlist1=hand1["lmList"]
            handType1=hand1["type"]
            #print(handType1)
        #print(handsDetector)
            
            current_fingersup=""
            
            fingers1=detector.fingersUp(hand1)
            if fingers1[0] == 1:
                current_fingersup="Thumb"
                
            elif fingers1[1] == 1:
                current_fingersup="Index Finger"
                
            elif fingers1[2] == 1:
                current_fingersup="Middle Finger"
                
            elif fingers1[3] == 1:
                current_fingersup="Ring Finger"
          
            elif fingers1[4] == 1:
                current_fingersup="Little Finger"
                
            else:
                current_fingersup=""


            cv2.putText(cameraFeedImage_flipped, handType1 + " : "+current_fingersup,(80,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
            print(fingers1)



        cv2.imshow("handDetection_flip",cameraFeedImage_flipped)
        if cv2.waitKey(25) == 27:
            break

    except Exception as e:
        print(e)

video.release()
cv2.destroyAllWindows()