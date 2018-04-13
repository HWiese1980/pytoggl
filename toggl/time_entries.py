from urllib.parse import urlencode
import dateutil.parser as parser
from datetime import datetime

from .base import ObjectList, Object, cached_property

__all__ = ['TimeEntryList', 'TimeEntry']


class TimeEntryList(ObjectList):
    """A collection of Time Entries."""

    def __init__(self, api, project_id = None):
        super(TimeEntryList, self).__init__(api)
        if project_id:
            self.filters = {
                "pid": project_id
            }

    get_instance_cls = lambda self: TimeEntry
    url = 'time_entries?%s' % urlencode({"start_date": "2017-01-01T00:00:00+02:00"})


class TimeEntry(Object):
    """TimeEntry object.

    API doc: https://github.com/toggl/toggl_api_docs/blob/master/chapters/time_entries.md

    """

    @cached_property
    def name(self):
        return self.description

    # @cached_property
    # def project_users(self):
    #     return ProjectUserList(self.api,
    #         url='projects/%d/project_users' % self.id)

    # @cached_property
    # def tasks(self):
    #     from .task import TaskList
    #     return TaskList(self.api, url='projects/%d/tasks' % self.id)
