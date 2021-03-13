# asynx.dev www Source

[https://asynx.dev](https://asynx.dev)

![full-check](https://github.com/asynx-dev/www/workflows/full-check/badge.svg)
![GitHub last commit (master)](https://img.shields.io/github/last-commit/asynx-dev/www/master?label=last%20main%20repo%20update)
![GitHub last commit (gh-pages)](https://img.shields.io/github/last-commit/asynx-dev/www/gh-pages?label=last%20depoloyment)
![GitHub repo size](https://img.shields.io/github/repo-size/asynx-dev/www)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/asynx-dev/www)
![GitHub license](https://img.shields.io/github/license/asynx-dev/www)

## ✨ Contributing ✨

👉 **If you are planning to contribute (which is great!) check
[CONTRIBUTING](CONTRIBUTING.md) page.**👈

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://www.alperyazar.com"><img src="https://avatars.githubusercontent.com/u/1757430?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alper Yazar</b></sub></a><br /><a href="https://github.com/asynx-dev/www/commits?author=alperyazar" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/aniltirli"><img src="https://avatars.githubusercontent.com/u/35190700?v=4?s=100" width="100px;" alt=""/><br /><sub><b>aniltirli</b></sub></a><br /><a href="#blog-aniltirli" title="Blogposts">📝</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the
[all-contributors](https://github.com/all-contributors/all-contributors)
specification. [Contributions](CONTRIBUTING.md) of any kind welcome!

## Building Locally

Site is built with `Jekyll`. Jekyll is a Ruby program and we use Bundler as
dependency and package manager. The following steps should work on both Linux
and Windows. We haven't tried it on MacOS yet.

After installing Ruby which should also have `gem`. Then, install `bundler`.
Check out `gem` documentation for further options such as user vs system-wide
installation. **If you have already `bundler` installed you can skip this
command.**

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

The site is published with Github Pages.

## CI/CD

We use Github Actions to implement CI/CD pipeline. We run some tests like
linting on both source code and output files. Please check files under
`.github/workflows` to see exact flow and commands that are used.

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
