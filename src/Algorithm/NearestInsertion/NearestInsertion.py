# complexity O(n^2)
from time import process_time

from src.utils.help import routeLength


def closestPoint(path,points,tsp):
    minLength = float("inf")
    closestPoint = None
    for inPoint in path:
        for outPoint in points:
            d = tsp[(inPoint, outPoint)]
            if d < minLength:
                minLength = d
                closestPoint = outPoint

    # return the length and closestPoint
    return minLength, closestPoint


def insertNodeToPath(path,tsp,insertNode):
    minLength = float("inf")
    insert = 0
    l = len(path)
    for i in range(l):
        tmpPath = path.copy()
        # make a try to insert the insertNode
        tmpPath.insert(i, insertNode)
        # make closed route
        d = routeLength(tsp,tmpPath)
        if d < minLength:
            minLength = d
            insert = i

    # return the insertion location
    return insert


def NearestInsertion(tsp, n, startPoint):
    points = list(range(n))
    points.remove(startPoint)
    path = [startPoint]
    #
    totalDistance = 0
    t1_start = process_time()
    while len(points) > 0:
        # find the nearest node to the route
        d, closePoint = closestPoint(path,points,tsp)
        # find the most proper location to insert the found point
        idInsert = insertNodeToPath(path,tsp,closePoint)
        # insert it to the route and remove it from the given set.
        path.insert(idInsert, closePoint)
        points.remove(closePoint)
        totalDistance += d
    t1_stop = process_time()
    return path, routeLength(tsp, path), (t1_stop - t1_start)
