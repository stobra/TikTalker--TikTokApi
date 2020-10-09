from TikTok import TikTokApi
# from TikTokApi import TikTokApi

def test_trending():
    api = TikTokApi()
    assert abs(len(api.byUsername('therock', 5))-5) <= 2
    assert abs(len(api.byUsername('therock', 10))-10) <= 2
    assert abs(len(api.byUsername('therock', 20))-20) <= 2

if __name__ == "__main__":
    api = TikTokApi()
    t = api.byUsername('therock', 5)
    print(t)
    # test_trending()