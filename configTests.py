import robitConfig

# access string values using brackets
right_pin = robitConfig.values['motor.right.gpio.pin']
print(right_pin, " : ", type(right_pin))

# or using getters
left_pin = robitConfig.values['motor.left.gpio.pin']
print(left_pin, " : ", type(left_pin))

# or built in typed methods if needed
test_bool = robitConfig.values.getboolean('misc.test.boolean')
print(test_bool, " : ", type(test_bool))

test_float = robitConfig.values.getfloat('misc.test.float')
print(test_float, " : ", type(test_float))

# https://docs.python.org/3/library/configparser.html