# asynx.dev www Source

[https://asynx.dev](https://asynx.dev)

![full-check](https://github.com/asynx-dev/www/workflows/full-check/badge.svg)

## Building

Site is built with `Jekyll`. Jekyll is a Ruby program and we use Bundler as
dependency and package manager. The following steps should work on both Linux
and Windows. We haven't tried it on MacOS yet.

After installing Ruby which should also have `gem`. Then, install `bundler`. Check out
`gem` documentation for further options such as user vs system-wide installation.
**If you have already `bundler` installed you can skip this command.**

```text
gem install bundler
```

then run

```text
bundle update
```

This will install all necessary components to build the site. You can run
`bundle update` whenever you want to update and use the latest gems.

You can serve locally the site while working on a new content or editing files.
To view locally modified the site run:

```text
bundle exec jekyll serve --livereload
```

By default, the server listens [http://localhost:4000](http://localhost:4000)
If you encounter any problem when building the site, retry by omitting
`--livereload` flag.

## Publishing

The site is published with Github Pages. If you are planning to contribute
(which is great!) check [CONTRIBUTING](CONTRIBUTING.md) page.

## CI/CD

We use Github Actions to implement
CI/CD pipeline. We run some tests like linting on both source code and output
files. Please check files under `.github/workflows` to see exact flow and commands
that are used.

* `quick.yml` Runs for each push on all branches except `master`. This quick
  check is for developers who plan to modify the site and gives quick check
  results *before* creating PR. If this fails, PR also fails so this test
  should be passing before PR.
* `merge.yml` Runs when a PR is created. If fails, the PR can't be merged. This
  test checks for errors on build process, runs linter on source files and test
  output files.
* `deploy.yml` Runs when a PR is merged. This publishes the latest commit on
  `master`.
* `full-check.yml` Runs periodically independent from pushes and merges. This
  runs additional tests on published content like broken link check test.

## License

[![GitHub License](https://img.shields.io/github/license/asynx-dev/www.svg?style=flat)](https://creativecommons.org/licenses/by/4.0/)

SPDX-License-Identifier: CC-BY-4.0

This project is licensed under CC BY 4.0 if otherwise stated.
Check [LICENSE](LICENSE) for further information.
