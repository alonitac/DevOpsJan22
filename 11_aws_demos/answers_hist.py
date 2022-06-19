import re
from collections import defaultdict
import boto3
import json
import matplotlib.pyplot as plt
import os
from loguru import logger

branch_name = os.environ.get('CODEBUILD_WEBHOOK_HEAD_REF', 'alonit/ans')
bucket_name = 'devops-jan22'


with open('README.md') as f:
    data = f.read()


answers = defaultdict(lambda: defaultdict(list))
sections = ['compute']

# iterate sections
for i, sec in enumerate(re.split(f'\[\/\/\]: # "Automatic generated line. Don\'t edit"', data)[1:]):
    # iterate question in each section
    for q in re.split(f'<details>\s+<summary>Votes</summary>\s+.*\s+</details>', sec):
        f = re.findall(r'^\s+\d+', q)
        if f:
            q_num = int(f[0])
            answers[sections[i]][q_num] = []

            logger.info(f'search answers for {sections[i]} question {q_num}')
            for ans in re.findall(f'.*\*\*.*\*\*.*', q):
                f2 = re.findall(r'\d+', ans)
                if f2:
                    answers[sections[i]][q_num].append(int(f2[0]))

    answers[sections[i]] = sorted(answers[sections[i]].items(), key=lambda item: item[0])



s3_client = boto3.client('s3')
s3_client.download_file(bucket_name, 'answers.json', 'answers.json')

with open('answers.json') as f:
    x = json.load(f)

x[branch_name] = answers

with open('answers.json', 'w') as f:
    json.dump(x, f)

s3_client.upload_file('answers.json', bucket_name, 'answers.json')


def draw_votes_hist(name, lst):
    plt.figure(figsize=(3.2, 2.4))
    plt.bar([f'A{l[0]}' for l in lst], [l[1] for l in lst], color='maroon', width=0.4)

    # plt.xlabel("Courses offered")
    # plt.ylabel("No. of students enrolled")
    # plt.title("Students enrolled in different courses")
    # plt.show()
    plt.savefig(f'compute.png')
    s3_client.upload_file('compute.png', bucket_name, f'compute{name}.png',
                          ExtraArgs={'ACL': 'public-read', 'ContentType': 'image/png'})


hists = {}
for branch, sections in x.items():
    for sec_name, section in sections.items():
        if sec_name not in hists:
            hists[sec_name] =
for vote in x.items():
    answer = vote['compute'][i - 1]
    if answer is None:
        continue
    if answer not in votes:
        votes[answer] = 0
    votes[answer] += 1

draw_votes_hist(i, sorted(votes.items(), key=lambda x: x[0]))

