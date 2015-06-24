#!/usr/bin/python


import sys


def usage():
        print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
        if len(sys.argv) != 2:
                usage()
                sys.exit(1)
        try:
                fp = open(sys.argv[1], "r")
        except IOError, e:
                print >> sys.stderr, "Not a valid file name"
                usage()
                sys.exit(1)
        fp.seek(0)
        max=-1
        min=11
        for idx, line in enumerate(list(fp)):
                a=line.split("\t")
                if len(a) < 4:
                        continue
                if max<float(a[3]):
                        prenume_max=a[0]
                        nume_max=a[1]
                        grupa_max=a[2]
                        max=float(a[3])
                if min>float(a[3]):
                        prenume_min=a[0]
                        nume_min=a[1]
                        grupa_min=a[2]
                        min=float(a[3])
        print "Studentul cu nota maxima:", prenume_max, nume_max, grupa_max
        print "Studentul cu nota minima:", prenume_min, nume_min, grupa_min


if __name__ == "__main__":
        sys.exit(main())
