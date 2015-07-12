from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

class EventCalendar(HTMLCalendar):

    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.events = self.group_by_day(events)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                if day in self.events:
                    cssclass += ' today-filled'
                else:
                    cssclass += ' today'
            if day in self.events:
                body = ['<a class="" href="/events/dayevents/%s/%s/%s/">' % (self.year, self.month, day)]
                if not date.today() == date(self.year, self.month, day):
                    cssclass += ' filled'
                body.append(str(day))
                body.append('</a>')
                return self.day_cell(cssclass, '%s' % (''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)

    def group_by_day(self, events):
        field = lambda event: event.start_date.day
        return dict(
            [(day, list(items)) for day, items in groupby(events, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)