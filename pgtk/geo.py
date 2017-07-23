import math

def deg2degmin(lat,lon):
    latdec,latdeg = math.modf(lat)
    londec,londeg = math.modf(lon)

    return (int(latdeg), latdec * 60, int(londeg), londec * 60)

def coords2str(latdeg, latdec, londeg, londec):
    latlet = 'N' if latdeg > 0 else 'S'
    lonlet = 'E' if londeg > 0 else 'W'

    #using round on multiplied integers to solve the issue with float rounding
    return "%s%02d %02.3f %s%03d %02.3f" % (latlet, latdeg, round(latdec*1000)/1000., lonlet, round(londeg*1000)/1000, londec)
