#!/usr/local/bin/python

import sys, os, subprocess

delimit='#!'

# Get cmd line argument
if len(sys.argv) < 2:
    print("Usage: multi filename")
    sys.exit()

filename = sys.argv[1]

# Parse out sections
with open(filename, 'r') as content_file:
    content = content_file.read()

sections = filter(None,content.split(delimit))

for idx, section in enumerate(sections):
    # Get first line of each section (the command to run)
    split_section = section.split('\n',1)
    tmpfilename = 'tmpfile' + str(idx)
    f = open(tmpfilename,'w')
    f.write('#!'+ split_section[0] + split_section[1])
    f.close()
    os.chmod(tmpfilename,0b111101101)
    result = subprocess.check_output([split_section[0].strip(), './' + tmpfilename])
    sys.stdout.write(result)
    os.remove(tmpfilename)
