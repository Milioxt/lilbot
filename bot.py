import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme/orslokx')
  json_data = json.loads(response.text)
  return json_data

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
        return
    if message.content.startswith('$meme'):
        meme_data = get_meme()

        embed = discord.Embed(
           title=meme_data['title'],
            url=meme_data['postLink'],
            color=discord.Color.blue()
        )
        embed.set_image(url=meme_data['url'])
        embed.set_footer(text=f"Subreddit: r/{meme_data['subreddit']}")

        await message.channel.send(embed=embed)



intents = discord.Intents.default()
intents.message_content = True