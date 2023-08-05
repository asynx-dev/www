---
# License: CC-BY-SA-4.0.
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
ax_video_id: "" # Fill if post has YouTube video. Example: -GNsF_dTmjU for https://www.youtube.com/watch?v=-GNsF_dTmjU
ax_podcast_id: "" # Fill if post has Podcast audio. Example Sumatra-PDF-TR-e1i0k3e for https://anchor.fm/asynxdev/episodes/Sumatra-PDF-TR-e1i0k3e
author: # User name of author. Example: ayazar. Must be in src/_data/authors.yml
toc: true # Change to false to hide TOC for small posts. Default true.
axseq: <SEQ> # Sequence number. Example: 5
published: true # Change to false to hide the post, only for debugging. Default true.
---

# Titles should be at highest level, single hash sign

First paragraph
