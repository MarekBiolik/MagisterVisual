from Segment import Point
from Segment import Segment
from Segment import SegmentType

xMin = 0
xMax = 900
yMin = 0
yMax = 900

def resize(min, max, orginal):
    temp = float(orginal) - min
    return int((temp * 900)/(max-min))

def readCoords(fileWithVertexs):
    vertexs = []
    with open(fileWithVertexs) as file:
        for row in file:
            xs, ys = row.split()
            x = float(xs)
            y = float(ys)
            #xi = resize(xMin, xMax, x)
            #yi = resize(yMin, yMax, y)
            vertexs.append(Point(x, y))

    return vertexs

def readSettings():
    datas = []
    with open('../data/settings.txt') as file:
        for row in file:
            datas.append(row)

    radius = int(datas[0])
    fileWithVertexs = "../data/" + datas[1].rstrip() + ".txt"
    fileWithPath = "../data/" + datas[1].rstrip() + "_out.txt"
    return radius, fileWithVertexs, fileWithPath

def decodeType(decodeSegment):
    switcher = {
        'L': SegmentType.Left,
        'R': SegmentType.Right,
        'S': SegmentType.Stra
    }
    return switcher.get(decodeSegment, "Invalid month")

def readSegments(fileWithPath):
    segments = []
    with open(fileWithPath) as file:
        for row in file:
            xas, yas, decodeSegment, xbs, ybs, lengthStr = row.split()
            xa = float(xas)
            ya = float(yas)
            xb = float(xbs)
            yb = float(ybs)
            length = float(lengthStr)
            typeOfSegment = decodeType(decodeSegment)
            segments.append(Segment(xa, ya, typeOfSegment, xb, yb, length))

    return segments