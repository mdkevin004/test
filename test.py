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



        a = ['#EXTM3U', '#EXTINF:-1 tvg-id="台視" tvg-name="台視" tvg-logo="https://logo.doube.eu.org/台視.png" group-title="新聞",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,2', 
'#EXTINF:-1 tvg-id="台視" tvg-name="台視" tvg-logo="https://logo.doube.eu.org/台視.png" group-title="新聞",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,6', 
'#EXTINF:-1 tvg-id="台視" tvg-name="台視" tvg-logo="https://logo.doube.eu.org/台視.png" group-title="新聞",台視', 
'https://www.youtube.com/watch?v=uDqQo8a7Xmk', 
'#EXTINF:-1 tvg-id="中視" tvg-name="中視" tvg-logo="https://logo.doube.eu.org/中視.png" group-title="新聞",中視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv040,1,6', 
'#EXTINF:-1 tvg-id="華視" tvg-name="華視" tvg-logo="https://logo.doube.eu.org/華視.png" group-title="新聞",華視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv041,1,6', 
'#EXTINF:-1 tvg-id="民視" tvg-name="民視" tvg-logo="https://logo.doube.eu.org/民視.png" group-title="新聞",民視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv002,1,10', 
'#EXTINF:-1 tvg-id="民視" tvg-name="民視" tvg-logo="https://logo.doube.eu.org/民視.png" group-title="新聞",民視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv002,1,10', 
'#EXTINF:-1 tvg-id="公視" tvg-name="公視" tvg-logo="https://logo.doube.eu.org/公視.png" group-title="新聞",公視', 
'https://www.youtube.com/watch?v=C6gYqSHLRw4', 
'#EXTINF:-1 tvg-id="鏡電視新聞台" tvg-name="鏡電視新聞台" tvg-logo="https://logo.doube.eu.org/鏡電視新聞台.png" group-title="新聞",鏡新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv075,1,2', 
'#EXTINF:-1 tvg-id="鏡電視新聞台" tvg-name="鏡電視新聞台" tvg-logo="https://logo.doube.eu.org/鏡電視新聞台.png" group-title="新聞",鏡新聞', 'https://www.youtube.com/watch?v=5n0y6b0Q25o']

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
