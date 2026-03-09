# Static Site Generator

[< Back Home](/)

![Asteroids image](/images/Static-Site-Generator-cropped.png)

## Overview

The [Static Site Generator](https://en.wikipedia.org/wiki/Static_site_generator) is a command-line tool that converts markdown files into a complete static website. It was my fourth Boot.dev project and the one this site is built with, making it unique in the portfolio as a project you can see working in real time.

## How It Was Built

The generator is built in Python and works by reading markdown files from a content directory, parsing them into HTML, and applying a template to produce the final pages. It handles headings, links, images, and code blocks, and outputs a complete static site ready to be served or hosted.

### To Do:

- Add support for gifs and video to allow projects to be demonstrated more effectively
- Improve the templating system to support multiple layouts
- Add navigation generation so links between pages are handled automatically

**GitHub**: [https://github.com/nathansmith-hub/static-site-generator](https://github.com/nathansmith-hub/static-site-generator)