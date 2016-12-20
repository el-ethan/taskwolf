from datetime import datetime


class GenericTask(object):

    _prefix_char = '?'
    date_format = None

    def __init__(self, title, duedate=None, tags=None, nesting=1):
        self._title = title
        self._duedate = duedate
        self._tags = tags
        self.now = datetime.now()
        self.nesting = nesting

    @property
    def duedate(self):
        if not self.date_format:
            return repr(self._duedate)
        return self._duedate.strftime(self.date_format)

    @property
    def is_due(self):
        return self._duedate <= self.now

    @property
    def prefix(self):
        return self.nesting * self._prefix_char + ' '

    @property
    def title(self):
        return self.prefix + self._title

    @property
    def tags(self):
        raise NotImplementedError


class OrgTask(GenericTask):

    _prefix_char = '*'

    date_format = 'DEADLINE: <%Y-%m-%d %a>'

    @property
    def prefix(self):
        return self._prefix_char * self.nesting + ' TODO '

    @property
    def title(self):
        return self.prefix + self._title

    @property
    def tags(self):
        return ':{}:'.format(':'.join(self._tags))


class TaskPaperTask(GenericTask):

    date_format = '@due(%Y-%m-%d)'

    _prefix_char = '- '

    @property
    def prefix(self):
        return '\t' * (self.nesting - 1) + self._prefix_char

    @property
    def tags(self):
        return ' '.join('@'+ tag for tag in self._tags)

class ToodledoTask(GenericTask):
    pass
