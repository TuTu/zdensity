#!/home/kmtu/bin/python3.2
import argparse

parser = argparse.ArgumentParser(description='Calculate z-density')
parser.add_argument('atom_name', 
    help='the atom whose z-density is to be calculated')
parser.add_argument('history', nargs='+', 
    type=argparse.FileType('r'),
    help='HISTORY files of DL_POLY in Chau\'s version')

args = parser.parse_args()
print(vars(args))
#target = sys.argv[sys.argv.index("-a") + 1]
#historyList = sys.argv[sys.argv.index("-f") + 1 : ]
#for arg in historyList:
#    if arg[0] == '-': 
#histories = [open(history, 'r') for history in historyList]

#print("Target atom: " + target)
#print("HISTORY files: " + str(historyList))
#
#atqref = open(r'ATQREF', 'r')
#atmlist = [line.split()[0] for line in atqref]
#targetIndex = [i for i in range(len(atmlist)) if atmlist[i] == target]

lineCounter = 0
for file in args.history:
    print(file.readline(), end='')
#  for line in file:
#    if lineCounter == 0: 
#        line.split()[0]
#  lineCounter += 1

