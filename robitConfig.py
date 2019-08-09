import configparser

def loadConfig():
    config = configparser.ConfigParser()
    config.read('robitConfig.ini')
    config_to_use = config['DEFAULT']['robit.config']
    print("                         `. ___\n                        __,' __`.                _..----....____\n            __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'\n      _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'\n    ,'________________                          \`-._`-','\n     `._              ```````````------...___   '-.._'-:\n        ```--.._      ,.   CONFIG            ````--...__\\\-.\n                `.--. `-`  LOADED               ____    |  |`\n                  `. `.                       ,'`````.  ;  ;`\n                    `._`.        __________   `.      \\'__/`\n                       `-:._____/______/___/____`.     \\  `\n                                   |       `._    `.    \\\n                                   `._________`-.   `.   `.___\n                                                      `------'`")
    print("Using config ", config_to_use)
    return config[config_to_use]

values = loadConfig()