import coreapi


class Docs(object):

    def __init__(self, schema_file):
        content = open(schema_file, 'r').read()
        codec = coreapi.codecs.CoreJSONCodec()
        self.document = codec.load(content)

    def get_docs(self):
        print '# %s' % self.document.title
        print

        for tag, sub_doc in self.document.data.items():
            print '## %s' % tag
            print

            for name, link in sub_doc.links.items():
                print '### %s' % name
                print
                print link.description
                print
                for field in link.fields:
                    if field.required:
                        print '* %s - %s' % (field.name, field.description)
                    else:
                        print '* [%s] - %s' % (field.name, field.description)
                print

            print '---'
            print

        return self.document
