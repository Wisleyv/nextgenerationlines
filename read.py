import os
import io
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--character', help='Character you want to search for', default='PICARD')
parser.add_argument('--file', help='Write lines to a file')

args = parser.parse_args()

charlines = []

for fi in os.listdir('.'):
    with io.open(fi, 'r', errors='replace') as f:
        lines = f.readlines()
        cursor = False
        sentence = ''
        for line in lines:
            if str(args.character).upper() in line and len(line.split('\t')) == 6:
                cursor = True
                continue
            if cursor and len(line.split('\t')) == 4:
                if len(sentence) == 0:
                    sentence += line.replace('\t', '').rstrip()
                else:
                    sentence += ' '+line.replace('\t', '').rstrip()
            if cursor and len(line.split('\t')) == 5:
                continue
            if cursor and len(line.split('\t')) != 4:
                cursor = False
                charlines.append(sentence)
                sentence = ''

if args.file:
    with open(args.file, 'w') as f:
        for line in charlines:
            f.write('%s\n' % line)

for i in charlines:
    print(i)
