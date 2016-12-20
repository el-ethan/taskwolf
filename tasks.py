from datetime import datetime


class GenericTask(object):

    _prefix_char = '?'
    date_format = None

    def __init__(self, title, duedate=None, tags=None, completed=False, nesting=1):
        self._title = title
        self._duedate = duedate
        self.tags = tags
        self.now = datetime.now()
        self.completed = completed
        self.nesting = nesting

    @property
    def duedate(self):
        if not self.date_format:
            return repr(self._duedate)
        return self._duedate.strftime(self.date_format)

    @property
    def is_due(self):
        return self._duedate <= datetime.now()

    @property
    def prefix(self):
        return self.nesting * self._prefix_char + ' '

    @property
    def title(self):
        return self.prefix + self._title

class WolfTask(GenericTask):
    pass


class OrgTask(GenericTask):

    _prefix_char = '*'

    date_format = 'DEADLINE: <%Y-%m-%d %a>'

    @property
    def prefix(self):
        return self._prefix_char * self.nesting + ' TODO '

    @property
    def title(self):
        return self.prefix + self._title

class TaskPaperTask(GenericTask):
    pass


class ToodledoTask(GenericTask):
    pass
