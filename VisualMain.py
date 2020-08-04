import time
import Reader
from Surface import Surface
from Segment import Segment

def chunk(segmentsAll, segmentsInOneIteration, iteration):
    segmentsTab = []
    for i in range(iteration):
        segments = []
        for j in range(segmentsInOneIteration):
            segments.append(segmentsAll[i * segmentsInOneIteration + j])
        segmentsTab.append(segments)

    return segmentsTab

def mainloop():
    diters = 0
    radius, fileWithVertexs, fileWithPath = Reader.readSettings()
    vertexs = Reader.readCoords(fileWithVertexs)
    countOfVertexs = len(vertexs)
    segmentsInOneIteration = countOfVertexs * 3
    segments, distances = Reader.readSegments(fileWithPath, segmentsInOneIteration)
    segmentsInOneIteration = countOfVertexs * 3
    iteration = int(len(segments) / segmentsInOneIteration)
    segmentsTab = chunk(segments, segmentsInOneIteration, iteration)
    sur = Surface()
    while True:
        sur.create(diters, countOfVertexs, distances)
        for point in vertexs:
            sur.drawCity(point.x, point.y)
        for segment in segmentsTab[diters]:
            sur.drawSegment(segment, radius)
        sur.updateGraphicsOutput()
        diters += 1
        if (diters == iteration):
            print("KONIEC")
            break
        time.sleep(0)
    
    time.sleep(1000)

mainloop()