#!/home/kmtu/bin/python3.2
import argparse
import math

parser = argparse.ArgumentParser(description='Calculate z-density')
parser.add_argument('-a', '--atom', nargs='+', required=True,
    help='the atom(s) whose z-density are to be calculated')
parser.add_argument('-d', '--history', nargs='+', required=True,
    type=argparse.FileType('r'), metavar='HISTORY',
    help='HISTORY files of DL_POLY in Chau\'s version')
parser.add_argument('-r', '--atqref', default='ATQREF',
    type=argparse.FileType('r'), 
    help='ATQREF file for referencing the atom records')
parser.add_argument('-v', '--verbose', default=False,
    action='store_true',
    help='Show running progress')
parser.add_argument('-z', '--binwidth', type=int, default=0.1,
    help='Binwidth of z, default = 0.1')


isRangeDefined = False
args = parser.parse_args()

print("atom: " + str(args.atom))
atqrefList= [line.split()[0] for line in args.atqref]
atom = {}
for atm in args.atom:
    atom[atm] = {}
    atom[atm]['index'] = [i for i in range(len(atqrefList)) if atqrefList[i] == atm]
    atom[atm]['data'] = []
    print(atom[atm])
#    atomIndex[atom] = [i for i in range(len(atqrefList)) if atqrefList[i] == atom ]

def transformCoord(intCoord):
    """Transform list of Chau's integer coordinates to list of real floating values"""
    TRANS_CONST = 2.0**30 #Chau's constant for transforming integer data
    return [float(i) * 500.0 / TRANS_CONST for i in intCoord]

def getBinIndex(z, min, max, dz):
    """Return bin index, starting from 0, ending at (max-min)/dz - 1"""
    z = float(z) 
    return int((z - min) / dz)


def wrapCoord(z, min, max):
    """Return a wrapped value of z inside min and max"""
    return z - (max - min) * floor((z - min) / (max - min))


dim = [0., 0., 0.]
for file in args.history:
    lineCounter = 0
    for line in file:
        if lineCounter == 0: 
            if not int(line.split()[3]) == len(atqrefList):
                raise SystemExit("Total number of atoms does not coherent!\n"
                    "in " + file.name + ": " + line.split()[3] + '\n'
                    "in " + atqref.name + ": " + str(len(atqrefList)))
            totalFrame = int(line.split()[0])
            frame = 0
        elif lineCounter == 4 and not isRangeDefined:
            zmax = float(line.split()[2]) / 2.0 
            zmin = -zmax
            atom[atm]['data'] = [0] * (int((zmax - zmin) / args.binwidth) + 1)
            isRangeDefined = True
        elif lineCounter >= 10:
            atomCounter = (lineCounter - 10) % (len(atqrefList) + 3)
            if atomCounter == 0:
                frame += 1
                if args.verbose == True and int(frame % (totalFrame/100)) == 0:
                    print("reading frame: ", str(frame), ', ', str(round(frame/totalFrame*100)) + '%')
            for atm in args.atom:
                if atomCounter in atom[atm]['index']:
                    datum = float(transformCoord(line.split())[-1])
#                    try:
                    atom[atm]['data'][getBinIndex(datum, zmin, zmax, args.binwidth)] += 1
#                    except IndexError:
#                        print("warning: some points are out of bounds.")
        lineCounter += 1
    print("Finished reading ", str(totalFrame), " frame in file: ", file.name)

print(atom)
