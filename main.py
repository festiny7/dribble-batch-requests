import requests


headers = {
    "Host": "dribbble.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "X-NewRelic-ID": "VQEAWVVACgoAXVVXBQ==",
    "X-CSRF-Token": "kzkOVCkayzvJ9esVhHTE3J4HRujnBP2PljNIcx33gZEWZ/sq5r64f/Q2r1tYuV4zlq76mi/XJoMbfewtAAH3bw==",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": "Windows",
    "Origin": "https://dribbble.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://dribbble.com/",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": '_sp_ses.bdb9=*; _vwo_uuid_v2=D540ABB7EB2578DF214C45B36ED3C2A54|95d8c3e089dc732bec64e971b2d257b9; _gcl_au=1.1.1202695003.1657562585; _ga=GA1.2.1380608552.1657562585; _gid=GA1.2.704271447.1657562585; amplitudeSessionId=1657562584181; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D540ABB7EB2578DF214C45B36ED3C2A54; _vwo_ds=3%241657562585%3A17.13361123%3A%3A; __ssid=0d1b911ff140f06389ebc07cbd8282e; g_state={"i_p":1657569790012,"i_l":1}; user_session_token=f3d6d9a9-648a-4486-a5cb-5778327eed2c; has_logged_in=true; _gat_gtag_UA_161659550_1=1; _gat_gtag_UA_42885094_2=1; _gat_gtag_UA_42885094_5=1; __stripe_sid=4d0e5f20-a31c-4382-8fec-5ba57f8f834cb6bdcd; __stripe_mid=963a0777-5dde-45fd-9451-14b5000f7bf4e022de; _sp_id.bdb9=5b6e018e-9512-412d-a8f1-ab6f8cf4e38a.1657562584.1.1657562653.1657562584.db554b6a-5950-4f0b-bc34-6d6b3a641077; _vwo_sn=0%3A5; amp_2cb22d=WbeEAIr70AnIwuihcdZIQn.MTI0MTM0ODc=..1g7n6rl3l.1g7n6tns5.c.4.g; _gat_gtag_UA_24041469_1=1; _dribbble_session=NjFIMkNKRlAxTTN2OVpMTzFaRDdiT0tJQjVuZzVzQ0N6SFBXNHpwZmdiNFVYV2dpR2lnUkZNamxXblV6VlpsNDF3aWFJRDdYRlppSmpDMDA4TE83a2dTdkpUN3Z6dkFDVHp4VUFSbW5DbEt6RCt3ZkFnTXpaY0ZVcFlnZzJlczFWaFRIWUh2dktSMmJwUWwyYzRGMCt0NmlQZU5pamQ5Q0pRZDB5NVd4M1B3V3VRMWRHSlM3SzIvZFRLSFB5ZkpyNDJVWnQwcW8ya1lPaWZGSkZGbUFJM0NXd3o4UlZOTjhCYXBJT2tUTTQ2QT0tLVMxb0JpNVBsZTB1cEQzSFZ6Q0dDdUE9PQ%3D%3D--c8175e1b9c554f767b571f69c1cd47951f4fee89',
    "Accept-Encoding": "gzip, deflate",
}


def dribble_like():
    import httpx

    id = "18920092"  # Account ID
    requests = httpx.post(
        "https://dribbble.com/Akhil07/likes?modal=false&on_hover=true&screenshot_id="
        + id,
        headers=headers,
        verify=False,
    )
    print(requests.text)


# dribble_like()


def dribble_save():
    import requests

    post_link = "https://dribbble.com/shots/18914294-Mater-Logo"
    a = post_link.split("/")
    b = a[4]
    b = b.split("-")
    c = b[0]
    print(c)
    headers = {
        "Host": "dribbble.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "X-NewRelic-ID": "VQEAWVVACgoAXVVXBQ==",
        "X-CSRF-Token": "FqmwYOTHcg3KN2p82imzoeA6AaLNdDRchn4c4dt5LGaT90UeK2MBSff0LjIG5ClO6JO90AWn71ALMLi/xo9amA==",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-platform": "Windows",
        "Origin": "https://dribbble.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": post_link,
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": '_sp_ses.bdb9=*; _vwo_uuid_v2=D540ABB7EB2578DF214C45B36ED3C2A54|95d8c3e089dc732bec64e971b2d257b9; _gcl_au=1.1.1202695003.1657562585; _ga=GA1.2.1380608552.1657562585; _gid=GA1.2.704271447.1657562585; amplitudeSessionId=1657562584181; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D540ABB7EB2578DF214C45B36ED3C2A54; _vwo_ds=3%241657562585%3A17.13361123%3A%3A; __ssid=0d1b911ff140f06389ebc07cbd8282e; g_state={"i_p":1657569790012,"i_l":1}; user_session_token=f3d6d9a9-648a-4486-a5cb-5778327eed2c; has_logged_in=true; __stripe_sid=4d0e5f20-a31c-4382-8fec-5ba57f8f834cb6bdcd; __stripe_mid=963a0777-5dde-45fd-9451-14b5000f7bf4e022de; _gat_gtag_UA_24041469_1=1; _sp_id.bdb9=5b6e018e-9512-412d-a8f1-ab6f8cf4e38a.1657562584.1.1657563022.1657562584.db554b6a-5950-4f0b-bc34-6d6b3a641077; amp_2cb22d=WbeEAIr70AnIwuihcdZIQn.MTI0MTM0ODc=..1g7n6rl3l.1g7n790du.n.c.13; _vwo_sn=0%3A13; _dribbble_session=RmdOWHVVNHhpQ2FpQU42akdpRGxBVlhlZk4xa0o4SUtyTlJaUS9HdDlvSEFGRlVpRDJTR2FWaW5tKzRFMEhGb0NLalJqSThHc0YzQ3BmcjZJZmNkazdqbnBCWHhoMVVqcHUvU0U3V1VnTFR5bHVsWGxsajQ1QWFnTGxlKzExbXBIRThBUSt1R21jSTlQS0NiaTRpQUhoS3k4dDlSVDE3OTRVNVh2a3JKRFZSLzlucFFSREdqdjltQWtySllEUzd4TjRFRkZNOFlrMUk5QWJTTGQzWTltM201b00zN2hlOVI5QWtMWjFPQUNvWT0tLXV0TkVSdXdkRDVLb3N6bWFsL1VDM1E9PQ%3D%3D--99ddde270f760b7df5f713982f6eb4937df34b45',
        "Accept-Encoding": "gzip, deflate",
    }

    payload = "bucket_id=5834847&screenshot_id=" + c
    requests = requests.post(
        post_link + "/bucketings", headers=headers, data=payload, verify=False
    )
    # payload2="bucket_id=5834829&screenshot_id="+c
    print(requests.text)


# dribble_save()


def dribble_follower():
    import httpx

    # user_link ="https://dribbble.com/"
    """headers = {"Host": "dribbble.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "X-NewRelic-ID": "VQEAWVVACgoAXVVXBQ==",
    "X-CSRF-Token": "M/7QMIFrfOke/onF2f/cHz/QA7G3ff6tUtpY5jjsCYS2oCVOTs8PrSM9zYsFMkbwN3m/w3+uJaHflPy4JRp/eg==",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": "Windows",
    "Origin": "https://dribbble.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": follow,
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": '_sp_ses.bdb9=*; _vwo_uuid_v2=D540ABB7EB2578DF214C45B36ED3C2A54|95d8c3e089dc732bec64e971b2d257b9; _gcl_au=1.1.1202695003.1657562585; _ga=GA1.2.1380608552.1657562585; _gid=GA1.2.704271447.1657562585; amplitudeSessionId=1657562584181; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D540ABB7EB2578DF214C45B36ED3C2A54; _vwo_ds=3%241657562585%3A17.13361123%3A%3A; __ssid=0d1b911ff140f06389ebc07cbd8282e; g_state={"i_p":1657569790012,"i_l":1}; user_session_token=f3d6d9a9-648a-4486-a5cb-5778327eed2c; has_logged_in=true; __stripe_sid=4d0e5f20-a31c-4382-8fec-5ba57f8f834cb6bdcd; __stripe_mid=963a0777-5dde-45fd-9451-14b5000f7bf4e022de; _dribbble_session=OUNzRGRLOWtycWNpaUlYTkZSc0hhdFg2VmV5ZUJzZ29kZWVyTFllYXB4UjlkS1lRc3FZckVOM3AwYk5rWXlFRlRnYjVwZk8xOE9NVHVZc0Iwb2FvWEZwWi9zK3JlQXRYdUVzMk5wamdObWFkeVJ3RGxOWlNpdFpvYnpvU2VESnhKSS9NZ0FyWGoyRTNiVzVVOWtlSmczalYvdkNBaytXYmtBV1plWkFRVHFhWXhEUU1KTkU4bnJNdXZYKzFaN0xjOU95QWRqdjV6cGcrSnk5T21XUTMzMWxpTWwrbUlyRXNwelV3dHFlVmpZUT0tLXNtQXhFS28xM3FQbG1JMDB1eGlUNVE9PQ%3D%3D--48c1b9fc4e3f32848436c6209832378e802f9707; _sp_id.bdb9=5b6e018e-9512-412d-a8f1-ab6f8cf4e38a.1657562584.1.1657565122.1657562584.db554b6a-5950-4f0b-bc34-6d6b3a641077; amp_2cb22d=WbeEAIr70AnIwuihcdZIQn.MTI0MTM0ODc=..1g7n6rl3l.1g7n9931u.1k.15.2p; _gat_gtag_UA_24041469_1=1; _gat_gtag_UA_161659550_1=1; _vwo_sn=2467%3A5',
    "Accept-Encoding": "gzip, deflate",
    }"""
    # usernames = ["kettle_studio","purrwebui","Obtic","marcato","theosm","musemindagency","Offdesignarea","kazierfan","dexignstudio","Echodesign","mousepotatolab","purrwebui","muhammadzaini","7ahang","Jahid621","oneandzeros","anastasia-tino","Samsad","properlystudio","flexyglobal","shakuro","ui_migulko","teamfluttertop","Khester"]
    # usernames = ["ibm-design","oniex","sebiat","OWWStudio","sollers","brander_agency","teamfluttertop","ana_insomnia","thedigitalpanda","lets_draw_letters","Kkopteva","Fireart-d","roryjsnow","DSpot","manifold_group","and__studio","redmadrobot","y_kashley","Chokun","gui_paulino"]
    # usernames = ["halolab","YevdokimovKirill","rokasaleliunas","RomainTrystram","bradhansen","Mousumi_akter","Type08","ethnfndr","coric_design","mockupcloud","marcelohoff","outer","rokasaleliunas","mrmockup","Xavier_Gomez","pat_kos","mockupcloud","mrmockup","katezest","Irina_Skaska","camilociprian","pommes","Michael-Driver","camilociprian"]
    # usernames = ["Mousumi_akter","nextmahamud","seanbrice","roberlan","Mousumi_akter","armagraphico","MoralLaurel","ana_insomnia","zzoeiggi","heykyle","NewhouseDesigns","heykyle","rick","coreydgeorge","wellscollins","amdadali17","coreydgeorge","NickBAbrams","GVeleski","karynje","MatthewBird","vectortshirt81","gui_paulino",]
    # usernames = ["alisha_design","emon_pixels","OWWStudio","kettle_studio","Orizon","nikoloznarsia","halolab","vaneltia","Duxica","YevdokimovKirill","dipainhouse","Folio","odamastudio","twintrick","mrstudio","aceagency","sandrojalabadze","Ramotion","vektora","aceagency","onixlab","Riyamoni","sajon","kretyastudio"]
    # for i in usernames:
    # follow = user_link+i
    headers = {
        "Host": "dribbble.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "X-NewRelic-ID": "VQEAWVVACgoAXVVXBQ==",
        "X-CSRF-Token": "M/7QMIFrfOke/onF2f/cHz/QA7G3ff6tUtpY5jjsCYS2oCVOTs8PrSM9zYsFMkbwN3m/w3+uJaHflPy4JRp/eg==",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-platform": "Windows",
        "Origin": "https://dribbble.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://dribbble.com/dmkers",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": '_sp_ses.bdb9=*; _vwo_uuid_v2=D540ABB7EB2578DF214C45B36ED3C2A54|95d8c3e089dc732bec64e971b2d257b9; _gcl_au=1.1.1202695003.1657562585; _ga=GA1.2.1380608552.1657562585; _gid=GA1.2.704271447.1657562585; amplitudeSessionId=1657562584181; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D540ABB7EB2578DF214C45B36ED3C2A54; _vwo_ds=3%241657562585%3A17.13361123%3A%3A; __ssid=0d1b911ff140f06389ebc07cbd8282e; g_state={"i_p":1657569790012,"i_l":1}; user_session_token=f3d6d9a9-648a-4486-a5cb-5778327eed2c; has_logged_in=true; __stripe_sid=4d0e5f20-a31c-4382-8fec-5ba57f8f834cb6bdcd; __stripe_mid=963a0777-5dde-45fd-9451-14b5000f7bf4e022de; _dribbble_session=OUNzRGRLOWtycWNpaUlYTkZSc0hhdFg2VmV5ZUJzZ29kZWVyTFllYXB4UjlkS1lRc3FZckVOM3AwYk5rWXlFRlRnYjVwZk8xOE9NVHVZc0Iwb2FvWEZwWi9zK3JlQXRYdUVzMk5wamdObWFkeVJ3RGxOWlNpdFpvYnpvU2VESnhKSS9NZ0FyWGoyRTNiVzVVOWtlSmczalYvdkNBaytXYmtBV1plWkFRVHFhWXhEUU1KTkU4bnJNdXZYKzFaN0xjOU95QWRqdjV6cGcrSnk5T21XUTMzMWxpTWwrbUlyRXNwelV3dHFlVmpZUT0tLXNtQXhFS28xM3FQbG1JMDB1eGlUNVE9PQ%3D%3D--48c1b9fc4e3f32848436c6209832378e802f9707; _sp_id.bdb9=5b6e018e-9512-412d-a8f1-ab6f8cf4e38a.1657562584.1.1657565122.1657562584.db554b6a-5950-4f0b-bc34-6d6b3a641077; amp_2cb22d=WbeEAIr70AnIwuihcdZIQn.MTI0MTM0ODc=..1g7n6rl3l.1g7n9931u.1k.15.2p; _gat_gtag_UA_24041469_1=1; _gat_gtag_UA_161659550_1=1; _vwo_sn=2467%3A5',
        "Accept-Encoding": "gzip, deflate",
    }
    requests = httpx.post(
        "https://dribbble.com/dmkers/followers", headers=headers, verify=False
    )
    print(requests.text)


# dribble_follower()


def dribble_views():
    import requests

    headers = {
        "Host": "dribbble.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://dribbble.com/search/ali",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": '_vwo_uuid_v2=D540ABB7EB2578DF214C45B36ED3C2A54|95d8c3e089dc732bec64e971b2d257b9; _gcl_au=1.1.1202695003.1657562585; _ga=GA1.2.1380608552.1657562585; _vwo_ds=3%241657562585%3A17.13361123%3A%3A; _vwo_uuid=D540ABB7EB2578DF214C45B36ED3C2A54; __ssid=0d1b911ff140f06389ebc07cbd8282e; g_state={"i_p":1657569790012,"i_l":1}; user_session_token=f3d6d9a9-648a-4486-a5cb-5778327eed2c; __stripe_mid=963a0777-5dde-45fd-9451-14b5000f7bf4e022de; _fbp=fb.1.1657565720766.1277296983; _clck=1orgzm5|1|f32|0; has_logged_in=true; _sp_ses.bdb9=*; _gid=GA1.2.239973062.1657736962; _vis_opt_s=2%7C; _vis_opt_test_cookie=1; amplitudeSessionId=1657736961861; __stripe_sid=80d67223-9a2a-4fce-abc5-a522cf411ad92d39e1; comments_sidebar_open=true; _uetsid=a7da8ba002da11ed88377fbd65ae7ea9; _uetvid=03379970014b11edae3c19987038471e; _hjSessionUser_2376661=eyJpZCI6Ijc0YTY4Zjg1LWMyNzItNTZkMi04YTNmLTY3NzUxZWJkNWMxZCIsImNyZWF0ZWQiOjE2NTc1NjU3MjEyMjUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_2376661=eyJpZCI6IjJhODE2MjljLTVjOGItNGRmNy1hZmYwLWZiMTJhNjYwZmQ2MiIsImNyZWF0ZWQiOjE2NTc3MzczNjY0MDYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _gat_gtag_UA_219538969_2=1; _gat_gtag_UA_161192219_1=1; _gat_gtag_UA_125456571_2=1; _gat_gtag_UA_54377582_1=1; _gat_gtag_UA_219538969_1=1; _vwo_sn=174377%3A39; amp_2cb22d=WbeEAIr70AnIwuihcdZIQn.MTI0MTM0ODc=..1g7sd57q5.1g7sdllce.62.3t.9v; _sp_id.bdb9=5b6e018e-9512-412d-a8f1-ab6f8cf4e38a.1657562584.3.1657737501.1657632263.3487c144-649a-4940-9f00-ebf1f85bdec6; _dribbble_session=RlM0Mmh3Yk8yQnUvR1B0OVRiRDJLd1QraVYzRnM3cFFydmNMZTFwTWRaeXlyUDNQWXd6Q3NEN1lxTWJJamRTM1k3ajEyODVGcEFJVDRtdVlNbmUrK3BuQXlTYU5rMGtqKzhlSlA5aHNuYlYxeVVJNVRXVUhvcWV3bWhjMFVZaWF3WVZmSjdrMU5RSC9tTW1rU09BN09UcjNtQTgrZkowU3dYYWFXbVdKTFBrb2UzZGhPZE1hNDYxZDZQTzZQWUxuTTM4TmtNSEhOcmRnWE52eXJxWGZ4WStIQVBiK3VnODNUYWczbnllTzdraz0tLUZsSmFOdm05VjN2UjYzVDE2WFdUR3c9PQ%3D%3D--5329dc5f7998d6c5f130b7c974373c9ab0ff9e7a',
        "If-None-Match": 'W/"c8280163d7936cc2c6f412e20ec9d566"',
        "Accept-Encoding": "gzip, deflate",
    }

    requests = requests.get(
        "https://dribbble.com/shots/5580623-Ali-Identity", headers=headers, verify=False
    )
    print(requests.text)

    for i in range(100):
        requests = requests.get(
            "https://dribbble.com/shots/5253855-Ali-s", headers=headers, verify=False
        )
        print(requests.text)
        print("request sent")


# dribble_views()
