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



        a = ['#EXTM3U', '#EXTINF:-1 tvg-id="台視" tvg-name="台視" tvg-logo="https://logo.doube.eu.org/台視.png" group-title="新聞",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,2', '#EXTINF:-1 tvg-id="台視" tvg-name="台視" tvg-logo="https://logo.doube.eu.org/台視.png" group-title="新聞",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,6', '#EXTINF:-1 tvg-id="台視" tvg-name="台視" tvg-logo="https://logo.doube.eu.org/台視.png" group-title="新聞",台視', 'https://www.youtube.com/watch?v=uDqQo8a7Xmk', '#EXTINF:-1 tvg-id="中視" tvg-name="中視" tvg-logo="https://logo.doube.eu.org/中視.png" group-title="新聞",中視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv040,1,6', '#EXTINF:-1 tvg-id="華視" tvg-name="華視" tvg-logo="https://logo.doube.eu.org/華視.png" group-title="新聞",華視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv041,1,6', '#EXTINF:-1 tvg-id="民視" tvg-name="民視" tvg-logo="https://logo.doube.eu.org/民視.png" group-title="新聞",民視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv002,1,10', '#EXTINF:-1 tvg-id="民視" tvg-name="民視" tvg-logo="https://logo.doube.eu.org/民視.png" group-title="新聞",民視', 'rtmp://9hv9.mine.nu/sat/tv051', '#EXTINF:-1 tvg-id="公視" tvg-name="公視" tvg-logo="https://logo.doube.eu.org/公視.png" group-title="新聞",公視', 'https://www.youtube.com/watch?v=C6gYqSHLRw4', '#EXTINF:-1 tvg-id="鏡電視新聞台" tvg-name="鏡電視新聞台" tvg-logo="https://logo.doube.eu.org/鏡電視新聞台.png" group-title="新聞",鏡新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv075,1,2', '#EXTINF:-1 tvg-id="鏡電視新聞台" tvg-name="鏡電視新聞台" tvg-logo="https://logo.doube.eu.org/鏡電視新聞台.png" group-title="新聞",鏡新聞', 'https://www.youtube.com/watch?v=5n0y6b0Q25o', '#EXTINF:-1 tvg-id="TaiwanPlus" tvg-name="TaiwanPlus" tvg-logo="https://logo.doube.eu.org/TaiwanPlus.png" group-title="新聞",TaiwanPlus', 'https://www.youtube.com/watch?v=gvV_mJsKLWQ', '#EXTINF:-1 tvg-id="中天亞洲" tvg-name="中天亞洲" tvg-logo="https://logo.doube.eu.org/中天亞洲.png" group-title="新聞",中天亞洲台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv109,1,7', '#EXTINF:-1 tvg-id="中天亞洲" tvg-name="中天亞洲" tvg-logo="https://logo.doube.eu.org/中天亞洲.png" group-title="新聞",中天亞洲台', 'https://www.youtube.com/watch?v=1gjlfQ4b1ZU', '#EXTINF:-1 tvg-id="公視台語台" tvg-name="公視台語台" tvg-logo="https://logo.doube.eu.org/公視台語台.png" group-title="新聞",公視台語台', 'https://www.youtube.com/watch?v=6KlRR_DGhmI', '#EXTINF:-1 tvg-id="大愛一臺" tvg-name="大愛一臺" tvg-logo="https://logo.doube.eu.org/大愛一臺.png" group-title="新聞",大愛一臺', 'https://pulltv1.wanfudaluye.com/live/tv1.m3u8', '#EXTINF:-1 tvg-id="大愛一臺" tvg-name="大愛一臺" tvg-logo="https://logo.doube.eu.org/大愛一臺.png" group-title="新聞",大愛一臺', 'https://www.youtube.com/watch?v=oV_i3Hsl_zg', '#EXTINF:-1 tvg-id="大愛二臺" tvg-name="大愛二臺" tvg-logo="https://logo.doube.eu.org/大愛二臺.png" group-title="新聞",大愛二臺', 'https://pulltv2.wanfudaluye.com/live/tv2.m3u8', '#EXTINF:-1 tvg-id="大愛二臺" tvg-name="大愛二臺" tvg-logo="https://logo.doube.eu.org/大愛二臺.png" group-title="新聞",大愛二臺', 'https://www.youtube.com/watch?v=OKvWtVoDR8I', '#EXTINF:-1 tvg-id="東森財經新聞台" tvg-name="東森財經新聞台" tvg-logo="https://logo.doube.eu.org/東森財經新聞台.png" group-title="新聞",東森財經新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv153,1,2', '#EXTINF:-1 tvg-id="東森財經新聞台" tvg-name="東森財經新聞台" tvg-logo="https://logo.doube.eu.org/東森財經新聞台.png" group-title="新聞",東森財經新聞', 'https://www.youtube.com/watch?v=1I2iq41Akmo', '#EXTINF:-1 tvg-id="東森財經新聞台" tvg-name="東森財經新聞台" tvg-logo="https://logo.doube.eu.org/東森財經新聞台.png" group-title="新聞",東森財經新聞', 'http://4gtv.mumi.rip:9877/293/4gtv-4gtv153/index.m3u8', '#EXTINF:-1 tvg-id="非凡新聞" tvg-name="非凡新聞" tvg-logo="https://logo.doube.eu.org/非凡新聞.png" group-title="新聞",非凡新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv010,1,6', '#EXTINF:-1 tvg-id="非凡新聞" tvg-name="非凡新聞" tvg-logo="https://logo.doube.eu.org/非凡新聞.png" group-title="新聞",非凡新聞', 'https://www.youtube.com/watch?v=jLeN_GbUzps', '#EXTINF:-1 tvg-id="非凡新聞" tvg-name="非凡新聞" tvg-logo="https://logo.doube.eu.org/非凡新聞.png" group-title="新聞",非凡新聞', 'rtmp://f13h.mine.nu/sat/tv581', '#EXTINF:-1 tvg-id="台視財經台" tvg-name="台視財經台" tvg-logo="https://logo.doube.eu.org/台視財經台.png" group-title="新聞",台視財經', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv056,1,2', '#EXTINF:-1 tvg-id="台視新聞台" tvg-name="台視新聞台" tvg-logo="https://logo.doube.eu.org/台視新聞台.png" group-title="新聞",台視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv051,1,2', '#EXTINF:-1 tvg-id="台視新聞台" tvg-name="台視新聞台" tvg-logo="https://logo.doube.eu.org/台視新聞台.png" group-title="新聞",台視新聞', 'https://www.youtube.com/watch?v=xL0ch83RAK8', '#EXTINF:-1 tvg-id="中視新聞台" tvg-name="中視新聞台" tvg-logo="https://logo.doube.eu.org/中視新聞台.png" group-title="新聞",中視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv074,1,2', '#EXTINF:-1 tvg-id="中視新聞台" tvg-name="中視新聞台" tvg-logo="https://logo.doube.eu.org/中視新聞台.png" group-title="新聞",中視新聞', 'https://www.youtube.com/watch?v=TCnaIE_SAtM', '#EXTINF:-1 tvg-id="華視新聞" tvg-name="華視新聞" tvg-logo="https://logo.doube.eu.org/華視新聞.png" group-title="新聞",華視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv052,1,2', '#EXTINF:-1 tvg-id="華視新聞" tvg-name="華視新聞" tvg-logo="https://logo.doube.eu.org/華視新聞.png" group-title="新聞",華視新聞', 'https://www.youtube.com/watch?v=wM0g8EoUZ_E', '#EXTINF:-1 tvg-id="民視新聞台" tvg-name="民視新聞台" tvg-logo="https://logo.doube.eu.org/民視新聞台.png" group-title="新聞",民視新聞台', 'https://www.youtube.com/watch?v=ylYJSBUgaMA', '#EXTINF:-1 tvg-id="民視新聞台" tvg-name="民視新聞台" tvg-logo="https://logo.doube.eu.org/民視新聞台.png" group-title="新聞",民視新聞台', 'http://4gtv.mumi.rip:9877/31/litv-ftv13/index.m3u8', '#EXTINF:-1 tvg-id="民視新聞台" tvg-name="民視新聞台" tvg-logo="https://logo.doube.eu.org/民視新聞台.png" group-title="新聞",民視新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv13,1,7', '#EXTINF:-1 tvg-id="中天新聞" tvg-name="中天新聞" tvg-logo="https://logo.doube.eu.org/中天新聞.png" group-title="新聞",中天新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv009,2,7', '#EXTINF:-1 tvg-id="中天新聞" tvg-name="中天新聞" tvg-logo="https://logo.doube.eu.org/中天新聞.png" group-title="新聞",中天新聞', 'https://www.youtube.com/watch?v=vr3XyVCR4T0', '#EXTINF:-1 tvg-id="東森新聞台" tvg-name="東森新聞台" tvg-logo="https://logo.doube.eu.org/東森新聞台.png" group-title="新聞",東森新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv152,1,6', '#EXTINF:-1 tvg-id="東森新聞台" tvg-name="東森新聞台" tvg-logo="https://logo.doube.eu.org/東森新聞台.png" group-title="新聞",東森新聞', 'https://www.youtube.com/watch?v=V1p33hqPrUk', '#EXTINF:-1 tvg-id="TVBS新聞" tvg-name="TVBS新聞" tvg-logo="https://logo.doube.eu.org/TVBS新聞.png" group-title="新聞",Tvbs新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv072,1,2', '#EXTINF:-1 tvg-id="TVBS新聞" tvg-name="TVBS新聞" tvg-logo="https://logo.doube.eu.org/TVBS新聞.png" group-title="新聞",Tvbs新聞台', 'https://www.youtube.com/watch?v=m_dhMSvUCIc', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="新聞",Tvbs', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv073,1,2', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="新聞",Tvbs', 'http://4gtv.mumi.rip:9877/183/4gtv-4gtv073/index.m3u8', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="新聞",Tvbs', 'http://125.227.210.55:8188/VideoInput/play.ts', '#EXTINF:-1 tvg-id="寰宇新聞台" tvg-name="寰宇新聞台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台.png" group-title="新聞",寰宇新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn14,1,2', '#EXTINF:-1 tvg-id="寰宇新聞台" tvg-name="寰宇新聞台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台.png" group-title="新聞",寰宇新聞台', 'http://4gtv.mumi.rip:9877/36/litv-longturn14/index.m3u8', '#EXTINF:-1 tvg-id="寰宇新聞台" tvg-name="寰宇新聞台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台.png" group-title="新聞",寰宇新聞台', 'https://www.youtube.com/watch?v=6IquAgfvYmc', '#EXTINF:-1 tvg-id="寰宇新聞台灣台" tvg-name="寰宇新聞台灣台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台灣台.png" group-title="新聞",寰宇新聞台灣台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv156,1,6', '#EXTINF:-1 tvg-id="寰宇新聞台灣台" tvg-name="寰宇新聞台灣台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台灣台.png" group-title="新聞",寰宇新聞台灣台', 'https://www.youtube.com/watch?v=w87VGpgd90U', '#EXTINF:-1 tvg-id="年代新聞台" tvg-name="年代新聞台" tvg-logo="https://logo.doube.eu.org/年代新聞台.png" group-title="新聞",年代新聞台', 'https://stream1.freetv.fun/28f2a175c45cd3d6885a0432398d36f149c45c516575d0da8a4312b445351c10.m3u8', '#EXTINF:-1 tvg-id="年代新聞台" tvg-name="年代新聞台" tvg-logo="https://logo.doube.eu.org/年代新聞台.png" group-title="新聞",年代新聞台', 'https://stream1.freetv.fun/be747d41b511a08679873d70f146d45d4c35c09256139e1a48dd9fdf20ac398b.m3u8', '#EXTINF:-1 tvg-id="鳳凰衛視資訊台" tvg-name="鳳凰衛視資訊台" tvg-logo="https://logo.doube.eu.org/鳳凰衛視資訊台.png" group-title="新聞",鳳凰衛視資訊台', 'https://www.youtube.com/watch?v=HFib76ySpbU', '#EXTINF:-1 tvg-id="鳳凰衛視資訊台" tvg-name="鳳凰衛視資訊台" tvg-logo="https://logo.doube.eu.org/鳳凰衛視資訊台.png" group-title="新聞",鳳凰衛視資訊台', 'http://php.jdshipin.com/TVOD/iptv.php?id=fhzx', '#EXTINF:-1 tvg-id="三立新聞" tvg-name="三立新聞" tvg-logo="https://logo.doube.eu.org/三立新聞.png" group-title="新聞",三立新聞', 'https://www.youtube.com/watch?v=MV9mI0GChwo', '#EXTINF:-1 tvg-id="三立新聞" tvg-name="三立新聞" tvg-logo="https://logo.doube.eu.org/三立新聞.png" group-title="新聞",三立新聞', 'http://4gtv.mumi.rip:9877/229/4gtv-live089/index.m3u8', '#EXTINF:-1 tvg-id="CCTV4" tvg-name="CCTV4" tvg-logo="https://logo.doube.eu.org/CCTV4.png" group-title="新聞",CCTV4', 'https://www.youtube.com/watch?v=SdzewdkJa-o', '#EXTINF:-1 tvg-id="TVBS歡樂台" tvg-name="TVBS歡樂台" tvg-logo="https://logo.doube.eu.org/TVBS歡樂台.png" group-title="綜藝",Tvbs歡樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv068,1,7', '#EXTINF:-1 tvg-id="TVBS歡樂台" tvg-name="TVBS歡樂台" tvg-logo="https://logo.doube.eu.org/TVBS歡樂台.png" group-title="綜藝",Tvbs歡樂台', 'http://122.117.71.103:8531/http/220.130.87.218:8081/hls/65/807/ch017.m3u8', '#EXTINF:-1 tvg-id="民視綜藝台" tvg-name="民視綜藝台" tvg-logo="https://logo.doube.eu.org/民視綜藝台.png" group-title="綜藝",民視綜藝', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv004,1,8', '#EXTINF:-1 tvg-id="靖天日本台" tvg-name="靖天日本台" tvg-logo="https://logo.doube.eu.org/靖天日本台.png" group-title="綜藝",靖天日本台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv047,1,8', '#EXTINF:-1 tvg-id="緯來日本" tvg-name="緯來日本" tvg-logo="https://logo.doube.eu.org/緯來日本.png" group-title="綜藝",緯來日本', 'rtmp://9hv9.mine.nu/sat/tv771', '#EXTINF:-1 tvg-id="豬哥亮歌廳秀" tvg-name="豬哥亮歌廳秀" tvg-logo="https://logo.doube.eu.org/豬哥亮歌廳秀.png" group-title="綜藝",豬哥亮歌廳秀', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv006,1,9', '#EXTINF:-1 tvg-id="豬哥亮歌廳秀" tvg-name="豬哥亮歌廳秀" tvg-logo="https://logo.doube.eu.org/豬哥亮歌廳秀.png" group-title="綜藝",豬哥亮歌廳秀', 'http://4gtv.mumi.rip:9877/113/4gtv-4gtv006/index.m3u8', '#EXTINF:-1 tvg-id="萬秀豬王" tvg-name="萬秀豬王" tvg-logo="https://logo.doube.eu.org/萬秀豬王.png" group-title="綜藝",萬秀豬王', 'https://www.youtube.com/watch?v=ADDSmXoPDY8', '#EXTINF:-1 tvg-id="大陸尋奇" tvg-name="大陸尋奇" tvg-logo="https://logo.doube.eu.org/大陸尋奇.png" group-title="綜藝",大陸尋奇', 'https://www.youtube.com/watch?v=UtOw97Ba8hE', '#EXTINF:-1 tvg-id="amc電影台" tvg-name="amc電影台" tvg-logo="https://logo.doube.eu.org/amc電影台.png" group-title="電影",amc電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv017,1,6', '#EXTINF:-1 tvg-id="HBO HD" tvg-name="HBO HD" tvg-logo="https://logo.doube.eu.org/HBO HD.png" group-title="電影",HBO HD', 'http://125.227.210.55:8153/VideoInput/play.ts', '#EXTINF:-1 tvg-id="HBO HD" tvg-name="HBO HD" tvg-logo="https://logo.doube.eu.org/HBO HD.png" group-title="電影",ROCK Action', 'http://aktv-stream.m16tv.cfd/stream/aktv/rockaction/AKTV.m3u8', '#EXTINF:-1 tvg-id="靖天映畫" tvg-name="靖天映畫" tvg-logo="https://logo.doube.eu.org/靖天映畫.png" group-title="電影",靖天映畫', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv055,1,8', '#EXTINF:-1 tvg-id="靖天電影台" tvg-name="靖天電影台" tvg-logo="https://logo.doube.eu.org/靖天電影台.png" group-title="電影",靖天電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv061,1,7', '#EXTINF:-1 tvg-id="龍華洋片台" tvg-name="龍華洋片台" tvg-logo="https://logo.doube.eu.org/龍華洋片台.png" group-title="電影",龍華洋片', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn02,5,2', '#EXTINF:-1 tvg-id="博斯魅力" tvg-name="博斯魅力" tvg-logo="https://logo.doube.eu.org/博斯魅力.png" group-title="體育",博斯魅力', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn04,5,2', '#EXTINF:-1 tvg-id="博斯高球1" tvg-name="博斯高球1" tvg-logo="https://logo.doube.eu.org/博斯高球1.png" group-title="體育",博斯高球1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn05,5,2', '#EXTINF:-1 tvg-id="博斯高球2" tvg-name="博斯高球2" tvg-logo="https://logo.doube.eu.org/博斯高球2.png" group-title="體育",博斯高球2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn06,5,2', '#EXTINF:-1 tvg-id="博斯運動1" tvg-name="博斯運動1" tvg-logo="https://logo.doube.eu.org/博斯運動1.png" group-title="體育",博斯運動1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn07,5,2', '#EXTINF:-1 tvg-id="博斯運動2" tvg-name="博斯運動2" tvg-logo="https://logo.doube.eu.org/博斯運動2.png" group-title="體育",博斯運動2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn08,5,2', '#EXTINF:-1 tvg-id="博斯網球1" tvg-name="博斯網球1" tvg-logo="https://logo.doube.eu.org/博斯網球1.png" group-title="體育",博斯網球', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn09,5,2', '#EXTINF:-1 tvg-id="博斯無限1" tvg-name="博斯無限1" tvg-logo="https://logo.doube.eu.org/博斯無限1.png" group-title="體育",博斯無限', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn10,5,2', '#EXTINF:-1 tvg-id="博斯無限2" tvg-name="博斯無限2" tvg-logo="https://logo.doube.eu.org/博斯無限2.png" group-title="體育",博斯無限2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn13,4,2', '#EXTINF:-1 tvg-id="緯來體育台" tvg-name="緯來體育台" tvg-logo="https://logo.doube.eu.org/緯來體育台.png" group-title="體育",緯來體育台', 'http://aktv-stream.m16tv.cfd/stream/test/null/AKTV.m3u8', '#EXTINF:-1 tvg-id="緯來體育台" tvg-name="緯來體育台" tvg-logo="https://logo.doube.eu.org/緯來體育台.png" group-title="體育",緯來體育台', 'rtmp://9hv9.mine.nu/sat/tv721', '#EXTINF:-1 tvg-id="緯來體育台" tvg-name="緯來體育台" tvg-logo="https://logo.doube.eu.org/緯來體育台.png" group-title="體育",緯來體育台', 'rtmp://f13h.mine.nu/sat/tv721', '#EXTINF:-1 tvg-id="Love Nrture" tvg-name="Love Nrture" tvg-logo="https://logo.doube.eu.org/Love Nrture.png" group-title="探索",Love Nrture', 'https://d18dyiwu97wm6q.cloudfront.net/playlist720p.m3u8', '#EXTINF:-1 tvg-id="亞洲旅遊台" tvg-name="亞洲旅遊台" tvg-logo="https://logo.doube.eu.org/亞洲旅遊台.png" group-title="探索",亞洲旅遊台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv076,1,2', '#EXTINF:-1 tvg-id="民視旅遊台" tvg-name="民視旅遊台" tvg-logo="https://logo.doube.eu.org/民視旅遊台.png" group-title="探索",民視旅遊', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv07,1,7', '#EXTINF:-1 tvg-id="民視影劇台" tvg-name="民視影劇台" tvg-logo="https://logo.doube.eu.org/民視影劇台.png" group-title="戲劇",民視影劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv09,1,2', '#EXTINF:-1 tvg-id="台灣戲劇台" tvg-name="台灣戲劇台" tvg-logo="https://logo.doube.eu.org/台灣戲劇台.png" group-title="戲劇",台灣戲劇台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn22,5,2', '#EXTINF:-1 tvg-id="全球時尚 Global Fashion " tvg-name="全球時尚 Global Fashion " tvg-logo="https://logo.doube.eu.org/全球時尚.png" group-title="時尚",全球時尚 Global Fashion ', 'https://pubgfc.teleosmedia.com/linear/globalfashionchannel/globalfashionchannel/playlist.m3u8', '#EXTINF:-1 tvg-id="法國時尚" tvg-name="法國時尚" tvg-logo="https://logo.doube.eu.org/法國時尚.png" group-title="時尚",法國時尚', 'http://lb.streaming.sk/fashiontv/stream/chunklist.m3u8', '#EXTINF:-1 tvg-id="Fashion TV HD" tvg-name="Fashion TV HD" tvg-logo="https://logo.doube.eu.org/FashionTVHD.png" group-title="時尚",Fashion TV HD', 'https://fashiontv-fashiontv-1-eu.rakuten.wurl.tv/playlist.m3u8']
		
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



        a = ['#EXTM3U', '#EXTINF:-1 tvg-id="台視" tvg-name="台視" tvg-logo="https://logo.doube.eu.org/台視.png" group-title="新聞",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,2', '#EXTINF:-1 tvg-id="台視" tvg-name="台視" tvg-logo="https://logo.doube.eu.org/台視.png" group-title="新聞",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,6', '#EXTINF:-1 tvg-id="台視" tvg-name="台視" tvg-logo="https://logo.doube.eu.org/台視.png" group-title="新聞",台視', 'https://www.youtube.com/watch?v=uDqQo8a7Xmk', '#EXTINF:-1 tvg-id="中視" tvg-name="中視" tvg-logo="https://logo.doube.eu.org/中視.png" group-title="新聞",中視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv040,1,6', '#EXTINF:-1 tvg-id="華視" tvg-name="華視" tvg-logo="https://logo.doube.eu.org/華視.png" group-title="新聞",華視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv041,1,6', '#EXTINF:-1 tvg-id="民視" tvg-name="民視" tvg-logo="https://logo.doube.eu.org/民視.png" group-title="新聞",民視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv002,1,10', '#EXTINF:-1 tvg-id="民視" tvg-name="民視" tvg-logo="https://logo.doube.eu.org/民視.png" group-title="新聞",民視', 'rtmp://9hv9.mine.nu/sat/tv051', '#EXTINF:-1 tvg-id="公視" tvg-name="公視" tvg-logo="https://logo.doube.eu.org/公視.png" group-title="新聞",公視', 'https://www.youtube.com/watch?v=C6gYqSHLRw4', '#EXTINF:-1 tvg-id="鏡電視新聞台" tvg-name="鏡電視新聞台" tvg-logo="https://logo.doube.eu.org/鏡電視新聞台.png" group-title="新聞",鏡新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv075,1,2', '#EXTINF:-1 tvg-id="鏡電視新聞台" tvg-name="鏡電視新聞台" tvg-logo="https://logo.doube.eu.org/鏡電視新聞台.png" group-title="新聞",鏡新聞', 'https://www.youtube.com/watch?v=5n0y6b0Q25o', '#EXTINF:-1 tvg-id="TaiwanPlus" tvg-name="TaiwanPlus" tvg-logo="https://logo.doube.eu.org/TaiwanPlus.png" group-title="新聞",TaiwanPlus', 'https://www.youtube.com/watch?v=gvV_mJsKLWQ', '#EXTINF:-1 tvg-id="中天亞洲" tvg-name="中天亞洲" tvg-logo="https://logo.doube.eu.org/中天亞洲.png" group-title="新聞",中天亞洲台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv109,1,7', '#EXTINF:-1 tvg-id="中天亞洲" tvg-name="中天亞洲" tvg-logo="https://logo.doube.eu.org/中天亞洲.png" group-title="新聞",中天亞洲台', 'https://www.youtube.com/watch?v=1gjlfQ4b1ZU', '#EXTINF:-1 tvg-id="公視台語台" tvg-name="公視台語台" tvg-logo="https://logo.doube.eu.org/公視台語台.png" group-title="新聞",公視台語台', 'https://www.youtube.com/watch?v=6KlRR_DGhmI', '#EXTINF:-1 tvg-id="大愛一臺" tvg-name="大愛一臺" tvg-logo="https://logo.doube.eu.org/大愛一臺.png" group-title="新聞",大愛一臺', 'https://pulltv1.wanfudaluye.com/live/tv1.m3u8', '#EXTINF:-1 tvg-id="大愛一臺" tvg-name="大愛一臺" tvg-logo="https://logo.doube.eu.org/大愛一臺.png" group-title="新聞",大愛一臺', 'https://www.youtube.com/watch?v=oV_i3Hsl_zg', '#EXTINF:-1 tvg-id="大愛二臺" tvg-name="大愛二臺" tvg-logo="https://logo.doube.eu.org/大愛二臺.png" group-title="新聞",大愛二臺', 'https://pulltv2.wanfudaluye.com/live/tv2.m3u8', '#EXTINF:-1 tvg-id="大愛二臺" tvg-name="大愛二臺" tvg-logo="https://logo.doube.eu.org/大愛二臺.png" group-title="新聞",大愛二臺', 'https://www.youtube.com/watch?v=OKvWtVoDR8I', '#EXTINF:-1 tvg-id="東森財經新聞台" tvg-name="東森財經新聞台" tvg-logo="https://logo.doube.eu.org/東森財經新聞台.png" group-title="新聞",東森財經新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv153,1,2', '#EXTINF:-1 tvg-id="東森財經新聞台" tvg-name="東森財經新聞台" tvg-logo="https://logo.doube.eu.org/東森財經新聞台.png" group-title="新聞",東森財經新聞', 'https://www.youtube.com/watch?v=1I2iq41Akmo', '#EXTINF:-1 tvg-id="東森財經新聞台" tvg-name="東森財經新聞台" tvg-logo="https://logo.doube.eu.org/東森財經新聞台.png" group-title="新聞",東森財經新聞', 'http://4gtv.mumi.rip:9877/293/4gtv-4gtv153/index.m3u8', '#EXTINF:-1 tvg-id="非凡新聞" tvg-name="非凡新聞" tvg-logo="https://logo.doube.eu.org/非凡新聞.png" group-title="新聞",非凡新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv010,1,6', '#EXTINF:-1 tvg-id="非凡新聞" tvg-name="非凡新聞" tvg-logo="https://logo.doube.eu.org/非凡新聞.png" group-title="新聞",非凡新聞', 'https://www.youtube.com/watch?v=jLeN_GbUzps', '#EXTINF:-1 tvg-id="非凡新聞" tvg-name="非凡新聞" tvg-logo="https://logo.doube.eu.org/非凡新聞.png" group-title="新聞",非凡新聞', 'rtmp://f13h.mine.nu/sat/tv581', '#EXTINF:-1 tvg-id="台視財經台" tvg-name="台視財經台" tvg-logo="https://logo.doube.eu.org/台視財經台.png" group-title="新聞",台視財經', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv056,1,2', '#EXTINF:-1 tvg-id="台視新聞台" tvg-name="台視新聞台" tvg-logo="https://logo.doube.eu.org/台視新聞台.png" group-title="新聞",台視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv051,1,2', '#EXTINF:-1 tvg-id="台視新聞台" tvg-name="台視新聞台" tvg-logo="https://logo.doube.eu.org/台視新聞台.png" group-title="新聞",台視新聞', 'https://www.youtube.com/watch?v=xL0ch83RAK8', '#EXTINF:-1 tvg-id="中視新聞台" tvg-name="中視新聞台" tvg-logo="https://logo.doube.eu.org/中視新聞台.png" group-title="新聞",中視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv074,1,2', '#EXTINF:-1 tvg-id="中視新聞台" tvg-name="中視新聞台" tvg-logo="https://logo.doube.eu.org/中視新聞台.png" group-title="新聞",中視新聞', 'https://www.youtube.com/watch?v=TCnaIE_SAtM', '#EXTINF:-1 tvg-id="華視新聞" tvg-name="華視新聞" tvg-logo="https://logo.doube.eu.org/華視新聞.png" group-title="新聞",華視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv052,1,2', '#EXTINF:-1 tvg-id="華視新聞" tvg-name="華視新聞" tvg-logo="https://logo.doube.eu.org/華視新聞.png" group-title="新聞",華視新聞', 'https://www.youtube.com/watch?v=wM0g8EoUZ_E', '#EXTINF:-1 tvg-id="民視新聞台" tvg-name="民視新聞台" tvg-logo="https://logo.doube.eu.org/民視新聞台.png" group-title="新聞",民視新聞台', 'https://www.youtube.com/watch?v=ylYJSBUgaMA', '#EXTINF:-1 tvg-id="民視新聞台" tvg-name="民視新聞台" tvg-logo="https://logo.doube.eu.org/民視新聞台.png" group-title="新聞",民視新聞台', 'http://4gtv.mumi.rip:9877/31/litv-ftv13/index.m3u8', '#EXTINF:-1 tvg-id="民視新聞台" tvg-name="民視新聞台" tvg-logo="https://logo.doube.eu.org/民視新聞台.png" group-title="新聞",民視新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv13,1,7', '#EXTINF:-1 tvg-id="中天新聞" tvg-name="中天新聞" tvg-logo="https://logo.doube.eu.org/中天新聞.png" group-title="新聞",中天新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv009,2,7', '#EXTINF:-1 tvg-id="中天新聞" tvg-name="中天新聞" tvg-logo="https://logo.doube.eu.org/中天新聞.png" group-title="新聞",中天新聞', 'https://www.youtube.com/watch?v=vr3XyVCR4T0', '#EXTINF:-1 tvg-id="東森新聞台" tvg-name="東森新聞台" tvg-logo="https://logo.doube.eu.org/東森新聞台.png" group-title="新聞",東森新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv152,1,6', '#EXTINF:-1 tvg-id="東森新聞台" tvg-name="東森新聞台" tvg-logo="https://logo.doube.eu.org/東森新聞台.png" group-title="新聞",東森新聞', 'https://www.youtube.com/watch?v=V1p33hqPrUk', '#EXTINF:-1 tvg-id="TVBS新聞" tvg-name="TVBS新聞" tvg-logo="https://logo.doube.eu.org/TVBS新聞.png" group-title="新聞",Tvbs新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv072,1,2', '#EXTINF:-1 tvg-id="TVBS新聞" tvg-name="TVBS新聞" tvg-logo="https://logo.doube.eu.org/TVBS新聞.png" group-title="新聞",Tvbs新聞台', 'https://www.youtube.com/watch?v=m_dhMSvUCIc', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="新聞",Tvbs', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv073,1,2', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="新聞",Tvbs', 'http://4gtv.mumi.rip:9877/183/4gtv-4gtv073/index.m3u8', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="新聞",Tvbs', 'http://125.227.210.55:8188/VideoInput/play.ts', '#EXTINF:-1 tvg-id="寰宇新聞台" tvg-name="寰宇新聞台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台.png" group-title="新聞",寰宇新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn14,1,2', '#EXTINF:-1 tvg-id="寰宇新聞台" tvg-name="寰宇新聞台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台.png" group-title="新聞",寰宇新聞台', 'http://4gtv.mumi.rip:9877/36/litv-longturn14/index.m3u8', '#EXTINF:-1 tvg-id="寰宇新聞台" tvg-name="寰宇新聞台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台.png" group-title="新聞",寰宇新聞台', 'https://www.youtube.com/watch?v=6IquAgfvYmc', '#EXTINF:-1 tvg-id="寰宇新聞台灣台" tvg-name="寰宇新聞台灣台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台灣台.png" group-title="新聞",寰宇新聞台灣台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv156,1,6', '#EXTINF:-1 tvg-id="寰宇新聞台灣台" tvg-name="寰宇新聞台灣台" tvg-logo="https://logo.doube.eu.org/寰宇新聞台灣台.png" group-title="新聞",寰宇新聞台灣台', 'https://www.youtube.com/watch?v=w87VGpgd90U', '#EXTINF:-1 tvg-id="年代新聞台" tvg-name="年代新聞台" tvg-logo="https://logo.doube.eu.org/年代新聞台.png" group-title="新聞",年代新聞台', 'https://stream1.freetv.fun/28f2a175c45cd3d6885a0432398d36f149c45c516575d0da8a4312b445351c10.m3u8', '#EXTINF:-1 tvg-id="年代新聞台" tvg-name="年代新聞台" tvg-logo="https://logo.doube.eu.org/年代新聞台.png" group-title="新聞",年代新聞台', 'https://stream1.freetv.fun/be747d41b511a08679873d70f146d45d4c35c09256139e1a48dd9fdf20ac398b.m3u8', '#EXTINF:-1 tvg-id="鳳凰衛視資訊台" tvg-name="鳳凰衛視資訊台" tvg-logo="https://logo.doube.eu.org/鳳凰衛視資訊台.png" group-title="新聞",鳳凰衛視資訊台', 'https://www.youtube.com/watch?v=HFib76ySpbU', '#EXTINF:-1 tvg-id="鳳凰衛視資訊台" tvg-name="鳳凰衛視資訊台" tvg-logo="https://logo.doube.eu.org/鳳凰衛視資訊台.png" group-title="新聞",鳳凰衛視資訊台', 'http://php.jdshipin.com/TVOD/iptv.php?id=fhzx', '#EXTINF:-1 tvg-id="三立新聞" tvg-name="三立新聞" tvg-logo="https://logo.doube.eu.org/三立新聞.png" group-title="新聞",三立新聞', 'https://www.youtube.com/watch?v=MV9mI0GChwo', '#EXTINF:-1 tvg-id="三立新聞" tvg-name="三立新聞" tvg-logo="https://logo.doube.eu.org/三立新聞.png" group-title="新聞",三立新聞', 'http://4gtv.mumi.rip:9877/229/4gtv-live089/index.m3u8', '#EXTINF:-1 tvg-id="CCTV4" tvg-name="CCTV4" tvg-logo="https://logo.doube.eu.org/CCTV4.png" group-title="新聞",CCTV4', 'https://www.youtube.com/watch?v=SdzewdkJa-o', '#EXTINF:-1 tvg-id="TVBS歡樂台" tvg-name="TVBS歡樂台" tvg-logo="https://logo.doube.eu.org/TVBS歡樂台.png" group-title="綜藝",Tvbs歡樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv068,1,7', '#EXTINF:-1 tvg-id="TVBS歡樂台" tvg-name="TVBS歡樂台" tvg-logo="https://logo.doube.eu.org/TVBS歡樂台.png" group-title="綜藝",Tvbs歡樂台', 'http://122.117.71.103:8531/http/220.130.87.218:8081/hls/65/807/ch017.m3u8', '#EXTINF:-1 tvg-id="民視綜藝台" tvg-name="民視綜藝台" tvg-logo="https://logo.doube.eu.org/民視綜藝台.png" group-title="綜藝",民視綜藝', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv004,1,8', '#EXTINF:-1 tvg-id="靖天日本台" tvg-name="靖天日本台" tvg-logo="https://logo.doube.eu.org/靖天日本台.png" group-title="綜藝",靖天日本台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv047,1,8', '#EXTINF:-1 tvg-id="緯來日本" tvg-name="緯來日本" tvg-logo="https://logo.doube.eu.org/緯來日本.png" group-title="綜藝",緯來日本', 'rtmp://9hv9.mine.nu/sat/tv771', '#EXTINF:-1 tvg-id="豬哥亮歌廳秀" tvg-name="豬哥亮歌廳秀" tvg-logo="https://logo.doube.eu.org/豬哥亮歌廳秀.png" group-title="綜藝",豬哥亮歌廳秀', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv006,1,9', '#EXTINF:-1 tvg-id="豬哥亮歌廳秀" tvg-name="豬哥亮歌廳秀" tvg-logo="https://logo.doube.eu.org/豬哥亮歌廳秀.png" group-title="綜藝",豬哥亮歌廳秀', 'http://4gtv.mumi.rip:9877/113/4gtv-4gtv006/index.m3u8', '#EXTINF:-1 tvg-id="萬秀豬王" tvg-name="萬秀豬王" tvg-logo="https://logo.doube.eu.org/萬秀豬王.png" group-title="綜藝",萬秀豬王', 'https://www.youtube.com/watch?v=ADDSmXoPDY8', '#EXTINF:-1 tvg-id="大陸尋奇" tvg-name="大陸尋奇" tvg-logo="https://logo.doube.eu.org/大陸尋奇.png" group-title="綜藝",大陸尋奇', 'https://www.youtube.com/watch?v=UtOw97Ba8hE', '#EXTINF:-1 tvg-id="amc電影台" tvg-name="amc電影台" tvg-logo="https://logo.doube.eu.org/amc電影台.png" group-title="電影",amc電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv017,1,6', '#EXTINF:-1 tvg-id="靖天映畫" tvg-name="靖天映畫" tvg-logo="https://logo.doube.eu.org/靖天映畫.png" group-title="電影",靖天映畫', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv055,1,8', '#EXTINF:-1 tvg-id="靖天電影台" tvg-name="靖天電影台" tvg-logo="https://logo.doube.eu.org/靖天電影台.png" group-title="電影",靖天電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv061,1,7', '#EXTINF:-1 tvg-id="龍華洋片台" tvg-name="龍華洋片台" tvg-logo="https://logo.doube.eu.org/龍華洋片台.png" group-title="電影",龍華洋片', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn02,5,2', '#EXTINF:-1 tvg-id="amc電影台" tvg-name="amc電影台" tvg-logo="https://logo.doube.eu.org/amc電影台.png" group-title="電影",amc電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv017,1,6', '#EXTINF:-1 tvg-id="HBO HD" tvg-name="HBO HD" tvg-logo="https://logo.doube.eu.org/HBO HD.png" group-title="電影",HBO HD', 'http://122.117.71.103:8556/http/61.222.53.250:8081/hls/71/813/ch41.m3u8', '#EXTINF:-1 tvg-id="靖天映畫" tvg-name="靖天映畫" tvg-logo="https://logo.doube.eu.org/靖天映畫.png" group-title="電影",靖天映畫', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv055,1,8', '#EXTINF:-1 tvg-id="靖天電影台" tvg-name="靖天電影台" tvg-logo="https://logo.doube.eu.org/靖天電影台.png" group-title="電影",靖天電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv061,1,7', '#EXTINF:-1 tvg-id="龍華洋片台" tvg-name="龍華洋片台" tvg-logo="https://logo.doube.eu.org/龍華洋片台.png" group-title="電影",龍華洋片', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn02,5,2', '#EXTINF:-1 tvg-id="博斯魅力" tvg-name="博斯魅力" tvg-logo="https://logo.doube.eu.org/博斯魅力.png" group-title="體育",博斯魅力', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn04,5,2', '#EXTINF:-1 tvg-id="博斯高球1" tvg-name="博斯高球1" tvg-logo="https://logo.doube.eu.org/博斯高球1.png" group-title="體育",博斯高球1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn05,5,2', '#EXTINF:-1 tvg-id="博斯高球2" tvg-name="博斯高球2" tvg-logo="https://logo.doube.eu.org/博斯高球2.png" group-title="體育",博斯高球2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn06,5,2', '#EXTINF:-1 tvg-id="博斯運動1" tvg-name="博斯運動1" tvg-logo="https://logo.doube.eu.org/博斯運動1.png" group-title="體育",博斯運動1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn07,5,2', '#EXTINF:-1 tvg-id="博斯運動2" tvg-name="博斯運動2" tvg-logo="https://logo.doube.eu.org/博斯運動2.png" group-title="體育",博斯運動2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn08,5,2', '#EXTINF:-1 tvg-id="博斯網球1" tvg-name="博斯網球1" tvg-logo="https://logo.doube.eu.org/博斯網球1.png" group-title="體育",博斯網球', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn09,5,2', '#EXTINF:-1 tvg-id="博斯無限1" tvg-name="博斯無限1" tvg-logo="https://logo.doube.eu.org/博斯無限1.png" group-title="體育",博斯無限', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn10,5,2', '#EXTINF:-1 tvg-id="博斯無限2" tvg-name="博斯無限2" tvg-logo="https://logo.doube.eu.org/博斯無限2.png" group-title="體育",博斯無限2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn13,4,2', '#EXTINF:-1 tvg-id="緯來體育台" tvg-name="緯來體育台" tvg-logo="https://logo.doube.eu.org/緯來體育台.png" group-title="體育",緯來體育台', 'rtmp://9hv9.mine.nu/sat/tv721', '#EXTINF:-1 tvg-id="緯來體育台" tvg-name="緯來體育台" tvg-logo="https://logo.doube.eu.org/緯來體育台.png" group-title="體育",緯來體育台', 'rtmp://f13h.mine.nu/sat/tv721', '#EXTINF:-1 tvg-id="Love Nrture" tvg-name="Love Nrture" tvg-logo="https://logo.doube.eu.org/Love Nrture.png" group-title="探索",Love Nrture', 'https://d18dyiwu97wm6q.cloudfront.net/playlist720p.m3u8', '#EXTINF:-1 tvg-id="亞洲旅遊台" tvg-name="亞洲旅遊台" tvg-logo="https://logo.doube.eu.org/亞洲旅遊台.png" group-title="探索",亞洲旅遊台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv076,1,2', '#EXTINF:-1 tvg-id="民視影劇台" tvg-name="民視影劇台" tvg-logo="https://logo.doube.eu.org/民視影劇台.png" group-title="戲劇",民視影劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv09,1,2', '#EXTINF:-1 tvg-id="台灣戲劇台" tvg-name="台灣戲劇台" tvg-logo="https://logo.doube.eu.org/台灣戲劇台.png" group-title="戲劇",台灣戲劇台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn22,5,2', '#EXTINF:-1 tvg-id="全球時尚 Global Fashion " tvg-name="全球時尚 Global Fashion " tvg-logo="https://logo.doube.eu.org/全球時尚.png" group-title="時尚",全球時尚 Global Fashion ', 'https://pubgfc.teleosmedia.com/linear/globalfashionchannel/globalfashionchannel/playlist.m3u8', '#EXTINF:-1 tvg-id="法國時尚" tvg-name="法國時尚" tvg-logo="https://logo.doube.eu.org/法國時尚.png" group-title="時尚",法國時尚', 'http://lb.streaming.sk/fashiontv/stream/chunklist.m3u8', '#EXTINF:-1 tvg-id="Fashion TV HD" tvg-name="Fashion TV HD" tvg-logo="https://logo.doube.eu.org/FashionTVHD.png" group-title="時尚",Fashion TV HD', 'https://fashiontv-fashiontv-1-eu.rakuten.wurl.tv/playlist.m3u8']

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
