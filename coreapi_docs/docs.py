import coreapi


class Docs(object):

    def __init__(self, schema_file):
        try:
            content = open(schema_file, 'r').read()
            codec = coreapi.codecs.CoreJSONCodec()
            self.document = codec.load(content)
            content.close()
        except (IOError, OSError) as e:
            self.document = None
            self.error = e
            pass

    def get_docs(self):
        return self.document
