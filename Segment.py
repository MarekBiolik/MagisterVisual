from enum import Enum
import math

class SegmentType(Enum):
    Left = 1
    Right = 2
    Stra = 3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, xa, ya, typeOfSegment, xb, yb, length):
        self.fstPoint = Point(xa, ya)
        self.typeOfSegment = typeOfSegment
        self.sndPoint = Point(xb, yb)
        self.length = length

    def delta(self, a, b, c):
        d = (b * b) - (4 * a * c)
        if (abs(d) < 0.001):
            licznik1 = -1 * b
            licznik2 = licznik1
        else:
            print(d)
            licznik1 = -1 * b + math.sqrt(d)
            licznik2 = -1 * b - math.sqrt(d)
        mianownik = 2 * a
        return licznik1 / mianownik, licznik2 / mianownik

    def findMiddleOfCircle(self, r):
        # assert A == B TODO
        # assert type == S TODO
        # środe |AB| = C
        xa = self.fstPoint.x
        ya = self.fstPoint.y
        xb = self.sndPoint.x
        yb = self.sndPoint.y
        print(f"{xa} {ya}")
        print(f"{xb} {yb}")
        # print(f"xa {xa} ya {ya} xb {xb} yb {yb}")
        xc = (xa + xb)/2
        yc = (ya + yb)/2
        # prost prostopadła do prosta przez A i B
        if (abs(xa - xb) < 0.001):
            at = 0
            #bt = xa
            ap = 0
            bp = yc
            print("równe")
            a = 1 + (ap * ap)
            b = 2 * ((ap * bp) - (ap * ya) - xa)
            c = (xa * xa) + (bp * bp) + (ya * ya) - (2 * bp * ya) - (r * r)

            xs1, xs2 = self.delta(a, b, c)
            ys1 = ap * xs1 + bp
            ys2 = ap * xs2 + bp
        else:
            at = (ya-yb)/(xa-xb) # a prostej przez A i B
            #bt = ya - at * xa
            if (abs(at) < 0.001):
                bp = xc
                print("ap 0")
                a = 1
                b = (-2) * (ya * ya)
                c = (ya * ya) - (r * r) + ((bp - xa) * (bp - xa))

                ys1, ys2 = self.delta(a, b, c)
                xs1 = xc
                xs2 = xc
            else:
                ap = -1/at
                bp = yc +  ((xa - xb)/(ya - yb)) * xc
                a = 1 + (ap * ap)
                b = 2 * ((ap * bp) - (ap * ya) - xa)
                c = (xa * xa) + (bp * bp) + (ya * ya) - (2 * bp * ya) - (r * r)

                xs1, xs2 = self.delta(a, b, c)
                ys1 = ap * xs1 + bp
                ys2 = ap * xs2 + bp


        # p0 A, p1 B, p2 S
        # p1 - p0
        x10 = xb - xa
        y10 = yb - ya
        # p2 - p0
        xs10 = xs1 - xa
        ys10 = ys1 - ya
        # iloczyn
        iloczyn = x10 * ys10 - xs10 * y10

        if (self.typeOfSegment == SegmentType.Right):
            if (iloczyn > 0):
                if (self.length < math.pi):
                    return xs2, ys2
                else:
                    return xs1, ys1
            else:
                if (self.length < math.pi):
                    return xs1, ys1 
                else:
                    return xs2, ys2
        else:
            if (iloczyn < 0):
                if (self.length < math.pi):
                    return xs2, ys2
                else:
                    return xs1, ys1
            else:
                if (self.length < math.pi):
                    return xs1, ys1
                else:
                    return xs2, ys2
        return xs1, ys1

    def calculateArc(self, r):
        xa = self.fstPoint.x
        ya = self.fstPoint.y
        xb = self.sndPoint.x
        yb = self.sndPoint.y
        #print(f"xa {xa} ya {ya} xb {xb} yb {yb}")
        xs, ys = self.findMiddleOfCircle(r)
        #print(f"xa {xs} ya {ys}")
        x0 = xs + r
        y0 = ys
        result1 = math.atan2(y0 - ys, x0 - xs) - math.atan2(ya - ys, xa - xs)
        result2 = math.atan2(y0 - ys, x0 - xs) - math.atan2(yb - ys, xb - xs)
        #print('kupa2', result1)
        #print('kupa2', result2)
        if (self.typeOfSegment == SegmentType.Right):
            return (xs + 100 - r, ys + 100 - r, 2 * r, 2 * r), result1, result2
        else:
            return (xs + 100 - r, ys + 100 - r, 2 * r, 2 * r), result2, result1