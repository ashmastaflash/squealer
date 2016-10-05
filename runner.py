import squealer
import os
import sys

reporter = squealer.SecurityReporter()
agent_id = os.getenv("HALO_AGENT_ID")
gh_token = os.getenv("GITHUB_TOKEN")
project = os.getenv("GITHUB_PROJECT")
commit_id = os.getenv("COMMIT_ID")
squeal = os.getenv("SQUEAL", "NO")
subject = "CloudPassage Halo Detected Issues on Building %s" % str(commit_id)
github_issue_body = ""
critical_findings = False

raw_results = reporter.scan_all_modules(agent_id)
for result in raw_results:
    if result["scan"]["module"] == "sca":
        github_issue_body = github_issue_body + squealer.MarkDowner.translate_csm(result, commit_id)
        if result["scan"]["critical_findings_count"] != 0:
            critical_findings = True
        else:
            print "Critical findings are zero.  Go you."


if critical_findings is True:
    print "Submitting issue to Github:"
    print project
    print subject
    print github_issue_body
    github = squealer.Github(gh_token)
    github.create_issue(project, subject, github_issue_body)

if critical_findings is True:
    if squeal != "NO":
        print "Hard exit to break CI process!"
        sys.exit(2)
