def ft2inch():
    """Function that is allowing conversion from feets to inches"""


def setup():
    """Setting up a working of an program"""
    import json
    initData = dict()
    with open(r'ptc\config.json',
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


def formula(data):
    """Function containing main core of app"""
    import numpy as np
    rho, rpm, d, p, v, units = data
    print(data)
    if units == 0:
        factor = 0.0254
    else:
        factor = 1
    force = rho*((np.pi * (factor * d)**2)/4) * \
        ((p*factor*(rpm/60))**2-(p*factor*(rpm/60))*v) * \
        ((d)/(factor*39.37008*p))**(1.5)
    return force


if __name__ == '__main__':
    data = setup()
    print(formula(data))
