# TODO:
#    I need to make it so that each time I add an entry it appends to the table
# that's already there instead of just showing only the most recently created
# entry
#  - research docutils instead of terminaltables
#  - write a function(?) to automatically calculate mpg based on trip and gal
# as well as fill in price based on total / gal etc
#  -  

import time
from terminaltables import AsciiTable

class GasLog(object):

    def __init__(self):
        self.logFile = open('autolog_gaslog.log', 'a')
        self.timestamp = time.asctime(time.localtime(time.time()))
        self.logEntry = {}

    def add_entry(self, odo=None, trip=None, ppg=None, price=None, vol=None, tag=None):
        self.logEntry = {'Odometer': float(odo),
                         'Tripometer': float(trip),
                         'pricePerGallon': float(ppg),
                         'Total': float(price),
                         'Volume(gal)': float(vol),
                         'tag': tag
                         }
        entry_data = [
                        ['Date/Time', 'Odometer', 'Tripometer', 'Price/gal', 'cost', 'Gallons', 'Tag'],
                        [self.timestamp, odo, trip, ppg, price, vol, tag]
                ]
        table = AsciiTable(entry_data)
        return table.table
        # self.logEntry['Odometer'] = float(odo)
        # self.logEntry['Tripometer'] = float(trip)
        # self.logEntry['Price/gal'] = float(ppg)
        # self.logEntry['Total Cost'] = float(price)
        # self.logEntry['Volume(gal)'] = float(vol)
        # self.logEntry['Tag'] = tag

        # for k, v in self.logEntry.iteritems():
        #     print("%s: %r\n" % (k, v))
        # print(self.timestamp + '\n')
        # self.close_log()

    def close_log(self):
        self.logFile.close()


log = GasLog()

# log.add_entry(odo=100000, trip=300, ppg=2.55, vol=30.2, price=20.00)
print log.add_entry(odo=135000, trip=325.4, ppg=2.55, vol=11.202, price=34.22)
