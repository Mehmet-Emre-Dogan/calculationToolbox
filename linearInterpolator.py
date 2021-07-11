def calculate():
    print("#"*50)
    print("y = f(x), press CTRL^C to exit.")
    xMin = float(input("x1--> " ))
    xKnown = float(input("xKnown--> " ))
    xMax = float(input("x2--> " ))
    yMin = float(input("y1--> " ))
    yMax = float(input("y2--> " ))

    deltax = xMax - xMin
    xDifference = xKnown - xMin
    ratio = xDifference/deltax

    deltay = yMax - yMin
    y = deltay*ratio + yMin
    print(f"==> y: {y}")

while True:
    try:
        calculate()
    except KeyboardInterrupt:
        break
    except Exception as ex:
        print(f"An error occured: {ex}")
    