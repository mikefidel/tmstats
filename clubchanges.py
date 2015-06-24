#!/usr/bin/python
from simpleclub import Club
import os, sys
from tmutil import cleandate




if __name__ == "__main__":
    import dbconn, tmparms
    
    # Make it easy to run under TextMate
    if 'TM_DIRECTORY' in os.environ:
        os.chdir(os.path.join(os.environ['TM_DIRECTORY'],'data'))
        
    # Get around unicode problems
    reload(sys).setdefaultencoding('utf8')
    
    # Define args and parse command line
    parms = tmparms.tmparms()
    parms.add_argument('--fromdate', default='yesterday', dest='fromdate')
    parms.add_argument('--todate', default='today', dest='todate')
    parms.add_argument('--notify', nargs='*', default=None, dest='notify', action='append')
    parms.add_argument('--mailpw', default=None, dest='mailpw')
    parms.add_argument('--mailserver', default=None, dest='mailserver')
    parms.add_argument('--mailfrom', default=None, dest='mailfrom')
    parms.parse()
    fromdate = cleandate(parms.fromdate)
    todate = cleandate(parms.todate)
    
    
    # print 'Connecting to %s:%s as %s' % (parms.dbhost, parms.dbname, parms.dbuser)
    conn = dbconn.dbconn(parms.dbhost, parms.dbuser, parms.dbpass, parms.dbname)
    curs = conn.cursor()
    
   
    # Get information for clubs as of the "from" date:
    oldclubs = Club.getClubsOn(fromdate, curs, setfields=True)
    newclubs = {}   # Where clubs created during the period go
    changedclubs = {}  # Where clubs changed during the period go

    
    # And compare to the the list of clubs at the end of the period
    for club in Club.getClubsOn(todate, curs).values():
        if club.clubnumber not in oldclubs:
            club.info = 'New Club'
            newclubs[club.clubnumber] = club
        elif club == oldclubs[club.clubnumber]:
            # Club is unchanged; just remove it
            del oldclubs[club.clubnumber]
        else:
            # Club has changed.  Get the list of changes as a tuple (item, old, new)
            changedclubs[club.clubnumber] = (oldclubs[club.clubnumber].clubname, 
                oldclubs[club.clubnumber].delta(club))
            del oldclubs[club.clubnumber]  # And we're done with the old club
            
    # And print results
    
    if oldclubs or newclubs or changedclubs:
        print "Club changes from %s to %s\n" % (fromdate, todate)
    
    if oldclubs:
        print "Clubs which have vanished:"
        for k in oldclubs:
            print k, oldclubs[k].clubname
         
    if newclubs:   
        print "-------------------------------------------------------"
        print "New clubs:"
        for k in newclubs:
            print newclubs[k]
        
    if changedclubs:
        print "-------------------------------------------------------"
        print "Changes:"
        for k in changedclubs:
            print k, changedclubs[k][0]
            for (item, old, new) in changedclubs[k][1]:
                print item, old, new
            print    


