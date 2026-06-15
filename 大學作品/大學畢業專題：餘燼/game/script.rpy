# 遊戲腳本位於此檔案。

# 聲明該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define Xin = Character("蕭瑀昕", who_color='#554545')
define Jack = Character("傑克•米勒", who_color='#554545')
define Ling = Character("季玲", who_color='#554545')
define Shan = Character("謝呂珊", who_color='#554545')
define Ni = Character("洪芸妮", who_color='#554545')
define unknown = Character("???", who_color='#554545')
define boy = Character("蕭宇航", who_color='#554545')
define man00 = Character("???男生", who_color='#554545')
define woman00 = Character("???女生", who_color='#554545')


image xin_normal = Animation(
    "images/Character/xin/正常拆圖/男主正常_00000.png", 0.2,
    "images/Character/xin/正常拆圖/男主正常_00001.png", 0.2,
    "images/Character/xin/正常拆圖/男主正常_00002.png", 0.2,
    "images/Character/xin/正常拆圖/男主正常_00003.png", 0.2,
    "images/Character/xin/正常拆圖/男主正常_00004.png", 0.2,
    "images/Character/xin/正常拆圖/男主正常_00005.png", 0.2,
    "images/Character/xin/正常拆圖/男主正常_00006.png", 0.2,
    "images/Character/xin/正常拆圖/男主正常_00007.png", 0.2,
    "images/Character/xin/男主正常閉眼_00000.png", 0.2,
)



image xin_angry = Animation(
    "images/Character/xin/生氣/男主生氣mp4_00000.png", 0.2,
    "images/Character/xin/生氣/男主生氣mp4_00001.png", 0.2,
    "images/Character/xin/生氣/男主生氣mp4_00002.png", 0.2,
    "images/Character/xin/生氣/男主生氣mp4_00003.png", 0.2,
    "images/Character/xin/生氣/男主生氣mp4_00004.png", 0.2,
    "images/Character/xin/生氣/男主生氣mp4_00005.png", 0.2,
    "images/Character/xin/生氣/男主生氣mp4_00006.png", 0.2,
    "images/Character/xin/生氣/男主生氣mp4_00007.png", 0.2,
)


image xin_think = Animation(
    "images/Character/xin/思考/男主思考半身_00000.png", 0.2,
    "images/Character/xin/思考/男主思考半身_00001.png", 0.2,
    "images/Character/xin/思考/男主思考半身_00002.png", 0.2,
    "images/Character/xin/思考/男主思考半身_00003.png", 0.2,
    "images/Character/xin/思考/男主思考半身_00004.png", 0.2,
    "images/Character/xin/思考/男主思考半身_00005.png", 0.2,
    "images/Character/xin/思考/男主思考半身_00006.png", 0.2,
    "images/Character/xin/思考/男主思考半身_00007.png", 0.2,
    "images/Character/xin/男主思考半身閉眼_00000.png", 0.2,
)

image xin_dilemma = Animation(
    "images/Character/xin/為難/男主為難_00000.png", 0.2,
    "images/Character/xin/為難/男主為難_00001.png", 0.2,
    "images/Character/xin/為難/男主為難_00002.png", 0.2,
    "images/Character/xin/為難/男主為難_00003.png", 0.2,
    "images/Character/xin/為難/男主為難_00004.png", 0.2,
    "images/Character/xin/為難/男主為難_00005.png", 0.2,
    "images/Character/xin/為難/男主為難_00006.png", 0.2,
    "images/Character/xin/為難/男主為難_00007.png", 0.2,
)

image xin_s_smile = Animation(
    "images/Character/xin/僵硬微笑/男主僵硬微笑_00000.png", 0.2,
    "images/Character/xin/僵硬微笑/男主僵硬微笑_00001.png", 0.2,
    "images/Character/xin/僵硬微笑/男主僵硬微笑_00002.png", 0.2,
    "images/Character/xin/僵硬微笑/男主僵硬微笑_00003.png", 0.2,
    "images/Character/xin/僵硬微笑/男主僵硬微笑_00004.png", 0.2,
    "images/Character/xin/僵硬微笑/男主僵硬微笑_00005.png", 0.2,
    "images/Character/xin/僵硬微笑/男主僵硬微笑_00006.png", 0.2,
    "images/Character/xin/僵硬微笑/男主僵硬微笑_00007.png", 0.2,
)

image xin_afraid_plus = Animation(
    "images/Character/xin/驚恐/男主驚恐_00000.png", 0.2,
    "images/Character/xin/驚恐/男主驚恐_00001.png", 0.2,
    "images/Character/xin/驚恐/男主驚恐_00002.png", 0.2,
    "images/Character/xin/驚恐/男主驚恐_00003.png", 0.2,
    "images/Character/xin/驚恐/男主驚恐_00004.png", 0.2,
    "images/Character/xin/驚恐/男主驚恐_00005.png", 0.2,
    "images/Character/xin/驚恐/男主驚恐_00006.png", 0.2,
    "images/Character/xin/驚恐/男主驚恐_00007.png", 0.2,
)

image xin_pain = Animation(
    "images/Character/xin/痛苦/男主痛苦_00000.png", 0.2,
    "images/Character/xin/痛苦/男主痛苦_00001.png", 0.2,
    "images/Character/xin/痛苦/男主痛苦_00002.png", 0.2,
    "images/Character/xin/痛苦/男主痛苦_00003.png", 0.2,
    "images/Character/xin/痛苦/男主痛苦_00004.png", 0.2,
    "images/Character/xin/痛苦/男主痛苦_00005.png", 0.2,
    "images/Character/xin/痛苦/男主痛苦_00006.png", 0.2,
    "images/Character/xin/痛苦/男主痛苦_00007.png", 0.2,
)

image ni_normal = Animation(
    "images/Character/ni/洪芸妮正常/洪芸妮正常_00000.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮正常_00001.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮正常_00002.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮正常_00003.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮正常_00004.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮正常_00005.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮正常_00006.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮正常_00007.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮閉眼_00000.png", 0.2,
)

image ni_afraid = Animation(
    "images/Character/ni/洪芸妮害怕/洪芸妮害怕_00000.png", 0.2,
    "images/Character/ni/洪芸妮害怕/洪芸妮害怕_00001.png", 0.2,
    "images/Character/ni/洪芸妮害怕/洪芸妮害怕_00002.png", 0.2,
    "images/Character/ni/洪芸妮害怕/洪芸妮害怕_00003.png", 0.2,
    "images/Character/ni/洪芸妮害怕/洪芸妮害怕_00004.png", 0.2,
    "images/Character/ni/洪芸妮害怕/洪芸妮害怕_00005.png", 0.2,
    "images/Character/ni/洪芸妮害怕/洪芸妮害怕_00006.png", 0.2,
    "images/Character/ni/洪芸妮害怕/洪芸妮害怕_00007.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮閉眼_00000.png", 0.2,
)

image ni_angry = Animation(
    "images/Character/ni/洪芸妮憤怒/洪芸妮憤怒_00000.png", 0.2,
    "images/Character/ni/洪芸妮憤怒/洪芸妮憤怒_00001.png", 0.2,
    "images/Character/ni/洪芸妮憤怒/洪芸妮憤怒_00002.png", 0.2,
    "images/Character/ni/洪芸妮憤怒/洪芸妮憤怒_00003.png", 0.2,
    "images/Character/ni/洪芸妮憤怒/洪芸妮憤怒_00004.png", 0.2,
    "images/Character/ni/洪芸妮憤怒/洪芸妮憤怒_00005.png", 0.2,
    "images/Character/ni/洪芸妮憤怒/洪芸妮憤怒_00006.png", 0.2,
    "images/Character/ni/洪芸妮憤怒/洪芸妮憤怒_00007.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮閉眼_00000.png", 0.2,
)

image ni_afraid_plus = Animation(
    "images/Character/ni/洪芸妮驚恐/洪芸妮驚恐_00000.png", 0.2,
    "images/Character/ni/洪芸妮驚恐/洪芸妮驚恐_00001.png", 0.2,
    "images/Character/ni/洪芸妮驚恐/洪芸妮驚恐_00002.png", 0.2,
    "images/Character/ni/洪芸妮驚恐/洪芸妮驚恐_00003.png", 0.2,
    "images/Character/ni/洪芸妮驚恐/洪芸妮驚恐_00004.png", 0.2,
    "images/Character/ni/洪芸妮驚恐/洪芸妮驚恐_00005.png", 0.2,
    "images/Character/ni/洪芸妮驚恐/洪芸妮驚恐_00006.png", 0.2,
    "images/Character/ni/洪芸妮驚恐/洪芸妮驚恐_00007.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮閉眼_00000.png", 0.2,
)

image ni_excited = Animation(
    "images/Character/ni/洪芸妮興奮/洪芸妮興奮_00000.png", 0.2,
    "images/Character/ni/洪芸妮興奮/洪芸妮興奮_00001.png", 0.2,
    "images/Character/ni/洪芸妮興奮/洪芸妮興奮_00002.png", 0.2,
    "images/Character/ni/洪芸妮興奮/洪芸妮興奮_00003.png", 0.2,
    "images/Character/ni/洪芸妮興奮/洪芸妮興奮_00004.png", 0.2,
    "images/Character/ni/洪芸妮興奮/洪芸妮興奮_00005.png", 0.2,
    "images/Character/ni/洪芸妮興奮/洪芸妮興奮_00006.png", 0.2,
    "images/Character/ni/洪芸妮興奮/洪芸妮興奮_00007.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮閉眼_00000.png", 0.2,
)

image ni_nervous = Animation(
    "images/Character/ni/洪芸妮緊張/洪芸妮緊張_00000.png", 0.2,
    "images/Character/ni/洪芸妮緊張/洪芸妮緊張_00001.png", 0.2,
    "images/Character/ni/洪芸妮緊張/洪芸妮緊張_00002.png", 0.2,
    "images/Character/ni/洪芸妮緊張/洪芸妮緊張_00003.png", 0.2,
    "images/Character/ni/洪芸妮緊張/洪芸妮緊張_00004.png", 0.2,
    "images/Character/ni/洪芸妮緊張/洪芸妮緊張_00005.png", 0.2,
    "images/Character/ni/洪芸妮緊張/洪芸妮緊張_00006.png", 0.2,
    "images/Character/ni/洪芸妮緊張/洪芸妮緊張_00007.png", 0.2,
    "images/Character/ni/洪芸妮正常/洪芸妮閉眼_00000.png", 0.2,
)


image boy_normal = Animation(
    "images/Character/boy/正常/男孩正常_00000.png", 0.2,
    "images/Character/boy/正常/男孩正常_00001.png", 0.2,
    "images/Character/boy/正常/男孩正常_00002.png", 0.2,
    "images/Character/boy/正常/男孩正常_00003.png", 0.2,
    "images/Character/boy/正常/男孩正常_00004.png", 0.2,
    "images/Character/boy/正常/男孩正常_00005.png", 0.2,
    "images/Character/boy/正常/男孩正常_00006.png", 0.2,
    "images/Character/boy/正常/男孩正常_00007.png", 0.2,
    "images/Character/boy/男孩正常閉眼_00000.png", 0.2,
)

image boy_angry = Animation(
    "images/Character/boy/生氣/男孩生氣_00000.png", 0.2,
    "images/Character/boy/生氣/男孩生氣_00001.png", 0.2,
    "images/Character/boy/生氣/男孩生氣_00002.png", 0.2,
    "images/Character/boy/生氣/男孩生氣_00003.png", 0.2,
    "images/Character/boy/生氣/男孩生氣_00004.png", 0.2,
    "images/Character/boy/生氣/男孩生氣_00005.png", 0.2,
    "images/Character/boy/生氣/男孩生氣_00006.png", 0.2,
    "images/Character/boy/生氣/男孩生氣_00007.png", 0.2,
    "images/Character/boy/男孩正常閉眼_00000.png", 0.2,
)

image boy_afraid = Animation(
    "images/Character/boy/哭/男孩哭_00000.png", 0.2,
    "images/Character/boy/哭/男孩哭_00001.png", 0.2,
    "images/Character/boy/哭/男孩哭_00002.png", 0.2,
    "images/Character/boy/哭/男孩哭_00003.png", 0.2,
    "images/Character/boy/哭/男孩哭_00004.png", 0.2,
    "images/Character/boy/哭/男孩哭_00005.png", 0.2,
    "images/Character/boy/哭/男孩哭_00006.png", 0.2,
    "images/Character/boy/哭/男孩哭_00007.png", 0.2,
    "images/Character/boy/男孩正常閉眼_00000.png", 0.2,
)

image boy_smile = Animation(
    "images/Character/boy/微笑/男孩微笑_00000.png", 0.2,
    "images/Character/boy/微笑/男孩微笑_00001.png", 0.2,
    "images/Character/boy/微笑/男孩微笑_00002.png", 0.2,
    "images/Character/boy/微笑/男孩微笑_00003.png", 0.2,
    "images/Character/boy/微笑/男孩微笑_00004.png", 0.2,
    "images/Character/boy/微笑/男孩微笑_00005.png", 0.2,
    "images/Character/boy/微笑/男孩微笑_00006.png", 0.2,
    "images/Character/boy/微笑/男孩微笑_00007.png", 0.2,
    "images/Character/boy/男孩正常閉眼_00000.png", 0.2,
)

image boy_black = Animation(
    "images/Character/boy/黑化/男孩黑化_00000.png", 0.2,
    "images/Character/boy/黑化/男孩黑化_00001.png", 0.2,
    "images/Character/boy/黑化/男孩黑化_00002.png", 0.2,
    "images/Character/boy/黑化/男孩黑化_00003.png", 0.2,
    "images/Character/boy/黑化/男孩黑化_00004.png", 0.2,
    "images/Character/boy/黑化/男孩黑化_00005.png", 0.2,
    "images/Character/boy/黑化/男孩黑化_00006.png", 0.2,
    "images/Character/boy/黑化/男孩黑化_00007.png", 0.2,
)

image boy_black2 = Animation(
    "images/Character/boy/黑化色違/黑化色違_00000.png", 0.2,
    "images/Character/boy/黑化色違/黑化色違_00001.png", 0.2,
    "images/Character/boy/黑化色違/黑化色違_00002.png", 0.2,
    "images/Character/boy/黑化色違/黑化色違_00003.png", 0.2,
    "images/Character/boy/黑化色違/黑化色違_00004.png", 0.2,
    "images/Character/boy/黑化色違/黑化色違_00005.png", 0.2,
    "images/Character/boy/黑化色違/黑化色違_00006.png", 0.2,
    "images/Character/boy/黑化色違/黑化色違_00007.png", 0.2,
)

image jack_normal = Animation(
    "images/Character/jack/正常/男2正常_00000.png", 0.2,
    "images/Character/jack/正常/男2正常_00001.png", 0.2,
    "images/Character/jack/正常/男2正常_00002.png", 0.2,
    "images/Character/jack/正常/男2正常_00003.png", 0.2,
    "images/Character/jack/正常/男2正常_00004.png", 0.2,
    "images/Character/jack/正常/男2正常_00005.png", 0.2,
    "images/Character/jack/正常/男2正常_00006.png", 0.2,
    "images/Character/jack/正常/男2正常_00007.png", 0.2,    
    "images/Character/jack/正常/閉眼/男2正常閉眼_00000.png", 0.2,
)

image jack_nervous = Animation(
    "images/Character/jack/緊張/男2緊張_00000.png", 0.2,
    "images/Character/jack/緊張/男2緊張_00001.png", 0.2,
    "images/Character/jack/緊張/男2緊張_00002.png", 0.2,
    "images/Character/jack/緊張/男2緊張_00003.png", 0.2,
    "images/Character/jack/緊張/男2緊張_00004.png", 0.2,
    "images/Character/jack/緊張/男2緊張_00005.png", 0.2,
    "images/Character/jack/緊張/男2緊張_00006.png", 0.2,
    "images/Character/jack/緊張/男2緊張_00007.png", 0.2,
    "images/Character/jack/正常/閉眼/男2正常閉眼_00000.png", 0.2,
)

image jack_afraid_plus = Animation(
    "images/Character/jack/驚恐/男2驚恐_00000.png", 0.2,
    "images/Character/jack/驚恐/男2驚恐_00001.png", 0.2,
    "images/Character/jack/驚恐/男2驚恐_00002.png", 0.2,
    "images/Character/jack/驚恐/男2驚恐_00003.png", 0.2,
    "images/Character/jack/驚恐/男2驚恐_00004.png", 0.2,
    "images/Character/jack/驚恐/男2驚恐_00005.png", 0.2,
    "images/Character/jack/驚恐/男2驚恐_00006.png", 0.2,
    "images/Character/jack/驚恐/男2驚恐_00007.png", 0.2,
    "images/Character/jack/正常/閉眼/男2正常閉眼_00000.png", 0.2,
)

image jack_delay = Animation(
    "images/Character/jack/遲疑/男2遲疑_00000.png", 0.2,
    "images/Character/jack/遲疑/男2遲疑_00001.png", 0.2,
    "images/Character/jack/遲疑/男2遲疑_00002.png", 0.2,
    "images/Character/jack/遲疑/男2遲疑_00003.png", 0.2,
    "images/Character/jack/遲疑/男2遲疑_00004.png", 0.2,
    "images/Character/jack/遲疑/男2遲疑_00005.png", 0.2,
    "images/Character/jack/遲疑/男2遲疑_00006.png", 0.2,
    "images/Character/jack/遲疑/男2遲疑_00007.png", 0.2,
    "images/Character/jack/正常/閉眼/男2正常閉眼_00000.png", 0.2,
)

image ling_normal = Animation(
    "images/Character/ling/季玲正常/季玲拆圖_00000.png", 0.2,
    "images/Character/ling/季玲正常/季玲拆圖_00001.png", 0.2,
    "images/Character/ling/季玲正常/季玲拆圖_00002.png", 0.2,
    "images/Character/ling/季玲正常/季玲拆圖_00003.png", 0.2,
    "images/Character/ling/季玲正常/季玲拆圖_00004.png", 0.2,
    "images/Character/ling/季玲正常/季玲拆圖_00005.png", 0.2,
    "images/Character/ling/季玲正常/季玲拆圖_00006.png", 0.2,
    "images/Character/ling/季玲正常/季玲拆圖_00007.png", 0.2,
    "images/Character/ling/季玲閉眼_00000.png", 0.2,
)

image ling_think = Animation(
    "images/Character/ling/季玲思考/季玲思考_00000.png", 0.2,
    "images/Character/ling/季玲思考/季玲思考_00001.png", 0.2,
    "images/Character/ling/季玲思考/季玲思考_00002.png", 0.2,
    "images/Character/ling/季玲思考/季玲思考_00003.png", 0.2,
    "images/Character/ling/季玲思考/季玲思考_00004.png", 0.2,
    "images/Character/ling/季玲思考/季玲思考_00005.png", 0.2,
    "images/Character/ling/季玲思考/季玲思考_00006.png", 0.2,
    "images/Character/ling/季玲思考/季玲思考_00007.png", 0.2,
    "images/Character/ling/季玲閉眼_00000.png", 0.2,
)

image ling_afraid_plus = Animation(
    "images/Character/ling/季玲驚恐/季玲驚恐_00000.png", 0.2,
    "images/Character/ling/季玲驚恐/季玲驚恐_00001.png", 0.2,
    "images/Character/ling/季玲驚恐/季玲驚恐_00002.png", 0.2,
    "images/Character/ling/季玲驚恐/季玲驚恐_00003.png", 0.2,
    "images/Character/ling/季玲驚恐/季玲驚恐_00004.png", 0.2,
    "images/Character/ling/季玲驚恐/季玲驚恐_00005.png", 0.2,
    "images/Character/ling/季玲驚恐/季玲驚恐_00006.png", 0.2,
    "images/Character/ling/季玲驚恐/季玲驚恐_00007.png", 0.2,
    "images/Character/ling/季玲閉眼_00000.png", 0.2,
)

image ling_nervous = Animation(
    "images/Character/ling/季玲緊張/季玲緊張_00000.png", 0.2,
    "images/Character/ling/季玲緊張/季玲緊張_00001.png", 0.2,
    "images/Character/ling/季玲緊張/季玲緊張_00002.png", 0.2,
    "images/Character/ling/季玲緊張/季玲緊張_00003.png", 0.2,
    "images/Character/ling/季玲緊張/季玲緊張_00004.png", 0.2,
    "images/Character/ling/季玲緊張/季玲緊張_00005.png", 0.2,
    "images/Character/ling/季玲緊張/季玲緊張_00006.png", 0.2,
    "images/Character/ling/季玲緊張/季玲緊張_00007.png", 0.2,
    "images/Character/ling/季玲閉眼_00000.png", 0.2,
)






image hall = "images/bg/大廳.png"
image newspaper = "images/bg/報紙.png"
image elevator = "images/bg/墜毀的電梯.png"
image counter = "images/bg/櫃台.png"
image reception = "images/bg/招待處.png"
image door = "images/bg/旋轉門.png"
image R_corridor = "images/bg/右走廊.png"
image L_corridor = "images/bg/左走廊.png"
image 2F_corridor = "images/bg/二樓走廊.png"
image 3F_corridor = "images/bg/3F走廊.png"
image 201_room = "images/bg/201.png"
image 202_room = "images/bg/202.png"
image 203_room = "images/bg/203.png"
image woman = "images/bg/woman.png"
image man = "images/bg/man.png"
image sink = "images/bg/sink.png"
image BanquetHall = "images/bg/BanquetHall.png"
image shadow = "images/bg/周圍陰影.png"
image W = "images/bg/W.png"
image Gameover_bg = "images/bg/GAME OVER.png"
image Gameendding_bg = "images/bg/完結圖.jpg"
image wu : 
    "images/bg/嗚嗚嗚 好恐怖.png"
    matrixcolor BrightnessMatrix(0.0)
    linear 0.3 matrixcolor BrightnessMatrix(-0.8)
    linear 0.1 matrixcolor BrightnessMatrix(0.0)
    repeat

image ning die = "images/bg/洪死亡圖.png"
image id_card = "images/bg/學生證.png"




image Boss_journal = "images/Props/日記本.png"
image key = "images/Props/飯店鑰匙.png"
image Employee_Records = "images/Props/員工紀錄.png"
image symbol = "images/Props/符咒.png"
image newspaper_prop = "images/Props/報紙.png"


transform shake_wiggle:
    # 強制鎖定大小為原比例 (防止變大)
    zoom 1.0 
    
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0


# 定義變暗的效果
transform t_dim:
    # 讓顏色變暗 (TintMatrix 是最現代的寫法，比 alpha 更好看)
    matrixcolor TintMatrix("#777") 
    # 稍微縮小一點點，增加景深感 (可選)


# 定義聚焦的效果
transform t_focus:
    # 恢復原色
    matrixcolor IdentityMatrix() 
    # 恢復原大小


init python:
    # 清除所有 auto-save 檔案
    for i in range(1, 20):  # 自動存檔數量，通常 1~9 就夠
        renpy.unlink_save("auto-" + str(i))


init:
    default hp = 100


init python:
    # 所有角色的 image tag（第一段）
    ALL_CHARS = ["xin", "ni", "boy", "jack", "ling"]

init python:
    # 確保角色列表包含所有可能的開頭
    ALL_CHARS = ["xin", "boy", "ni", "jack", "ling"]

    def focus(speaker):
        tags = renpy.get_showing_tags(layer="master")

        for tag in tags:
            for char in ALL_CHARS:
                if tag.startswith(char):
                    
                    # 1. 取得目前的 transform 列表
                    current_at_list = list(renpy.get_at_list(tag, layer="master"))
                    
                    # 2. 清理舊的濾鏡 (把之前的 t_dim 或 t_focus 拿掉，避免無限疊加)
                    clean_at_list = [t for t in current_at_list if t is not t_dim and t is not t_focus]

                    if char == speaker:
                        # 是說話者：套用聚焦濾鏡 + 設定 zorder 為 100 (最上層)
                        renpy.show(tag, at_list=clean_at_list + [t_focus], zorder=100, layer="master")
                    else:
                        # 不是說話者：套用變暗濾鏡 + 設定 zorder 為 0 (下層)
                        renpy.show(tag, at_list=clean_at_list + [t_dim], zorder=0, layer="master")
                    
                    break


# 遊戲從這裡開始。

label start:
    #遊戲血量
    show screen hp_display
    #遊戲內背景音樂
    play music "audio/background/遊戲內音樂.mp3" loop

    scene hall
    show shadow
    show W
    show xin_pain at left


    Xin "好痛……。"


    Xin "怎麼回事？為什麼我會在這裡。"
    #轉頭張望的動態?
    Xin "對了！其他人呢？"
    Xin "（我只記得我們進了這個旅館，然後……發生了什麼？）"
    Xin "在想下去也沒用，總之先試著找看看他人吧。"
    
    hide xin_pain
    show xin_normal  at left

    window hide  

    $ chosen_a = False
    $ chosen_b = False
    $ chosen_c = False
    $ chosen_d = False
    $ chosen_e = False
    $ chosen_f = False
    $ chosen_g = False
    jump Menu_00_01  # 直接跳到選單   
    
#序章選單
label Menu_00_01:

    # 如果選項都選過，則繼續故事
    if chosen_a and chosen_b and chosen_c and chosen_d and chosen_e and chosen_f and chosen_g:
        "你已經選擇了所有選項，故事繼續發展。"
        jump story00_01

    menu:
            "大廳" if not chosen_a:
                jump Explore_Halls

            "櫃檯" if not chosen_b:
                jump Explore_Counter

            "招待處" if not chosen_c:
                jump Explore_Reception

            "再調查一次" if not chosen_d:
                jump Explore_one_more_time

            "大門處" if not chosen_e:
                jump Explore_Door

            "右邊走廊" if not chosen_f:
                jump Explore_Right_corridor

            "左邊走廊" if not chosen_g:
                jump Explore_left_corridor


    window show 


label Explore_Halls: #大廳

    Xin "大廳好像沒什麼有用的東西，只是這裝潢也太復古了吧，要從哪裡先開始看呢？"

    $ chosen_a = True
    jump Menu_00_01

label Explore_Counter: #櫃檯
    scene counter
    show shadow
    show W
    show xin_normal  at left
    play sound "audio/sound/翻.mp3"
    Xin "好雜亂的櫃檯，就像有人匆忙逃走一般，看來要翻一下才能找到東西了。"
    hide xin_normal
    show xin_think at left
    show Employee_Records at Transform(xalign=1.0, yalign=0.5) #員工紀錄
    Xin "啊……！這是……入住紀錄？日期是……………………2004年……20年前的入住紀錄？為什麼會出現在這裡？也太奇怪了吧？"
    hide xin_think
    hide Employee_Records
    $ chosen_b = True
    jump Menu_00_01

label Explore_Reception: #招待處
    scene reception
    show shadow
    show W
    show xin_normal  at left
    Xin "這裡好像沒什麼特別的..."
    hide xin_normal
    $ chosen_c = True
    jump Menu_00_01

label Explore_one_more_time: #再調查一次
    scene newspaper
    show shadow
    show W
    show xin_think at left
    show newspaper_prop at Transform(xalign=1.0, yalign=0.5) #報紙
    play sound "audio/sound/拿報紙.mp3"
    Xin "啊！椅子的角落有一張紙。這是……報紙？一樣是2004年的。"
    "2004年4月4號，■■旅館發生大火災，死傷■8人，有■■人■蹤，目前還未找■屍體。"
    Xin "（有些地方損壞了讀不了，但旅館沒記錯的話我們去的那間以前也發生過火災...）"
    Xin "（會在這裡昏倒會跟這有關係嗎？……頭好痛，為什麼會感覺好像忘記了什麼？）"
    hide xin_think at left
    hide newspaper_prop
    $ chosen_d = True
    jump Menu_00_01

label Explore_Door: #旋轉門
    scene door
    show shadow
    show W
    show xin_normal  at left
    play sound "audio/sound/門推不開.mp3"
    Xin "（旋轉門，推不開，好像被某種力量控制住凝固在那一樣）"
    hide xin_normal
    $ chosen_e = True
    jump Menu_00_01

label Explore_Right_corridor : #右走廊
    scene R_corridor
    show shadow
    show W
    show xin_normal at left #要放疑惑
    play sound "audio/sound/男孩哭泣.mp3"
    Xin "（右邊走廊傳來了哭泣聲，雖然不知道是誰，但先去看看吧。）"
    hide xin_normal
    show xin_think  at left
    Xin "（小孩？為什麼會出現在這裡？難道他跟我一樣是突然出現在這的嗎？但是他一直在哭，總之先搭話看看吧，說不定能問出什麼。）"
    hide xin_think
    show xin_s_smile at left
    show boy_afraid at right
    $ focus("xin")
    Xin "哈、哈囉，那個小朋友，你好啊，你怎麼一個人在這裡？你知道這裡是哪裡嗎？"

    
    $ focus("boy")
    unknown "我、我不知道……嗚嗚嗚……我是和…媽媽一起…來的……但是……"
    unknown "嗚嗚……我們走散了……剛剛又遇到好可怕的姐姐……我、我好害怕……大哥哥……你能陪我…找媽媽嗎……？"
    hide xin_s_smile
    show xin_think at left
    $ focus("xin")
    Xin "（可怕的姐姐？是指謝呂姍嗎？那確實，她生氣起來是挺可怕的，但也不至於把小孩嚇成這樣吧？好吧，也不能放著這孩子不放。）"
    Xin "好，大哥哥陪你找媽媽，那你能告訴我你的名字嗎？"
    $ focus("boy")
    unknown "嗯……大哥哥……我叫蕭宇航，大哥哥可以叫我小航就好。"
    $ focus("xin")
    Xin "（蕭宇航？跟我的名字好像……？而且總覺得，在哪裡聽過？）"
    Xin "（這裡好像沒什麼特別的。）"
    hide xin_think
    hide boy_afraid
    $ chosen_f = True
    jump Menu_00_01

label Explore_left_corridor : #左走廊
    scene L_corridor
    show shadow
    show W
    show xin_think at left
    Xin "（電梯雖然被封鎖住了，但我記得左邊走廊這裡有逃生用樓梯。）"
    Xin "（去地下室的樓梯像是受到地震大力搖晃一樣被碎石堵住，看來接下來只能去樓上了）"
    hide xin_think
    $ chosen_g = True
    jump Menu_00_01


label story00_01 :
    scene L_corridor
    show shadow
    show W
    show xin_normal at left
    show boy_normal  at right

    $ focus("boy")
    boy "哥哥，你是跟誰一起來的啊？這裡有很多可怕的東西，小航一直自己在這裡躲來躲去..."
    boy "但是哥哥身上有媽媽的感覺，所以小航想要跟哥哥走，小航相信哥哥。"
    hide xin_normal
    show xin_s_smile at left

    $ focus("xin")
    Xin "那個……小航啊，雖然很想跟你說隨便相信陌生人不好。但是……畢竟現在是緊急事態，我不能保證一定能找到你媽媽，但是……"
    Xin "哥哥保證一定會保護好你的，所以等一下要牽好我的手，不要走散了。"
    Xin "還有，哥哥是跟朋友一起來的……哥哥的朋友們，我想可能有你剛剛見過的人，但他們……都不是壞人。"
    Xin "我……現在打算去找他們，順便帶你找媽媽，小航，你願意乖乖的跟著哥哥嗎？"
    hide boy_normal 
    show boy_smile  at right

    $ focus("boy")
    boy "嗯！小航會乖乖跟著哥哥的！"

    scene 2F_corridor
    show shadow
    show W
    show xin_normal  at left
    show boy_normal  at right
    "（飯？店 • 2？樓？走？廊）"
    play sound "audio/sound/女人尖叫.mp3"
    hide xin_normal
    hide boy_normal 
    show xin_afraid_plus at left
    show boy_afraid at right #嚇到
    $ focus("xin")
    Xin "（女人的尖叫聲！？難道是她們兩個？）"
    

    $ key_201 = False  # 是否拿到201號房的鑰匙
    $ explored_202 = False  # 是否進入過202號房


    jump Menu_00_02  # 直接跳到選單   
    

label Menu_00_02:


    "你要探索哪個房間？"

    menu:
        "201號房":
            if key_201:  # 只有拿到鑰匙才能進入
                jump room_201
            else:
                scene 2F_corridor
                show shadow
                show W
                play sound "audio/sound/門鎖住了.mp3"
                "門鎖住了，似乎需要鑰匙才能打開。"
                jump Menu_00_02  # 回到選單
        "202號房" if not explored_202:
            jump room_202



    jump story00_02     


# === 202號房劇情 ===
label room_202:
    scene 202_room
    show shadow
    show W
    show xin_afraid_plus at left #緊張

    Xin "（啊、門開了，動靜應該是從這邊傳來的，小心點開門吧）"
    play sound "audio/sound/推開門.mp3"
    "蕭瑀昕小心的將蕭宇航護在後面，悄悄的打開門，看到房間角落有個不停顫抖的熟悉身影……"
    Xin "洪云妮……？"
    show ni_nervous at right

    $ focus("ni")
    Ni "蕭瑀昕？是蕭瑀昕對吧！" 
    
    $ focus("xin")   
    Xin "對……是我，發生什麼了嗎？你怎麼一個人在這裡？你沒跟謝呂珊一起嗎？"
    hide ni_nervous  
    show ni_afraid at right

    $ focus("ni") 
    Ni "呂珊……對……呂珊她、她死了！！"
    hide xin_afraid_plus
    show xin_afraid_plus at left
    $ focus("xin") 
    Xin "洪云妮，你先冷靜一下，謝呂珊到底是怎麼了，我們又怎麼會在這裡，你能慢慢跟我講嗎？"
    hide ni_afraid  
    show ni_angry at right

    $ focus("ni")
    Ni "你、你忘了嗎……？哈哈……哈哈哈，都是你們！都是你們說要玩的！結果你卻忘了！開什麼玩笑！要不是你們的話！"
    "(洪云妮再次緊抓著蕭瑀昕的肩膀，用力的晃著他，正打算繼續發洩自己的心情)"
    "(洪云妮卻瞄到了蕭瑀昕身後的蕭宇航，像是看到什麼可怕的惡鬼一樣，瞬間往後退，縮成一團，顫抖的開口。)"
    hide ni_angry
    show ni_afraid_plus at right
    $ focus("ni")
    Ni "不...不要，為什麼會在這，明明我逃掉了。"
    #xin疑惑
    Ni "不要，別過來，都是你！都是你們！！"
    "(蕭瑀昕感到疑惑，打算上前安撫洪云妮時，洪云妮一把拍掉蕭瑀昕的手，激動的推倒蕭瑀昕後害怕的邊喊邊跑。)"
    hide ni_afraid_plus
    show boy_afraid at right 

    $ focus("boy") 
    boy "哥哥，你沒事嗎？"

    $ focus("xin") 
    Xin "啊，沒事的，只是有點被嚇到而已，小航沒被嚇到吧？"
    hide xin_afraid_plus
    show xin_s_smile at left
    $ focus("xin")
    Xin "那個姐姐……平時不是那樣的，可能真的出了什麼事才會這樣，抱歉讓你擔心了。"
    hide boy_afraid
    hide xin_s_smile
    show xin_think at left
    $ focus("xin")
    Xin "（雖然這麼說，但看洪云妮的反應，八成出事了，也不知道洪云妮為什麼會突然反應這麼大...）"
    Xin "（但是現在追上去估計也沒有什麼好結果，還是等她冷靜一下再去找她吧，總之先調查這個房間看看。）"
    Xin "（剛剛洪云妮坐的那個位子，好像有個閃著光的東西。）"
    Xin "（啊、是201號房的鑰匙，可能是洪云妮太激動掉出來的吧，總之能調查201號房了。目前房間裡也沒其他東西，先調查到這裡吧。）"

    show key at Transform(xalign=1.0, yalign=0.5)
    $ key_201 = True  # 拿到201號房鑰匙
    $ explored_202 = True  # 記錄已探索202號房
    
    "你獲得了【201號房的鑰匙】。現在可以進去看看了。"
    hide xin_think
    hide key

    jump Menu_00_02  # 回到探索選單

# === 201號房劇情 ===
label room_201:
    window hide

    pause 1.0

    scene 201_room
    show shadow
    show W
    show boy_normal  at right 
    show xin_pain  at left
    play sound "audio/sound/門開了.mp3"

    $ focus("xin")
    Xin "抱歉，小航，你能先去外面等我嗎？"
    #boy疑惑
    
    hide xin_pain 
    show xin_dilemma  at left

    $ focus("boy")
    boy "怎麼了嗎哥哥？被你擋住我什麼都看不到？"
    
    $ focus("xin")
    Xin "啊……你不要看到最好，可能會嚇到你，所以你能現在外面乖乖等我嗎？"
    
    $ focus("boy")
    boy "我知道了，那哥哥要快點喔，小航一個人等太久會害怕的。"
    hide boy_normal 
    hide xin_dilemma
    

    scene id_card
    show shadow
    show W
    show xin_afraid_plus  at left
    $ focus("xin")
    Xin "不是吧……洪云妮說的……都是真的……"
    Xin "（我看著手中的卡，不對，是謝呂珊的學生證，所以……眼前這個肉塊，是謝呂珊……）"
    Xin "（得知這是認識的人的屍體，我突然感覺到一股反胃的感覺，忍住不適爬到房間的廁所旁吐了起來）"
    Xin "（難以想像好好一個人，怎麼會變成那種樣子，讓我不舒服的好似把整個胃都吐出來一樣，無力的攤在馬桶旁休息。）"
    hide xin_afraid_plus
    show xin_pain  at left
    Xin "為什麼……到底……發生了什麼……我……又忘了什麼……"
    Xin "（我嘗試回憶，但是只能感受得到頭痛和疲憊，加上剛剛嘔吐過的虛弱，我撐不下去，昏了過去）"
    hide xin_pain

label story00_02:
    scene 2F_corridor
    show shadow
    show W
    "（（飯？店 • 2？樓？201？號？房？外）"
    show boy_black2 
    boy "嘻嘻～不知道我的作品哥哥喜不喜歡，但是好像對哥哥的打擊有點大？"
    boy "真可惜，還想再跟哥哥玩呢，要是這麼快就玩壞那就不好了。"
    boy "那就再準備一個新作品給哥哥好了 至於素材嗎……"
    boy "就用剛剛狼狽逃走的那個姐姐好了！"
    boy "哈哈……誰叫那個姐姐差點就在哥哥面前暴露了我的存在，明明都說好要保密的。"
    boy "既然素材也有想法了，那就趕快處理吧！趁著哥哥還在昏迷的時候～"
    hide boy_black

    jump story01_01

# === 第一章 ===
label story01_01:
    scene 3F_corridor
    show shadow
    show W
    "（飯？店？3？樓？走？廊？）"
    show jack_afraid_plus
    Jack "啊痛痛痛痛、都怪電梯突然往下掉，全身酸痛的要命。"
    "（傑克•米勒揉著酸痛的部位，然後看了看四周，一臉茫然的愣在原地。）"
    hide jack_afraid_plus
    show jack_delay
    Jack "這裡是……？哪啊？？？？"
    Jack "（等等，電梯不是故障墜毀了？那照理來我應該會墜落在一樓啊，可是這個裝潢，完全不像大廳，又復古沒看過的裝修……）"
    hide jack_delay
    show jack_afraid_plus
    Jack "天啊……該、該不會我已經死了吧！？這這裡是天堂嗎！？"
    "（傑克•米勒抱著頭在原地喃喃自語，這時，一個少女緩緩向他走來，在他面前站定，往他頭上來了一記手刀。）"
    hide jack_afraid_plus
    show jack_nervous at left
    show ling_normal at right

    $ focus("ling")
    unknown "笨蛋，你可總算醒了，你知不知道老娘為了等你醒來在旁邊坐了多久？"
    "（傑克•米勒摀著被手刀攻擊過的頭，愣愣的看著眼前的少女。）"
    unknown "你……該不會剛剛那一記下去敲傻了吧？唉……我是季玲，是個（實習）道士，你沒死，然後我是被顧來救你們的。"
    "（季玲揉著太陽穴，無語的看著面前傻愣著的少年。）"
    #Jack興奮
    "（傑克•米勒聽到季玲的話，激動的上前握住她的手。）"
    $ focus("jack")
    Jack "你說真的嗎！我沒死！"
    hide jack_nervous
    show jack_delay  at left
    $ focus("jack")
    "（傑克•米勒講完後意識到什麼疑惑的開口）"
    Jack "你說我沒死的話？那你……那什麼實習道士？為什麼要來救我們？"
    "（季玲似乎有些懶得解釋一臉不耐煩，但她看到面前少年單純愚蠢的表情，還是勉為其難解釋了一下。）"
    $ focus("ling")
    Ling "你們確實沒死，但是你們玩了吧？電梯遊戲？"
    "（傑克•米勒沒想到季玲連這都知道，怔怔的點頭應答。）"
    $ focus("jack")
    Jack "對……你怎麼……"
    "（還沒等傑克•米勒講完自己的疑問季玲就打斷他繼續講。）"
    $ focus("ling")
    Ling "但是中途電梯出現了意外，墜毀了……"
    Ling "也就是說你們在進行儀式到一半的時候終止了，終止造就你們現在處於一個死和生的中間地帶。"
    Ling "嘛、也可以說是靈體存在的地方吧。"
    Ling "你們的身體在醫院病房裡昏迷著呢，現在在這裡的你們所有人，都是靈魂狀態，也就是所謂的生靈。"
    Ling "而我呢，就是來帶你們回去的。哼哼，這可是很重要的啊，我告訴你，生靈若是離開身體太久，或是遭到其他靈體攻擊"
    Ling "一旦你現在這靈魂死亡，那你的身體也會同時停止心跳，靈魂受到些許傷害都有可能影響你現實的身體。"
    Ling "因為醫院的你們已經昏迷很久了，你的父母才求到我這邊請我幫忙"
    Ling "你知道剛剛為了保護昏迷的你不被其他惡靈攻擊我消耗了多少符紙嗎？"
    Ling "這些可是很貴的，等會去可要一筆一筆跟你算帳，懂了嗎？"
    "（傑克•米勒聽著季玲的話還有些愣愣的腦袋轉不過來，他確實喜歡都市傳說也想要看看真實的鬼長怎樣，但那也只是“想”）"
    "（他沒想到只是一個玩笑的試膽挑戰，竟然成真了，而且事情似乎很嚴重，他父母甚至請了道士來。）"
    $ focus("jack")
    Jack "（雖然她說的煞有其事，但是果然太突然還是讓人懷疑是不是真的，總之先跟著他吧）"
    Jack "（而且既然情勢這麼緊張，那我也要先趕快找到我的兄弟，畢竟要不是我任性拉他一起玩的話……"
    Jack "我知道了，雖然還搞不太清楚，但我先相信你吧。"
    Jack "不過，要先找到我的兄弟和同伴才行。"
    $ focus("ling")
    Ling "欸？沒想到你還挺有義氣的啊，雖然我的委託只有保障你的人生安全帶你回去而已"
    Ling "但是看在你這麼講義氣的份上，我就陪你找找人吧，不過，要加錢喔，小少爺～"
    $ focus("jack")
    Jack "啊，只要能找到人，多少我都付。"
    hide jack_delay
    hide ling_normal


    scene 201_room
    show shadow
    show W
    "（同一時間的另一邊）"
    "（飯？店？201？號？房）"
    show xin_pain  at left
    "（蕭瑀昕從昏迷中醒來，輕揉著疼痛的頭，環顧周圍，冷靜的思考發生的事。）"
    hide xin_pain
    show xin_afraid_plus  at left
    Xin "（對了……我看到了那個）"
    Xin "（然後反胃感上來忍不住吐了之後就不舒服的昏過去了。）"
    Xin "（對了！我昏迷了多久？假如真的有能把人弄成那樣的怪物在的話，那小航他……！）"
    hide xin_afraid_plus
    scene 2F_corridor
    show shadow
    show W
    show xin_afraid_plus  at left
    "（蕭瑀昕推開門，但門外本該站著蕭宇航的地方空無一人。）"
    Xin "小航！？"
    hide xin_afraid_plus
    show xin_think  at left
    Xin "（雖然很想大聲呼喊小航的名字，但這樣也許只會引來怪物……冷靜，我要先冷靜。）"
    Xin "（啊、小航剛剛站的地方好像有什麼，被燒掉一半的照片……？）"
    Xin "（似乎是遭到火燒過，只能勉強辨識出照片中的小男孩，那張臉，跟小航一樣，只是這照片感覺已經有好幾年了）"
    Xin "（背景也是，還有旁邊這個女人，雖然上半身被燒焦看不清楚，但總覺得很熟悉……先收著吧，等找到小航還給他。）"

    window hide  

    $ chosen_201 = False
    $ chosen_203 = False
    $ chosen_204 = False
    $ chosen_205 = False
    
    jump Menu_01_01


label Menu_01_01:


    "你要探索哪個房間？"

    if chosen_201 and chosen_203 and chosen_204 and chosen_205:
        "你已經選擇了所有選項，故事繼續發展。"
        $ women_toilet = False
        $ men_toilet = False
        jump Menu_01_02

    menu:
        "你要調查哪一間？"
        "201號室" if not chosen_201:
            jump room_201_01
        "203號室" if not chosen_203:
            jump room_203_01
        "204號室" if not chosen_204:
            jump room_204_01
        "205號室" if not chosen_205:
            jump room_205_01



 
label room_201_01:
    
    scene 201_room
    show shadow
    show W
    show xin_dilemma at left
    Xin "（201號室嗎……實在不想再進去一次）"


    menu:
        "確定要再次調查201號室嗎？"
        "確定":
            play sound "audio/sound/女人尖叫2.mp3"
            show wu
            $ renpy.pause(2.0, hard=True)
            hide wu
            Xin "（果然還是沒辦法習慣這股味道，還有翻找同學的屍體什麼的……糟糕又開始有點不舒服了，沒什麼特別的其他東西。）"
            $ hp -= 15
            if hp <= 0:
                jump game_over

            "精神力 -15"
        "不要":
            Xin "（還是別進去好了……）"
    
    $ chosen_201 = True
    jump Menu_01_01

label room_203_01:
    scene 203_room
    show shadow
    show W
    show xin_dilemma at left

    Xin "（房間的擺設都差不多……雖說每間都有燒焦痕跡，但是這一間大火燃燒的痕跡好嚴重，嗯？地上掉落著什麼？）"
    "（失、失火了，不是說飯店很安全嗎？）"
    "（為什麼失火到現在都還沒被撲滅，消防系統在幹嘛，好燙，不要我不想被燒死，要想辦法，逃出去才行。）"
    Xin "火災……？確實有火燒的痕跡還有之前撿到的報紙，難道火災是發生在這裡的嗎？"

    $ chosen_203 = True
    jump Menu_01_01

label room_204_01:
    scene 203_room
    show shadow
    show W
    show xin_dilemma at left

    Xin "（房間的擺設都差不多……這裡好像沒什麼特別的）"

    $ chosen_204 = True
    jump Menu_01_01

label room_205_01:
    scene 203_room
    show shadow
    show W
    show xin_dilemma at left

    Xin "（房間的擺設都差不多……啊、那裡有個閃亮亮的東西，三樓樓梯間的鑰匙？這樣就能去三樓了吧。）"
    Xin "（總之二樓能調查的地方基本上都看過了吧，等一下，好像還有廁所，但是小航會在廁所嗎？……還是去看看好了）"

    $ chosen_205 = True
    jump Menu_01_01

label Menu_01_02:



    "接下來要調查？"

    menu:
        "女廁":
            if women_toilet:  # 只有拿到鑰匙才能進入
                jump women_toilet_a
            else:
                window show
                scene 2F_corridor
                show shadow
                show W
                Xin "（不……女廁再怎麼說還是不太好吧...也許應該先調查其他地方。）。"
                jump Menu_01_02  # 回到選單
        "男廁" if not men_toilet:
            jump men_toilet_a

    window show
    jump story01_02

label men_toilet_a:
    scene man
    show shadow
    show W
    show xin_dilemma at left

    Xin "小航？蕭宇航？你在嗎？"
    "（蕭瑀昕小聲的邊喊著邊打開一間一間的廁所門，但都沒有回應，他走到洗手台，想要用水洗一下臉打氣精神）"
    scene sink
    show shadow
    show W
    show xin_afraid_plus at left
    "（打開水龍頭，流出來的卻是如同鮮紅血液般的液體，他嚇到的往後退了一步。）"
    Xin "（怎麼回事，為什麼水……。算了，這裡好像沒有什麼其他東西，還是趕快找到人吧。）"
    
    $ women_toilet = True
    $ men_toilet = True
    jump Menu_01_02

label women_toilet_a:
    scene woman
    show shadow
    show W
    show xin_dilemma at left

    Xin "（二樓只剩這邊沒有調查了……果然還是進去吧，希望不要被人看到。）"
    Xin "（慢慢走進女廁，發現女廁裡有股血腥的噁臭味，第二次聞到這種味道，噁心感比第一次好多了，不過意識到味道的來源）"
    Xin "（我在心裡祈求著不是我想的那樣，但推開最後一道門時，果然……門裡的畫面跟想的一樣，我絕望的閉上眼）"
    scene ning die
    play sound "audio/sound/洪哭.mp3"
    show shadow
    show W
    show xin_dilemma at left
    Xin "（不敢想像剛剛還說過話的同學，頭像是被人暴力按進馬桶一般，早已扭曲變形，就這樣死在血泊中的——洪云妮）"
    Xin "（我嘗試著讓自己冷靜下來，然後簡單查看洪云妮屍體旁邊有沒有什麼線索，找到了一本隨身筆記，內容好像是洪云妮寫的。）"
    #獲得筆記
    show Boss_journal at right
    window hide
    call screen note_screen(
        "筆記："
        
        """
        電梯墜落後，好在我和呂珊掉在同一個地方，有彼此能扶持，還不算太糟，但以防萬一，還是記錄一下吧。

        這裡，和呂珊一起探索的過程中，我們大概得出了結論，我們應該是透過儀式成功的進到了異世界，也就是說那個電梯傳說是真的，雖然有點害怕，但是呂珊說了，兩個人一起一定能找到回去的方法，我也這麼相信，嗯，只要兩個人的話，一定沒問題。

        那是什麼？為什麼會這樣？為什麼我們要玩這個遊戲？我們沒有惹任何人啊？為什麼？呂珊，不是說要兩個人一起的嗎？為什麼丟下我？

        我不要，根本不可能回去，我一個人根本沒辦法，被騙了，被那個人騙了，如果不是那個人的話，呂珊就不會……

        為什麼那個人會在那邊？為什麼？為什麼？為什麼？為什麼？為什麼？為什麼？明明我都逃走了？為什麼還不放過我？不要，我不想死？我不要，不要不要不要不要不要不……
        """)
    window show
    Xin "（筆記到這裡就結束了……）"
    
    Xin "（洪云妮和謝呂珊到底發生了什麼，儀式和異世界又是什麼意思……？不行……思緒好亂。總之去三樓之前，先整理一下目前收集到的資訊吧……）"
    hide Boss_journal





# 記得先定義初始 hp (如果你還沒定義)
default hp = 100

label story01_02:
    scene 2F_corridor
    show shadow
    show xin_think at left # 假設你已經改用正確的命名與 transform
    "思考時間"
    jump q1

# --- 第一題 ---
label q1:
    # 呼叫視窗，並把結果存入 _return 變數
    # 格式： [ ("選項文字", 是否正確), ("選項文字", 是否正確) ]
    call screen quiz_screen("這裡是哪裡？", [
        ("A. 2024年的飯店", False), 
        ("B. 2004年的飯店", True)
    ])

    # 判斷結果
    if _return == "game_over":
        jump game_over

    # 如果程式跑到這裡，代表玩家選對了 (screen 只有選對才會 Return "correct")
    # 這裡放選對後的劇情
    
    Xin "（對了，在櫃檯的入住記錄，上面寫著2004年...）"
    Xin "（難道這就是洪云妮筆記裡說的異世界嗎？）"

    jump q2


# --- 第二題 ---
label q2:
    
    call screen quiz_screen("飯店裡發生過什麼？", [
        ("A. 火災", True), 
        ("B. 地震", False)
    ])

    if _return == "game_over":
        jump game_over

    # 選對後的劇情
    Xin "（從剛剛房間裡火燒的痕跡和大廳撿到的報紙...）"
    Xin "（但是10年前的大火的話...）"
    
    jump story01_03

label story01_03:
    Xin "（總之，現在能確定的應該就是這些了吧？感覺好像快能想起什麼了）"
    Xin "（但是還差一點契機，看來只能去三樓看看了吧……我握緊手中的鑰匙，往通往三樓的樓梯間走去。）"
    "（當時的蕭瑀昕還不知道，這只是大家被迫捲入，蕭瑀昕悲慘又複雜的命運開端。）"

# === 第二章 ===
label story02_01:
    scene 3F_corridor
    show shadow
    show W
    show xin_think at left
    "（飯？店？3？樓？樓？梯？間？）"
    "蕭瑀昕走上三樓，看著與二樓不一樣的格局，他想著要從哪裡開始著手調查。"
    jump Explore02_WC00




label Explore02_WC00:
    scene man
    show shadow
    show W
    show xin_think at left
    Xin "（應該不會有人躲在廁所裡吧，還是最後再來好了。）"


    jump Explore02_BanquetHall


label Explore02_BanquetHall:
    scene 3F_corridor 
    show shadow
    show W
    show xin_think at left
    Xin "（果然要調查的話，還是宴會廳最引人注目吧。）"
    "（蕭瑀昕推宴會廳的門，但門好像被什麼擋住一樣，推不開。）"
    Xin "（怎麼辦，這樣沒辦法調查啊……）"
    Xin "（說不定是有人在裡面，然後用椅子擋住之類的，要不要……開口問問看？）"
    "（蕭瑀昕思考了一番後，最後下定決心開口呼喊。）"
    hide xin_think
    show xin_normal at left
    Xin "那個！裡面有人嗎？可以開一下門嗎？"
    "（蕭瑀昕喊完後，門後沒什麼反應，他嘆了口氣。）"
    Xin "唉、果然是不可能有人吧……"
    "（這時，門後突然傳來搬動東西的聲音，有人開口說話。）"
    man00 "喂！有人在外面是嗎？等著，我現在就打開門。"
    woman00 "欸！不要亂開門啦！萬一又是惡靈怎麼辦？我可沒這麼多符紙給你浪費！"
    "（室內的兩人開始爭吵著要不要開門，這讓門外的蕭瑀昕有些無語）"
    "（但他在仔細聽男生的聲音後，辨別出來聲音的主人）"
    "（但還是有些不確定，蕭瑀昕小心翼翼的開口。）"
    Xin "傑克？是你嗎？"
    "（聽到蕭瑀昕的提問，裡面的爭吵停了下來）"
    "（然後門迅速被打開，一個高個子的男生從門內飛撲出來抱住了蕭瑀昕。）"
    hide xin_normal
    show xin_pain at left
    show jack_normal at right
    $ focus("jack")
    Jack "兄弟！！！！！你沒事太好了！！"
    $ focus("xin")
    Xin "等……傑克，你這樣勒到我脖子有點難受、不對，你為什麼會在這裡……？"
    hide xin_pain
    show xin_normal at left
    $ focus("xin")
    Xin "還有你身後的那個女生是？"
    "（聽到蕭瑀昕說難受，傑克•米勒鬆開了懷抱，改成將手搭在蕭瑀昕肩上開心的開口。）"
    $ focus("jack")
    Jack "喔，我為什麼會在這裡，這解釋起來有點麻煩啊，總之那女生叫季玲，姑且……是個道士吧？"
    scene BanquetHall
    show shadow
    show W
    show xin_normal at left
    show jack_normal at right
    $ focus("jack")
    Jack "總之先趕快進來吧，要是讓惡靈闖進來就麻煩了，進來我慢慢解釋給你聽。"
    "（傑克•米勒帶著蕭瑀昕一起進了宴會大廳，然後再次用宴會廳的椅子堵上了門）"
    "（確保沒問題後，他招呼蕭瑀昕一起到季玲旁邊的位子坐下。）"
    "（蕭瑀昕坐在位子上冷靜的聽著傑克•米勒緩緩道來一切，然後在腦袋中梳理了一下，開口。）"
    "（確保沒問題後，他招呼蕭瑀昕一起到季玲旁邊的位子坐下。）"
    $ focus("xin")
    Xin "所以，我們玩了那個電梯遊戲？還成功了？然後現在我們是靈體狀態？"
    hide jack_normal
    show ling_normal at right
    $ focus("ling")
    Ling "對！沒錯，然後現在因為這個人說要找到大家，所以我們還沒有走。"
    hide xin_normal
    show jack_normal at left
    $ focus("jack")
    Jack "畢竟是我提議玩的啊！總不能丟下大家不管吧！"
    $ focus("ling")
    Ling "但是我只能帶走一位回去，不然我們就必須找到這裡的出口，只是找到出口前說不定你們的靈魂會先消散呢。"
    $ focus("jack")
    Jack "別說那種喪氣的話啊！一定可以找到大家然後一起從出口回去的！你說對吧！兄弟！"  
    "（聽到傑克•米勒的話，蕭瑀昕沉思了一下）"
    "（因為他知道，已經沒辦法大家一起回去了，他斟酌了一下要用什麼詞語開口。）"
    hide ling_normal
    show xin_dilemma at right
    $ focus("xin")
    Xin "傑克……那個大家……沒辦法一起回去了"
    $ focus("jack")
    Jack "？兄弟？你這是什麼意思？"
    $ focus("xin")
    Xin "洪云妮和謝呂珊……已經……死了"
    hide jack_normal
    show jack_afraid_plus at left
    $ focus("jack")
    Jack "什……"
    hide xin_dilemma
    show ling_think at right
    $ focus("ling")
    Ling "哎呀，看來已經有犧牲者出現了呢。我們可得加快腳步了，不然下一個，還不知道是誰？"
    $ focus("jack")
    Jack "現在是那種用玩笑態度講話的時候嗎！"
    hide ling_think
    show xin_normal at right
    $ focus("xin")
    Xin "……冷靜點，傑克……他說的是對的。"
    hide jack_afraid_plus
    show ling_think at left
    $ focus("ling")
    Ling "怎麼？我說實話還錯了啊？再說，要不是你們自己作死，怎麼會發生這種事？"
    Ling "一切都是你們自己的因果關係！"
    Ling "再說你們繼續在那裡消沉也沒用吧？難道你們也要去送死嗎？"
    $ focus("xin")
    Xin "啊……沒錯，繼續消沉也不是辦法。傑克，我們必須找到出口。"
    hide ling_think
    show jack_delay at left
    $ focus("jack")
    Jack "兄弟……我知道了，但是出口，你們有什麼想法嗎？"
    $ focus("xin")
    Xin "我沒什麼想法但是，一樓二樓我都探索過了，這是我收集到的東西，總之我們目前是在2004年火災後的飯店空間裡。"
    $ focus("jack")
    Jack "我們有嘗試過上樓，但上樓的樓梯像是被什麼封住一樣打不開，所以樓上大約是不行。"
    $ focus("ling")
    Ling "估計在地下室，在地下室能感受到一股很大的能量。" 
    $ focus("xin")
    Xin "地下室……？但是地下室的路被碎石檔住了、不，以我們三個人的話，應該能搬開碎石。"
    $ focus("jack")
    Jack "那樣目的地就確定了呢"
    "（看到傑克開心的傻笑，季玲又給他的額頭來了一記手刀。）"
    hide xin_normal
    show ling_think at right
    $ focus("ling")
    Ling "別說的這麼簡單，你們已經死兩個人了，再說地下室的那股能量，估計是維持這個空間也就是所謂Boss的所在地。"
    Ling "這麼危險的地方，先不說找到出口，想要出去，還需要讓Boss產生動搖，空間才會動搖出現漏洞" 
    Ling "這樣我們才能出去，這可不是簡單的事。" 
    $ focus("jack")
    Jack "那、那你說，我們該怎麼辦比較好？"
    $ focus("ling")
    Ling "專注，警戒，別獨自一人行動。然後在此之前，我們還要找到能讓Boss動搖的方法"
    Ling "這個空間的生靈應該只有你們和我而已，蕭瑀昕你有遇過其他的人嗎？說不定能成為什麼線索。"
    hide jack_delay
    show xin_think at left
    $ focus("xin")
    Xin "（其他的人……啊、小航，但他會跟Boss有關係嗎？）"
    Xin "（不過我記得當初洪云妮看到他的時候好像很驚恐……難道？不、我還需要更多線索才能確認。）"
    Xin "我想……我大概有點想法，但是還不能完全確定，我還需要更多的線索。"
    $ focus("ling")
    Ling "是嗎？那我們一路上再調查一次吧。Boss動搖的方法，就交給你了喔。"
    hide xin_think
    show xin_dilemma at left
    $ focus("xin")
    Xin "啊、沒問題。"
    hide xin_dilemma
    show jack_normal at left
    $ focus("jack")
    Jack "那我呢？我呢？我做什麼？"
    $ focus("ling")
    Ling "你別亂跑就好！"
    "（傑克•米勒又被季玲一記手刀攻擊，他疼著捂著額頭，隨後又打氣精神，整理好隨身的東西。）"
    $ focus("jack")
    Jack "那麼，傑克小隊！準備出擊囉！"
    $ focus("ling")
    Ling "那是什麼爛名字……"
    hide jack_normal
    show xin_dilemma at left
    $ focus("xin")
    Xin "哈、哈哈……"


    scene Gameendding_bg
    "接著三個人在傑克•米勒帶起的尷尬氣氛中，朝著目的地的地下一樓走去，而這一路上，還有很多阻礙在等著他們。"


    jump story02_02


label story02_02:

    
    # 遊戲結束。
    return


label game_over:
    scene Gameover_bg

    with fade
    play music "gameover.ogg"
    "你的精神力歸零了……"
    show xin_pain at left
    Xin "（頭好痛，視野不知道何時慢慢變暗，已經撐不下去了，我不知不覺中陷入了黑暗）"
    "醒醒，我的孩子。"
    Xin "（誰……？黑暗中傳來熟悉的呼喚聲，我努力的想睜開眼睛，回應那個聲音。）"

    menu:
        "我累了，就這樣吧……(回到主選單)":
            return
        "回應他（復活）":
            hide xin_pain
            jump start

    return

    








