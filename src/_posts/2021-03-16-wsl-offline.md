---
title: "Using WSL on an offline Windows machine"
excerpt: "How to install WSL on a Windows machine not connected to the Internet"
categories:
    - guide
tags:
    - en
    - offline
    - wsl
    - windows
    - ubuntu
author: ayazar
axseq: 1
---

In this post, we will install Ubuntu 20.04 WSL package on an offline Windows
machine. Although this post is prepared with Ubuntu 20.04, the steps should be
valid for other WSL packages too.

# Getting files

If your Windows machine is connected to the Internet and you can easily install
WSL packages via Microsoft Store like clicking *Download from the Microsoft Store*
[here](https://ubuntu.com/wsl). To install it on an offline machine, first we
get corresponding `.appx` package from Microsoft. Packages are listed
[here](https://docs.microsoft.com/en-us/windows/wsl/install-manual#downloading-distributions).
Transfer the downloaded package to the target offline machine. For example when
I am writing this post, to install Ubuntu 20.04 I get `Ubuntu_2004.2020.424.0_x64.appx`.

# Enabling WSL on Windows

Open a PowerShell terminal and type `wsl`. If you get an error about not recognized
command, first you should enable WSL. The official instructions are given
[here](https://docs.microsoft.com/en-us/windows/wsl/install-win10#set-your-distribution-version-to-wsl-1-or-wsl-2).
Alternatively you can do it with GUI. Find `Program and Feature` on `Control Plane`,
then click `Turn Windows feature on or off` as shown below.

![WSL enable](/assets/images/blog/21/1-wsl-enable.png)

After rebooting `wsl` command should work on PowerShell. Since we don't have
any installed WSL on the target PC, it will say *... no installed distributions.*

If your machine
[satisfies](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-2---check-requirements-for-running-wsl-2)
requirements for WSL 2 and you don't have any [specific
reason](https://docs.microsoft.com/en-us/windows/wsl/compare-versions) to stick
with WSL (1), I recommended to switch to WSL 2 now but you can stick with WSL
(1) either. I am not using WSL 2 but I think the following steps should be fine
for WSL 2 too.
{: .notice--info}

# Installing files

