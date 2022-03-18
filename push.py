#!/usr/bin/env python

import requests
import argparse
import os

def push(title, content, token):
    requests.post(
        url="http://www.pushplus.plus/send",
        data={
            "token": token,
            "title": title,
            "content": content
        }
    )

if __name__ == '__main__':
    token = os.getenv("PUSH_TOKEN")
    
    parser = argparse.ArgumentParser('pushplus tool')
    parser.add_argument('-t', '--title', required=True, help="title")
    parser.add_argument('-c', '--content', required=True, help="content")
    args = parser.parse_args()
    
    if token:
        push(args.title, args.content, token)
    else: 
        print("export PUSH_TOKEN='your_token'")