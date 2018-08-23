#!/usr/bin/env python3
"""Events:

    Houses the Event class definitions. Trainings, Contests, and 
    Great Events are all examples of Event implementations.
"""


class Event:
    ptemplate = '%Y-%m-%d %H:%M:%S'
    
    def __init__(area, venues, *args, **kwargs):
        for item in contents:
            ours = item.replace("_","")
            self.__dict__[ours] = contents[item]
        if '_EventVenueID' in contents:
            v = int(self.EventVenueID)
            for item in venues[v]:
                ours = item.replace("_","")
                self.__dict__[ours] = venues[v][item]
        self.start = datetime.strptime(self.EventStartDate, self.ptemplate)
        self.end = datetime.strptime(self.EventEndDate, self.ptemplate)
        self.include = (self.start >= parms.start) and (self.end <= parms.end)
        self.showreg = parms.showpast or (self.end > parms.now)
        self.name = name
        self.title = title
        self.posts, self.venuenumbers = self.getinfo(curs, 

#    def getinfo(self, curs, table, post_list):
#        venue_numbers = set()
#        posts = {}
#        # Get all the event information from the database
#        stmt = "SELECT post_id, meta_key, meta_value FROM %s WHERE post_id IN (%s)" % (table,post_list)
#        curs.execute(stmt)
#        for (post_id, meta_key, meta_value) in curs.fetchall():
#            if post_id not in posts:
#                posts[post_id] = {'post_id':post_id}
#            posts[post_id][meta_key] = meta_value.strip()
#            if meta_key == '_EventVenueID':
#                venue_numbers.add(meta_value)
#        
#        return (posts, venue_numbers)  




