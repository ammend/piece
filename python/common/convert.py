# -*- coding: utf-8 -*-
import argparse
import csv
import json

def convert(csv_path, repo_owner):
    data = {}
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or len(row) < 3:
                continue
            repo = row[0].strip()
            scm = row[1].strip()
            reviewer = row[2].strip()
            if not scm:
                continue
            reviewers = data.get(repo)
            if reviewers is None:
                reviewers = set()
                data[repo] = reviewers
            if reviewer:
                reviewers.add(reviewer)
    result = []
    for repo, reviewers in sorted(data.items()):
        reviewers_list = sorted(reviewers)
        result.append({
            "repo_name": repo,
            "repo_owner": repo_owner,
            "config": {
                "reviewers": json.dumps(reviewers_list[:3], ensure_ascii=False)
            }
        })
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    parser.add_argument("repo_owner")
    parser.add_argument("--output", "-o", default="output.json")
    args = parser.parse_args()
    result = convert(args.csv_file, args.repo_owner)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()