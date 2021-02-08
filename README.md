# asynx.dev www Source

[https://asynx.dev](https://asynx.dev)

![full-check](https://github.com/asynx-dev/www/workflows/full-check/badge.svg)

## Building

Site is built with `Jekyll`. Follow the official [installation page](https://jekyllrb.com/docs/installation/)
for detailed instructions. We recommend to work with latest Ubuntu WSL if you
are working on Windows 10. Quick summary:

* Follow Ubuntu installation **until** `bundler` and `jekyll` installation.
  **Don't install Jekyll now.**

Install only `bundler`

```text
gem install bundler
```

then run

```text
bundle
```

That's all. Run `bundle update` if you want to update and use the latest gems.
(This is the case when site is build by Github Actions before deployment)

## License

[![GitHub License](https://img.shields.io/github/license/asynx-dev/www.svg?style=flat)](https://creativecommons.org/licenses/by/4.0/)

SPDX-License-Identifier: CC-BY-4.0

This project is licensed under CC BY 4.0 if otherwise stated.
Check [LICENSE](LICENSE) for further information.
