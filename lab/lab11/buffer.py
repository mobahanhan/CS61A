class Buffer(object):
    """A Buffer provides a way of accessing a sequence one at a time.
    Its constructor takes a sequence, called the "source".
    The Buffer supplies elements from source one at a time through its pop_first()
    method. In addition, Buffer provides a current() method to look at the
    next item to be supplied, without moving past it.
    >>> buf = Buffer(['(', '+', 15, 12, ')'])
    >>> buf.pop_first()
    '('
    >>> buf.pop_first()
    '+'
    >>> buf.current()
    15
    >>> buf.pop_first()
    15
    >>> buf.current()
    12
    >>> buf.pop_first()
    12
    >>> buf.pop_first()
    ')'
    >>> buf.pop_first()  # returns None
    """
    def __init__(self, source):
        self.index = 0
        self.source = source

    def pop_first(self):
        """Remove the next item from self and return it. If self has
        exhausted its source, returns None."""
        current = self.current() #current是current()的输出物
        self.index += 1 #index加一
        return current #弹出current

    def current(self):
        """Return the current element, or None if none exists."""
        if self.index >= len(self.source):
            return None #如果index比输入物长，不输出
        else:
            return self.source[self.index] #否则，输出输入物中index对应的东西

    def expect(self, expected):
        actual = self.pop_first() #看看current
        if expected != actual:#不希望这个出现，就错误
            raise SyntaxError("expected '{}' but got '{}'".format(expected, actual))
        else:
            return actual #否则照旧

    def __str__(self):
        return str(self.source[self.index:])

