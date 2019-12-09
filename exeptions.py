class TestException(IOError):
    """There was an ambiguous exception that occurred while handling your
    request.
    """

    def __init__(self, *args, **kwargs):
        """Initialize RequestException with `request` and `response` objects."""
        response = kwargs.pop('response', None)
        self.response = response
        self.request = kwargs.pop('request', None)
        if (response is not None and not self.request and
                hasattr(response, 'request')):
            self.request = self.response.request
        super(TestException, self).__init__(*args, **kwargs)


class HTTPError(TestException):
    """An HTTP error occurred."""


class A:
    def __init__(self):
        self.aname = 'hahah'


a = A()

try:
    if a.bname == 'kakak':
        print('LOL')
except AttributeError as e:
    print('')
