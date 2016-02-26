import coreapi


class Docs(object):

    def __init__(self, schema_file):
        content = open(schema_file, 'r').read()
        codec = coreapi.codecs.CoreJSONCodec()
        self.document = codec.load(content)

    def get_docs(self):
        return self.document
