# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.passwordUnicode='sha1:9af7daaba8ea:d4865f1d8732eb570009a869a2a5fe603172f13e'
