---
title: "Claude Project: Thermal Printer Guestbook"
publishDate: 2026-03-19T00:00:00-07:00
---

## Overview

I've always admired folks who release web toys for the anonymous public to play with.
I'm also interested in bridging the gap between online spaces and real life.
In some ways, I wish we could make online spaces more like real life without having to completely lose digital privacy. 
I made [this guestbook](https://guestbook.emilabraham.com/) to explore that concept.
It was loosely inspired by the [guestbook at Good Enough](https://goodenough.us/guestbook).
All mentioned source code can be found on [my github](https://github.com/emilabraham/guestbook).

## The Process

### Setting up the Printer

I have a mini-PC I set up that's on 24/7. I've set up Claude on it and I can [SSH to it from my phone](https://emilabraham.com/thoughts/claude-car-replacement-tracker/).
I figured that would be a good candidate to set up [the thermal printer](https://www.amazon.com/dp/B08V4H7T47).
First things first, was to plug it in and see if I can get something to print.
Claude was great at helping me install the necessary driver, troubleshoot, and get me to a point where I could `echo` some text to a print script and it'd print.
Claude even suggested we set it up a [udev](https://www.man7.org/linux/man-pages/man7/udev.7.html) (a command I've never used) rule so that the printer auto-binds as soon as it's plugged in.

One thing I learned is that thermal printers are surprisingly simple mechanically.
It has a single button to open the paper refill tray.
They are easy to open and refill.
They are designed to be set up once and forgotten.
A far cry from the software update ridden, subscription only, user account required technologies of today.

### Setting up a printer server background service

The next step was to setup a small HTTP server that's run as a systemd service.
All it does is accept print jobs and send it to the thermal printer.

### Building the backend service

I gave Claude the requirements for the guestbook application:
- Store every message and when it was made.
- Have sensible rate limiting to prevent spam.
- Sanitize the input to prevent injection vulnerabilities.
- Allow me to review them before publishing to a gallery of my favorites.
- When reviewing, allow me to add commentary which will be displayed on the gallery.

Claude ended up setting up a SQLite database with an `approved` column to control what gets published.
It set up the appropriate API endpoints for the gallery and user submission.
It sanitizes for printer control characters.
It uses SQLite sanitzation to prevent SQL injection.
It created a script that will query the DB and let me approve any messages one by one and add commentary.
It suggested a per-IP rate limit as well as a global rate limit and a character limit per message.
Finally, it started the service as a systemd service so that it automatically recovers in case of reboot or crashes.

### Building the frontend

It created a simple HTML pages for the guestbook and gallery.
I wanted to be extremely barebones.
No need to setup a whole frontend framework if not necessary.
And finally, we setup a DNS record and pointed it to the server and secured it with Let's Encrypt SSL certificate.

## Final Thoughts

This was a really fun experience that I feel like I was only able to accomplish in a reasonable amount of time with AI assistance.
The idea of troubleshooting printer drivers on a Linux machine sounds arduous and boring with little payoff.
But Claude made it a relatively painless process.
Setting up a simple web server and basic frontend is realtively easy.
However, I'd spend most of my time spent analyzing tradeoffs with which stack to use or troubleshooting configs until it actually works.
Claude took the friction away and turned this from a multi-weekend project into a single evening project.
I feel like AI assistants are great at filling this niche.
