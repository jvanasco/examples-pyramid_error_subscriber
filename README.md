# examples-pyramid_error_subscriber

these exceptions are caught by pyramid:

* /test-1
  error in __init__ of class based view

* /test-2
  error in method of class based view

these exceptions are not caught by pyramid, and passed onto waitress

* /test-3
  error in subscriber


