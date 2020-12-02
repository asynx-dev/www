import re
from mkdocs import utils
import posixpath
import pathlib

class AxMkdocs:
    def __init__(self):
        self.isBlogPage_pattern = re.compile(r"blog/(\d{2})/(\d+)-(\S+)\.(\S+)")
        self.blogpages = {}
        self.key_allblogposts = r'{{{{ axmk_all_blog_posts }}}}'

    def sayhi(self):
        print("Hi!")

    def onprepage(self, page, config, files):
        return

    def onpagemarkdown(self, markdown, page, config, files):
        if self.key_allblogposts in markdown:
            print(page.file.src_path)
            allblogposts = ""
            for key in sorted(self.blogpages,reverse=True):
                print('ID: {}, file: {}'.format(key,self.blogpages[key].filename))
                allblogposts += '* [{}]({}) `{}`\n'.format(self.blogpages[key].title,utils.get_relative_url(pathlib.Path(self.blogpages[key].filename).as_posix(),pathlib.Path(page.file.src_path).as_posix()),self.blogpages[key].year + "/" + self.blogpages[key].seqnum)
            return markdown.replace(self.key_allblogposts,allblogposts)

    def onfiles(self, files, config):
        return

    def onnav(self, nav, config, files):
        for file in files.documentation_pages():
            page = file.page

            page.read_source(config)

            isBlogPage = self.isBlogPage(page.url)
            if isBlogPage:
                blogpage = BlogPage()
                blogpage.year = isBlogPage.groups()[0]
                blogpage.seqnum = isBlogPage.groups()[1]
                blogpage.id = blogpage.year + blogpage.seqnum
                blogpage.title = page.title
                blogpage.filename = page.file.src_path
                blogpage.url = page.url
                blogpage.fileobj = file

                if blogpage.id in self.blogpages:
                    raise Exception('Duplicate keys: {}:{} and {}:{}'.format(blogpage.id,self.blogpages[blogpage.id].filename,blogpage.id,blogpage.filename))

                self.blogpages[blogpage.id]=blogpage

    def isBlogPage(self, url):
        return self.isBlogPage_pattern.match(url)

class BlogPage:
    def __init__(self):
        self.id = ""
        self.year = ""
        self.seqnum = ""
        self.title = ""
        self.filename =""
        self.url = ""
        return

def onconfig(*args, **kwargs):
    global axmkdocs
    axmkdocs = AxMkdocs()

def onfiles(files, config, **kwargs):
    global axmkdocs
    axmkdocs.onfiles(files, config)

def onprepage(page, config, files, **kwargs):
    global axmkdocs
    axmkdocs.onprepage(page, config, files)
    return

def onnav(nav, config, files, **kwargs):
    global axmkdocs
    axmkdocs.onnav(nav, config, files)

def onpagemarkdown(markdown, page, config, files, **kwargs):
    global axmkdocs
    return axmkdocs.onpagemarkdown(markdown, page, config, files)

    #for key, value in kwargs.items() :
        #print (key)

    # if "axlang" in kwargs["page"].meta:
    #     #print(kwargs["page"].meta["axlang"])
    #     kwargs["page"].title += " [" + kwargs["page"].meta["axlang"].upper() + "]"
    #     return kwargs["page"].markdown.replace('# ','# ' + "[" + kwargs["page"].meta["axlang"].upper() + "] ", 1)
