import os
import pelican
from pelican.readers import MarkdownReader, BaseReader, METADATA_PROCESSORS
from pelican.utils import SafeDatetime, escape_html, get_date, pelican_open, \
    posixize_path
from markdown import Markdown

CONTENT = "content/"
HUGO = "hugo/"


class MyReader(BaseReader):
    """Reader for Markdown files"""

    enabled = True
    file_extensions = ['md', 'markdown', 'mkd', 'mdown']

    def __init__(self, *args, **kwargs):
        super(MyReader, self).__init__(*args, **kwargs)
        settings = self.settings['MARKDOWN']
        settings.setdefault('extension_configs', {})
        settings.setdefault('extensions', [])
        for extension in settings['extension_configs'].keys():
            if extension not in settings['extensions']:
                settings['extensions'].append(extension)
        if 'markdown.extensions.meta' not in settings['extensions']:
            settings['extensions'].append('markdown.extensions.meta')
        self._source_path = None

    def _parse_metadata(self, meta):
        """Return the dict containing document metadata"""
        formatted_fields = self.settings['FORMATTED_FIELDS']

        output = {}
        for name, value in meta.items():
            name = name.lower()
            if name in formatted_fields:
                # formatted metadata is special case and join all list values
                formatted_values = "\n".join(value)
                # reset the markdown instance to clear any state
                self._md.reset()
                formatted = self._md.convert(formatted_values)
                output[name] = self.process_metadata(name, formatted)
            elif name in METADATA_PROCESSORS:
                if len(value) > 1:
                    logger.warning(
                        'Duplicate definition of `%s` '
                        'for %s. Using first one.',
                        name, self._source_path)
                output[name] = self.process_metadata(name, value[0])
            elif len(value) > 1:
                # handle list metadata as list of string
                output[name] = self.process_metadata(name, value)
            else:
                # otherwise, handle metadata as single string
                output[name] = self.process_metadata(name, value[0])
        return output

    def read(self, source_path):
        """Parse content and metadata of markdown files"""

        self._source_path = source_path
        self._md = Markdown(**self.settings['MARKDOWN'])
        with pelican_open(source_path) as text:
            content = self._md.convert(text)
            content = text

        if hasattr(self._md, 'Meta'):
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}
        return content, metadata

os.makedirs(HUGO, exist_ok=True)

p, s = pelican.get_instance(pelican.parse_arguments())
mr = MyReader(s)

for root, dirs, files in os.walk(CONTENT):
    print(root)
    print(files)

    os.makedirs(os.path.join(HUGO, root), exist_ok=True)
    for file in files:
        content, meta = mr.read(os.path.join(root, file))
        print(meta)
        new_meta = """+++
title = "{title}"
description = "{description}"
tags = {tags}
date = "{date}"
+++
""".format(**{
    'title': meta['title'],
    'description': meta['summary'],
    'tags': '[{}]'.format(", ".join(['"{}"'.format(tag.name) for tag in meta['tags']])),
    'date': meta['date'].isoformat()
})

        with open(os.path.join(HUGO, root, file), 'w') as f:
            f.write(new_meta)
            f.write(content)

