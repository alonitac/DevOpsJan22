#!/bin/sh

# general branches
git branch bugfix/fix_readme_typo
git branch feature/upgrade_angular_version
git branch feature/data_retention_policy
git branch feature/elasticsearch_helm_chart
git branch bugfix/open_kibana_port

# Changes in working tree and switch branches
git checkout -b dev
echo "a" >> take.txt
echo "b" >> take.txt
echo "c" >> take.txt
git add take.txt && git commit -m "add take.txt in dev"
git checkout main

# Reset
git checkout -b reset_question

for i in {1..10}
do
    echo "$i" > $i.txt
    git add $i.txt
    git commit -m "$i"
done
git checkout main


git branch feature/version1
git branch feature/version2


git checkout main



