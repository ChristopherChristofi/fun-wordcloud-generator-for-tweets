#!/bin/bash

jq -r ' . | [.user.id, .id, .created_at, .full_text, .lang] | @csv' tweetstest.jsonl > tweettest.csv