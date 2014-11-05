#!/usr/bin/env python
"""
find callsigns which aren't in either list,
written in a completely non-pythonic manner
"""

from string import ascii_lowercase


def loadFile(fname):
  with open(fname) as f:
    content = [x.strip('\n') for x in f.readlines()]
  return content


def makeCallsigns(known_f_signs, known_i_signs):
  intialChar = 'e'
  result = []
  for c1 in ascii_lowercase :
    if c1 >= intialChar:
      for c2 in ascii_lowercase:
        for c3 in ascii_lowercase:
          fsign = ("m6" + c1 + c2 + c3).upper()
          isign = ("20" + c1 + c2 + c3).upper()
          if fsign not in known_f_signs and isign not in known_i_signs:
            result.append(fsign)
  return result


def main():
  for sign in makeCallsigns(loadFile("foundation.txt"), loadFile("intermediate.txt")):
    print sign

if __name__ == '__main__':
  main()
