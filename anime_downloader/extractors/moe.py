import requests
import re
import base64

from anime_downloader import util
from anime_downloader.extractors.base_extractor import BaseExtractor


class StreamMoe(BaseExtractor):
    def _get_data(self):
        url = self.url
        res = requests.get(url, **util.get_requests_options())
        content_re = re.compile(r"= atob\('(.*?)'\)")
        source_re = re.compile(r'source src="(.*?)"')

        enc_cont = content_re.findall(res.text)[0]
        content = base64.b64decode(enc_cont).decode('utf-8')

        stream_url = source_re.findall(content)[0]

        return {
            'stream_url': stream_url,
            'meta': {
                'title': '',
                'thumbnail': '',
            }
        }
