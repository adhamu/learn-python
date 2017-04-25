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
    # Should probably exit at this point - either by
    # 1) not catching
    # 2) putting 'trow' to re-throw the exception (which might have useful info about the failure after all)
    # 3) calling sys.exit
    # That way you don't need the if block below
if data:
    item = data['computer'][platform]
    releaseData = item['release_date']
    version = item['version']
    for release in item['releases']:
        if release['build'] == architecture and release['distro'] == distro:
            label = release['label']
            downloadUrl = release['url']
            # its more 'pythonic' to use snake_case - (eventually you might want to take a look at pep8)
            fileName = downloadUrl.rsplit('/', 1)[1]
            # this file name might still have special characters or '..' or something nasty (more on this below)
    if downloadUrl: # if downloadUrl never gets set then this will result in a NameError
        print('Downloading ' + label + '\n' + fileName)
        if urllib.request.urlretrieve(downloadUrl, fileName):
            # I think if you omit the second arg it will securely create a named file for you in tmp (and return the name in a tuple with some other data)
            subprocess.run(['dpkg', '-i', fileName])
            subprocess.run(['rm', fileName])
            # use shutil.unlink instead!
            # Also this deletion should happen in a 'finally' block so it always gets deleted
else:
    print('ERROR: Looks like there\'s a problem with the API response')
    # Is this indented properly? looks liek it should be the else for 'if downloadUrl'