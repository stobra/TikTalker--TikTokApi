# %%
from time import sleep
from TikTalker import TikTokApi 
import autoJ as aj 
from pandas import DataFrame

driverlocation = r"C:\ProgramData\Python\Chromedrivers\chromedriver_85.exe"
# api =TikTokApi(debug=True, executablePath=driverlocation)
api =TikTokApi(debug=True)
# d = api.discoverMusic()
# print(d)
# sleep(2)
# %%
# print(u) 
# print(u.keys()) 
# udf = DataFrame([u['userInfo']['user']])
# print(udf)

# for i in u['userInfo']['user']:
#     print(i, u['userInfo']['user'][i])
# sleep(2)

# %%
users = api.getSuggestedUsersbyIDCrawler(count=2, startingId='6880621118412653573', language='en', proxy=None)
print(users)
for i in users:
    print(i)
# %%
# t = api.trending()
# # print(t)
# ta = aj.parse_json(t)
# print(ta.df)
# %%

# d = {'statusCode': 0, 'userInfo': {'user': {'id': '6880621118412653573', 'uniqueId': 'stobra', 'nickname': 'bradyston', 'avatarThumb': 'https://sf16-muse-va.ibytedtos.com/obj/tiktok-obj/1613746256880653', 'avatarMedium': 'https://sf16-muse-va.ibytedtos.com/obj/tiktok-obj/1613746256880653', 'avatarLarger': 'https://sf16-muse-va.ibytedtos.com/obj/tiktok-obj/1613746256880653', 'signature': '', 'verified': False, 'secUid': 'MS4wLjABAAAAor4ugcXglxkM3p9B9mxB9-HG98xPndiV5DYvQ7YJrF5K-E6s664ocWqUNueTEauJ', 'secret': False, 'ftc': False, 'relation': 0, 'openFavorite': False, 'commentSetting': 0, 'duetSetting': 0, 'stitchSetting': 0, 'privateAccount': False}, 'stats': {'followingCount': 1, 'followerCount': 0, 'heartCount': 0, 'videoCount': 0, 'diggCount': 0, 'heart': 0}, 'shareMeta': {'title': 'bradyston on TikTok', 'desc': '@stobra 0 Followers, 1 Following, 0 Likes - Watch awesome short videos created by bradyston'}}} 
# d['userInfo']
# %%
import asyncio
from proxybroker import Broker
# %%
async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        print('Found proxy: %s' % proxy)

proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTP', 'HTTPS'], limit=1),
    show(proxies))

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)


# %%
