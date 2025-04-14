# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/3/23 21:55
import base64
import sys
import time
import json
import requests
sys.path.append('..')
from base.spider import Spider


class Spider(Spider):
    def getName(self):
        return "Litv"

    def init(self, extend):
        self.extend = extend
        try:
            self.extendDict = json.loads(extend)
        except:
            self.extendDict = {}

        proxy = self.extendDict.get('proxy', None)
        if proxy is None:
            self.is_proxy = False
        else:
            self.proxy = proxy
            self.is_proxy = True
        pass

    def getDependence(self):
        return []

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass


    def liveContent(self, url):



        a = ['#EXTM3U', '#EXTINF:-1 tvg-id="亞洲旅遊台" tvg-name="亞洲旅遊台" tvg-logo="https://logo.doube.eu.org/亞洲旅遊台.png" group-title="",亞洲旅遊台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv076,1,2', '#EXTINF:-1 tvg-id="TraceSportStars" tvg-name="TraceSportStars" tvg-logo="https://logo.doube.eu.org/TraceSportStars.png" group-title="",TRACE SPORTS STARS', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv082,1,2', '#EXTINF:-1 tvg-id="ARIRANG" tvg-name="ARIRANG" tvg-logo="https://logo.doube.eu.org/ARIRANG.png" group-title="",阿里郎', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv079,1,2', '#EXTINF:-1 tvg-id="TraceUrban" tvg-name="TraceUrban" tvg-logo="https://logo.doube.eu.org/TraceUrban.png" group-title="",TRACE URBAN', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv082,1,6', '#EXTINF:-1 tvg-id="MezzoLiveHD" tvg-name="MezzoLiveHD" tvg-logo="https://logo.doube.eu.org/MezzoLiveHD.png" group-title="",MEZZO LIVE', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv083,1,6', '#EXTINF:-1 tvg-id="智林體育台" tvg-name="智林體育台" tvg-logo="https://logo.doube.eu.org/智林體育台.png" group-title="",智林體育台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv101,1,5', '#EXTINF:-1 tvg-id="智林體育台" tvg-name="智林體育台" tvg-logo="https://logo.doube.eu.org/智林體育台.png" group-title="",智林體育台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv101,1,6', '#EXTINF:-1 tvg-id="第1商業台" tvg-name="第1商業台" tvg-logo="https://logo.doube.eu.org/第1商業台.png" group-title="",第1商業台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv104,1,7', '#EXTINF:-1 tvg-id="美國之音" tvg-name="美國之音" tvg-logo="https://logo.doube.eu.org/美國之音.png" group-title="",美國之音', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv03,1,7', '#EXTINF:-1 tvg-id="半島國際新聞" tvg-name="半島國際新聞" tvg-logo="https://logo.doube.eu.org/半島國際新聞.png" group-title="",半島新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv10,1,7', '#EXTINF:-1 tvg-id="Smart知識台" tvg-name="Smart知識台" tvg-logo="https://logo.doube.eu.org/Smart知識台.png" group-title="",Smart知識台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn19,5,2', '#EXTINF:-1 tvg-id="ELTV生活英語台" tvg-name="ELTV生活英語台" tvg-logo="https://logo.doube.eu.org/ELTV生活英語台.png" group-title="",生活英語台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn20,5,6','#EXTINF:-1 tvg-id="民視" tvg-name="民視" tvg-logo="https://logo.doube.eu.org/民視.png" group-title="",民視', 'https://tv.cctv.com/live/cctv13/?spm=C28340.PpiaYs0TLjHK.ExidtyEJcS5K.25']

        return '\n'.join(a)

    def homeContent(self, filter):
        return {}

    def homeVideoContent(self):
        return {}

    def categoryContent(self, cid, page, filter, ext):
        return {}

    def detailContent(self, did):
        return {}

    def searchContent(self, key, quick, page='1'):
        return {}

    def searchContentPage(self, keywords, quick, page):
        return {}

    def playerContent(self, flag, pid, vipFlags):
        return {}

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        if params['type'] == "ts":
            return self.get_ts(params)
        return [302, "text/plain", None, {'Location': 'https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4'}]
    def proxyM3u8(self, params):
        pid = params['pid']
        info = pid.split(',')
        a = info[0]
        b = info[1]
        c = info[2]
        timestamp = int(time.time() / 4 - 355017625)
        t = timestamp * 4
        m3u8_text = f'#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:4\n#EXT-X-MEDIA-SEQUENCE:{timestamp}\n'
        for i in range(10):
            url = f'https://ntd-tgc.cdn.hinet.net/live/pool/{a}/litv-pc/{a}-avc1_6000000={b}-mp4a_134000_zho={c}-begin={t}0000000-dur=40000000-seq={timestamp}.ts'
            if self.is_proxy:
                url = f'http://127.0.0.1:9978/proxy?do=py&type=ts&url={self.b64encode(url)}'

            m3u8_text += f'#EXTINF:4,\n{url}\n'
            timestamp += 1
            t += 4
        return [200, "application/vnd.apple.mpegurl", m3u8_text]

    def get_ts(self, params):
        url = self.b64decode(params['url'])
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, stream=True, proxies=self.proxy)
        return [206, "application/octet-stream", response.content]

    def destroy(self):
        return '正在Destroy'

    def b64encode(self, data):
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')

    def b64decode(self, data):
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')


if __name__ == '__main__':
    pass
