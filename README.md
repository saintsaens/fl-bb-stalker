# fl-bb-stalker
<b>v0.1:</b> Receive an email notification if there is a thread in Korean on the first page of the [WordPress.com help forum](https://en.forums.wordpress.com/forum/support/).

## Prerequisites
- Install BeautifulSoup (full doc [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup))
```
$ apt-get install python-bs4
```
## Setup
### Mails
Edit the file <b>conf_mail.py</b> and change the following values:
- SRC_EMAIL: full email address of the Gmail account used to send emails
- SRC_PW: password of the SRC_EMAIL (must be written in clear, with double-quotes)
- DST_EMAIL: full email address of the account receiving emails (not necessarily Gmail)

You will need to [allow access to less secure apps](https://myaccount.google.com/lesssecureapps) on the SRC_EMAIL account, and also [disable CAPTCHA](https://accounts.google.com/b/0/DisplayUnlockCaptcha) on that account. I recommend creating a new account just for this purpose.
### Tests
If you plan to run tests with `pytest` ([how to do that?](https://docs.pytest.org/en/latest/getting-started.html)), create the file <b>fake_html.html</b> with at least the following lines (which is the first sticky thread of the WordPress.com help forum):
```
<ul id="bbp-topic-3065850" class="odd super-sticky bbp-parent-forum-13 user-id-3167629 post-3065850 topic type-topic status-closed hentry">
	<li class="bbp-topic-title">
		<a class="bbp-topic-permalink" href="https://en.forums.wordpress.com/topic/best-practices-community-standards/">Best Practices &amp; Community&nbsp;Standards</a>
	</li>
	<li class="bbp-topic-reply-count">1</li>
	<li class="bbp-topic-last-poster">
			<a href="https://en.forums.wordpress.com/users/supernovia/" title="View supernovia&#039;s profile" class="bbp-author-name" rel="nofollow">supernovia</a>
	</li>
	<li class="bbp-topic-freshness">
		<a href="https://en.forums.wordpress.com/topic/best-practices-community-standards/" title="Best Practices &amp; Community&nbsp;Standards">10 months</a>
	</li>
</ul><!-- #bbp-topic-3065850 -->
```
## Usage
```
$ python fl-bb-stalker.py
```
will read the first page of the [WordPress.com help forum](https://en.forums.wordpress.com/forum/support/). If a thread title contains at least one Korean character, it will send an email to DST_EMAIL (view the Setup section about Mails).

Each Korean thread sends one email. The email has the following form:
- Subject
```
New Korean thread: <Title>
```
- Body
```
<link_to_the_Korean_thread>
```

A log is kept on all new Korean threads, so you will only receive one mail per thread (new threads with the same title as an existing thread still send an email, since the ID is checked).
