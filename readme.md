# TOC Project 2021 - Tarot ChatBot

### 功能說明
利用chatbot進行塔羅牌占卜，目前提供學業、人際、健康、七天運勢和其他類五種占卜方向，除了七天運勢外的項目可選擇要使用一張牌(簡易法)和三張牌(標準法)來進行占卜，占卜所使用的牌組為基本22張大秘儀

### 資料取得
五大類占卜結果是從我本身在用的工具書和長年占卜的經驗中得出"較為精簡"的結果，若是使用者想更了解每張牌的內容及含意，亦能點選觀看更多牌義，查看經驗更豐富的占卜師在網路上所分享的結果(利用爬蟲)，另外，占卜過程所使用到的塔羅牌皆是由我手工繪製

### 使用技術
1. python
2. linechatbot api
3. web crawling
4. deploy(Heroku)
5. multiple users

### 使用版本
- python == 3.6.9
- pandas == 1.1.5
- BeatifulSoup4 == 4.10.0

### FSM
![fsm](./img/show-fsm.png)

### 使用畫面截圖
![](./img/result_1.jpg)
![](./img/result_2.jpg)
![](./img/result_3.jpg)
![](./img/result_4.jpg)
![](./img/result_5.jpg)
![](./img/result_6.jpg)

### Install pandas and bs4 on HEROKU
1. add pandas==(your pandas version) in requirements.txt
2. add pandas = "==your pandas version" in Pipfile
3. same operation for bs4 (and other packages)
4. run pipenv install to renew Pipfile.lock
5. run git &rarr; add &rarr; commit &rarr; push again and verify your url on line developer

### Reference
TOC slides 2021(https://docs.google.com/presentation/d/1HSf3-m6_h9Uv2N_y9mgOG6fOho-bRhl0oInhHdC45ZU/edit#slide=id.g25a54d5e5a4faf37_26)
Install pandas on HEROKU(https://www.codenong.com/94e124b895399dea9c7d/)
Flex Message Tutorial(https://ithelp.ithome.com.tw/articles/10243334)
Flex Message Simulator(https://developers.line.biz/flex-simulator/?fbclid=IwAR3pc2iSGY3GLSZwBU55ooY3v-xSZQ8J3Wih8Z4K9Gux9LXfjxqsYJUzdMY)
Other notes(https://cloud-stone-4a6.notion.site/FINAL-PROJECT-daabd7ad551543d585a8dfaddef0885c)

### Repos for Chatbot
Line Fitness (https://github.com/aqwefghnm/LineChatBot)
Line Movie (https://github.com/lofoz/LineBot?fbclid=IwAR1rGyFue0UGdl4FA-gYUgFM0tKJrEAnq6-wgghuS5PTx6uaa6pMGvLAZa4)


