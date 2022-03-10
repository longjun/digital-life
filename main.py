# -*- coding: utf-8 -*-
import argparse
import requests
from github import Github


def main(token, repo_name, issue_num, message):
    u = Github(token)
    repo = u.get_repo(repo_name)
    issue = repo.get_issue(number=int(issue_num))
    issue.create_comment(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    parser.add_argument("issue_num", help="issue_number")
    parser.add_argument("--message", help="comment_message", default=None, required=False)
    options = parser.parse_args()
    main(options.github_token, options.repo_name, options.issue_num, options.message)