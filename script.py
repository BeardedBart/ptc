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

    print(initData)


if __name__ == '__main__':
    setup()
