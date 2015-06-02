# Setup

Install a venv by doing `virtualenv -p /usr/bin/python3 venv`
Add the publish remote:
`git add remote publish ssh://leva.blue/srv/leva.blue/leva.blue.git`

# Publishing

Publish by doing `git push publish` on master.

To push an alternative branch:
    git push publish TestBranch:master

# Dependencies

You need [Pelican](blog.getpelican.com) to build the site.
You need python3 and `pip install pelican CommonMark`

## Git-related
Shared repositories should have `core.sharedRepository = group`
