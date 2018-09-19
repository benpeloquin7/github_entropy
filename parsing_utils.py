class EventParser:
    def __init__(self, data, idx):
        self.raw_data = data
        self.idx = idx

    def parse(self, data):
        """Extract attributes from data."""
        NotImplementedError()

    def to_dict(self):
        """Attributes to dict."""
        NotImplementedError()


class PushEventParser(EventParser):
    def __init__(self, data, idx):
        super(PushEventParser, self).__init__(data, idx)
        self.type = "PushEvent"

    def parse(self):
        """Extract attributes from data."""
        self.repo_id = data['repo']['id']
        self.repo_name = data['repo']['name']
        self.before = data['payload']['before']
        self.commits = data['payload']['commits']
        self.processed_commits = self._extract_commits()
        self.distinct = data['payload'][
            'distinct_size']  # Number of commits in payload
        self.created_at = data['created_at']

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
