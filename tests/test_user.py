from TikTok import TikTokApi
from time import sleep

def test_user():
    api = TikTokApi()

    assert api.getUser('charlidamelio')['userInfo']['user']['uniqueId'] == 'charlidamelio'
    sleep(1)
    assert api.getUserObject('charlidamelio')['uniqueId'] == 'charlidamelio'
    sleep(1)
    assert abs(len(api.userPosts(userID="5058536", secUID="MS4wLjABAAAAoRsCq3Yj6BtSKBCQ4rf3WQYxIaxe5VetwJfYzW_U5K8", count=5))-5) <= 1
    sleep(1)
    assert abs(len(api.userPosts(userID="5058536", secUID="MS4wLjABAAAAoRsCq3Yj6BtSKBCQ4rf3WQYxIaxe5VetwJfYzW_U5K8", count=10))-10) <= 1
    sleep(1)
    assert abs(len(api.userPosts(userID="5058536", secUID="MS4wLjABAAAAoRsCq3Yj6BtSKBCQ4rf3WQYxIaxe5VetwJfYzW_U5K8", count=30))-30) <= 1

    # assert len(api.userLikedbyUsername(username="", count=30)) == 30

# api = TikTokApi()
# t = api.getUser('charlidamelio')
# print(t)
# print(t['userInfo']['user'])