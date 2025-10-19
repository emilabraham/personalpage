---
title: "Renewing SSL Certificate"
publishDate: 2017-04-29T18:59:30-07:00
---

The day has finally come. My SSL certificate with
[StartSSL](https://www.startcomca.com) has expired. I tried renewing it, but
their site was down. Also they had warnings saying that major browsers would
stop supporting certificates issued by them. So I guess that's means it is time
to jump ship to [Let's Encrypt](https://letsencrypt.org/).

Let's Encrypt made it easy to create an SSL certificate. And best of all, it's
free (they highly recommend [donating to
EFF](https://letsencrypt.org/donate/)). They have a [tool called
certbot](https://certbot.eff.org/) that is a brilliant swiss-army knife for SSL
certficates. It allows you to generate new certificates with one command or
even to renew and automatically renew them. The best part about it was that the
error messages are very clear. Obviously, I'm an idiot and can never get a
command to automatically work on the first try. So when I ran the command to
generate a new certificate for a specific domain, it said that it doesn't
support multiple virtualnamehosts in a single file. And that's exactly what the
issue was! I simply split up the virtualnamehosts by port 80 and port 443 into
separate files and it worked like a charm.

My previous experience with all-purpose tools like this is they usually
compromise with error messages. They often are not very descriptive.

After I generated the separate .conf files that I needed for all my subdomains
and domains, and generated all their certificates, I simply created a cronjob
that runs twice daily to renew the certificates. If the certificates are not up
for renewal, they simply won't renew. It's brilliant.
