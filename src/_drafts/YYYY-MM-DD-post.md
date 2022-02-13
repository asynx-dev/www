---
title: "Title of the post" # This is the main title
excerpt: "Single sentence summary" # Keep it as short as possible, like a tweet <140 chars. This appears on blog listing and below title
categories:
    - guide
    - podcast # Keep it if sound file is attached, delete otherwise
    - youtube # Keep it if post is indeed in video format and contains video (not embedded, the content is video), delete otherwise
tags:
    - tr # Keep it if post contains is in Turkish, delete otherwise. Even if we don't prefer, a post may have both tr and en tag.
    - en # Keep it if post contains is in English, delete otherwise. Even if we don't prefer, a post may have both tr and en tag.
    - tag1 # Other tags related to post. Try to keep number of tags below 5 and try to use previously used tags as possible.
    - tag2
    - tagN
header:
    teaser: /assets/images/blog/<YY>/<SEQ>_teaser.png #Min: 720px. Ratio: 16x9. Prefer png. Example: /assets/images/blog/21/5_teaser.png
    overlay_image: /assets/images/blog/<YY>/<SEQ>_image.png #Min width: 1920px. Ratio: 16x9. Prefer png but jpeg is mostly OK. On widescreens, only horizontal center will be shown thus try to keep content on center horizontal bar. Example: /assets/images/blog/21/5_image.png
    overlay_filter: 0.5 # Value between 0-1. Default 0.5. Depending on color spectrum of overlay_image, adjust by trying. Higher value if image is bright.
podcast_link: "" # Link to podcast file. Remove if no podcast episode exists. Example: https://www.alperyazar.com/downloads/asynxdev/podcast/21/ax-21-5.m4a
podcast_art: /assets/images/blog/<YY>/<SEQ>_teaser.png # Remove if no podcast episode exists.
podcast_duration: # Podcast duration in secs. Remove if no podcast episode exists. Example: 126
podcast_length: # Podcast file length in bytes. Remove if no podcast episode exists. Example: 2042945
podcast_guid: ax-<YY>-<SEQ> # Podcast GUIO. Remove if no podcast episode exists. Example: ax-21-5
# Remove podcast_content if no podcast episode exists. THIS IS AN MULTI LINE EXAMPLE. Supports simple markdown. Typically this is description text of YouTube video if the post also has a video.
podcast_content: |
    SumatraPDF,  Windows için tasarlanmış, hafif, hızlı bir PDF okuyucusu.

    <https://www.sumatrapdfreader.org>

    LaTeX kullananlar için SyncTeX desteklemesi, dosya açık iken değiştirilmesine izin vermesi gibi bir çok güzel özelliği bulunuyor. Bu videoda kısaca özelliklerini tanıtıyoruz.

    axid: ax-21-5

    Hazırlayan: Alper Yazar

    0:00 Giriş

    0:11 Fare desteği

    0:34 LaTeX ve SyncTeX kolaylığı

    1:00 İndirme ve kurma

    1:17 Sekmeli ve sekmesiz kullanım

    1:30 Advanced options

    1:34 Karşılaştırma

    1:53 Linux desteği

    SumatraPDF ile TeXstudio arasında SyncTeX ile arama bağlantısı kurulumunu anlattığımız ax-21-6 nolu yazımız (İngilice): <https://asynx.dev/blog/2021/10/sumatrapdf-texstudio-synctex-search-link.html>

ax_video_id: "" # Fill if post has YouTube video. Example: -GNsF_dTmjU for https://www.youtube.com/watch?v=-GNsF_dTmjU
author: # User name of author. Example: ayazar. Must be in src/_data/authors.yml
toc: true # Change to false to hide TOC for small posts. Default true.
axseq: <SEQ> # Sequence number. Example: 5
published: true # Change to false to hide the post, only for debugging. Default true.
---

# Titles should be at highest level, single hash sign

First paragraph
