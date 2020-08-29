# docker-pyotp
Use a docker image and pyotp to generate TOTP codes from a secret.

You can just run the script like this:

    python3 src/app.py AAAAAAAAAAAAAAAA

However, it's really meant for Docker.

    docker run mtik00/pyotp AAAAAAAAAAAAAAAA

or better yet:

    echo ${TOKEN} | xargs docker run mtik00/pyotp '{}'

# Arguments

The script takes a couple of optional arguments.

* `-c`/`--continuous`: Continuously output the current code.  Updates about once per second.
* `-i`/`--interval`: The interval of the secret.  This is _probably_ 30, the default.
