import math

def main():
    while True:
        n = int(input())
        if n==0:
            break

        hus = list()
        for i in range(n):
            pt = tuple([float(x) for x in input().split()])
            hus.append(pt)

        top = 200000
        bottom = -200000
        EPS = 1E-6  
        
        while abs(top-bottom) > EPS:
            third = (top-bottom)/3
            Lthird = bottom + third        
            Hthird = top - third

            if distance(Lthird, hus) < distance(Hthird, hus):
                top = Hthird
            else:
                bottom = Lthird
        
        result = (top + bottom)/2
        print(result, distance(result, hus))
        input()
        
    
def distance(rendezvous, pts):
    lengst = 0.0
    for pt in pts:
        x, y = pt
        dist = math.sqrt((x-rendezvous)**2 + y**2)
        if dist > lengst:
            lengst = dist
    return lengst

if __name__ == '__main__':
    main()
