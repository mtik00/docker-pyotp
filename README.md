# docker-pyotp
Use a docker image and pyotp to generate TOTP codes from a secret.

You can just run the script like this:

    python3 main.py AAAAAAAAAAAAAAAA

However, it's really meant for Docker.

    docker run mtik00/pyotp AAAAAAAAAAAAAAAA

or better yet:

    echo ${TOKEN} | xargs docker run mtik00/pyotp '{}'