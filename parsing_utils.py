"""Github event classes.

Note there are more:

https://developer.github.com/v3/activity/events/types/

But this is the complete list from a publicly available dataset that doesn't
require bigquery.

[X] 'CommitCommentEvent',
[] 'CreateEvent',
[] 'DeleteEvent',
[] 'ForkEvent',
[] 'GollumEvent',
[] 'IssueCommentEvent',
[] 'IssuesEvent',
[] 'MemberEvent',
[] 'PublicEvent',
[] 'PullRequestEvent',
[] 'PullRequestReviewCommentEvent',
[X] 'PushEvent',
[] 'ReleaseEvent',
[] 'WatchEvent'

"""

class EventParser:
    def __init__(self, data, idx):
        self.data = data
        self.idx = idx

    def parse(self):
        """Extract attributes from data."""
        NotImplementedError()

    def to_dict(self):
        """Attributes to dict."""
        NotImplementedError()


class CommitCommentEvent(EventParser):
    """Commit comment event.

    https://developer.github.com/v3/activity/events/types/#commitcommentevent

    """
    def __init__(self, data, idx):
        super(CommitCommentEvent, self).__init__(data, idx)
        self.type = "CommitCommentEvent"

    def parse(self):
        self.repo_id = self.data['repo']['id']
        self.repo_name = self.data['repo']['name']
        self.message = self.data['payload']['comment']['body']
        self.created_at = self.data['created_at']

    def to_dict(self):
        data = []
        d_global = {
            "repo_id": self.repo_id,
            "repo_name": self.repo_name,
            "message": self.message,
            "created_at": self.created_at
        }
        data.append(d_global)
        return data


class CreateEvent(EventParser):
    """Create event.

    https://developer.github.com/v3/activity/events/types/#createevent

    """
    def __init__(self, data, idx):
        super(CreateEvent, self).__init__(data, idx)
        self.type = "CreateEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class DeleteEvent(EventParser):
    """Delete event.

    https://developer.github.com/v3/activity/events/types/#deleteevent

    """
    def __init__(self, data, idx):
        super(DeleteEvent, self).__init__(data, idx)
        self.type = "DeleteEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class ForkEvent(EventParser):
    """Fork event.

    https://developer.github.com/v3/activity/events/types/#forkevent

    """
    def __init__(self, data, idx):
        super(ForkEvent, self).__init__(data, idx)
        self.type = "ForkEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class GollumEvent(EventParser):
    def __init__(self, data, idx):
        super(GollumEvent, self).__init__(data, idx)
        self.type = "GollumEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class IssueCommentEvent(EventParser):
    def __init__(self, data, idx):
        super(IssueCommentEvent, self).__init__(data, idx)
        self.type = "IssueCommentEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class IssuesEvent(EventParser):
    def __init__(self, data, idx):
        super(IssuesEvent, self).__init__(data, idx)
        self.type = "IssuesEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class MemberEvent(EventParser):
    def __init__(self, data, idx):
        super(MemberEvent, self).__init__(data, idx)
        self.type = "MemberEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class PublicEvent(EventParser):
    def __init__(self, data, idx):
        super(PublicEvent, self).__init__(data, idx)
        self.type = "PublicEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class PullRequestEvent(EventParser):
    def __init__(self, data, idx):
        super(PullRequestEvent, self).__init__(data, idx)
        self.type = "PullRequestEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass

        pass


class PullRequestReviewCommentEvent(EventParser):
    def __init__(self, data, idx):
        super(PullRequestReviewCommentEvent, self).__init__(data, idx)
        self.type = "PullRequestReviewCommentEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class PushEventParser(EventParser):
    def __init__(self, data, idx):
        super(PushEventParser, self).__init__(data, idx)
        self.type = "PushEvent"

    def parse(self):
        """Extract attributes from data."""
        self.repo_id = self.data['repo']['id']
        self.repo_name = self.data['repo']['name']
        self.before = self.data['payload']['before']
        self.commits = self.data['payload']['commits']
        self.processed_commits = self._extract_commits()
        self.distinct = self.data['payload'][
            'distinct_size']  # Number of commits in payload
        self.created_at = self.data['created_at']

    def to_dict(self):
        """Attributes to dict list of dicts.

        Note that we return list of dicts to handle payloads with lists.

        Expect to accumulate data in lists using .extend()

        """
        data = []
        d_global = {
            "repo_id": self.repo_id,
            "repo_name": self.repo_name,
            "distinct": self.distinct,
            "created_at": self.created_at
        }
        for commit in self.processed_commits:
            commit.update(d_global)
            data.append(commit)
        return data

    def _extract_commits(self):
        processed_commits = []
        for i, commit in enumerate(self.commits):
            curr_commmit = {
                'commit_idx': i,
                'commit_sha': commit['sha'],
                'is_unique': commit['distinct'],
                'message': commit['message']
            }
            processed_commits.append(curr_commmit)
        return processed_commits


class ReleaseEvent(EventParser):
    def __init__(self, data, idx):
        super(ReleaseEvent, self).__init__(data, idx)
        self.type = "ReleaseEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class WatchEvent(EventParser):
    def __init__(self, data, idx):
        super(WatchEvent, self).__init__(data, idx)
        self.type = "WatchEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass
