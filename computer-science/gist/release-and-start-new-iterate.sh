#!/usr/bin/env bash

# fast fail
set -e

RESET_COLOR="$(tput sgr0)"

function echo_error() {
    echo "$(tput setaf 1)$1$RESET_COLOR"
}

function echo_error_and_exit() {
    echo_error $1
    exit
}

function show_usage() {
    echo "Usage $0 <new-iterate-version>"
    echo "    new-iterate-version should in X.X.X-SNAPSHOT format"
}

if [ $# -lt 1 ]; then
    show_usage
    exit
fi

new_iterate_ver=$1
if [ "$new_iterate_ver" != "$(echo $new_iterate_ver | sed -nE '/[0-9]+\.[0-9]+\.[0-9]+-SNAPSHOT/p')" ]; then
    show_usage
    exit
fi

echo "New iterate version: $(tput setaf 6)$new_iterate_ver$RESET_COLOR"

if [ "$(git status --porcelain)" != "" ]; then
    echo_error_and_exit "There are Changes or Untracked files in this repository. Commit or stash first."
fi

curr_ver=$(head -10 pom.xml | sed -nE '/^.*>([0-9]+\.[0-9]+\.[0-9]+-SNAPSHOT)<.*$/s//\1/p')
if [ "$curr_ver" = "" ]; then
    echo_error_and_exit "Failed to get current version"
fi

echo "Current version: $(tput setaf 2)$curr_ver$RESET_COLOR"

if [ "$new_iterate_ver" = "$curr_ver" ]; then
    echo_error_and_exit "New iterate version should be different from current version"
fi

if [ "$(git branch | sed -n '/\* /s///p')" != "master" ]; then
    echo_error_and_exit "Can only release on master branch."
fi

git tag -a $curr_ver -m "$curr_ver" &> /dev/null || echo_error_and_exit "Failed to tag"
git push --tag &> /dev/null || echo_error_and_exit "Failed to push tag"
mvn -Dmaven.test.skip=true clean deploy &> /dev/null || echo_error_and_exit "Failed to do 'mvn deploy'"
mvn versions:set -DnewVersion=$new_iterate_ver -DgenerateBackupPoms=false &> /dev/null || echo_error_and_exit "Failed to set new version"
git add . && git commit -m "start new iterate $new_iterate_ver" && git push &>/dev/null || echo_error_and_exit "Failed to commit new version"

