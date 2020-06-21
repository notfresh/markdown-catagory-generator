#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the file you want to generate a catatory")
parser.add_argument("-L",  '--level', type=int, help="the level you want to generate, the default is 4, the valid range is 2-4")
args = parser.parse_args()

filename = args.filename
level = args.level

if not level:
    level = 4
elif level >= 4:
    level = 4
elif level < 2:
    level = 2

def main():
    global filename
    global level
    file = open(filename, mode='r', encoding='utf-8')
    cata = []
    WHITE_SAPCE = '&nbsp;'
    for line in file.readlines():
        if line.startswith("# "):
            txt = line[2:-1]
            txt_link = txt.replace(' ', '-').replace('.', '')
            cata.append(WHITE_SAPCE * 0 + '[{}](#{})'.format(txt, txt_link))
        elif line.startswith("## "):
            txt = line[3:-1]
            txt_link = txt.replace(' ', '-').replace('.', '')
            cata.append(WHITE_SAPCE * 4 + '[{}](#{})'.format(txt, txt_link))
        elif level >= 3 and line.startswith("### "):
            txt = line[4:-1]
            txt_link = txt.replace(' ', '-').replace('.', '')
            cata.append(WHITE_SAPCE * 8 + '[{}](#{})'.format(txt, txt_link))
        elif level >= 4 and line.startswith("#### "):
            txt = line[5:-1]
            txt_link = txt.replace(' ', '-').replace('.', '')
            cata.append(WHITE_SAPCE * 12 + '[{}](#{})'.format(txt, txt_link))

    file.close()
    cata = [item + '<br/>' for item in cata]
    catagory = "\n".join(cata)
    with open(filename + '.catagory.txt', 'w+', encoding='utf-8') as f:
        f.writelines(catagory)


if __name__ == '__main__':
    main()





