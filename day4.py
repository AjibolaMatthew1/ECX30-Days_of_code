def hexadecimal_converter(number):
    ###This function converts an input integer (decimal) to an hexadecimal number. An hexadecimal number rangees from 0 - F (0 - 15). Note the number is prefixed with the standard 0x E.G. hexadecimal_converter(9999) -> 0x270F.. In the example, the result is prefixed by 0x and the actual result is 270F###
    hexadecimal_dict = {0: 0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:"A", 11:"B", 12:"C", 13: "D", 14: "E", 15: "F"}
    output = ""
    while (number // 16) != 0:
        result = number % 16
        output += str(hexadecimal_dict[result])
        number = number // 16
    result = number % 16
    output += str(hexadecimal_dict[result])
    print(f"0x{output[::-1]}")
    return output[::-1]

hexadecimal_converter(1128)
hexadecimal_converter(9999)
