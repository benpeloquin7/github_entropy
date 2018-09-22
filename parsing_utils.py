"""Github event classes.

Note there are more:

https://developer.github.com/v3/activity/events/types/

But this is the complete list from a publicly available dataset that doesn't
require bigquery.

[X] CommitCommentEvent
[X] CreateEvent
[X] DeleteEvent  # No language data attached
[X] ForkEvent
[X] GollumEvent  # Not clear what these are, ignoring for now...
[] IssueCommentEvent
[X] IssuesEvent
[] MemberEvent
[] PublicEvent
[X] PullRequestEvent # Note that there are multiple language data
                     # possibe more in comments / commits? just pulling body now
[] PullRequestReviewCommentEvent
[X] PushEvent
[] ReleaseEvent
[] WatchEvent

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

    def get_type(self):
        return self.type


class CommitCommentEventParser(EventParser):
    """Commit comment event.

    https://developer.github.com/v3/activity/events/types/#commitcommentevent

    """

    def __init__(self, data, idx):
        super(CommitCommentEventParser, self).__init__(data, idx)
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


class CreateEventParser(EventParser):
    """Create event.

    https://developer.github.com/v3/activity/events/types/#createevent

    """

    def __init__(self, data, idx):
        super(CreateEventParser, self).__init__(data, idx)
        self.type = "CreateEvent"

    def parse(self):
        self.repo_id = self.data['repo']['id']
        self.repo_name = self.data['repo']['name']
        self.message = self.data['payload']['description']
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


class DeleteEventParser(EventParser):
    """Delete event.

    https://developer.github.com/v3/activity/events/types/#deleteevent

    """
    def __init__(self, data, idx):
        super(DeleteEventParser, self).__init__(data, idx)
        self.type = "DeleteEvent"

    def parse(self):
        self.repo_id = self.data['repo']['id']
        self.repo_name = self.data['repo']['name']
        self.created_at = self.data['created_at']

    def to_dict(self):
        data = []
        d_global = {
            "repo_id": self.repo_id,
            "repo_name": self.repo_name,
            "message": "",
            "created_at": self.created_at
        }
        data.append(d_global)
        return data


class ForkEventParser(EventParser):
    """Fork event.

    https://developer.github.com/v3/activity/events/types/#forkevent

    """
    def __init__(self, data, idx):
        super(ForkEventParser, self).__init__(data, idx)
        self.type = "ForkEvent"

    def parse(self):
        self.repo_id = self.data['repo']['id']
        self.repo_name = self.data['repo']['name']
        self.message = self.data['payload']['forkee']['description']
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


class GollumEventParser(EventParser):
    def __init__(self, data, idx):
        super(GollumEventParser, self).__init__(data, idx)
        self.type = "GollumEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class IssueCommentEventParser(EventParser):
    def __init__(self, data, idx):
        super(IssueCommentEventParser, self).__init__(data, idx)
        self.type = "IssueCommentEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class IssuesEventParser(EventParser):
    """Issue event.

    Note that this current eversion ignores the body text which has more
    text than title. Instead we use `title` for the message.

    """

    def __init__(self, data, idx):
        super(IssuesEventParser, self).__init__(data, idx)
        self.type = "IssuesEvent"

    def parse(self):
        self.repo_id = self.data['repo']['id']
        self.repo_name = self.data['repo']['name']
        self.message = self.data['payload']['issue']['title']
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


class MemberEventParser(EventParser):
    def __init__(self, data, idx):
        super(MemberEventParser, self).__init__(data, idx)
        self.type = "MemberEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class PublicEventParser(EventParser):
    def __init__(self, data, idx):
        super(PublicEventParser, self).__init__(data, idx)
        self.type = "PublicEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class PullRequestEventParser(EventParser):
    def __init__(self, data, idx):
        super(PullRequestEventParser, self).__init__(data, idx)
        self.type = "PullRequestEvent"

    def parse(self):
        self.repo_id = self.data['repo']['id']
        self.repo_name = self.data['repo']['name']
        self.message = self.data['payload']['pull_request']['body']
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


class PullRequestReviewCommentEventParser(EventParser):
    def __init__(self, data, idx):
        super(PullRequestReviewCommentEventParser, self).__init__(data, idx)
        self.type = "PullRequestReviewCommentEventParser"

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


class ReleaseEventParser(EventParser):
    def __init__(self, data, idx):
        super(ReleaseEventParser, self).__init__(data, idx)
        self.type = "ReleaseEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass


class WatchEventParser(EventParser):
    def __init__(self, data, idx):
        super(WatchEventParser, self).__init__(data, idx)
        self.type = "WatchEvent"

    def parse(self):
        pass

    def to_dict(self):
        pass
