''' The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.
string.join(iterable) '''

val = 'I ma doog yob'

print(' '.join([i[::-1] for i in val.split(' ')]))
