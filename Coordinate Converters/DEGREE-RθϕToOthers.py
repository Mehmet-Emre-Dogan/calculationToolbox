from math import sqrt, atan2, degrees, cos, sin, radians
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Rθϕ input - Degree Edition")
while True:
    try:
        print("#"*70)
        with open("precision.txt", "r", encoding="utf-8") as fil:
            precision = int(fil.read())
        print("Please enter Cylindrical coordinates. Press CTRL^C to exit.")
        print(f"Precision is set to {precision}. You can change it by editing 'precision.txt'\n")
        r = float(input("R (meters): "))
        theta = radians(float(input("θ (degrees): ")))
        phi = radians(float(input("ϕ (degrees): ")))

        print("\n" + " Cartesian ".center(70, "="))
        x = r*sin(theta)*cos(phi)
        y = r*sin(theta)*sin(phi)
        z = r*cos(theta)

        maxVal = str( max( (abs(int(x)), abs(int(y)), abs(int(z))) ) )
        print(f"--> x: {round(x, precision)} ".ljust(10 + len(maxVal) + precision) + "meters")
        print(f"--> y: {round(y, precision)} ".ljust(10 + len(maxVal) + precision) + "meters")
        print(f"--> z: {round(z, precision)} ".ljust(10 + len(maxVal) + precision) + "meters")
        
        print("\n" + " Cylindrical ".center(70, "="))
        rCyl = sqrt(x**2 + y**2)
        phiCyl = atan2(y, x)
        
        print(f"--> r: {round(rCyl, precision)} meters")
        print(f"--> ϕ: {round(degrees(phiCyl), precision)}°  --> ϕ: {round(phiCyl, precision)} radians")
        print(f"--> z: {round(z, precision)} meters")
        print(" ")

    except KeyboardInterrupt:
        break
    except Exception as ex:
        print(ex)
