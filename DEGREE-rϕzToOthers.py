from math import sqrt, atan2, degrees, cos, sin, radians
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("rϕz input - Degrees Edition")
while True:
    try:
        print("#"*70)
        with open("precision.txt", "r", encoding="utf-8") as fil:
            precision = int(fil.read())
        print("Please enter Cylindrical coordinates. Press CTRL^C to exit.")
        print(f"Precision is set to {precision}. You can change it by editing 'precision.txt'\n")
        r = float(input("r (meters): "))
        phi = radians(float(input("ϕ (degrees): ")))
        z = float(input("z (meters): "))

        print("\n" + " Cartesian ".center(70, "="))
        x = r*cos(phi)
        y = r*sin(phi)

        maxVal = str( max( (abs(int(x)), abs(int(y)), abs(int(z))) ) )
        print(f"--> x: {round(x, precision)} ".ljust(10 + len(maxVal) + precision) + "meters")
        print(f"--> y: {round(y, precision)} ".ljust(10 + len(maxVal) + precision) + "meters")
        print(f"--> z: {round(z, precision)} ".ljust(10 + len(maxVal) + precision) + "meters")
        
        print("\n" + " Spherical ".center(70, "="))
        rSph = sqrt(x**2 + y**2 + z**2)
        thetaSph = atan2(sqrt(x**2 + y**2), z)
        phiSph = atan2(y, x)
        
        print(f"--> R: {round(rSph, precision)} meters")
        print(f"--> θ: {( str(round(degrees(thetaSph), precision)) + '°').ljust(6 + precision)}  --> θ: {str(round(thetaSph, precision)).ljust(5 + precision)} radians")
        print(f"--> ϕ: {( str(round(degrees(phiSph), precision)) + '°').ljust(6 + precision)}  --> ϕ: {str(round(phiSph, precision)).ljust(5 + precision)} radians")
        print(" ")

    except KeyboardInterrupt:
        break
    except Exception as ex:
        print(ex)