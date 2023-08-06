---
title: "Creating a Mail Server and Enabling SSL"
date: 2016-05-09T18:17:46-07:00
---

This weekend, I finally finished creating my mail server. I have always been interested in creating my own for a few reasons:

1. Curiosity on how they work and what kind of effort it would take to build one from the ground up
2. A fancy custom domain as an email address. I was always jealous of those who had one
3. To see what kind of control I could have over my email

I first started by reading about how mail servers worked. Linode has a great guide on running a mail server. 
It talks about the pros and cons of running your own mail server. It also gives a quick overview on how a mail server works.

Basically, a mail server can be divided into 3 components: 

1. The Mail Transfer Agent (MTA)
2. The Mail Delivery Agent (MDA)
3. And the IMAP/POP3 server

This structure is remarkably similar to its real world counterpart: the post office (only without the long lines)!
The MTA acts as the post office itself. This is where mail goes after traveling through the internet.
Whether it be receiving it, or sending it, the MTA handles it by sending mail to the proper address.
After the mail is queued up by the MTA, the MDA takes the mail and delivers it to the proper mailbox on the server.
The MDA Is analogous to the postman. Finally, the server deals with users and their mailboxes as they check their mail.

For my setup, I used [postfix](https://www.postfix.org) as my MTA and [dovecot](https://www.dovecot.org/)
as my MDA and IMAP/POP3 server combined solution.
Mainly because Linode has a great [tutorial](https://www.linode.com/docs/guides/email-with-postfix-dovecot-and-mysql/)
that I followed to set everything up using postfix, dovecot, and mysql.
As I started following the guide, I realized that I would need an SSL certificate in order to use my mail server with Gmail.
So, why not go all the way and just make my entire site work over a secure, encrypted connection?

I obtained my certificate for free from [startssl](https://www.startssl.com).
Thank god, because some of these certificates from trusted Certificate Authorities(CA) cost a fucking arm and a leg.
I am already paying for hosting and keeping a domain name. Why should I also have to pay to keep my site secure?
Nuh uh. Count me out.
It was a bit painful to set up, mainly because their Certificate Wizard was a bit unclear and not well documented.
I had to use an Subject Alternative Name in order to get all of my subdomains registered under the same certificate.
I also had to append the intermediate/root certificate to my personal one.
Having my personal one alone would be the same as having a self-signed certificate, which is not good enough security overall.
Google demands a certificate signed by a trusted CA.
After all this setup and struggle with poorly documented procedures, I found out about [Let's Encrypt](https://letsencrypt.org/).
It seems to be a relatively new and modern looking CA.
It seems to have some good documentation for things like renewing the certificate automatically.
As usual, I only discovered this alternative after tunneling myself very deep into the rabbit hole.
It wasn't worth digging myself out, so I stuck with the startssl certificate. Just my luck, right?

And now, finally, my site is embellished with the shiny green lock in the address bar, signifying that I care a little bit about privacy and encryption.
