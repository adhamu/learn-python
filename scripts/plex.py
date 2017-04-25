#!/usr/bin/env python3

import urllib.request
import json
import subprocess

platform = "Linux"
architecture = "linux-ubuntu-x86_64"
distro = 'ubuntu'
plexDownloadApi = "https://plex.tv/api/downloads/1.json?channel=plexpass"

print("Looking up available downloads")
try:
    with urllib.request.urlopen(plexDownloadApi) as url:
        data = json.loads(url.read())
except:
    print('ERROR: There was an error looking up available downloads. Please try again later')

if data:
    item = data['computer'][platform]
    releaseData = item['release_date']
    version = item['version']

    for release in item['releases']:
        if release['build'] == architecture and release['distro'] == distro:
            downloadUrl = release['url']
            fileName = downloadUrl.rsplit('/', 1)[1]

    if downloadUrl:
        print('Downloading from ' + downloadUrl)

        if urllib.request.urlretrieve(downloadUrl, fileName):
            subprocess.run(['ls', fileName], stdout=subprocess.PIPE)

else:
    print('ERROR: Looks like there\'s a problem with the API response')