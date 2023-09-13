#!/usr/bin/python3
def to_subtract(lists_num):
    to_subb = 0
    maxm_list = max(lists_num)
    for x in lists_num:
        if maxm_list > x:
            to_subb += x
    return (maxm_list - to_subb)
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rom_ns = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_of_keys = list(rom_ns.keys())
    numb = 0
    lasts_rom = 0
    lists_num = [0]
    for chtr in roman_string:
        for rn_num in list_of_keys:
            if rn_num == chtr:
                if rom_ns.get(chtr) <= lasts_rom:
                    numb += to_subtract(lists_num)
                    lists_num = [rom_ns.get(chtr)]
                else:
                    lists_num.append(rom_ns.get(chtr))
                lasts_rom = rom_ns.get(chtr)
    numb += to_subtract(lists_num)
    return (numb)
