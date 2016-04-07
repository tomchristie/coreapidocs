import coreapi


class Docs(object):

    def __init__(self, schema):
        codec = coreapi.codecs.CoreJSONCodec()
        self.document = codec.load(schema)

    def get_docs(self):
        return self.document
