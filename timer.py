import time
import datetime
import threading


class Timer:

    def __init__(self, duration):
        self.duration = int(duration.split()[0])
        self.unit = duration.split()[1]
        if any(word in self.unit for word in ['minute', 'minutes']):
            self.duration *= 60
        elif any(word in self.unit for word in ['hour', 'hours']):
            self.duration *= 3600
        self.t = threading.Timer(self.duration, self.ring)

    def ring(self):
        print('\nRing! Ring!' * 3)
        return self.t.cancel()

    def start_timer(self):
        self.settimer = int(time.time())
        print('Starting a count down at {} {}'.format(self.duration, self.unit))
        return self.t.start()

    def cancel_timer(self):
        self.hour_left, self.min_left, self.sec_left = '0'
        print('Cancelled your timer')
        return self.t.cancel()

    def check_timer(self):
        self.hour_left, self.min_left, self.sec_left = str(datetime.timedelta(
            seconds=self.duration-(int(time.time())-self.settimer))).split(':')

        if int(self.hour_left) == 1:
            self.hour_left = ' {} {}'.format(
                self.hour_left.lstrip('0'), 'hour')
        elif int(self.hour_left) > 1:
            self.hour_left = ' {} {}'.format(
                self.hour_left.lstrip('0'), 'hours')
        else:
            self.hour_left = ''

        if int(self.min_left) == 1:
            self.min_left = ' {} {}'.format(
                self.min_left.lstrip('0'), 'minute')
        elif int(self.min_left) > 1:
            self.min_left = ' {} {}'.format(
                self.min_left.lstrip('0'), 'minutes')
        else:
            self.min_left = ''

        if int(self.sec_left) == 1:
            self.sec_left = ' {} {}'.format(
                self.sec_left.lstrip('0'), 'second')
        elif int(self.sec_left) > 1:
            self.sec_left = ' {} {}'.format(
                self.sec_left.lstrip('0'), 'seconds')
        else:
            self.sec_left = ''

        return 'You\'ve got{}{}{} on your timer'.format(self.hour_left, self.min_left, self.sec_left)
