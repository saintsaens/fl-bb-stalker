# fl-bb-stalker
A foreign alphabet bulletin board.

In its current state, running `python fl-bb-stalker.py` will look at the first page of the [WordPress.com forum](https://en.forums.wordpress.com/forum/support/), and send an email if there is a topic with a title using the Korean alphabet.

## Setup
### Mails
Edit the file <b>conf_mail.py</b> and change the following values:
- SRC_EMAIL: full email address of the Gmail account used to send emails
- SRC_PW: password of the SRC_EMAIL (must be written in clear, with double-quotes)
- DST_EMAIL: full email address of the account receiving emails (not necessarily Gmail)
### Tests
If you plan to run tests with `pytest`, create the file <b>fake_html.html</b> with at least the following lines (which is the first sticky thread of the WordPress.com help forum):
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
