# setuptools pkg_resources pip wheel failed with error code 1
# OSError: Command /opt/ansible-runtime/bin/python2 - setuptools pkg_resources pip wheel failed with error code 1

# https://github.com/certbot/certbot/issues/2883




# issue on ubuntu 16.04 with the client from git

# I resolved the issue by setting the locale variables. Without these, the script seems to break.
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"


pip install setuptools
pip install --upgrade setuptools






