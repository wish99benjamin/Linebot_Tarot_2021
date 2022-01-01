definition = {
    "type": "bubble",
    "size": "kilo",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "text",
                "size": "md",
                "wrap": True
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "介紹與說明",
                    "text": "功能介紹與說明"
                }
            }
        ]
    }
}

notice = {
  "type": "bubble",
  "size": "kilo",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/s2EDHNX.jpg",
    "aspectMode": "cover",
    "gravity": "center",
    "align": "center",
    "size": "5xl"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "塔羅牌占卜注意事項⭐",
        "style": "normal",
        "weight": "bold",
        "margin": "md",
        "size": "md"
      },
      {
        "type": "text",
        "text": "1. 同一個問題，一天只能問一次",
        "wrap": True
      },
      {
        "type": "text",
        "text": "2. 問的問題答案必須是\"要\"或\"不要\"，\"可以\"或\"不可以\"",
        "wrap": True
      },
      {
        "type": "text",
        "text": "3. 占卜的時候盡量讓心情保持在一種愉快的狀況下，如果事情很急，不妨先深呼吸幾次，再開始占卜喔",
        "wrap": True
      },
      {
        "type": "text",
        "text": "4. 算牌指示給一個建議，任何事情還是要靠自己來做或是認真面對",
        "wrap": True
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回首頁",
          "text": "返回首頁"
        }
      }
    ]
  }
}