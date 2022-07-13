"""
depend on: pygtrans lib
Thanks to 田所flow, and zhaochenyang20
This program can work in wsl2, I haven't try it in MacOS.
"""

from pygtrans import Translate
import argparse
import os
import re
import numpy as npy
from tqdm import tqdm
from pygtrans import Translate
from IPython import embed

def parser_data():
    """
    命令行参数：
    1. -n 用户希望复习的单词数量(default: 50)
    2. -s 用户希望范围从第几个单词开始
    3. -l 用户希望复习的范围大小
    Returns:
        num, start, length
    """
    parser = argparse.ArgumentParser(
        description="生成单词本"
    )
    parser.add_argument(
        "-n", "--num",
        dest="num",
        type=int,
        default=50,
        help="The number of words you want to review, default: 50"
    )
    parser.add_argument(
        "-s", "--start",
        dest="start",
        type=int,
        default=0,
        help="Where to start from, default: 0"
    )
    parser.add_argument(
        "-l", "--length",
        dest="length",
        type=int,
        default=100,
        help="How many words to choose from, default: 100"
    )
    args = parser.parse_args()
    return args.num, args.start, args.length

def get_index():
    """
    To get the available index for the word list in generating
    Return:
        the index
    """
    for _, __, files in os.walk("./data"):
        index = 0
        for file in files:
            if file.endswith(".txt"):
                index = max(
                    index, int((re.findall(r'\d+', file))[0])
                )
    return index + 1

def get_words(wordline: str):
    """
    To get words in the line
    Return:
        a list of words
    """
    wordlist = re.findall(r'[a-zA-Z| ]+', wordline)
    return [word.strip() for word in wordlist]

def not_emptyLine(line: str):
    if line != "\n":
        return True
    else:
        return False

def generator(num, start, length):
    """
    To generate the word list
    params:
    num: 单词个数
    start: 考察范围从哪里开始
    length: 考察范围大小
    """
    client = Translate()
    with open("./collection.txt", "r") as origin:
        word_lines = origin.readlines()
    tmplist = filter(not_emptyLine, word_lines)
    word_lines = list(tmplist)

    start = max(0, start)
    start = min(start, len(word_lines))
    if start + length > len(word_lines):
        length = len(word_lines) - start
    
    random_set = set()
    while len(random_set) < num:
        random_set.add(int(npy.random.randint(start, start + length, size=1)))
    random_list = list(random_set)
    
    index = get_index()
    with open(f"./data/untranslated_{index}.txt", "w") as f:
        for i in range(len(random_list)):
            f.write(f"第{i + 1}词组： ")
            try:
                f.write(word_lines[random_list[i]])
            except:
                embed()
    with open(f"./data/translated_{index}.txt", "w") as f:
        for i in tqdm(range(num)):
            f.write(f"第{i + 1}词组： ")
            word_list = get_words(word_lines[random_list[i]])
            for each in word_list:
                try:
                    text = client.translate(each)
                    f.write(
                        each + ": " + text.translatedText + " "
                    )
                except Exception as e:
                    f.write(each + ": " + "翻译失败 ")
            f.write("\n")
    print("114514")

if __name__ == "__main__":
    generator(*parser_data())