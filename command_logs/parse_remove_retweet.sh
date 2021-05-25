#!/bin/bash

jq -r ' . | select(.retweeted_status == null)' test.jsonl > noretweetstest.jsonl