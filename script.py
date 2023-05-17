def ft2inch():
    """Function that is allowing conversion from feets to inches"""


def setup():
    """Setting up a working of an program"""
    import json
    initData = dict()
    with open(r'config.json',
              'r',
              encoding='utf-8') as f:
        initData = json.load(f)

    rho = float(initData['density'])
    rpm = float(initData['revolutions'])
    d = float(initData['diameter'])
    p = float(initData['pitch'])
    v = None
    if len(initData["speed"]) == 1:
        v = initData["speed"][0]
    if len(initData["speed"]) != 1:
        v = initData["speed"]
    units = int(initData['units'])
    return [rho, rpm, d, p, v, units]


def static_formula(data):
    """Function calculating static thrust of a propeller"""
    import numpy as np
    rho, rpm, d, p, v, units = data
    # print(data)
    if units == 0:
        factor = 0.0254
    else:
        factor = 1
    force = rho*((np.pi * (factor * d)**2)/4) * \
        ((p*factor*(rpm/60))**2-(p*factor*(rpm/60))*v) * \
        ((d)/(factor*39.37008*p))**(1.5)
    return force


def dynamic_formula(data):
    """Funciotn calculating dynamic thrust of a propeller"""
    import numpy as np
    rho, rpm, d, p, speedData, units = data
    # print(data)
    force_o = []
    if units == 0:
        factor = 0.0254
    else:
        factor = 1

    spd = 0
    while spd < len(speedData):
        print(speedData[spd])
        force = rho*((np.pi * (factor * d)**2)/4) * \
            ((p*factor*(rpm/60))**2-(p*factor*(rpm/60))*speedData[spd]) * \
            ((d)/(factor*39.37008*p))**(1.5)
        print(force)
        force_o.append(force)
        spd += 1
    return force_o


def main():
    """General logic group for app"""
    data = setup()
    print("""
          What do you want to calculate?
          1) - static thrust;
          2) - dynamic thrust
          """)
    setting = int(input("Chose 1 or 2: "))
    if setting == 1:
        print(static_formula(data))
    if setting == 2:
        print(dynamic_formula(data))


if __name__ == '__main__':
    main()
