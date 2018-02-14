class Call(object):
    NUMCALLS = 0
    def __init__(self, name, number, time, reason):
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
        self.id = Call.NUMCALLS
        Call.NUMCALLS +=1

    def display_info(self):
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = self.queue_size()

    def queue_size(self):
        return len(self.calls)

    def add(self, phone_call):
        self.calls.append(phone_call)

    def remove(self, remove_call):
        self.calls.remove(remove_call)

    def info(self):
        for call in self.calls:
            call.display_info()

def handle_call():
    print "Make call?"
    print "1 for yes and 0 for no"
    user_response = raw_input()
    return int(user_response)

def take_call():
    print "What is your name?"
    name = raw_input()
    print "Please confirm your phone number"
    num = raw_input()
    print "What time is it?"
    time = raw_input()
    print "What is your reason for calling?"
    reason = raw_input()
    return Call(name, num, time, reason)

game_on = True
center = CallCenter()
while game_on:
    ring = handle_call()
    if ring == 1:
        center.calls.append(take_call())
        print "All calls today:"
        center.info()
    else:
        game_on = False