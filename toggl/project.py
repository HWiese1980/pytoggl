from .base import ObjectList, Object, cached_property

__all__ = ['ProjectList', 'Project', 'ProjectUserList', 'ProjectUser']


class ProjectList(ObjectList):
    """A collection of Projects."""

    get_instance_cls = lambda self: Project
    url = 'projects'


class Project(Object):
    """Project object.

    API doc: https://github.com/toggl/toggl_api_docs/blob/master/chapters/projects.md

    """
    @cached_property
    def project_users(self):
        return ProjectUserList(self.api,
            url='projects/%d/project_users' % self.id)

    @cached_property
    def tasks(self):
        from .task import TaskList
        return TaskList(self.api, url='projects/%d/tasks' % self.id)

    @cached_property
    def time_entries(self):
        from .time_entries import TimeEntryList
        l = TimeEntryList(self.api, self.id)
        return l


class ProjectUserList(ObjectList):
    """A collection of Project-User mappings."""

    get_instance_cls = lambda self: ProjectUser


class ProjectUser(Object):
    """Project-User mapping.

    API doc: https://github.com/toggl/toggl_api_docs/blob/master/chapters/project_users.md

    """
    @cached_property
    def user(self):
        return self.api.workspaces[self.wid].users[self.uid]
