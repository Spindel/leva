from CommonMark import DocParser, HTMLRenderer
from pelican.readers import BaseReader


class CommonMarkReader(BaseReader):
    file_extensions = ['md']

    def read(self, source_path):
        source = open(source_path)
        metadata = {}
        reading_metadata = True
        while reading_metadata:
            line = source.readline()
            if line.count(':') > 0:
                key, value = map(str.strip, line.split(':', maxsplit=1))
                key = key.lower()
                metadata[key] = self.process_metadata(key, value)
            else:
                reading_metadata = False

        content = HTMLRenderer().render(DocParser().parse(source.read()))
        return content, metadata


def register():
    pass
