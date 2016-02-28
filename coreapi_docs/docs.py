import coreapi


class Docs(object):

    def __init__(self, schema_file):
        try:
            file = open(schema_file, 'r')
            content = file.read()
            codec = coreapi.codecs.CoreJSONCodec()
            self.document = codec.load(content)
            self.error = None
            file.close()
        except (IOError, OSError) as e:
            self.document = None
            self.error = e
            pass

    def get_docs(self):
        return self.document
