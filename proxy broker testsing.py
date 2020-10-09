# %%
from TikTok import TikTokApi 
import autoJ as aj 
from pandas import DataFrame
from time import sleep
import asyncio
from proxybroker import Broker
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

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
# api =TikTokApi(debug=True)
# d = api.discoverMusic()
# users = api.getSuggestedUsersbyIDCrawler(count=2, startingId='6880621118412653573', language='en', proxy=None)
# print(users)
# for i in users:
#     print(i)
