#!/bin/bash

jq -r ' . | [.user.id, .id, .full_text] | @csv' tweetstest.jsonl > tweettest.csv