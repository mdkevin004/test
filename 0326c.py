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



        a = ['#EXTM3U', '#EXTINF:-1 tvg-id="中天新聞" tvg-name="中天新聞" tvg-logo="https://logo.doube.eu.org/中天新聞.png" group-title="新聞",中天新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv009,2,7', '#EXTINF:-1 tvg-id="中天新聞" tvg-name="中天新聞" tvg-logo="https://logo.doube.eu.org/中天新聞.png" group-title="新聞",中天新聞', 'https://www.youtube.com/watch?v=vr3XyVCR4T0', '#EXTINF:-1 tvg-id="東森新聞台" tvg-name="東森新聞台" tvg-logo="https://logo.doube.eu.org/東森新聞台.png" group-title="新聞",東森新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv152,1,6', '#EXTINF:-1 tvg-id="東森新聞台" tvg-name="東森新聞台" tvg-logo="https://logo.doube.eu.org/東森新聞台.png" group-title="新聞",東森新聞', 'https://www.youtube.com/watch?v=V1p33hqPrUk', '#EXTINF:-1 tvg-id="TVBS新聞" tvg-name="TVBS新聞" tvg-logo="https://logo.doube.eu.org/TVBS新聞.png" group-title="新聞",Tvbs新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv072,1,2', '#EXTINF:-1 tvg-id="TVBS新聞" tvg-name="TVBS新聞" tvg-logo="https://logo.doube.eu.org/TVBS新聞.png" group-title="新聞",Tvbs新聞台', 'https://www.youtube.com/watch?v=m_dhMSvUCIc', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="新聞",Tvbs', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv073,1,2', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="新聞",Tvbs', 'http://4gtv.mumi.rip:9877/183/4gtv-4gtv073/index.m3u8', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="新聞",Tvbs', 'http://125.227.210.55:8188/VideoInput/play.ts', '#EXTINF:-1 tvg-id="寰宇新聞台" tvg-name="寰宇新聞台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台.png" group-title="新聞",寰宇新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn14,1,2', '#EXTINF:-1 tvg-id="寰宇新聞台" tvg-name="寰宇新聞台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台.png" group-title="新聞",寰宇新聞台', 'http://4gtv.mumi.rip:9877/36/litv-longturn14/index.m3u8', '#EXTINF:-1 tvg-id="寰宇新聞台" tvg-name="寰宇新聞台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台.png" group-title="新聞",寰宇新聞台', 'https://www.youtube.com/watch?v=6IquAgfvYmc', '#EXTINF:-1 tvg-id="寰宇新聞台灣台" tvg-name="寰宇新聞台灣台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台灣台.png" group-title="新聞",寰宇新聞台灣台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv156,1,6', '#EXTINF:-1 tvg-id="寰宇新聞台灣台" tvg-name="寰宇新聞台灣台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台灣台.png" group-title="新聞",寰宇新聞台灣台', 'https://www.youtube.com/watch?v=w87VGpgd90U', '#EXTINF:-1 tvg-id="年代新聞台" tvg-name="年代新聞台" tvg-logo="https://logo.doube.eu.org/年代新聞台.png" group-title="新聞",年代新聞台', 'https://stream1.freetv.fun/28f2a175c45cd3d6885a0432398d36f149c45c516575d0da8a4312b445351c10.m3u8', '#EXTINF:-1 tvg-id="年代新聞台" tvg-name="年代新聞台" tvg-logo="https://logo.doube.eu.org/年代新聞台.png" group-title="新聞",年代新聞台', 'https://stream1.freetv.fun/be747d41b511a08679873d70f146d45d4c35c09256139e1a48dd9fdf20ac398b.m3u8', '#EXTINF:-1 tvg-id="鳳凰衛視資訊台" tvg-name="鳳凰衛視資訊台" tvg-logo="https://logo.doube.eu.org/鳳凰衛視資訊台.png" group-title="新聞",鳳凰衛視資訊台', 'https://www.youtube.com/watch?v=HFib76ySpbU', '#EXTINF:-1 tvg-id="鳳凰衛視資訊台" tvg-name="鳳凰衛視資訊台" tvg-logo="https://logo.doube.eu.org/鳳凰衛視資訊台.png" group-title="新聞",鳳凰衛視資訊台', 'http://php.jdshipin.com/TVOD/iptv.php?id=fhzx', '#EXTINF:-1 tvg-id="三立新聞" tvg-name="三立新聞" tvg-logo="https://logo.doube.eu.org/三立新聞.png" group-title="新聞",三立新聞', 'http://4gtv.mumi.rip:9877/229/4gtv-live089/index.m3u8', '#EXTINF:-1 tvg-id="三立新聞" tvg-name="三立新聞" tvg-logo="https://logo.doube.eu.org/三立新聞.png" group-title="新聞",三立新聞', 'https://www.youtube.com/watch?v=MV9mI0GChwo', '#EXTINF:-1 tvg-id="CCTV4" tvg-name="CCTV4" tvg-logo="https://logo.doube.eu.org/CCTV4.png" group-title="新聞",CCTV4', 'https://www.youtube.com/watch?v=SdzewdkJa-o', '#EXTINF:-1 tvg-id="CCTV13" tvg-name="CCTV13" tvg-logo="https://logo.doube.eu.org/CCTV13.png" group-title="新聞",CCTV13', 'http://www.cdnstv.com:6398/hls/13/index.m3u8',]

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
