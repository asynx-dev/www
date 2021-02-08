---
title: "Use pip and pipenv with self signed SSL certificates"
excerpt: "Use pip and pipenv with self signed SSL certificates"
author: ayazar
axseq: 1
categories:
    - guide
tags:
    - en
    - pip
    - pipenv
    - proxy
    - ssl
---

If you work in a cooperate environment, you may be working behind proxies and
SSL traffic may be signed by self-signed certificates. This may cause problems
while working with `pip` and especially with `pipenv`. With current versions
of `pip`, it is possible to ignore SSL errors using the following
example command [^1f].

```bash
$ pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>
```

This approach is suitable if you **know** that you are behind a proxy or
a similar equipment that signs the traffic with self-signed certificates.
Since `--trusted-host` flag disables SSL checking, this will cause a
potential security risk if you are not in such network, like working at
home.
{: .notice--warning}

I found that `--trusted-host` flag doesn't work as expected while working with
`pipenv`. There are some records about this issue [^2f], [^3f]. Even with the
flag, `pip` throws errors when invoked by `pipenv` in my setup.

# Solution

For me, setting `REQUESTS_CA_BUNDLE` environment variable prior to calling
`pipenv` solves the problem. (I found the solution on the Stack Overflow but I
can't remember the link). Of course, the certificate file pointed by the
varible should include the self signed certificate.

## Ubuntu

I tested on Ubuntu 16.04 but this may work on all Debian and Ubuntu derived
distros.

```bash
$ export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

## CentOS

I tested on CentOS 7.8 but this may work on all RedHat derived distros.

```bash
$ export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/extracted/openssl/ca-bundle.trust.crt
```

[^1f]: [https://stackoverflow.com/a/29751768](https://stackoverflow.com/a/29751768)
[^2f]: [https://github.com/pypa/pipenv/issues/3841](https://github.com/pypa/pipenv/issues/3841)
[^3f]: [https://github.com/pypa/pipenv/issues/2979](https://github.com/pypa/pipenv/issues/2979)
