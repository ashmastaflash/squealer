import github3


class Github(object):
    def __init__(self, gh_token):
        self.session = github3.login(token=gh_token)

    def create_issue(self, project, subject, github_issue_body):
        gh_user, gh_project = project.split('/')
        repo = self.session.repository(gh_user, gh_project)
        repo.create_issue(subject, github_issue_body)
