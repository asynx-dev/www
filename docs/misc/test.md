# Test Page

## Extensions

### admonition

!!! danger
    danger check

!!! note
    note check

!!! question
    question check

!!! todo
    todo check

!!! warning
    warning check

## footnotes

There should be two footnotes at end of the sentence. You should be get back
here clicking links at end of the footnotes. [^1f], [^iki]. If `mkdocs-bibtex`
is enabled, it is better to use identifiers different than `[^1]`, like `[^1f]`
or `[^iki]` to avoid confusion because this format is used by the plugin.

## Plugins

### mkdocs-asynx-plugin

!!! Warning
    Functions of this plugin is called by `mkdocs-simple-hooks` and it is under
    development.

#### List All Blog Posts

{{{{ axmk_all_blog_posts }}}}

### disqus

Check bottom of the page. Disqus form should appear.

### mkdocs-bibtex

Check `Extensions` → `footnotes`.

A citation to test entry in bibliography file: [@test]

## Built-in

### Code Highlight

#### Shell

```shell
$ sudo apt install firefox
# apt install firefox
```

#### Tcl

```tcl
% puts Hello World!
# This is a comment
```

#### Text

```text
This is a plain text.
```

[^1f]: This is the first footnote. Check the link →
[^iki]: This is the second footnote. Check the link →

\bibliography
