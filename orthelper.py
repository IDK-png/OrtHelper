import discord
from discord.ext import commands
import asyncio
from datetime import datetime
import json
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
import random
bot = commands.Bot(command_prefix = '$') 
@bot.event
async def on_ready():
   try:
    print("הולך ליום עבודה קשה")
    channel = bot.get_channel(677164675888054332)
    await channel.send('הבוט נפעל ועכשיו הולך לעבוד בשביל השרת')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('תיקון באגים'))
   except NameError:
    print("!NameError!")
@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name="תלמיד ז1")
    await member.add_roles(role)
    embed=discord.Embed(title="!שלום לך")
    embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/whatsapp/238/bird_1f426.png")
    embed.add_field(name="? מי אני", value="אני בוט שכתב מקסים בשביל השרת הזה ובשביל להשתמש בה תכנסו לכל צאט ותכתבו שם פקודות", inline=False)
    embed.add_field(name="? איפה הפקודות ", value=":הנה הם", inline=True)
    await member.send(embed=embed)
    embed=discord.Embed(title="__**עזרה בפקודות**__", color=0xff8080)
    embed.add_field(name="כלכלת השרת", value="--------------", inline=True)
    embed.add_field(name="$work", value="להתחיל לעבוד ולקבל כסף", inline=False)
    embed.add_field(name="$shop", value="לראות את החנות של הביזנסים", inline=True)
    embed.add_field(name="ביזנס", value="אם אתם קונים ביזנס \n אז גם השכר שלכם עולה", inline=True)
    embed.add_field(name="$buy ", value="לקנות את מה שבחנות", inline=False)
    embed.add_field(name="$eco_info", value="הפרופיל שלכם בכלכלת השרת", inline=True)
    embed.add_field(name="$pay", value="לשלם למישהו כסף", inline=True)
    embed.set_footer(text="_מקסים היה פה_")
    await member.send(embed=embed)
@bot.event
async def on_message(message):
    slova = ['הומו', 'שרמוטה', 'זונה', 'תמות', 'קוקסינל', 'תזדיין', 'זין', 'בטול', 'נבלות', 'נבל', 'נבלה', 'זבלים', 'זבל', 'מטומטמים', 'זונות', 'זיינים', 'שרמוטות', 'תמותו', 'קוקסינלים', 'תזדיינו', 'בטולים', 'חרה', 'חרות']
    for a in slova:
       if a in message.content:
            with open('warn.json', 'r') as warns_file:
               data = json.load(warns_file)
               warns_file.close()
               if str(message.author.id) not in data:
                  a_dict = {str(message.author.id) : "1"}
                  data.update(a_dict)
                  with open('warn.json', 'w') as f:
                     json.dump(data, f)
               else:
                 for p in data:
                    if p == str(message.author.id):
                      data[p] = str(int(data[p]) + 1)
                      jsonFile = open("warn.json", "w+")
                      jsonFile.write(json.dumps(data))
                      jsonFile.close()
            await message.delete()
            with open('users.json', 'r') as json_file:
                  data = json.load(json_file)
                  json_file.close()
                  for p in data:
                    if len(p) == 18 and data[p] == "0":
                      embed=discord.Embed(title="מילה גסה", description=f"השתמש במילה גסה  {message.author} משתמש בשם")
                      embed.add_field(name=f"משפט שבו היה נמצא מילה גסה", value=f"{message.content} : {message.author}", inline=True)
                      user = bot.get_user(int(p))
                      await user.send(embed=embed)
    await bot.process_commands(message)
@bot.command()
async def mute(ctx, member: discord.Member, duration: int=None, *, reason=None):
    with open('users.json', 'r') as json_file:
      data = json.load(json_file)
      json_file.close()
      if str(ctx.message.author.id) in data:
          role = discord.utils.get(ctx.guild.roles, name="מוט")
          await member.add_roles(role)
          embed = discord.Embed(title=f":lock:מיוט:lock: ", color=0xff0000)
          embed.set_thumbnail(url= member.avatar_url)
          embed.add_field(name="__***משתמש***__", value=f"{member}\n<@{member.id}>", inline=True)
          embed.add_field(name="__***סיבה***__", value=f"{str(reason)}", inline=True)
          embed.add_field(name="__***זמן***__", value=f"דקות {duration}", inline=True)
          await ctx.send(embed=embed)
          duration = int(duration) * 60
          await asyncio.sleep(duration)
          await member.remove_roles(role)
      else:
          embed=discord.Embed(color=0xfff700)
          embed.set_thumbnail(url="https://fkutaman.ru/images/warning.png")
          embed.add_field(name="ERROR", value=".אתם לא ברשימת האדמינים", inline=False)
          embed.add_field(name="פתרון הבעיה", value="ולכתוב בא הוכחה שאתם מורה זה נעשה בשביל להגן מספאם request נא לעשות בקשת הוספה לאדמינים בעזרת הפקודה", inline=False)
          embed.set_footer(text="ERROR_ADMIN_SIGN_IN")
          await ctx.message.author.send(embed=embed)
@bot.command()
async def unmute(ctx, member: discord.Member, *, reason=None):
    with open('users.json', 'r') as json_file:
      data = json.load(json_file)
      json_file.close()
      if str(ctx.message.author.id) in data:
          role = discord.utils.get(ctx.guild.roles, name="מוט")
          await member.add_roles(role)
          embed = discord.Embed(title=f":unlock:אן-מיוט:unlock:", color=0xff0000)
          embed.set_thumbnail(url= member.avatar_url)
          embed.add_field(name="__***משתמש***__", value=f"{member}\n<@{member.id}>", inline=True)
          embed.add_field(name="__***סיבה***__", value=f"{reason}", inline=True)
          await ctx.send(embed=embed)
          await member.send(embed=embed)
          await member.remove_roles(role)
          await member.send(f"***הזמן של המיוט עבר***")
      else:
          embed=discord.Embed(color=0xfff700)
          embed.set_thumbnail(url="https://fkutaman.ru/images/warning.png")
          embed.add_field(name="ERROR", value=".אתם לא ברשימת האדמינים", inline=False)
          embed.add_field(name="פתרון הבעיה", value="ולכתוב בא הוכחה שאתם מורה זה נעשה בשביל להגן מספאם request נא לעשות בקשת הוספה לאדמינים בעזרת הפקודה", inline=False)
          embed.set_footer(text="ERROR_ADMIN_SIGN_IN")
          await ctx.message.author.send(embed=embed)
@bot.command()
async def pop(ctx, *, amount):
    with open('users.json', 'r') as json_file:
      data = json.load(json_file)
      json_file.close()
      if str(ctx.message.author.id) in data:
          await ctx.channel.purge(limit=int(amount)+1)
          emb = discord.Embed(title="ניקוי הצאט", description=f"הודעות נמחקו {amount}", color=0xff0000)
          await ctx.send(embed=emb)
          await ctx.channel.purge(limit=1)
      else:
          embed=discord.Embed(color=0xfff700)
          embed.set_thumbnail(url="https://fkutaman.ru/images/warning.png")
          embed.add_field(name="ERROR", value=".אתם לא ברשימת האדמינים", inline=False)
          embed.add_field(name="פתרון הבעיה", value="ולכתוב בא הוכחה שאתם מורה זה נעשה בשביל להגן מספאם request נא לעשות בקשת הוספה לאדמינים בעזרת הפקודה", inline=False)
          embed.set_footer(text="ERROR_ADMIN_SIGN_IN")
          await ctx.message.author.send(embed=embed)
@bot.command()
async def off_logs(ctx):
   array_to_json = {str(ctx.message.author.id) : '1'}
   with open('users.json', 'r') as json_file:
    data = json.load(json_file)
    json_file.close()
    for p in data:
      if p == str(ctx.message.author.id):
        if data[p] == "0":
          data[p] = "1"
          jsonFile = open("users.json", "w+")
          jsonFile.write(json.dumps(data))
          jsonFile.close()
          embed=discord.Embed(color=0xff0000)
          embed.add_field(name="כבוי לוגים", value="הלוגים נכבו בהצלחה", inline=False)
          embed.set_footer(text="$on_logs אם אתם תרצו להדליק אותם חזרה נא לכתוב")
          await ctx.message.author.send(embed=embed)
        if data[p] == "1":
          print("None")
      if str(ctx.message.author.id) not in data:
        embed=discord.Embed(color=0xfff700)
        embed.set_thumbnail(url="https://fkutaman.ru/images/warning.png")
        embed.add_field(name="ERROR", value=".אתם לא ברשימת האדמינים", inline=False)
        embed.add_field(name="פתרון הבעיה", value="ולכתוב בא הוכחה שאתם מורה זה נעשה בשביל להגן מספאם request נא לעשות בקשת הוספה לאדמינים בעזרת הפקודה", inline=False)
        embed.set_footer(text="ERROR_ADMIN_SIGN_IN")
        await ctx.message.author.send(embed=embed)

@bot.command()
async def on_logs(ctx):
   array_to_json = {str(ctx.message.author.id) : '0'}
   with open('users.json', 'r') as json_file:
    data = json.load(json_file)
    json_file.close()
    for p in data:
      if p == str(ctx.message.author.id):
        if data[p] == "1":
          data[p] = "0"
          jsonFile = open("users.json", "w+")
          jsonFile.write(json.dumps(data))
          jsonFile.close()
          embed=discord.Embed(color=0x00ff40)
          embed.add_field(name="הדלקת לוגים", value="הלוגים נדלקו בהצלחה", inline=False)
          embed.set_footer(text="$off_logs אם אתם תרצו לכבות אותם נא לכתוב")
          await ctx.message.author.send(embed=embed)
      if str(ctx.message.author.id) not in data:
        embed=discord.Embed(color=0xfff700)
        embed.set_thumbnail(url="https://fkutaman.ru/images/warning.png")
        embed.add_field(name="ERROR", value=".אתם לא ברשימת האדמינים", inline=False)
        embed.add_field(name="פתרון הבעיה", value="ולכתוב בא הוכחה שאתם מורה זה נעשה בשביל להגן מספאם request נא לעשות בקשת הוספה לאדמינים בעזרת הפקודה", inline=False)
        embed.set_footer(text="ERROR_ADMIN_SIGN_IN")
        await ctx.message.author.send(embed=embed)

@bot.command()
async def request(ctx, *, args):
    array_to_json = {str(ctx.message.author.id) : str(args)}
    with open("request.json", "r") as json_file:
       data = json.load(json_file)
       json_file.close()
       data.update(array_to_json)
       with open('request.json', 'w') as f:
            json.dump(data, f)
       user = bot.get_user(373718196794032130)
       embed=discord.Embed(color=0x00e1ff)
       embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/hotel-vacation/33/bell_2-2-512.png")
       embed.add_field(name=f"ID:{str(ctx.message.author.id)} / Name:{str(ctx.message.author)}", value=f"{data[str(ctx.message.author.id)]}", inline=False)
       await user.send(embed=embed)
@bot.command()
async def request_answer(ctx, *, id):
  with open('users.json', 'r') as json_file:
    data = json.load(json_file)
    json_file.close()
    for b in data:
      if str(message.author.id) in data:
        with open('request.json', 'r') as json_file:
          data = json.load(json_file)
          json_file.close()
          user = bot.get_user(373718196794032130)
          for a in data:
             if id in data:
               a_dict = {str(a) : "0"}
               data.update(a_dict)
               with open('users.json', 'w') as f:
                 json.dump(data, f)
@bot.command()
async def warns_list(ctx):
 with open('users.json', 'r') as s:
   a = json.load(s)
   s.close()
   if str(ctx.message.author.id) in a:
      with open('warn.json', 'r') as f:
       data = json.load(f)
       f.close()
       warnlist = []
       for b in data:
           if len(b) == 18:
             warnlist.append(f"{bot.get_user(int(b))}| {data[b]}\n")
       a = "".join(warnlist)
       embed=discord.Embed(color=0xff0000)
       embed.add_field(name="מספר אזהרות | שם משתמש", value=f"{a}", inline=False)
       await ctx.message.author.send(embed=embed)
       warnlist.clear()
@bot.command()
async def work(ctx):
  with open('economic.json', 'r') as f:
    data = json.load(f)
    f.close()
    with open('economic_business.json', 'r') as s:
       dataa = json.load(s)
       s.close()
       with open('anti_spam_economic.json', 'r') as p:
         dataaa = json.load(p)
         p.close()
         if str(ctx.message.author.id) not in data or str(ctx.message.author.id) not in dataa or str(ctx.message.author.id) not in dataaa:
           array_econom = {str(ctx.message.author.id) : "0"}
           array_business = {str(ctx.message.author.id) : "0"}
           array_anti_spam = {str(ctx.message.author.id) : "0"}
           data.update(array_econom)
           dataa.update(array_business)
           dataaa.update(array_anti_spam)
           with open('economic.json', 'w+') as s:
               json.dump(data, s)
           with open('economic_business.json', 'w+') as x:
               json.dump(dataa, x)
           with open('anti_spam_economic.json', 'w+') as c:
               json.dump(dataaa, c)
           embed=discord.Embed(title="ERROR", color=0xff0000)
           embed.add_field(name="User_Find_Error:", value="אתה לא הייתה נמצא ברשימה של הכלכלת השרת", inline=False)
           embed.add_field(name="פתרון", value="הוספנו אותך לרשימה ובשביל להתחיל להרוויח כסף נא לכתוב את הפקודה הזאת עוד פעם", inline=True)
           embed.set_footer(text="מקסים היה פה")
           await ctx.message.channel.send(embed=embed)
         else:
          if dataaa[str(ctx.message.author.id)] == "0":
             money = data[str(ctx.message.author.id)] # --> 0
             embed=discord.Embed(color=0xffffff)
             embed.add_field(name="עבודה", value=f"***לבשתם בגדים והלכתם לעוד יום עבודה קשה {ctx.message.author.mention}***", inline=False)
             await ctx.message.channel.send(embed=embed)
             a_dict = {str(ctx.message.author.id) : "1"}
             dataaa.update(a_dict)
             with open('anti_spam_economic.json', 'w') as f:
                json.dump(dataaa, f)
             duration_work = random.randint(20, 60)
             await asyncio.sleep(duration_work)
             def func():
                with open('economic_business.json', 'r') as s:
                 dataa = json.load(s)
                 s.close()
                if dataa[str(ctx.message.author.id)] == "0":
                  value = random.randint(20, 100)
                  return value
                if dataa[str(ctx.message.author.id)] == "1":
                  value = random.randint(50, 200) + 50
                  return value
                if dataa[str(ctx.message.author.id)] == "2":
                  value = random.randint(60, 220) + 85
                  return value
                if dataa[str(ctx.message.author.id)] == "3":
                  value = random.randint(85, 238) + 125
                  return value
                if dataa[str(ctx.message.author.id)] == "4":
                  value = random.randint(105, 300) + 260
                  return value
                if dataa[str(ctx.message.author.id)] == "5":
                  value = random.randint(110, 500) + 410
                  return value
                if dataa[str(ctx.message.author.id)] == "6":
                  value = random.randint(115, 700) + 590
                  return value
                if dataa[str(ctx.message.author.id)] == "7":
                  value = random.randint(200, 900) + 890
                  return value
             _money_after_work = func()
             print(_money_after_work)
             data[str(ctx.message.author.id)] = str(int(money) + _money_after_work)
             jsonFile = open("economic.json", "w+")
             jsonFile.write(json.dumps(data))
             jsonFile.close()
             embed=discord.Embed(color=0xffffff)
             embed.add_field(name="עבודה", value=f"***סיימתם לעבוד וקיבלתם {ctx.message.author.mention}***\n***שקלים {_money_after_work}***", inline=False)
             await ctx.message.channel.send(embed=embed)
             a_dict = {str(ctx.message.author.id) : "0"}
             dataaa.update(a_dict)
             with open('anti_spam_economic.json', 'w') as f:
                json.dump(dataaa, f)
          if dataaa[str(ctx.message.author.id)] == "1":
            embed=discord.Embed(title="ASS(Anti-Spam-System) ", description="--------------------------------", color=0xff0000)
            embed.add_field(name="!אתם כבר בעבודה!", value="אסור לאספים! תחכו עד שתסיימו לעבוד", inline=False)
            await ctx.message.channel.send(embed=embed)
@bot.command()
async def shop(ctx):
  embed=discord.Embed(title="__**חנות**__", description="פה אתם יכולים לקנות ביזנס", color=0xa8ffb7)
  embed.add_field(name="(דוחן פלאפל (200", value="$buy 1 : לקניה תכתבו ", inline=True)
  embed.add_field(name="(מלך השקל (1200", value="$buy 2 : לקניה תכתבו ", inline=True)
  embed.add_field(name="(מאפייה (2900", value="$buy 3 : לקניה תכתבו ", inline=True)
  embed.add_field(name="(חנות בגדים (4100", value="$buy 4 : לקניה תכתבו ", inline=True)
  embed.add_field(name="(חנות יוקרה (5800", value="$buy 5 : לקניה תכתבו ", inline=True)
  embed.add_field(name="(מסעדה יוקרתית (7850", value="$buy 6 : לקניה תכתבו ", inline=True)
  embed.add_field(name="(סופר-מרקט (10000", value="$buy 7 : לקניה תכתבו ", inline=True) # כשדרכשכדש
  await ctx.message.channel.send(embed=embed)
@bot.command()
async def buy(ctx, *, num):
  with open('economic.json', 'r') as f:
    data = json.load(f)
    f.close()
  with open('economic_business.json', 'r') as x:
    dataa = json.load(x)
    x.close()
  if num == "1":
    if str(ctx.message.author.id) in data and str(ctx.message.author.id) in dataa:
         if int(data[str(ctx.message.author.id)]) > 200 or int(data[str(ctx.message.author.id)]) == 200:
           data[str(ctx.message.author.id)] = str(int(data[str(ctx.message.author.id)]) - 200)
           jsonFile = open("economic.json", "w+")
           jsonFile.write(json.dumps(data))
           jsonFile.close()
           dataa[str(ctx.message.author.id)] = "1"
           jsonFile = open("economic_business.json", "w+")
           jsonFile.write(json.dumps(dataa))
           jsonFile.close()
           embed=discord.Embed(title=" __**קנייה**__", color=0xff8080)
           embed.set_thumbnail(url=ctx.message.author.avatar_url)
           embed.add_field(name="__**תשלום**__", value="-200", inline=True)
           embed.add_field(name="__**ביזנס**__", value="דוחן פלאפל", inline=True)
           embed.set_footer(text="!אין החזר כספי!")
           await ctx.message.channel.send(embed=embed)
         else:
           embed=discord.Embed(title="תשלום", description="------------", color=0xff0000)
           embed.add_field(name="בעיה בעברת התשלום", value="אין לכם את כמות הכסף שרציתם לעביר", inline=True) 
           await ctx.message.channel.send(embed=embed)
    else:
           embed=discord.Embed(title="ERROR", color=0xff0000)
           embed.add_field(name="User_Find_Error:", value="אתה לא הייתה נמצא ברשימה של הכלכלת השרת", inline=False)
           embed.add_field(name="פתרון", value="הוספנו אותך לרשימה ובשביל להתחיל להרוויח כסף נא לכתוב את הפקודה הזאת עוד פעם", inline=True)
           embed.set_footer(text="מקסים היה פה")
           await ctx.message.channel.send(embed=embed)
  if num == "2":
    if str(ctx.message.author.id) in data and str(ctx.message.author.id) in dataa:
         if int(data[str(ctx.message.author.id)]) > 1200 or int(data[str(ctx.message.author.id)]) == 1200:
           data[str(ctx.message.author.id)] = str(int(data[str(ctx.message.author.id)]) - 1200)
           jsonFile = open("economic.json", "w+")
           jsonFile.write(json.dumps(data))
           jsonFile.close()
           dataa[str(ctx.message.author.id)] = "2"
           jsonFile = open("economic_business.json", "w+")
           jsonFile.write(json.dumps(dataa))
           jsonFile.close()
           embed=discord.Embed(title=" __**קנייה**__", color=0xff8080)
           embed.set_thumbnail(url=ctx.message.author.avatar_url)
           embed.add_field(name="__**תשלום**__", value="-1200", inline=True)
           embed.add_field(name="__**ביזנס**__", value="מלך השקל", inline=True)
           embed.set_footer(text="!אין החזר כספי!")
           await ctx.message.channel.send(embed=embed)
         else:
           embed=discord.Embed(title="תשלום", description="------------", color=0xff0000)
           embed.add_field(name="בעיה בעברת התשלום", value="אין לכם את כמות הכסף שרציתם לעביר", inline=True) 
           await ctx.message.channel.send(embed=embed)
  if num == "3":
    if str(ctx.message.author.id) in data and str(ctx.message.author.id) in dataa:
         if int(data[str(ctx.message.author.id)]) > 2900 or int(data[str(ctx.message.author.id)]) == 2900:
           data[str(ctx.message.author.id)] = str(int(data[str(ctx.message.author.id)]) - 2900)
           jsonFile = open("economic.json", "w+")
           jsonFile.write(json.dumps(data))
           jsonFile.close()
           dataa[str(ctx.message.author.id)] = "3"
           jsonFile = open("economic_business.json", "w+")
           jsonFile.write(json.dumps(dataa))
           jsonFile.close()
           embed=discord.Embed(title=" __**קנייה**__", color=0xff8080)
           embed.set_thumbnail(url=ctx.message.author.avatar_url)
           embed.add_field(name="__**תשלום**__", value="-2900", inline=True)
           embed.add_field(name="__**ביזנס**__", value="מאפייה", inline=True)
           embed.set_footer(text="!אין החזר כספי!")
           await ctx.message.channel.send(embed=embed)
         else:
           embed=discord.Embed(title="תשלום", description="------------", color=0xff0000)
           embed.add_field(name="בעיה בעברת התשלום", value="אין לכם את כמות הכסף שרציתם לעביר", inline=True) 
           await ctx.message.channel.send(embed=embed)
  if num == "4":
    if str(ctx.message.author.id) in data and str(ctx.message.author.id) in dataa:
         if int(data[str(ctx.message.author.id)]) > 4100 or int(data[str(ctx.message.author.id)]) == 4100:
           data[str(ctx.message.author.id)] = str(int(data[str(ctx.message.author.id)]) - 4100)
           jsonFile = open("economic.json", "w+")
           jsonFile.write(json.dumps(data))
           jsonFile.close()
           dataa[str(ctx.message.author.id)] = "4"
           jsonFile = open("economic_business.json", "w+")
           jsonFile.write(json.dumps(dataa))
           jsonFile.close()
           embed=discord.Embed(title=" __**קנייה**__", color=0xff8080)
           embed.set_thumbnail(url=ctx.message.author.avatar_url)
           embed.add_field(name="__**תשלום**__", value="-4100", inline=True)
           embed.add_field(name="__**ביזנס**__", value="חנות בגדים", inline=True)
           embed.set_footer(text="!אין החזר כספי!")
           await ctx.message.channel.send(embed=embed)
         else:
           embed=discord.Embed(title="תשלום", description="------------", color=0xff0000)
           embed.add_field(name="בעיה בעברת התשלום", value="אין לכם את כמות הכסף שרציתם לעביר", inline=True) 
           await ctx.message.channel.send(embed=embed)
  if num == "5":
    if str(ctx.message.author.id) in data and str(ctx.message.author.id) in dataa:
         if int(data[str(ctx.message.author.id)]) > 5800 or int(data[str(ctx.message.author.id)]) == 5800:
           data[str(ctx.message.author.id)] = str(int(data[str(ctx.message.author.id)]) - 5800)
           jsonFile = open("economic.json", "w+")
           jsonFile.write(json.dumps(data))
           jsonFile.close()
           dataa[str(ctx.message.author.id)] = "5"
           jsonFile = open("economic_business.json", "w+")
           jsonFile.write(json.dumps(dataa))
           jsonFile.close()
           embed=discord.Embed(title=" __**קנייה**__", color=0xff8080)
           embed.set_thumbnail(url=ctx.message.author.avatar_url)
           embed.add_field(name="__**תשלום**__", value="-5800", inline=True)
           embed.add_field(name="__**ביזנס**__", value="חנות יוקרה ", inline=True)
           embed.set_footer(text="!אין החזר כספי!")
           await ctx.message.channel.send(embed=embed)
         else:
           embed=discord.Embed(title="תשלום", description="------------", color=0xff0000)
           embed.add_field(name="בעיה בעברת התשלום", value="אין לכם את כמות הכסף שרציתם לעביר", inline=True) 
           await ctx.message.channel.send(embed=embed)
  if num == "6":
    if str(ctx.message.author.id) in data and str(ctx.message.author.id) in dataa:
         if int(data[str(ctx.message.author.id)]) > 7850 or int(data[str(ctx.message.author.id)]) == 7850:
           data[str(ctx.message.author.id)] = str(int(data[str(ctx.message.author.id)]) - 7850)
           jsonFile = open("economic.json", "w+")
           jsonFile.write(json.dumps(data))
           jsonFile.close()
           dataa[str(ctx.message.author.id)] = "6"
           jsonFile = open("economic_business.json", "w+")
           jsonFile.write(json.dumps(dataa))
           jsonFile.close()
           embed=discord.Embed(title=" __**קנייה**__", color=0xff8080)
           embed.set_thumbnail(url=ctx.message.author.avatar_url)
           embed.add_field(name="__**תשלום**__", value="-7850", inline=True)
           embed.add_field(name="__**ביזנס**__", value="מסעדה יוקרתית", inline=True)
           embed.set_footer(text="!אין החזר כספי!")
           await ctx.message.channel.send(embed=embed)
         else:
           embed=discord.Embed(title="תשלום", description="------------", color=0xff0000)
           embed.add_field(name="בעיה בעברת התשלום", value="אין לכם את כמות הכסף שרציתם לעביר", inline=True) 
           await ctx.message.channel.send(embed=embed)
  if num == "7":
    if str(ctx.message.author.id) in data and str(ctx.message.author.id) in dataa:
         if int(data[str(ctx.message.author.id)]) > 10000 or int(data[str(ctx.message.author.id)]) == 10000:
           data[str(ctx.message.author.id)] = str(int(data[str(ctx.message.author.id)]) - 10000)
           jsonFile = open("economic.json", "w+")
           jsonFile.write(json.dumps(data))
           jsonFile.close()
           dataa[str(ctx.message.author.id)] = "7"
           jsonFile = open("economic_business.json", "w+")
           jsonFile.write(json.dumps(dataa))
           jsonFile.close()
           embed=discord.Embed(title=" __**קנייה**__", color=0xff8080)
           embed.set_thumbnail(url=ctx.message.author.avatar_url)
           embed.add_field(name="__**תשלום**__", value="-10000", inline=True)
           embed.add_field(name="__**ביזנס**__", value="סופר-מרקט", inline=True)
           embed.set_footer(text="!אין החזר כספי!")
           await ctx.message.channel.send(embed=embed)
         else:
           embed=discord.Embed(title="תשלום", description="------------", color=0xff0000)
           embed.add_field(name="בעיה בעברת התשלום", value="אין לכם את כמות הכסף שרציתם לעביר", inline=True) 
           await ctx.message.channel.send(embed=embed)
@bot.command()
async def eco_info(ctx):
  with open('economic.json', 'r') as f:
    data = json.load(f)
    f.close()
    with open('economic_business.json', 'r') as x:
      dataa = json.load(x)
      x.close()
      if str(ctx.message.author.id) in data and str(ctx.message.author.id) in dataa:
        if dataa[str(ctx.message.author.id)] != "0":
         embed=discord.Embed(title=" __***פרופיל***__", color=0xff8080)
         embed.set_thumbnail(url= ctx.message.author.avatar_url)
         embed.add_field(name=" __**כסף**__", value=f"{data[str(ctx.message.author.id)]}", inline=False)
         embed.add_field(name="__**מספר הביזנס בחנות**__", value=f"{dataa[str(ctx.message.author.id)]}", inline=True)
         await ctx.message.channel.send(embed=embed)
        else:
         embed=discord.Embed(title=" __***פרופיל***__", color=0xff8080)
         embed.set_thumbnail(url= ctx.message.author.avatar_url)
         embed.add_field(name=" __**כסף**__", value=f"{data[str(ctx.message.author.id)]}", inline=False)
         embed.add_field(name="__**מספר הביזנס בחנות**__", value=f"!אין ביזנס!", inline=True)
         await ctx.message.channel.send(embed=embed)
      else:
           embed=discord.Embed(title="ERROR", color=0xff0000)
           embed.add_field(name="User_Find_Error:", value="אתה לא הייתה נמצא ברשימה של הכלכלת השרת", inline=False)
           embed.add_field(name="פתרון", value="הוספנו אותך לרשימה ובשביל להתחיל להרוויח כסף נא לכתוב את הפקודה הזאת עוד פעם", inline=True)
           embed.set_footer(text="מקסים היה פה")
           await ctx.message.channel.send(embed=embed)
@bot.command()
async def cmd_help(ctx):
  embed=discord.Embed(title="__**עזרה בפקודות**__", color=0xff8080)
  embed.set_thumbnail(url=ctx.message.author.avatar_url)
  embed.add_field(name="כלכלת השרת", value="--------------", inline=True)
  embed.add_field(name="$work", value="להתחיל לעבוד ולקבל כסף", inline=False)
  embed.add_field(name="$shop", value="לראות את החנות של הביזנסים", inline=True)
  embed.add_field(name="ביזנס", value="אם אתם קונים ביזנס \n אז גם השכר שלכם עולה", inline=True)
  embed.add_field(name="$buy ", value="לקנות את מה שבחנות", inline=False)
  embed.add_field(name="$eco_info", value="הפרופיל שלכם בכלכלת השרת", inline=True)
  embed.add_field(name="$pay", value="לשלם למישהו כסף", inline=True)
  embed.set_footer(text="_מקסים היה פה_")
  await ctx.message.channel.send(embed=embed)
@bot.command()
async def pay(ctx, member: discord.Member, *, money: int=None):
    with open('economic.json', 'r') as f:
        data = json.load(f)
        f.close()
        if str(ctx.message.author.id) in data and str(member.id) in data and str(member.id) != str(ctx.message.author.id):
           if int(data[str(ctx.message.author.id)]) > int(money) or int(data[str(ctx.message.author.id)]) == int(money):
             data[str(ctx.message.author.id)] = str(int(data[str(ctx.message.author.id)]) - int(money))
             data[str(member.id)] = str(int(data[str(member.id)]) + int(money))
             jsonFile = open("economic.json", "w+")
             jsonFile.write(json.dumps(data))
             jsonFile.close()
             embed=discord.Embed(title="__***עברת כסף***__", color=0xff0000)
             embed.set_thumbnail(url=ctx.message.author.avatar_url)
             embed.add_field(name="כסף", value=f"{money}", inline=True)
             embed.add_field(name="למי", value=f"{member}", inline=True)
             embed.set_footer(text="מקסים היה פה")
             await ctx.message.channel.send(embed=embed)
        elif str(member.id) == str(ctx.message.author.id):
          embed=discord.Embed(title="!נסיון יפה!", description="-----------------", color=0xff0000)
          embed.add_field(name="**אחלה נסיון**", value="***:sunglasses:  לשלם לעצמכם תמיד תספיקו :sunglasses: ***", inline=False)
          await ctx.message.channel.send(embed=embed)
        else:
          embed=discord.Embed(title="User_Find_Error:", description="-----------------", color=0xff0000)
          embed.add_field(name="**לא היה נמצא המשתמש שחיפשתם**", value="***!משתמש היינו רשום ברשימת המשתמשים של כלכלת השרת!***", inline=False)
          await ctx.message.channel.send(embed=embed)
@bot.command()
async def eco_player_info(ctx, member: discord.Member):
  with open('economic.json', 'r') as f:
    data = json.load(f)
    f.close()
    with open('economic_business.json', 'r') as x:
      dataa = json.load(x)
      x.close()
      if str(member.id) in data and str(member.id) in dataa:
       if dataa[str(member.id)] != "0":
         embed=discord.Embed(title=" __***פרופיל***__", color=0xff8080)
         embed.set_thumbnail(url= member.avatar_url)
         embed.add_field(name=" __**כסף**__", value=f"{data[str(member.id)]}", inline=False)
         embed.add_field(name="__**מספר הביזנס בחנות**__", value=f"{dataa[str(member.id)]}", inline=True)
         await ctx.message.channel.send(embed=embed)
       else:
         embed=discord.Embed(title=" __***פרופיל***__", color=0xff8080)
         embed.set_thumbnail(url= member.avatar_url)
         embed.add_field(name=" __**כסף**__", value=f"{data[str(member.id)]}", inline=False)
         embed.add_field(name="__**מספר הביזנס בחנות**__", value=f"!אין ביזנס!", inline=True)
         await ctx.message.channel.send(embed=embed)
      else:
          embed=discord.Embed(title="User_Find_Error:", description="-----------------", color=0xff0000)
          embed.add_field(name="**לא היה נמצא המשתמש שחיפשתם**", value="***!משתמש היינו רשום ברשימת המשתמשים של כלכלת השרת!***", inline=False)
          await ctx.message.channel.send(embed=embed)
@bot.command()
async def set_money(ctx, member: discord.Member, *, money):
  with open('users.json', 'r') as d:
    data = json.load(d)
    d.close()
  with open('economic.json', 'r') as s:
      dataa = json.load(s)
      s.close()
  if str(ctx.message.author.id) in data:
    if str(member.id) in dataa:
      array_to_json = {str(member.id) : str(money)}
      dataa.update(array_to_json)
      with open('economic.json', 'w') as f:
          json.dump(dataa, f)
@bot.command()
async def set_business(ctx, member: discord.Member, *, money):
  with open('users.json', 'r') as d:
    data = json.load(d)
    d.close()
  with open('economic_business.json', 'r') as s:
      dataa = json.load(s)
      s.close()
  if str(ctx.message.author.id) in data:
    if str(member.id) in dataa:
      if int(money) <= 7:
         array_to_json = {str(member.id) : str(money)}
         dataa.update(array_to_json)
         with open('economic_business.json', 'w') as f:
            json.dump(dataa, f)
@bot.command()
async def set_news(ctx):
bot.run('Njc3MTYzMjg0MjY0MjU1NDg4.XkWuPw.fJtapSDa_LZysRwcdWbxUFRrzG8')