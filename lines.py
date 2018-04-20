import os
import io
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--character', help='Character you want to search for. Default is "picard"', default='PICARD')
parser.add_argument('--file', help='Write lines to a file')

args = parser.parse_args()

charlines = []

for episode in os.listdir('.'):
    if episode.endswith('.txt'):
        with io.open(episode, 'r', errors='replace') as f:
            lines = f.readlines()
            cursor = False
            sentence = ''
            for l in lines:
                line = l.split('\t')
                if str(args.character).upper() in l and len(line) == 6:
                    cursor = True
                    continue
                if cursor:
                    if len(line) == 4:
                        if len(sentence) != 0:
                            sentence += ' '
                        sentence += l.replace('\t', '').rstrip()
                    elif len(line) == 5:
                        continue
                    else:
                        cursor = False
                        charlines.append(sentence)
                        sentence = ''

if args.file:
    with open(args.file, 'w') as f:
        for line in charlines:
            f.write('%s\n' % line)

for i in charlines:
    print(i)
