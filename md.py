#!/usr/bin/env python3
# coding=utf-8


def catatory_gen(args):
    filename = args.filename
    level = args.level

    if not level:
        level = 4
    elif level >= 4:
        level = 4
    elif level < 2:
        level = 2

    file = open(filename, mode='r', encoding='utf-8')
    cata = []
    WHITE_SAPCE = '&nbsp;'
    CODE_BLOCK_NUM = 0
    for line in file.readlines():
        if line.startswith('```'):
            CODE_BLOCK_NUM += 1
        elif CODE_BLOCK_NUM % 2 == 0 and line.startswith("# "):
            txt = line[2:-1]
            txt_link = txt.replace(' ', '-').replace('.', '')
            cata.append(WHITE_SAPCE * 0 + '[{}](#{})'.format(txt, txt_link))
        elif CODE_BLOCK_NUM % 2 == 0 and line.startswith("## "):
            txt = line[3:-1]
            txt_link = txt.replace(' ', '-').replace('.', '')
            cata.append(WHITE_SAPCE * 4 + '[{}](#{})'.format(txt, txt_link))
        elif CODE_BLOCK_NUM % 2 == 0 and level >= 3 and line.startswith("### "):
            txt = line[4:-1]
            txt_link = txt.replace(' ', '-').replace('.', '')
            cata.append(WHITE_SAPCE * 8 + '[{}](#{})'.format(txt, txt_link))
        elif CODE_BLOCK_NUM % 2 == 0 and level >= 4 and line.startswith("#### "):
            txt = line[5:-1]
            txt_link = txt.replace(' ', '-').replace('.', '')
            cata.append(WHITE_SAPCE * 12 + '[{}](#{})'.format(txt, txt_link))


    file.close()
    cata = [item + '<br/>' for item in cata]
    catagory = "\n".join(cata)
    with open(filename + '.catagory.txt', 'w+', encoding='utf-8') as f:
        f.writelines(catagory)


def readme_gen(args):
    import os
    from shutil import copyfile

    language = args.language
    script_file_path = os.path.split(os.path.realpath(__file__))[0]
    working_path = os.getcwd()
    # print("script_file_path", script_file_path)
    # print("working_path", working_path)
    if language == 'en':
        template_path = "templates/README.md"
    elif language == 'cn':
        template_path = "templates/README-CN.md"
    try:
        copyfile(os.path.join(script_file_path, template_path), os.path.join(working_path, "README.md"))
    except Exception:
        print("no privilige to write")


def reading_note(args):
    import os
    from shutil import copyfile

    reading_name = args.reading_name
    script_file_path = os.path.split(os.path.realpath(__file__))[0]
    working_path = os.getcwd()
    # print("script_file_path", script_file_path)
    # print("working_path", working_path)
    template_path = "templates/READING-NOTE.md"
    try:
        copyfile(os.path.join(script_file_path, template_path), os.path.join(working_path, reading_name + "-READING-NOTE.md"))
    except Exception:
        print("no privilige to write")

import argparse
parser = argparse.ArgumentParser(prog='md-gen') # 使用md作为文件开始
subparsers = parser.add_subparsers(title='subcommands',
                                   description='catagory,readme',
                                   help='additional help')

catatory_parser = subparsers.add_parser("catagory", help="the file you want to generate a catatory")
catatory_parser.add_argument("filename", help="the file you want to generate a catatory")
catatory_parser.add_argument("-L",  '--level', type=int, help="the level you want to generate, the default is 4, the valid range is 2-4")
catatory_parser.set_defaults(func=catatory_gen)

readme_parser = subparsers.add_parser("readme", help="generate a template standard readme for you")
readme_parser.add_argument("language", help="choose the lanuge you prefer, cn for Chinese or en for English")
readme_parser.set_defaults(func=readme_gen)

readme_parser = subparsers.add_parser("reading", help="generate a template reading note for you")
readme_parser.add_argument("reading_name", help="the book or article title you just read")
readme_parser.set_defaults(func=reading_note)

args = parser.parse_args()
args.func(args)

