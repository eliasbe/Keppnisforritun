import math

def main():
    (h, v) = tuple([int(x) for x in input().split()])
    l = h / math.sin(math.radians(v))
    print(math.ceil(l))

if __name__ == '__main__':
    main()
