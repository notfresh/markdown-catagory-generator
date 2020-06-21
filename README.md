# markdown-catagory-generator

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

This is a tool to help you generator mardown catagory start with `#` or `##` automatically.

If you are bothered to create the catagory after you have finished your long README.md  or other markdown file, this is the right tool for you.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [example](#example)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

I had once seen  [a long C++ turtorial](https://github.com/AnkerLeng/Cpp-0-1-Resource) in Github, it's very good but there is no catagory for it.

I know you can download the repository and view it locally by typora or something else,  Yes, it's truly convenient. BUT it's not friendly for us to view the markdown file on GitHub.

So I create the script with less than 100 lines to help us create the markdown catagory automatically.

I hope it will free you from the unpleasant process of writing the dummy catagory writting. 

It's not perfect now, but it's a step from 0 to 1.


## Install

open the termial, and in python3.6+ enviroment, run the following script:

```
pip install md-cata-notfresh==0.0.2
```



## Usage

open the termial, and in python3.6+ enviroment, run the following script:

```
md-cata THE_MARKDOWN_FILE_YOU_WANT_TO_GENERATE_A_CATAGORY
```



As you follow the script above, you will have a `THE_MARKDOWN_FILE_YOU_WANT_TO_GENERATE_A_CATAGORY.catagory.txt ` in the same direcotory, you can copy the content to the location in the `THE_MARKDOWN_FILE_YOU_WANT_TO_GENERATE_A_CATAGORY` wherever you prefer.

then you can delete the useless file.

It's so easy and need future improvement.  But for now, it's useful enough for me in the daily writing.

> I have place the **source code and  release dir** in the repository root.

notice: the catagory is generated base on [Github favored markdown](https://github.github.com/gfm/). 

## example

if you download the reposity and install it.

then you run `md-cata README.md`, you will get README.md.catagory.txt and the content will be the following:

```
[markdown-catagory-generator](#markdown-catagory-generator)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[Table of Contents](#Table-of-Contents)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[Background](#Background)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[Install](#Install)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[Usage](#Usage)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[example](#example)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[Maintainers](#Maintainers)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[Contributing](#Contributing)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[License](#License)<br/>
```

**so you can copy it the README.md and place it in a prefered position**, and then delete the file.

it won't be very useful in a short README.md or ANDY_FILE.md, but it will be a good tool in the long markdown file such as 1000 lines in the file.



## Maintainers

[@notfresh](https://github.com/notfresh)

## Contributing

See [the contributing file](contributing.md)!

PRs accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © not fresh 2020

