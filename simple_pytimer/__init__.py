import time


def human_friendly_duration(seconds):
    if seconds > 60:
        minutes = seconds / 60.0
        if minutes > 60:
            hours = minutes / 60.0
            if hours > 24:
                days = hours / 24.0
                return '{:0.1f} days'.format(days)
            else:
                return '{:0.1f} hours'.format(hours)
        else:
            return '{:0.1f} min'.format(minutes)
    else:
        return '{:0.1f} s'.format(seconds)


class Timer(object):
    def __init__(self, name):
        self.name = name
        self.clear()

    def __enter__(self, *args, **kwargs):
        self.restart()

    def __exit__(self, *args, **kwargs):
        self.mark()

    def clear(self):
        return self.restart()

    def restart(self):
        self.start_time = time.perf_counter()
        self.end_time = self.start_time
        return self

    def mark(self):
        self.end_time = time.perf_counter()
        return self

    def seconds(self):
        return self.end_time - self.start_time

    def __str__(self):
        '"{}" block took {}'.format(self.name, self.human_friendly_duration())

    def human_friendly_duration(self):
        return human_friendly_duration(self.seconds())


class AccumulatingTimer(Timer):
    def __enter__(self, *args, **kwargs):
        self.restart()

    def __exit__(self, *args, **kwargs):
        self.mark()

    def clear(self):
        self.s = 0
        return self.restart()

    def restart(self):
        self.start_time = time.perf_counter()
        return self

    def mark(self):
        self.s += time.perf_counter() - self.start_time
        return self

    def duration_s(self):
        return self.s