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


def path_load(path1, path2):
    import os
    if not os.path.exists(path1):
        return path2


def template_func(args):
    import os
    from shutil import copyfile
    import sys

    template_name = args.template_name
    # we presume the default prefix as .md
    if template_name and template_name[-3:] != '.md':
        template_name += '.md'

    user_templates_path = os.path.join(os.environ['HOME'], ".templates")
    if not os.path.exists(user_templates_path):
        os.mkdir(user_templates_path)
    script_file_path = os.path.split(os.path.realpath(__file__))[0]
    default_templates__path = os.path.join(script_file_path, 'templates')

    working_path = os.getcwd()
    # print("script_file_path", script_file_path)
    # print("working_path", working_path)

    template_path = os.path.join(user_templates_path, template_name)
    if not os.path.exists(template_path):
        template_path = os.path.join(default_templates__path, template_name)
    if not os.path.exists(template_path):
        print("template not find")
        sys.exit(1)

    try:
        copyfile(template_path, os.path.join(working_path, template_name))
    except Exception:
        print("no privilige to write")
        sys.exit(1)


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

readme_parser = subparsers.add_parser("template", help="generate the template as you difined, the templates directory locates in ~/.templates, use `md-gen` template TEMPLATE_NAME.md to generate")
readme_parser.add_argument("template_name", help="choose the template name in your template dir")
readme_parser.set_defaults(func=template_func)


args = parser.parse_args()
try:
    args.func(args)
except:
    print("use -h to get help")



import yaml
import os

class ConfigManager:

    def __init__(self):
        self.file = os.path.join(os.environ['HOME'], ".md-tool-config.yml")
        if not os.path.exists(self.file):
            file = open(self.file, "w")
            file.close()
        self.dataMap = {}

    def read(self, key):
        f = open(self.file)
        self.dataMap = yaml.load(f)
        f.close()
        return self.dataMap.get(key, '')

    def write(self, key, value):
        f = open(self.file, "w+")
        self.dataMap[key] = value
        yaml.dump(self.dataMap, f,default_flow_style=False)
        f.close()


configer = ConfigManager()
