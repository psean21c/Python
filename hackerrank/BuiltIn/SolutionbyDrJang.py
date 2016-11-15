'''
@author: Dr. DongWook Jang

score.txt
------------------
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

'''

#!/usr/bin/env python

import sys

def main(argv):

    tag = "score.txt"
    
    nargs = len(argv)
    if nargs > 0: tag = argv[0]

    data = {}
    ndata = None
    name = None
    counter = 0
    
    try:
        fin = open(tag)
        for iline, line in enumerate(fin):
            if iline == 0:
                ndata = int(line.strip())
                continue
            if iline%2 == 1: name = line.strip()
            else:
                score = float(line.strip())
                data.setdefault(score,[]).append(name)
                counter += 1
        fin.close()
    except:
        print ("IO Error for filename :", tag)
    
    assert ndata == counter
    
    scores = list(data.keys())
    print(scores)
    scores.sort()
    # for score in scores:
    #     print data[score], score
    names = data[scores[1]]
    names.sort()
    for name in names:
        print (name)
        

if __name__ == '__main__':
    main(sys.argv[1:])
    
