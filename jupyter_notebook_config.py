# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password="sha1:08ab1cf81a7e:f2cd18ac0b12f63c9bfc238999d05baef5fd7483"
