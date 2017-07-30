
def TroyMartian(x ,y):
    # x is antennas, y is eyes
    TroyMartian_state = True

    if x > 3:
        TroyMartian_state = False

    if y < 4:
        TroyMartian_state = False

    return TroyMartian_state


def VladSaturnian(x, y):
    # x is antennas, y is eyes
    VladSaturnian_state = True

    if x > 6:
        VladSaturnian_state = False

    if y < 2:
        VladSaturnian_state = False

    return VladSaturnian_state


def GraemeMercurian(x,y):
    # x is antennas, y is eyes

    GraemeMercurian_state = True

    if x > 2:
        GraemeMercurian_state = False

    if y > 3:
        GraemeMercurian_state = False

    return GraemeMercurian_state


x = float(input("How many antennas?\n"))
y = float(input("How many eyes?\n"))

TMartian = TroyMartian(x, y)
VMartian = VladSaturnian(x, y)
GMartian = GraemeMercurian(x, y)

if TMartian == True:
    print("TroyMartian")

if VMartian == True:
    print("VladSaturnian")

if GMartian == True:
    print("GraemeMercurian")