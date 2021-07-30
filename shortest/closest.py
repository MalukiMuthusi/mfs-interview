from shortest.distance import distance


def closest(points):
    l = len(points)
    close = 0
    p1 = []
    p2 = []
    for i in range(l):
        for j in range(i+1,l):
            d = distance(points[i],points[j])
            if i == 0 and j==1:
                close = d
                p1.extend(points[0])
                p2.extend(points[1])
            else:
                if d < close:
                    close = d
                    p1.extend(points[i])
                    p2.extend(points[j])
    return p1,p2, close
            
