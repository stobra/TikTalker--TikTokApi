# %%
from time import sleep
from TikTok import TikTokApi 
import autoJ as aj 
from pandas import DataFrame


api =TikTokApi(debug=True)
# d = api.discoverMusic()
# print(d)

# %%
# print(u) 
# print(u.keys()) 
# udf = DataFrame([u['userInfo']['user']])
# print(udf)

# for i in u['userInfo']['user']:
#     print(i, u['userInfo']['user'][i])
# sleep(2)

# %%
users = api.getSuggestedUsersbyIDCrawler(count=4, startingId='6880621118412653573', language='en', proxy=None)
print(users)
for i in users:
    print(i)
# %%
# t = api.trending()
# # print(t)
# ta = aj.parse_json(t)
# print(ta.df)
# %%
