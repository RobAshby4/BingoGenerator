import os, sys
import random
import textwrap
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def list_from_file():
    filename = input("Name of list file (ext included)(first item is free space): ")
    try:
        f = open(filename, 'r')
    except:
        print("file does not exist")
        exit()
    input_list = f.readlines()
    f.close()
    ret_list = []
    for li in input_list:
        fmt_li = li.replace("\n","")
        ret_list.append(fmt_li)
    return ret_list

def list_from_stdin():
    print("please input 25 items for bingo (first item is free space)")
    ret_list = []
    for i in range(1, 26):
        li = input(str(i) + ": ")
        ret_list.append(li)
    return ret_list

def fmt_free_space(bl):
    free_space = bl.pop(0)
    random.shuffle(bl)
    bl.insert(12, free_space)
    return bl

def main():
    while True:
        read_from_file = input("would you like to read from file? (y/n): ")
        if read_from_file.lower() == "y":
            bingo_list = list_from_file()
            break
        elif read_from_file.lower() == "n":
            bingo_list = list_from_stdin()
            break
        else:
            print("invalid input, please answer y or n")
            continue
    
    bingo_list = fmt_free_space(bingo_list)
    font = ImageFont.truetype("DejaVuSans.ttf", 50)
    img = Image.open("bingo_board.png")
    draw = ImageDraw.Draw(img)

    for y in range(333, 1774, 360):
        for x in range(105, 1546, 360):
            y_text = 0
            tile_txt = bingo_list.pop(0)
            tile_txt = textwrap.wrap(tile_txt, width = 12)
            for lines in tile_txt:
                w,h = draw.textsize(lines, font = font)
                draw.text((((x + 175) - (w / 2)) , (y + 175) - ((h / 2) * len(tile_txt))  + y_text), lines, (0,0,0), font = font)
                y_text += h + 2;

    img.save('bingo_out.png')    

if __name__ == "__main__":
    main()