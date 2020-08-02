import time
import Reader
from Surface import Surface
from Segment import Segment

from itertools import islice

def chunk(segmentsAll, segmentsInOneIteration, iteration):
    segmentsTab = []
    for _ in range(iteration):
        segments = []
        for j in range(segmentsInOneIteration):
            segments.append(segmentsAll[j])
        segmentsTab.append(segments)

    return segmentsTab

def mainloop():
    diters = 0
    radius, fileWithVertexs, fileWithPath = Reader.readSettings()
    vertexs = Reader.readCoords(fileWithVertexs)
    segments = Reader.readSegments(fileWithPath)
    countOfVertexs = len(vertexs)
    segmentsInOneIteration = countOfVertexs * 3
    iteration = int(len(segments) / segmentsInOneIteration)
    segmentsTab = chunk(segments, segmentsInOneIteration, iteration)
    sur = Surface()
    while True:
        sur.create(diters, countOfVertexs)
        for point in vertexs:
            sur.drawCity(point.x, point.y)
        for segment in segmentsTab[diters]:
            sur.drawSegment(segment, radius)
        sur.updateGraphicsOutput()
        # wait a moment (SLEEP may be zero):
        diters += 1
        if (diters == iteration):
            print("KONIEC")
            break
        time.sleep(10)
    
    time.sleep(10)

mainloop()