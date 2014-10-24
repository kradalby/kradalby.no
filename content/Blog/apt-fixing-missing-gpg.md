Title: Fixing missing gpg key for apt-get
Tags: apt-get, debian, ubuntu, linux, gpg
Summary: Fixing missing gpg key for apt-get


Some days ago i ran into a problem where the debian repos could not find a gpg key so it could be verified. After some googling i found this handy command which fixes the problem:

    :::bash
    apt-get update 2> /tmp/keymissing; for key in $(grep "NO_PUBKEY" /tmp/keymissing |sed "s/.*NO_PUBKEY //"); do echo -e "\nProcessing key: $key"; gpg --keyserver pgpkeys.mit.edu --recv $key && gpg --export --armor $key | apt-key add -; done

The command basicly saves the error message and the id of the missing key, then fetches it from the MIT gpg server and installs it.

Notes:
If you use debian, keep using the MIT keyserver, if you use ubuntu, replace it with subkeys.pgp.net.
