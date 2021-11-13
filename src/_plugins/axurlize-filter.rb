module Jekyll
    module UrlizeFilter
      def axurlize(input)
        "<a rel=\"external\" href=\"#{input}\">#{input}</a>"
      end
    end
  end

  Liquid::Template.register_filter(Jekyll::UrlizeFilter)

# REF: https://ahermosilla.com/tools/2016/11/02/starting-jekyll.html#no-auto-urlize

# Initially added for podcast.xml but this urlize whole think, not auto URLize
# Kept for further reference to add a plugin
