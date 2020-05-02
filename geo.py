# 3点を与えて三角形の面積を計算する
# v = (x,y)
def triS(v1,v2,v3):
    v2 = v2[0]-v1[0],v2[1]-v1[1]
    v3 = v3[0]-v1[0],v3[1]-v1[1]
    
    return abs(v2[0]*v3[1]-v2[1]*v3[0])/2