import pygame
import pygame_gui
import time
from collections import deque
from queue import PriorityQueue


def drawMaze():
    global pacmanMaze
    global mazeRealCost
    global heursiticData

    pacmanMaze=[
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0],
        [0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0],
        [0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0],
        [0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0],
        [0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0],
        [0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,0,0,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,3,1,1,0,1,1,1,1,1,0],
        [0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0],
        [0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0],
        [0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0],
        [0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0],
        [0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0],
        [0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0],
        [0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0],
        [0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0],
        [0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0],
        [0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0],
        [0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0],
        [0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0],
        [0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]

    mazeRealCost =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 142, 75, 31, 44, 101, 0, 34, 185, 0, 87, 71, 31, 67, 127, 0, 183, 95, 29, 198, 166, 0, 35, 174, 0, 21, 76, 62, 35, 72, 0, 123, 106, 0, 57, 198, 53, 58, 25, 0, 65, 60, 190, 145, 134, 0, 146, 77, 0, 186, 128, 146, 135, 51, 0, 4, 62, 145, 11, 183, 0, 43, 199, 91, 98, 22, 2, 146, 167, 81, 86, 126, 75, 7, 121, 0], 
        [0, 66, 44, 0, 0, 0, 0, 30, 164, 0, 0, 0, 0, 91, 32, 0, 83, 184, 0, 0, 0, 0, 81, 111, 0, 0, 0, 0, 52, 98, 0, 189, 140, 0, 88, 47, 0, 0, 0, 0, 0, 0, 0, 92, 81, 0, 43, 76, 0, 23, 10, 0, 116, 200, 0, 0, 0, 0, 22, 41, 0, 0, 0, 0, 111, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 102, 46, 176, 66, 106, 103, 45, 152, 22, 160, 170, 0, 22, 98, 0, 195, 65, 49, 79, 42, 51, 150, 125, 111, 114, 90, 110, 159, 7, 0, 31, 149, 24, 89, 165, 0, 40, 123, 31, 121, 151, 159, 50, 15, 168, 182, 170, 0, 16, 168, 0, 88, 46, 0, 158, 61, 124, 63, 196, 67, 85, 82, 0, 15, 111, 0, 76, 130, 87, 121, 43, 88, 74, 125, 0],
        [0, 0, 0, 0, 0, 0, 0, 176, 166, 0, 56, 65, 0, 44, 51, 0, 163, 173, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 171, 121, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 190, 0, 19, 32, 0, 0, 0, 0, 6, 81, 0, 104, 138, 0, 0, 0, 0, 0, 0, 0, 178, 199, 0, 0, 0, 0, 0, 0, 0, 117, 106, 0],
        [0, 14, 112, 0, 97, 150, 0, 75, 151, 0, 104, 150, 0, 80, 120, 0, 46, 185, 14, 33, 165, 71, 84, 173, 61, 152, 15, 0, 29, 174, 0, 107, 159, 0, 124, 79, 155, 38, 6, 0, 163, 23, 170, 72, 131, 0, 161, 65, 131, 182, 141, 107, 110, 98, 0, 135, 149, 34, 139, 197, 100, 35, 74, 66, 161, 50, 168, 66, 6, 75, 17, 110, 11, 198, 81, 0], 
        [0, 99, 151, 0, 179, 165, 0, 0, 0, 0, 119, 112, 0, 102, 12, 0, 0, 0, 0, 158, 9, 0, 0, 0, 0, 70, 85, 0, 140, 93, 0, 115, 154, 0, 16, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 143, 63, 0, 64, 147, 0, 0, 0, 0, 0, 0, 0, 144, 74, 0, 98, 147, 0, 0, 0, 0, 40, 24, 0],
        [0, 136, 64, 0, 28, 126, 190, 200, 124, 0, 16, 200, 0, 36, 146, 106, 164, 63, 177, 124, 143, 0, 108, 81, 188, 154, 21, 9, 96, 190, 176, 26, 112, 0, 143, 9, 82, 59, 195, 98, 188, 164, 0, 86, 105, 0, 56, 35, 5, 88, 57, 28, 4, 48, 0, 99, 41, 0, 68, 127, 109, 138, 165, 196, 159, 131, 0, 60, 97, 0, 109, 115, 32, 149, 127, 0],
        [0, 94, 120, 0, 185, 194, 0, 0, 0, 0, 181, 166, 0, 162, 100, 0, 0, 0, 0, 0, 0, 0, 85, 46, 0, 0, 0, 0, 131, 118, 0, 0, 0, 0, 0, 0, 0, 166, 164, 0, 0, 0, 0, 185, 142, 0, 0, 0, 0, 143, 120, 0, 0, 0, 0, 93, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 94, 0, 0, 0, 0, 98, 3, 0], 
        [0, 13, 148, 130, 190, 143, 71, 112, 106, 0, 164, 88, 81, 179, 125, 0, 91, 68, 0, 100, 189, 33, 177, 84, 0, 103, 163, 121, 83, 134, 172, 162, 108, 0, 55, 40, 0, 125, 100, 38, 163, 76, 110, 9, 77, 0, 167, 179, 82, 168, 21, 45, 38, 11, 0, 117, 43, 0, 117, 151, 0, 198, 3, 86, 21, 161, 0, 22, 97, 0, 198, 47, 0, 158, 43, 0], 
        [0, 0, 0, 0, 71, 195, 0, 49, 109, 0, 21, 95, 0, 0, 0, 0, 162, 137, 0, 188, 50, 0, 0, 0, 0, 77, 31, 0, 0, 0, 0, 0, 0, 0, 8, 178, 0, 0, 0, 0, 0, 0, 0, 190, 54, 0, 164, 171, 0, 177, 50, 0, 0, 0, 0, 28, 16, 0, 101, 26, 0, 83, 89, 0, 0, 0, 0, 169, 194, 0, 102, 41, 0, 0, 0, 0],
        [0, 27, 153, 0, 49, 52, 0, 144, 97, 139, 139, 19, 0, 12, 197, 0, 114, 3, 70, 27, 172, 0, 99, 139, 174, 14, 156, 35, 5, 29, 120, 133, 16, 198, 148, 114, 55, 147, 24, 0, 53, 183, 155, 63, 44, 0, 42, 180, 0, 108, 89, 30, 11, 20, 0, 144, 79, 74, 122, 1, 0, 132, 190, 55, 174, 186, 0, 124, 75, 0, 62, 14, 20, 7, 88, 0], 
        [0, 162, 115, 0, 158, 196, 0, 0, 0, 0, 169, 71, 0, 38, 26, 0, 0, 0, 0, 198, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 22, 0, 139, 166, 0, 0, 0, 0, 62, 135, 0, 0, 0, 0, 86, 107, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 14, 199, 0, 0, 0, 0, 99, 168, 0], 
        [0, 84, 43, 172, 199, 49, 0, 20, 99, 147, 160, 168, 0, 194, 200, 5, 103, 167, 160, 183, 121, 175, 57, 61, 0, 164, 143, 195, 132, 41, 0, 1, 176, 0, 87, 173, 151, 169, 156, 130, 26, 58, 200, 7, 116, 0, 126, 36, 0, 19, 169, 160, 18, 99, 0, 135, 130, 38, 46, 131, 199, 132, 104, 0, 70, 88, 64, 105, 132, 0, 60, 149, 147, 8, 30, 0],
        [0, 0, 0, 0, 70, 4, 0, 17, 67, 0, 0, 0, 0, 117, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 106, 26, 0, 0, 0, 0, 19, 183, 0, 0, 0, 0, 168, 176, 0, 0, 0, 0, 0, 44, 0, 171, 185, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 44, 50, 0, 0, 0, 0, 5, 193, 0, 36, 3, 0, 0, 0, 0, 141, 111, 0], 
        [0, 62, 109, 85, 107, 89, 0, 73, 183, 45, 29, 195, 0, 181, 119, 0, 84, 148, 145, 37, 176, 0, 112, 34, 0, 108, 77, 142, 162, 190, 157, 40, 17, 0, 18, 151, 0, 53, 24, 0, 151, 187, 0, 26, 107, 182, 155, 121, 0, 191, 165, 161, 164, 25, 0, 156, 84, 41, 108, 87, 0, 90, 40, 190, 61, 89, 0, 185, 34, 112, 139, 57, 144, 196, 40, 0],
        [0, 161, 14, 0, 0, 0, 0, 54, 169, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 39, 184, 0, 197, 55, 0, 0, 0, 0, 43, 97, 0, 0, 0, 0, 67, 44, 0, 159, 200, 0, 89, 4, 0, 0, 0, 0, 99, 181, 0, 16, 20, 0, 0, 0, 0, 0, 0, 0, 166, 3, 0, 31, 121, 0, 0, 0, 0, 124, 94, 0, 0, 0, 0, 163, 115, 0],
        [0, 80, 43, 124, 151, 57, 0, 114, 147, 121, 68, 84, 0, 8, 41, 24, 19, 56, 0, 9, 115, 127, 123, 54, 20, 186, 38, 0, 70, 58, 37, 159, 81, 6, 198, 160, 36, 19, 179, 0, 172, 70, 0, 42, 53, 0, 33, 2, 0, 77, 23, 177, 75, 138, 29, 94, 114, 24, 107, 135, 0, 32, 186, 0, 161, 93, 10, 15, 8, 50, 175, 57, 0, 144, 177, 0],
        [0, 117, 1, 0, 27, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 196, 0, 0, 89, 104, 0, 0, 0, 0, 43, 106, 0, 0, 0, 0, 177, 69, 0, 125, 20, 0, 0, 0, 0, 162, 143, 0, 186, 63, 0, 58, 18, 0, 197, 10, 0, 0, 0, 0, 102, 84, 0, 110, 96, 0, 0, 0, 0, 39, 180, 0, 0, 0, 0, 145, 133, 0, 179, 155, 0],
        [0, 106, 135, 0, 168, 144, 107, 93, 150, 200, 184, 1, 0, 138, 127, 158, 20, 130, 62, 88, 125, 127, 10, 194, 0, 200, 0, 0, 73, 95, 0, 9, 147, 0, 91, 132, 82, 61, 178, 86, 190, 114, 0, 106, 143, 67, 149, 3, 52, 182, 8, 0, 120, 66, 0, 161, 180, 0, 35, 51, 170, 17, 22, 58, 175, 151, 46, 60, 123, 0, 166, 10, 0, 34, 131, 0],
        [0, 197, 149, 0, 0, 0, 0, 0, 0, 0, 62, 28, 0, 0, 0, 0, 8, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 16, 0, 0, 0, 0, 96, 103, 0, 25, 36, 0, 0, 0, 0, 0, 0, 0, 135, 30, 0, 12, 49, 0, 33, 54, 0, 79, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 164, 0, 0, 104, 0, 75, 145, 0], 
        [0, 108, 162, 0, 134, 1, 122, 102, 148, 36, 112, 37, 3, 169, 189, 166, 142, 125, 197, 103, 44, 100, 68, 100, 0, 136, 27, 121, 96, 38, 0, 61, 95, 33, 23, 191, 0, 166, 115, 148, 63, 120, 164, 48, 175, 0, 169, 91, 0, 43, 18, 0, 178, 50, 76, 51, 123, 0, 103, 4, 127, 60, 56, 42, 126, 33, 186, 185, 115, 0, 139, 17, 0, 80, 168, 0], 
        [0, 142, 106, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 84, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 54, 77, 0, 117, 179, 0, 0, 0, 0, 0, 0, 0, 118, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77, 120, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 125, 115, 0, 17, 113, 0], 
        [0, 49, 173, 46, 177, 85, 0, 110, 11, 60, 197, 95, 149, 68, 137, 0, 177, 99, 58, 52, 109, 110, 10, 178, 0, 81, 31, 0, 1, 26, 0, 136, 90, 57, 149, 161, 12, 84, 189, 0, 181, 72, 92, 179, 151, 0, 107, 88, 150, 124, 155, 172, 194, 115, 0, 127, 186, 0, 46, 134, 0, 5, 79, 124, 91, 166, 19, 170, 99, 0, 74, 31, 0, 146, 49, 0],
        [0, 0, 0, 0, 133, 145, 0, 129, 28, 0, 181, 21, 0, 0, 0, 0, 1, 21, 0, 0, 0, 0, 0, 0, 0, 108, 161, 0, 157, 124, 0, 61, 147, 0, 0, 0, 0, 190, 59, 0, 0, 0, 0, 10, 177, 0, 0, 0, 0, 0, 0, 0, 59, 164, 0, 191, 76, 0, 150, 68, 0, 121, 139, 0, 0, 0, 0, 34, 174, 0, 0, 0, 0, 17, 149, 0],
        [0, 189, 193, 120, 76, 155, 0, 62, 13, 0, 133, 190, 68, 61, 76, 173, 183, 51, 42, 14, 7, 60, 153, 27, 0, 109, 153, 0, 91, 133, 29, 104, 75, 0, 25, 46, 0, 168, 25, 0, 17, 51, 152, 193, 187, 0, 162, 102, 125, 105, 124, 109, 89, 128, 0, 196, 9, 152, 76, 9, 0, 74, 14, 38, 174, 190, 0, 188, 6, 130, 156, 115, 0, 51, 78, 0],
        [0, 113, 11, 0, 55, 2, 0, 0, 0, 0, 0, 0, 0, 171, 74, 0, 111, 103, 0, 0, 0, 0, 167, 173, 0, 0, 0, 0, 116, 19, 0, 0, 0, 0, 161, 183, 0, 0, 0, 0, 66, 71, 0, 0, 0, 0, 0, 0, 0, 37, 199, 0, 0, 0, 0, 0, 0, 0, 165, 172, 0, 0, 0, 0, 0, 0, 0, 70, 38, 0, 0, 0, 0, 66, 132, 0], 
        [0, 48, 166, 0, 178, 132, 0, 95, 159, 40, 91, 138, 0, 170, 124, 0, 115, 36, 26, 71, 152, 0, 183, 6, 0, 3, 198, 0, 61, 49, 0, 98, 180, 117, 178, 79, 31, 48, 60, 29, 65, 43, 0, 51, 80, 115, 138, 61, 0, 43, 198, 118, 160, 175, 0, 190, 4, 20, 5, 73, 0, 5, 16, 160, 85, 0, 0, 28, 69, 0, 178, 100, 0, 8, 66, 0], 
        [0, 0, 0, 0, 14, 191, 0, 0, 0, 0, 158, 28, 0, 111, 4, 0, 0, 0, 0, 155, 53, 0, 0, 0, 0, 42, 11, 0, 0, 0, 0, 13, 13, 0, 0, 0, 0, 0, 0, 0, 107, 114, 0, 0, 0, 0, 28, 90, 0, 164, 54, 0, 166, 5, 0, 0, 0, 0, 93, 5, 0, 0, 0, 0, 90, 97, 0, 0, 0, 0, 137, 73, 0, 102, 89, 0],
        [0, 70, 45, 184, 41, 195, 0, 40, 154, 1, 180, 76, 182, 42, 61, 0, 145, 125, 65, 75, 161, 169, 90, 71, 36, 117, 25, 0, 56, 187, 52, 67, 185, 0, 91, 190, 54, 21, 102, 106, 4, 138, 159, 127, 89, 70, 158, 170, 138, 70, 102, 0, 93, 191, 87, 167, 160, 63, 96, 179, 0, 160, 181, 84, 12, 5, 112, 194, 99, 0, 67, 183, 46, 169, 93, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    heursiticData=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 47, 155, 53, 73, 45, 0, 151, 30, 0, 151, 151, 185, 69, 131, 0, 186, 87, 143, 8, 133, 0, 51, 34, 0, 186, 57, 196, 124, 90, 0, 168, 43, 0, 159, 137, 16, 83, 133, 0, 186, 109, 91, 163, 52, 0, 133, 173, 0, 183, 6, 77, 189, 17, 0, 83, 20, 55, 184, 181, 0, 176, 153, 82, 136, 123, 140, 122, 1, 10, 88, 106, 48, 28, 13, 0],
        [0, 37, 98, 0, 0, 0, 0, 35, 165, 0, 0, 0, 0, 88, 119, 0, 113, 10, 0, 0, 0, 0, 124, 21, 0, 0, 0, 0, 17, 85, 0, 132, 39, 0, 185, 76, 0, 0, 0, 0, 0, 0, 0, 108, 69, 0, 175, 121, 0, 127, 105, 0, 23, 69, 0, 0, 0, 0, 159, 143, 0, 0, 0, 0, 125, 98, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 82, 124, 101, 88, 174, 109, 117, 147, 65, 86, 130, 0, 132, 16, 0, 145, 188, 26, 95, 17, 43, 41, 182, 153, 146, 12, 119, 88, 4, 0, 72, 78, 160, 181, 182, 0, 23, 91, 172, 81, 185, 136, 129, 175, 177, 155, 57, 0, 65, 47, 0, 37, 127, 0, 47, 124, 115, 21, 73, 157, 30, 152, 0, 23, 98, 0, 111, 19, 189, 16, 127, 117, 140, 32, 0], 
        [0, 0, 0, 0, 0, 0, 0, 105, 198, 0, 197, 144, 0, 132, 90, 0, 59, 139, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 158, 196, 0, 155, 182, 0, 0, 0, 0, 39, 134, 0, 15, 171, 0, 0, 0, 0, 0, 0, 0, 130, 166, 0, 0, 0, 0, 0, 0, 0, 40, 171, 0], 
        [0, 98, 161, 0, 126, 14, 0, 52, 200, 0, 1, 185, 0, 173, 67, 0, 154, 65, 111, 75, 106, 98, 68, 63, 40, 186, 83, 0, 26, 5, 0, 149, 98, 0, 140, 152, 39, 51, 150, 0, 101, 176, 108, 161, 108, 0, 105, 185, 118, 199, 173, 110, 176, 19, 0, 55, 56, 198, 126, 79, 195, 53, 9, 61, 98, 157, 6, 139, 82, 92, 36, 148, 43, 83, 94, 0], 
        [0, 199, 53, 0, 186, 73, 0, 0, 0, 0, 49, 103, 0, 112, 41, 0, 0, 0, 0, 35, 166, 0, 0, 0, 0, 114, 148, 0, 108, 78, 0, 103, 194, 0, 182, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 109, 151, 0, 44, 126, 0, 0, 0, 0, 0, 0, 0, 46, 105, 0, 133, 199, 0, 0, 0, 0, 141, 60, 0], 
        [0, 190, 39, 0, 178, 100, 140, 84, 13, 0, 77, 14, 0, 123, 166, 186, 119, 176, 78, 3, 181, 0, 134, 11, 146, 21, 93, 177, 186, 37, 128, 5, 9, 0, 73, 50, 124, 189, 35, 68, 4, 53, 0, 41, 48, 0, 147, 109, 77, 27, 168, 132, 107, 102, 0, 142, 154, 0, 130, 101, 37, 66, 77, 112, 23, 68, 0, 125, 87, 0, 171, 9, 124, 164, 182, 0],
        [0, 6, 2, 0, 114, 177, 0, 0, 0, 0, 172, 137, 0, 13, 8, 0, 0, 0, 0, 0, 0, 0, 72, 107, 0, 0, 0, 0, 184, 182, 0, 0, 0, 0, 0, 0, 0, 196, 10, 0, 0, 0, 0, 129, 74, 0, 0, 0, 0, 6, 62, 0, 0, 0, 0, 23, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 199, 162, 0, 0, 0, 0, 37, 47, 0], 
        [0, 105, 123, 145, 28, 157, 31, 106, 197, 0, 10, 135, 181, 120, 153, 0, 56, 164, 0, 111, 180, 188, 52, 145, 0, 118, 167, 171, 133, 176, 97, 43, 32, 0, 58, 63, 0, 76, 175, 182, 67, 140, 79, 114, 133, 0, 54, 173, 184, 13, 195, 145, 8, 16, 0, 30, 187, 0, 117, 24, 0, 126, 3, 92, 104, 176, 0, 28, 73, 0, 29, 92, 0, 193, 175, 0],
        [0, 0, 0, 0, 137, 67, 0, 117, 5, 0, 102, 63, 0, 0, 0, 0, 128, 22, 0, 3, 44, 0, 0, 0, 0, 73, 112, 0, 0, 0, 0, 0, 0, 0, 189, 143, 0, 0, 0, 0, 0, 0, 0, 12, 83, 0, 19, 3, 0, 76, 195, 0, 0, 0, 0, 156, 81, 0, 169, 55, 0, 177, 114, 0, 0, 0, 0, 135, 60, 0, 2, 60, 0, 0, 0, 0],
        [0, 179, 4, 0, 196, 17, 0, 31, 154, 89, 41, 121, 0, 122, 128, 0, 29, 48, 191, 182, 72, 0, 97, 84, 129, 189, 174, 112, 42, 174, 134, 68, 139, 11, 123, 149, 117, 197, 63, 0, 119, 175, 72, 91, 142, 0, 184, 23, 0, 185, 116, 162, 150, 138, 0, 168, 27, 156, 199, 131, 0, 162, 150, 124, 64, 166, 0, 0, 34, 0, 86, 142, 191, 194, 106, 0], 
        [0, 184, 19, 0, 27, 44, 0, 0, 0, 0, 93, 40, 0, 122, 53, 0, 0, 0, 0, 18, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 193, 32, 0, 143, 140, 0, 0, 0, 0, 19, 123, 0, 0, 0, 0, 112, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 94, 34, 0, 73, 31, 0, 0, 0, 0, 144, 90, 0],
        [0, 197, 123, 40, 37, 66, 0, 63, 43, 174, 197, 111, 0, 121, 35, 170, 136, 57, 29, 14, 104, 121, 74, 24, 0, 115, 47, 63, 103, 169, 0, 132, 50, 0, 190, 3, 58, 84, 132, 170, 191, 157, 118, 57, 197, 0, 191, 99, 0, 176, 7, 189, 133, 81, 0, 101, 17, 79, 121, 57, 168, 63, 177, 0, 4, 159, 132, 42, 93, 0, 150, 57, 133, 183, 180, 0], 
        [0, 0, 0, 0, 86, 4, 0, 180, 140, 0, 0, 0, 0, 6, 131, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 68, 121, 0, 0, 0, 0, 173, 32, 0, 0, 0, 0, 7, 142, 0, 0, 0, 0, 47, 154, 0, 82, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 77, 0, 0, 0, 0, 37, 116, 0, 197, 138, 0, 0, 0, 0, 156, 115, 0], 
        [0, 149, 180, 36, 153, 165, 0, 155, 67, 200, 115, 110, 0, 23, 156, 0, 153, 30, 171, 192, 55, 0, 11, 136, 0, 35, 124, 185, 31, 46, 197, 32, 138, 0, 146, 194, 0, 64, 1, 0, 73, 57, 0, 133, 191, 100, 87, 63, 0, 24, 80, 118, 7, 154, 0, 170, 64, 166, 66, 125, 0, 5, 159, 195, 126, 147, 0, 170, 35, 190, 32, 27, 156, 190, 175, 0], 
        [0, 118, 134, 0, 0, 0, 0, 4, 132, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 131, 60, 0, 2, 100, 0, 0, 0, 0, 146, 72, 0, 0, 0, 0, 22, 81, 0, 200, 189, 0, 31, 1, 0, 0, 0, 0, 4, 131, 0, 163, 38, 0, 0, 0, 0, 0, 0, 0, 137, 113, 0, 34, 126, 0, 0, 0, 0, 96, 102, 0, 0, 0, 0, 147, 29, 0], 
        [0, 48, 109, 4, 23, 140, 0, 19, 182, 92, 39, 140, 0, 193, 140, 131, 118, 64, 0, 179, 143, 51, 69, 90, 60, 98, 52, 0, 101, 18, 182, 27, 81, 181, 87, 12, 78, 171, 110, 0, 195, 166, 0, 33, 40, 0, 71, 173, 0, 167, 30, 192, 22, 184, 119, 157, 165, 64, 37, 58, 0, 129, 57, 0, 41, 113, 98, 20, 37, 154, 63, 117, 0, 154, 162, 0],
        [0, 126, 174, 0, 1, 197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 154, 185, 0, 81, 179, 0, 0, 0, 0, 130, 19, 0, 0, 0, 0, 166, 116, 0, 147, 148, 0, 0, 0, 0, 52, 116, 0, 21, 162, 0, 46, 91, 0, 121, 116, 0, 0, 0, 0, 138, 128, 0, 4, 200, 0, 0, 0, 0, 172, 101, 0, 0, 0, 0, 147, 82, 0, 20, 52, 0],
        [0, 80, 48, 0, 23, 65, 172, 176, 41, 81, 127, 83, 0, 33, 7, 136, 100, 0, 25, 162, 54, 200, 9, 73, 0, 171, 49, 0, 4, 36, 0, 80, 167, 0, 193, 181, 60, 140, 38, 146, 112, 21, 0, 0, 183, 54, 65, 37, 199, 181, 80, 0, 92, 198, 0, 145, 18, 0, 44, 56, 8, 187, 71, 82, 9, 157, 57, 162, 54, 0, 108, 122, 0, 191, 177, 0],
        [0, 84, 93, 0, 0, 0, 0, 0, 0, 0, 19, 23, 0, 0, 0, 0, 119, 133, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 71, 153, 0, 0, 0, 0, 157, 87, 0, 166, 115, 0, 0, 0, 0, 0, 0, 0, 143, 180, 0, 40, 190, 0, 48, 12, 0, 95, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 68, 97, 0, 54, 182, 0, 5, 81, 0],
        [0, 13, 182, 0, 46, 59, 21, 157, 112, 177, 68, 147, 83, 98, 162, 82, 27, 37, 25, 197, 91, 5, 176, 77, 0, 118, 116, 177, 79, 83, 0, 176, 8, 61, 125, 15, 0, 173, 118, 156, 198, 92, 129, 169, 19, 0, 54, 9, 0, 28, 20, 0, 107, 140, 197, 33, 187, 0, 166, 184, 151, 36, 153, 0, 159, 114, 104, 134, 72, 0, 35, 58, 0, 17, 59, 0],
        [0, 179, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 154, 151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 17, 0, 113, 121, 0, 0, 0, 0, 0, 0, 0, 110, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 191, 92, 0, 0, 0, 0, 184, 48, 0, 0, 0, 0, 0, 0, 0, 167, 14, 0, 138, 19, 0], 
        [0, 0, 149, 123, 194, 137, 0, 170, 22, 180, 132, 94, 73, 109, 84, 0, 66, 66, 62, 147, 2, 82, 102, 199, 0, 136, 50, 0, 29, 117, 0, 103, 118, 183, 40, 183, 103, 124, 130, 0, 61, 102, 65, 20, 29, 0, 162, 86, 137, 63, 15, 57, 27, 85, 0, 12, 88, 0, 3, 22, 0, 36, 103, 175, 186, 43, 188, 123, 84, 0, 42, 71, 0, 26, 168, 0], 
        [0, 0, 0, 0, 197, 189, 0, 39, 67, 0, 177, 53, 0, 0, 0, 0, 147, 141, 0, 0, 0, 0, 0, 0, 0, 165, 11, 0, 190, 57, 0, 195, 142, 0, 0, 0, 0, 169, 29, 0, 0, 0, 0, 200, 73, 0, 0, 0, 0, 0, 0, 0, 66, 38, 0, 41, 2, 0, 193, 175, 0, 182, 184, 0, 0, 0, 0, 178, 154, 0, 0, 0, 0, 54, 197, 0],
        [0, 119, 33, 171, 47, 90, 0, 69, 166, 0, 97, 193, 87, 103, 36, 12, 28, 22, 3, 85, 200, 47, 68, 171, 0, 108, 1, 0, 130, 90, 90, 189, 107, 0, 43, 84, 0, 84, 6, 0, 138, 196, 91, 99, 135, 0, 182, 46, 2, 77, 157, 55, 127, 90, 0, 174, 199, 100, 59, 162, 0, 57, 176, 68, 60, 16, 0, 99, 180, 25, 72, 75, 0, 117, 47, 0],
        [0, 187, 158, 0, 49, 65, 0, 0, 0, 0, 0, 0, 0, 182, 71, 0, 161, 102, 0, 0, 0, 0, 99, 177, 0, 0, 0, 0, 162, 189, 0, 0, 0, 0, 95, 83, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 173, 175, 0, 0, 0, 0, 0, 0, 0, 19, 147, 0, 0, 0, 0, 0, 0, 0, 20, 25, 0, 0, 0, 0, 78, 195, 0],
        [0, 146, 24, 0, 174, 92, 0, 94, 174, 172, 152, 73, 0, 156, 183, 0, 130, 83, 182, 6, 143, 0, 12, 102, 0, 43, 34, 0, 191, 182, 0, 156, 181, 194, 195, 193, 89, 143, 49, 23, 193, 185, 0, 41, 7, 0, 154, 192, 0, 133, 57, 146, 140, 26, 0, 42, 157, 34, 74, 111, 0, 158, 115, 83, 34, 119, 44, 151, 10, 0, 186, 46, 0, 103, 69, 0],
        [0, 0, 0, 0, 85, 195, 0, 0, 0, 0, 119, 85, 0, 173, 55, 0, 0, 0, 0, 131, 40, 0, 0, 0, 0, 118, 121, 0, 0, 0, 0, 181, 43, 0, 0, 0, 0, 0, 0, 0, 56, 131, 0, 0, 0, 0, 128, 44, 0, 145, 97, 0, 70, 33, 0, 0, 0, 0, 70, 18, 0, 0, 0, 0, 164, 65, 0, 0, 0, 0, 95, 83, 0, 75, 88, 0],
        [0, 184, 22, 67, 63, 39, 0, 197, 78, 82, 178, 31, 12, 45, 23, 0, 118, 24, 118, 74, 186, 20, 0, 88, 133, 71, 135, 0, 84, 173, 42, 18, 49, 0, 89, 66, 190, 65, 172, 79, 65, 156, 123, 180, 3, 139, 91, 23, 106, 54, 4, 0, 71, 6, 145, 30, 110, 108, 37, 45, 0, 160, 27, 58, 28, 23, 162, 4, 178, 0, 58, 77, 35, 24, 97, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


square = 20
drawMaze()
(width, height) = (len(pacmanMaze) * square*2.4, len(pacmanMaze[0]) * square/2.45)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
solution = {}
startTime=0
endTime=0
xInitial = 0
yInitial = 0 
endX = 0
endY = 0
realPath = []
Visited = [] 
Frontier = []
running =True

def drawWall(i,j):
    pygame.draw.rect(screen,(0,0,255),(j*square,i*square,square,square))
def endGoal(i,j):
    pygame.draw.circle(screen,(173, 255, 47),(j*square+square//2, i * square+square//2),square//4)
def backgroundFloor(i,j):
    pygame.draw.rect(screen,(0, 0, 0),(j*square,i*square,square,square))
def startNode(i,j):
    pygame.draw.circle(screen, (183,28,28),(j*square+square//2, i * square+square//2),square//4)
def greenPath(i,j):
    pygame.draw.rect(screen,(0,255,0),(j*square,i*square,square,square))
def yellowTrack(i,j):
    pygame.draw.rect(screen,(255,255,0),(j*square,i*square,square,square))

def Render():
    global xInitial, yInitial,endX, endY
    screen.fill((0,0,0))
    for i in range(len(pacmanMaze)):
        for j in range(len(pacmanMaze[0])):
            element = pacmanMaze[i][j]
            if element == 0:
                drawWall(i,j)
            elif element == 4:
                realPath.append((j,i))
                endX = j
                endY = i
                endGoal(i,j)
            elif element == 1:
                    backgroundFloor(i,j)
                    realPath.append((j,i))
            elif element == 3:
                xInitial = j
                yInitial = i
                startNode(i,j)
            elif element == 9:
                realPath.append((j,i))
                greenPath(i,j)
            elif element == 10:
                realPath.append((j,i))
                yellowTrack(i,j)
    pygame.display.update()

def move(x,y):
    pacmanMaze[y][x] = 10

def DFS(x,y):
    Frontier.append((x,y)) 
    solution[x,y] = x,y 
    while len(Frontier) > 0: 
        time.sleep(0) 
        current = (x,y) 
        if (x - 1,y) in realPath and (x - 1,y) not in Visited: 
            left = (x - 1,y)
            solution[left] = x,y 
            Frontier.append(left)
        if (x,y + 1) in realPath and (x,y + 1) not in Visited:
            down = (x,y+1)
            solution[down] = x,y
            Frontier.append(down)
        if (x + 1,y) in realPath and (x+1,y) not in Visited:
            right = (x + 1,y)
            solution[right] = x,y
            Frontier.append(right)
        if (x,y-1) in realPath and (x,y-1) not in Visited:
            up = (x,y-1)
            solution[up] = x,y
            Frontier.append(up)
        x,y = Frontier.pop() 
        pacmanMaze[y][x] = 9
        Visited.append(current)
        if (x,y) == (endX,endY):
            return
        Render()

def BFS(x,y):
    Frontier = deque()
    Visited = set()
    Frontier.append((x,y))
    solution[x,y] = x,y
    while len(Frontier) > 0:
        time.sleep(3)
        x,y = Frontier.popleft()

        if(x - 1,y) in realPath and (x-1,y) not in Visited:
            left = (x-1,y)
            solution[left] = x,y
            pacmanMaze[left[1]][left[0]] = 9
            Frontier.append(left)
            Visited.add((x-1,y))
        if(x,y-1) in realPath and (x,y-1) not in Visited:
            up = (x,y-1)
            solution[up] = x,y
            pacmanMaze[up[1]][up[0]] = 9
            Frontier.append(up)
            Visited.add((x,y-1))
        if(x+1,y) in realPath and (x+1,y) not in Visited:
            right = (x+1,y)
            solution[right] = x,y
            pacmanMaze[right[1]][right[0]] = 9
            Frontier.append(right)
            Visited.add((x+1,y))
        if (x,y+1) in realPath and (x,y+1) not in Visited:
            down = (x,y+1)
            solution[down] = x,y
            pacmanMaze[down[1]][down[0]] = 9
            Frontier.append(down)
            Visited.add((x,y+1))
        if (x,y) == (endX,endY):
            return
        Render()

def gbfs(x,y):
    Frontier = PriorityQueue()
    Visited = set()
    Frontier.put((heursiticData[y][x],(x,y)))
    solution[x,y] = x,y
    while not Frontier.empty():
        time.sleep(0)
        node = Frontier.get()
        Cost,pacmanPosition=node
        if(pacmanPosition[0] - 1,pacmanPosition[1]) in realPath and (pacmanPosition[0]-1,pacmanPosition[1]) not in Visited:
            left = (pacmanPosition[0]-1,pacmanPosition[1])
            solution[left] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[left[1]][left[0]] = 9
            Frontier.put((heursiticData[pacmanPosition[1]][pacmanPosition[0]-1],(left)))
            Visited.add((pacmanPosition[0]-1,pacmanPosition[1]))
        if(pacmanPosition[0],pacmanPosition[1]-1) in realPath and (pacmanPosition[0],pacmanPosition[1]-1) not in Visited:
            up = (pacmanPosition[0],pacmanPosition[1]-1)
            solution[up] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[up[1]][up[0]] = 9
            Frontier.put((heursiticData[pacmanPosition[1]-1][pacmanPosition[0]],(up)))
            Visited.add((pacmanPosition[0],pacmanPosition[1]-1))
        if(pacmanPosition[0]+1,pacmanPosition[1]) in realPath and (pacmanPosition[0]+1,pacmanPosition[1]) not in Visited:
            right = (pacmanPosition[0]+1,pacmanPosition[1])
            solution[right] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[right[1]][right[0]] = 9
            Frontier.put((heursiticData[pacmanPosition[1]][pacmanPosition[0]+1],(right)))
            Visited.add((pacmanPosition[0]+1,pacmanPosition[1]))
        if (pacmanPosition[0],pacmanPosition[1]+1) in realPath and (pacmanPosition[0],pacmanPosition[1]+1) not in Visited:
            down = (pacmanPosition[0],pacmanPosition[1]+1)
            solution[down] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[down[1]][down[0]] = 9
            Frontier.put((heursiticData[pacmanPosition[1]+1][pacmanPosition[0]],(down)))
            Visited.add((pacmanPosition[0],pacmanPosition[1]+1))
        if (pacmanPosition[0],pacmanPosition[1]) == (endX,endY):
            return
        Render()

def UCS(x,y): 
    Frontier = PriorityQueue()
    Visited = set()
    Frontier.put((mazeRealCost[y][x],(x,y)))
    solution[x,y] = x,y
    while not Frontier.empty():
        time.sleep(0)
        node = Frontier.get()
        Cost,pacmanPosition=node
        if(pacmanPosition[0] - 1,pacmanPosition[1]) in realPath and (pacmanPosition[0]-1,pacmanPosition[1]) not in Visited:
            left = (pacmanPosition[0]-1,pacmanPosition[1])
            solution[left] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[left[1]][left[0]] = 9
            Frontier.put((Cost+mazeRealCost[pacmanPosition[1]][pacmanPosition[0]-1],(left)))
            Visited.add((pacmanPosition[0]-1,pacmanPosition[1]))
        if(pacmanPosition[0],pacmanPosition[1]-1) in realPath and (pacmanPosition[0],pacmanPosition[1]-1) not in Visited:
            up = (pacmanPosition[0],pacmanPosition[1]-1)
            solution[up] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[up[1]][up[0]] = 9
            Frontier.put((Cost+mazeRealCost[pacmanPosition[1]-1][pacmanPosition[0]],(up)))
            Visited.add((pacmanPosition[0],pacmanPosition[1]-1))
        if(pacmanPosition[0]+1,pacmanPosition[1]) in realPath and (pacmanPosition[0]+1,pacmanPosition[1]) not in Visited:
            right = (pacmanPosition[0]+1,pacmanPosition[1])
            solution[right] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[right[1]][right[0]] = 9
            Frontier.put((Cost+mazeRealCost[pacmanPosition[1]][pacmanPosition[0]+1],(right)))
            Visited.add((pacmanPosition[0]+1,pacmanPosition[1]))
        if (pacmanPosition[0],pacmanPosition[1]+1) in realPath and (pacmanPosition[0],pacmanPosition[1]+1) not in Visited:
            down = (pacmanPosition[0],pacmanPosition[1]+1)
            solution[down] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[down[1]][down[0]] = 9
            Frontier.put((Cost+mazeRealCost[pacmanPosition[1]+1][pacmanPosition[0]],(down)))
            Visited.add((pacmanPosition[0],pacmanPosition[1]+1))
        if (pacmanPosition[0],pacmanPosition[1]) == (endX,endY):
            return
        Render() 

def AStar(x,y):
    Frontier = PriorityQueue()
    Visited = set()
    Frontier.put((mazeRealCost[y][x]+heursiticData[y][x],(x,y)))
    solution[x,y] = x,y
    while not Frontier.empty():
        time.sleep(0)
        node = Frontier.get()
        Cost,pacmanPosition=node
        if(pacmanPosition[0] - 1,pacmanPosition[1]) in realPath and (pacmanPosition[0]-1,pacmanPosition[1]) not in Visited:
            left = (pacmanPosition[0]-1,pacmanPosition[1])
            solution[left] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[left[1]][left[0]] = 9
            Frontier.put((Cost+mazeRealCost[y][x]+heursiticData[pacmanPosition[1]][pacmanPosition[0]-1],(left)))
            Visited.add((pacmanPosition[0]-1,pacmanPosition[1]))
        if(pacmanPosition[0],pacmanPosition[1]-1) in realPath and (pacmanPosition[0],pacmanPosition[1]-1) not in Visited:
            up = (pacmanPosition[0],pacmanPosition[1]-1)
            solution[up] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[up[1]][up[0]] = 9
            Frontier.put((Cost+mazeRealCost[y][x]+heursiticData[pacmanPosition[1]-1][pacmanPosition[0]],(up)))
            Visited.add((pacmanPosition[0],pacmanPosition[1]-1))
        if(pacmanPosition[0]+1,pacmanPosition[1]) in realPath and (pacmanPosition[0]+1,pacmanPosition[1]) not in Visited:
            right = (pacmanPosition[0]+1,pacmanPosition[1])
            solution[right] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[right[1]][right[0]] = 9
            Frontier.put((Cost+mazeRealCost[y][x]+heursiticData[pacmanPosition[1]][pacmanPosition[0]+1],(right)))
            Visited.add((pacmanPosition[0]+1,pacmanPosition[1]))
        if (pacmanPosition[0],pacmanPosition[1]+1) in realPath and (pacmanPosition[0],pacmanPosition[1]+1) not in Visited:
            down = (pacmanPosition[0],pacmanPosition[1]+1)
            solution[down] = pacmanPosition[0],pacmanPosition[1]
            pacmanMaze[down[1]][down[0]] = 9
            Frontier.put((Cost+mazeRealCost[y][x]+heursiticData[pacmanPosition[1]+1][pacmanPosition[0]],(down)))
            Visited.add((pacmanPosition[0],pacmanPosition[1]+1))
        if (pacmanPosition[0],pacmanPosition[1]) == (endX,endY):
            return
        Render()          

def backRoute(x,y):
    startTime = time.time()
    global cost
    global score
    while(x,y) != (xInitial,yInitial): 
        x,y = solution[x,y]
        score+=mazeRealCost[y][x]
        move(x,y)
        time.sleep(0)
        Render()
        cost += 1
        FONT = pygame.font.SysFont("Sans",32)
        TEXT_COLOR = (255, 0, 0)
        BG_COLOR = (0, 0, 0)
        screen.fill(BG_COLOR,(730,70,150,100))
        endTime = time.time()
        
        costOutput = 'Total Cost : '+ str(cost)
        scoreOutput = 'Total Score : '+ str(score) 
        timeOutput = 'Total Time : '+ str(endTime-startTime)
        screen.blit(FONT.render(costOutput, True, TEXT_COLOR), (200, 650))
        screen.blit(FONT.render(scoreOutput, True, TEXT_COLOR), (400, 650))
        screen.blit(FONT.render(timeOutput, True, TEXT_COLOR), (700, 650))

    
        

        pygame.display.flip()

pygame.init()


window_surface = pygame.display.set_mode((1510,700))
background = pygame.Surface((1510, 700))
background.fill(pygame.Color('#FFFFFF'))
manager = pygame_gui.UIManager((1510, 700))

BFSButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 500), (150, 50)),text='BFS',manager=manager)
DFSButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((525, 425), (150, 50)),text='DFS',manager=manager)
UCSButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 350), (150, 50)),text='UCS',manager=manager)
AStarButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 275), (150, 50)),text='A*',manager=manager)
GBFSButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((325, 200), (150, 50)),text='GBFS',manager=manager)
q = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 350), (150, 50)),text='Quit',manager=manager)
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             is_running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == BFSButton:
                    Render()
                    BFS(xInitial,yInitial)
                    drawMaze()
                    Render()
                    cost = 0
                    score=0
                    backRoute(endX,endY)
                    time.sleep(5)
                    drawMaze()
                    

                if event.ui_element == DFSButton:
                    Render()
                    DFS(xInitial,yInitial)
                    drawMaze()
                    Render()
                    cost = 0
                    score=0
                    backRoute(endX,endY)
                    time.sleep(5)
                    drawMaze()

                if event.ui_element == UCSButton:
                    Render()
                    UCS(xInitial,yInitial)
                    drawMaze()
                    Render()
                    cost = 0
                    score=0
                    backRoute(endX,endY)
                    time.sleep(5)
                    drawMaze()

                if event.ui_element == AStarButton:
                    Render()
                    AStar(xInitial,yInitial)
                    drawMaze()
                    Render()
                    cost = 0
                    score=0
                    backRoute(endX,endY)
                    time.sleep(5)
                    drawMaze()

                if event.ui_element == GBFSButton:
                    Render()
                    gbfs(xInitial,yInitial)
                    drawMaze()
                    Render()
                    cost = 0
                    score=0
                    backRoute(endX,endY)
                    time.sleep(5)
                    drawMaze()

                if event.ui_element == q:
                    pygame.quit()
                

    manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()    
        


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

