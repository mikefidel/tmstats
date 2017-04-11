#!/usr/bin/env python
""" Create the index.html page for the alignment directory on d101tm """

import dbconn, tmutil, sys, os
from time import localtime, strftime
import tmglobals
globals = tmglobals.tmglobals()


### Insert classes and functions here.  The main program begins in the "if" statement below.

if __name__ == "__main__":
 
    import tmparms
    # Handle parameters
    parms = tmparms.tmparms()
    parms.add_argument('--quiet', '-q', action='count')
    
    # Do global setup
    globals.setup(parms)
    conn = globals.conn
    curs = globals.curs

    
    lfile = 'd101location.html'
    mfile = 'd101newmarkers.js'
    rfile = 'd101proforma.html'
    # Get the last-modified dates for the alignment files.
    ltime = strftime("%Y-%m-%d %X", localtime(os.path.getmtime(lfile)))
    mtime = strftime("%Y-%m-%d %X", localtime(os.path.getmtime(mfile)))
    rtime = strftime("%Y-%m-%d %X", localtime(os.path.getmtime(rfile)))
    
    sys.stdout.write("""<html>
    <head>
      <title>D101 Proposed Realignment</title>
    </head>
    <body>
      <p>This page lets you see the proposed realignment in four different ways:
      <ul>
        <li>As a <a href="d101align.htm">map</a> (updated %s)</li>
        <li>As a <a href="d101proforma.html"><i>pro forma</i> Green/Yellow/Red report</a> (updated %s)</li>
        <li>As a <a href="d101location.html">summary report, including club movement</a> (updated %s)</li>
      </ul>
      %s
    </body>
</html>""" % (mtime, rtime, ltime, open('alignmentsource.txt').read()))
    
    
    
