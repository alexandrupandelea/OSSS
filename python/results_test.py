#!/usr/bin/env python

import sys
import csv


def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    try:
        fp = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename"
        usage()
        sys.exit(1)
    tests = []
    lines = csv.reader(fp, delimiter=',', quotechar='"')
    for line in lines:
        found = 0
        for idx, test in enumerate(tests):
                if test['test_name'] == line[0]:
                        found = 1
                        k = idx
        if found == 0:
                newtest = {
                        'test_name': line[0],
                        'school': line[1],
                        'stud_name': line[2],
                        'grade': int(line[3])
                        }
                tests.append(newtest)
        elif tests[k]['grade'] < int(line[3]):
                        (tests[k]['school'], tests[k]['stud_name'],
                                tests[k]['grade']) = \
                                (line[1], line[2], int(line[3]))
    for t in tests:
        print "For test %s maximum grade is %d, student %s from %s" \
                % (t['test_name'], t['grade'], t['stud_name'], t['school'])


if __name__ == "__main__":
    sys.exit(main())
