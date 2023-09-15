
import cv2 
import mediapipe as mp

class handTracker():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, modeComplexity = 1, trackCon = 0.5 ):
        self.mode = mode 
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modeComplexity = modeComplexity
        self.trackCon = trackCon 
        self.mpHands = mp.solutions.hands
        self.hands = mp.solutions.hands.Hands(self.mode, self.maxHands,  self.detectionCon,
                                        self.modeComplexity,  self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
