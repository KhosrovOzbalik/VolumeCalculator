def sekil():
    global hs
    import math
    pistr = input("Enter pi\n(Write 'pi' for the real value of pi.): ")
    if pistr == "pi":
        pi = math.pi
    else:
        try:
            pi = float(pistr)
        except:
            print("Please enter a valid number.")
            quit()
    girdi = input("Which volume do you want to calculate? \n""E.g: prism,cylinder,pyramid,cone,cube \n"
                  "(All of them is regular shapes.):")
    if girdi == "prism":
        kenarsayisi = input("Enter the shape of base:\n(3,4,5,6...)")
        try:
            int(kenarsayisi)
        except:
            print("Please enter an integer.")
            quit()
        if int(kenarsayisi) < 3:
            print("Polygon can't be lower than 3.")
            quit()
        import math
        kenarcm = input("The length of one side of the base :")
        yukseklik = input("Height of the object:")
        try:
            prh = float(yukseklik)
            knsy = float(kenarsayisi)
            knrcm = float(kenarcm)
        except:
            print("Please enter valid numbers.")
            quit()
        aciderece = (180 - (360 / knsy)) / 2
        radyan = aciderece / 180
        tanj = math.tan(math.pi * radyan)
        minih = (knrcm / 2) * tanj
        tabanalan = knsy * (knrcm / 2) * minih
        hacim = tabanalan * prh
        print("Area of base:",tabanalan)
        print("Volume:")
        return (hacim)
    elif girdi == "pyramid":
        kenarsayisi = input("Enter the shape of base:\n 3,4,5,6...:")
        try:
            int(kenarsayisi)
        except:
            print("Please enter an integer.")
            quit()
        if int(kenarsayisi) < 3:
            print("Polygon can't be lower than 3.")
            quit()
        import math
        kenarcm = input("The length of one side of the base :")
        yukseklik = input("The height of the object:")
        try:
            knsy = float(kenarsayisi)
            knrcm = float(kenarcm)
            piramith = float(yukseklik)
        except:
            print("Please enter a valid number.")
            quit()
        aciderece = (180 - (360 / knsy)) / 2
        radyan = aciderece / 180
        tanj = math.tan(math.pi * radyan)
        minih = (knrcm / 2) * tanj
        tabanalan = knsy * (knrcm / 2) * minih
        hacim = tabanalan * piramith
        print("Area of base:", tabanalan)
        print("Volume:")
        return (hacim)
    elif girdi == "cylinder":
        yaricap = input("Radius of the cylinder's base:")
        yukseklik = input("The height of the object:")
        try:
            rs = float(yaricap)
            hs = float(yukseklik)
        except:
            print("Please enter valid numbers.")
            quit()
        hacim = pi * rs**2 * hs
        return (hacim)
    elif girdi == "cone":
        yaricap = input("Radius of the cylinder's base:")
        yukseklik = input("The height of the object:")
        try:
            rs = float(yaricap)
            hs = float(yukseklik)
        except:
            print("Please enter valid numbers.")
            quit()
        hacim = (pi * rs**2 * hs) / 3
        print("Volume:")
        return (hacim)
    elif girdi == "cube":
        kenar = input("Enter the side length.")

        try:
            a = float(kenar)
        except:
            print("Please enter valid numbers.")
            quit()
        hacim = a**3

        return (hacim)
    else:
        print("Please enter a valid name.")
print(sekil())
