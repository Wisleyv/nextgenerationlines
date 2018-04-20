# STNG character lines

Searches through the entire manuscript for Star Trek: The Next Generation and prints out the selected characters dialog, one line at a time. Can also write the output to a file.

This makes it easy to parse for any uses you may have, e.g in my case I have a telegram bot which picks a line at random and returns it to the user

## Usage

  * Unzip scripts_tng.zip: `unzip scripts_tng.zip`
  * Run lines.py with your choices

```
usage: lines.py [-h] [--character CHARACTER] [--file FILE]

optional arguments:
  -h, --help            show this help message and exit
  --character CHARACTER
                        Character you want to search for. Default is "picard"
  --file FILE           Write lines to a file
```
