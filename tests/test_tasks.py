from datetime import datetime, timedelta
from ..tasks import GenericTask, OrgTask, TaskPaperTask


class TestGenericTask(object):

    def test_is_due(self):
        title = 'I am a generic task'
        duedate = datetime.now() - timedelta(weeks=1)
        task = GenericTask(title, duedate=duedate)
        assert task.is_due

    def test_is_not_due(self):
        title = 'I am a generic task'
        duedate = datetime.now() + timedelta(weeks=1)
        task = GenericTask(title, duedate=duedate)
        assert not task.is_due

    def test_now_is_due(self):
        title = 'I am a generic task'
        duedate = datetime.now()
        task = GenericTask(title, duedate=duedate)
        assert task.is_due

    def test_prefix(self):
        title = 'I am a generic task'
        task = GenericTask(title)
        assert task.prefix == '? '

    def test_nesting(self):
        title = 'I am a generic nested task'
        task = GenericTask(title, nesting=3)
        assert task.prefix == '??? '


class TestOrgTask(object):

    def test_title(self):
        title = 'I am an org task'
        task = OrgTask(title)
        assert task.title == '* TODO ' + title

    def test_nesting(self):
        title = 'I am a nested task'
        task = OrgTask(title, nesting=2)
        assert task.title == '** TODO ' + title

    def test_duedate_format(self):
        due = datetime(2013, 10, 6)
        task = OrgTask('Task with duedate', duedate=due)
        assert task.duedate == 'DEADLINE: <2013-10-06 Sun>'

    def test_tags(self):
        task = OrgTask('Task with tags', tags=['work', 'test'])
        assert task.tags == ':work:test:'


class TestTaskpaperTask(object):

    def test_title(self):
        title = 'I am an org task'
        task = TaskPaperTask(title)
        assert task.title == '- ' + title

    def test_nesting(self):
        title = 'I am a nested task'
        task = TaskPaperTask(title, nesting=2)
        assert task.title == '\t- ' + title

    def test_duedate_format(self):
        due = datetime(2013, 10, 6)
        task = TaskPaperTask('Task with duedate', duedate=due)
        assert task.duedate == '@due(2013-10-06)'

    def test_tags(self):
        task = TaskPaperTask('Task with tags', tags=['work', 'test'])
        assert task.tags == '@work @test'
