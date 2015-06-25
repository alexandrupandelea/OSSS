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

        student = {
                'name': line[2],
                'school': line[1]
                }
        if found == 0:
                newtest = {
                        'test_name': line[0],
                        'students': [student],
#                        'school': line[1],
#                         'stud_name': line[2],
                        'grade': int(line[3])
                        }
                tests.append(newtest)
        else:
            if tests[k]['grade'] < int(line[3]):
                        (tests[k]['students'],
                                tests[k]['grade']) = \
                                ([student], int(line[3]))
            elif tests[k]['grade'] == int(line[3]):
                tests[k]['students'].append(student)

    for t in tests:
        print "For test %s maximum grade is %d" \
                % (t['test_name'], t['grade'])
        for st in t['students']:
            print "\t\t", st['name'], st['school']
        print

if __name__ == "__main__":
    sys.exit(main())
