```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./users.py --urlname=info
```

```console
$ ./users.py --urlname=info
{
  "data": {
    "id": 120,
    "nickname": "note公式",
    "urlname": "info",
    "note_count": 1210,
    "magazine_count": 14,
    "following_count": 2189,
    "follower_count": 2126306,
    "draft_count": 44,
    "profile": "ミッションは、「だれもが創作をはじめ、続けられるようにする」こと。noteの最新情報や機能カイゼンを紹介していきます。 noteにまつわるヒトの紹介 : https://note.com/notemag |noteのイベント情報 : https://note.com/events",
    "tokusyo_name": "株式会社ピースオブケイク",
    "tokusyo_contact": "support@note.mu",
    "user_profile_image_path": "https://d2l930y2yx77uc.cloudfront.net/production/uploads/images/22397911/profile_79013990336380788a6d4d07701f0df8.png",
    "user_wallpaper_image_path": "https://d2l930y2yx77uc.cloudfront.net/assets/default/default_magazine_cover-e7f150c27242f5bccfd0ce8a8319ab917b5d70115029f84000502d8ae5ae4c73.png",
    "is_me": false,
    "is_following": false,
    "is_blocked": false,
    "tweet_text": "note公式｜note（ノート）",
    "is_official": true,
    "no_urlname_user": false,
    "point_balance": 0,
    "custom_domain": null,
    "authentications": {
      "twitter": {
        "provider": "twitter",
        "uid": "2426595726",
        "name": "note",
        "nickname": "note_PR"
      }
    }
  }
}
```
