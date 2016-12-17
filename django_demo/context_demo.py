from django.template import Context


c = Context({"foo": "bar"})
print c['foo']

del c['foo']
try:
    print c['foo']
except:
    print "This operation illegal!"

c['newvariable'] = 'hello'
print c['newvariable']