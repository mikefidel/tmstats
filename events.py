#!/usr/bin/env python3
""" 
docs

"""

class Event:
    ptemplate = '%Y-%m-%d %H:%M:%S'
    
    # Putting this database connection method inside the Event namespace
    @staticmethod
    def connect_to_db():
        conn = dbconn.dbconn(config['DB_HOST'], config['DB_USER'], config['DB_PASSWORD'], config['DB_NAME'])
        return curs

    def __init__(self, contents, venues, parms):
        for item in contents:
            ours = item.replace("_","")
            self.__dict__[ours] = contents[item]
        if '_EventVenueID' in contents:
            v = int(self.EventVenueID)
            for item in venues[v]:
                ours = item.replace("_","")
                self.__dict__[ours] = venus[v][item]
                  
        self.start = datetime.strptime(self.EventStartDate, self.ptemplate)
        self.end = datetime.strptime(self.EventEndDate, self.ptemplate)
        self.include = (self.start >= parms.start) and (self.end <= parms.end)
        self.showreg = parms.showpast or (self.start > parms.now)

class Training(Event):
    def __init__(self, name, title, *args, **kwargs):
        super().__init__(**kwargs):
            self.name = name
            self.title = title
        
            
    def __repr__(self):
        self.date = self.start.strftime('%A, %B %d').replace(' 0',' ')
        self.time = self.start.strftime(' %I:%M') + '-' + self.end.strftime(' %I:%M %p')
        self.time = self.time.replace(' 0', ' ').replace(' ','').lower()
        self.addr = '<td><b>%(VenueName)s</b><br>%(VenueAddress)s<br>%(VenueCity)s, %(VenueState)s %(VenueZip)s</td>' % self.__dict__
        try:
            self.special = '<br>%s' % self.eventspecialnote
        except AttributeError:
            self.special = ''
        if self.showreg and self.EventURL:
            self.register = ' | <a href="%(EventURL)s">Register</a>' % self.__dict__
        else:
            self.register = ""
        ans = """<tr><td><b>%(name)s</b>%(special)s<br><a href="/%(title)s">More Information</a>%(register)s</td><td><b>%(date)s</b><br>%(time)s%(addr)s</tr>""" % self.__dict__
        return ans

    
def output(what, outfile):
    outfile.write('%s\n' % what)



class Contest(Event):
    def __init__(self, area, **kwargs):
        super().__init__(**kwargs)
        self.area = area

            
    def __repr__(self):
        if len(self.area) == 1:
            self.name = '<b>Division %s Contest</b>' % self.area
        else:
            self.name = '<b>Area %s Contest</b>' % self.area
        self.date = self.start.strftime('%B %d').replace(' 0',' ')
        self.time = self.start.strftime(' %I:%M') + '-' + self.end.strftime(' %I:%M %p')
        self.time = self.time.replace(' 0', ' ').replace(' ','').lower()
        self.addr = '<td><b>%(VenueName)s</b><br>%(VenueAddress)s<br>%(VenueCity)s, %(VenueState)s %(VenueZip)s</td>' % self.__dict__
        if self.showreg:
            self.register = '<br><a href="%(EventURL)s">Register</a>' % self.__dict__
        else:
            self.register = ""
        ans = """<tr><td>%(name)s%(register)s</td><td><b>%(date)s</b><br>%(time)s%(addr)s</tr>""" % self.__dict__
        return ans

def tocome(what):
    return '<tr><td>%s</td><td>TBA</td><td>&nbsp;</td>' % what        
    
def output(what, outfile):
    outfile.write('%s\n' % what)

def getinfo(curs, table, post_list):
    venue_numbers = set()
    posts = {}
    # Get all the event information from the database
    stmt = "SELECT post_id, meta_key, meta_value FROM %s WHERE post_id IN (%s)" % (table,post_list)
    curs.execute(stmt)
    for (post_id, meta_key, meta_value) in curs.fetchall():
        if post_id not in posts:
            posts[post_id] = {'post_id':post_id}
        posts[post_id][meta_key] = meta_value.strip()
        if meta_key == '_EventVenueID':
            venue_numbers.add(meta_value)
        
    return (posts, venue_numbers)  

     
