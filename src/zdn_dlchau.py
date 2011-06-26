#!/home/kmtu/bin/python3.2
import argparse

parser = argparse.ArgumentParser(description='Calculate z-density')
parser.add_argument('-a', '--atom', nargs='+', required=True,
    help='the atom(s) whose z-density are to be calculated')
parser.add_argument('-d', '--history', nargs='+', required=True,
    type=argparse.FileType('r'), metavar='HISTORY',
    help='HISTORY files of DL_POLY in Chau\'s version')
parser.add_argument('-r', '--atqref', default='ATQREF',
    type=argparse.FileType('r'), 
    help='ATQREF file for referencing the atom records')

args = parser.parse_args()
print("atom: " + str(args.atom))
atqrefList= [line.split()[0] for line in args.atqref]
atom = {}
for atm in args.atom:
    atom[atm] = {}
    atom[atm]['index'] = [i for i in range(len(atqrefList)) if atqrefList[i] == atom]
    atom[atm]['data'] = []
#    atomIndex[atom] = [i for i in range(len(atqrefList)) if atqrefList[i] == atom ]

print(atom['index'])

for file in args.history:
    lineCounter = 0
    for line in file:
        if lineCounter == 0: 
            if not int(line.split()[3]) == len(atqrefList):
                raise SystemExit("Total number of atoms does not coherent!\n"
                    "in " file.name ": " + line.split()[3]
                    "in " atqref.name ": " + str(len(atqrefList)))
            frame = line.split()[0]
        elif 2 <= lineCounter <= 4:
            index = lineCounter - 2
            dim[index] = [float(line.split()[index])] 
        elif lineCounter >= 10
            atomCounter = (lineCounter - 10) % (len(atqrefList) + 3)
            for atm in args.atom:
                if atomCounter in atomIndex[atom]
        lineCounter += 1

