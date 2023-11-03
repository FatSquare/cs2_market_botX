
# <a href="#">Contents</a>
1. [Introduction](#introduction)  
2. [Screenshots](#ss)  
2. [Installation](#install)  
3. [Configuration](#confs)  
    1. [Bot Configuration](#conf1)  
    1. [Steam account configuration](#conf2)  
4. [License](#license)  

<br>

# <a id="introduction">CS2 botX </a>
CS2 botX is a  tool that watchs the steam community market for skins floats/prices in counter strike 2 (aka CS:GO)
<br>Currently you can't buy skins yet. you just get a list of skins floats
<br><br>___Note: This tool is against steam TOS and it's only for educational purpose. Using it might result in a steam community ban.___

## <a id="ss">Screenshots</a>  

![App Screenshot](https://i.imgur.com/ofhjoSj.png)


## <a id="install">Run Locally </a>

Clone the project  

~~~bash  
  git clone https://github.com/FatSquare/cs2_market_botX
~~~

Go to the project directory  

~~~bash  
  cd cs2_market_botX
~~~

Install dependencies  

~~~bash  
pip install -r requirements.txt
~~~

Start the bot  

~~~bash  
python bot.py
~~~

## <a id="confs">Configuration  </a>

#### <a id="conf1">_Skin Config_</a> 
To configurate the bot please enter `bot.py` and change these lines however you like  

```python
skins_start,skins_count = 0,100  # skins_count < 100
skin_name = "M4A1-S | VariCamo"  # Skin name in this format
rarity = "Field-Tested"          # Any csgo rarity
statrak = False                  # False or True
max_float = 1                    # Between 0 and 1
```

#### <a id="conf2">_Steam Account Config_</a>
one problem is steam will output the prices currency  depending on the owner region
<br>if you want to get the same currency with all the skins follow this method<br>

1) Copy the `steam_login_secure` value from the cookies
2) Paste it in `bot_config.py`
```python
steam_login_secure = 'my_token_that_i_just_copied'
```
3) Every time the currency problem happens again that means that token expired just redo all the steps

## <a id="license"> License </a>  

[MIT](https://choosealicense.com/licenses/mit/)
