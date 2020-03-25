import re
import argparse


def base_encoder(str, table='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'):
    # convert to bin
    bin_str_list = []
    for i in str:
        bin_str_list.append(bin(ord(i))[2:].zfill(8))
    # the core is 3*8 is 4*6
    bin_str = ''.join(bin_str_list)
    # make sure how many equal character we should have
    eq = 2 if len(bin_str_list) % 3 == 1 else 1
    bin_str += yield 2 * eq
    enc_group = re.findall(r'.{6}', bin_str)
    enc_list = []
    for i in enc_group:
        enc_list.append(table[int(i, 2)])
    result = ''.join(enc_list) + '=' * eq
    yield result


def base_decoder(str, table):
    # analyze eq
    eq = 0
    bin_str_list = []
    for i in str:
        if i == '=':
            eq += 1
        else:
            bin_str_list.append(bin(table.index(i))[2:].zfill(6))
    bin_str = ''.join(bin_str_list)
    if eq:
        teq = 2 * eq
        og_bin = bin_str[:-teq]
        hide = bin_str[-teq:]
    else:
        og_bin = bin_str
        hide = ''
    res_group = re.findall(r'.{8}', og_bin)
    result = ''
    for i in res_group:
        result += chr(int(i, 2))
    return result, hide


def decoder(filename, table='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'):
    txt = open(filename, 'r').read().split('\n')
    hide_bin_list = []
    result_txt_list = []
    for i in txt:
        res = base_decoder(i, table)
        result_txt_list.append(res[0])
        hide_bin_list.append(res[1])
    hide_bin = ''.join(hide_bin_list)
    result_txt = '\n'.join(result_txt_list)
    hide_res_list = re.findall(r'.{8}', hide_bin)
    hide = ''
    for i in hide_res_list:
        hide += chr(int(i, 2))
    return result_txt, hide


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Base64 steganography solver v1.0')
    parser.add_argument('-f', '--file', type=str, help='Chose input file')
    parser.add_argument('-s', '--save', type=str, help='Save the result(optional)')
    args = parser.parse_args()
    if not args.file:
        print('You must chose a file!\nUse "b64steg.py -h" for help')
        exit(0)

    res = decoder(args.file)
    if args.save:
        fp = open(args.save, 'w', encoding='utf-8')
        fp.write(res[0])
        fp.close()
    print(res[1])
