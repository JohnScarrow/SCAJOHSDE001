#!/usr/bin/python3

import os
import sys
import json
import requests
import facebook

fbResponse = requests.get("https://graph.facebook.com/oauth/access_token?client_id=339457266615866&client_secret=c789054f20158471cbd919d6b8e176f1&grant_type=client_credentials")
ACCESS_TOKEN = fbResponse.json()
post = requests.get("https://graph.facebook.com/v2.9/expedia/posts?access_token={ACCESS_TOKEN}")
post = json.dumps(post.json())
postFile = open("Expedia.txt", 'w')
postFile.write(post)
postFile.close()
