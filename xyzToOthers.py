from math import sqrt, atan2, degrees
import ctypes
from os import read
ctypes.windll.kernel32.SetConsoleTitleW("xyz input")

while True:
    try:
        print("#"*70)
        with open("precision.txt", "r", encoding="utf-8") as fil:
            precision = int(fil.read())
        print("Please enter Cartesian coordinates. Press CTRL^C to exit.")
        print(f"Precision is set to {precision}. You can change it by editing 'precision.txt'\n")
        x = float(input("x (meters): "))
        y = float(input("y (meters): "))
        z = float(input("z (meters): "))

        print("\n" + " Cylindrical ".center(70, "="))
        rCyl = sqrt(x**2 + y**2)
        phiCyl = atan2(y, x)

        print(f"--> r: {round(rCyl, precision)} meters")
        print(f"--> ϕ: {round(degrees(phiCyl), precision)}°  --> ϕ: {round(phiCyl, precision)} radians")
        print(f"--> z: {round(z, precision)} meters")
        
        print("\n" + " Spherical ".center(70, "="))
        rSph = sqrt(x**2 + y**2 + z**2)
        thetaSph = atan2(sqrt(x**2 + y**2), z)
        phiSph = atan2(y, x)
        
        print(f"--> R: {round(rSph, precision)} meters")
        print(f"--> θ: {( str(round(degrees(thetaSph), precision)) + '°').ljust(5 + precision)}  --> θ: {str(round(thetaSph, precision)).ljust(4 + precision)} radians")
        print(f"--> ϕ: {( str(round(degrees(phiSph), precision)) + '°').ljust(5 + precision)}  --> ϕ: {str(round(phiSph, precision)).ljust(4 + precision)} radians")
        print(" ")
   
    except KeyboardInterrupt:
        break
    except Exception as ex:
        print(ex)