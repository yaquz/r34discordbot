# мне лень было делить на коги поэтому всё в основном файле

import discord
from discord.ext import commands
import asyncio
import random
from pyrule34 import AsyncRule34

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# функция дабы бот не кидал один и тотже контент
async def find_unique_post(r34, tag_list):
    page_id = 0
    while True:
        posts = await r34.search(tags=tag_list, page_id=page_id)
        if not posts:
            return None
        random.shuffle(posts)
        return posts[0]
        page_id += 1

#команда для порно
@bot.command(name="порно", aliases=["r34", "парнуха"])
async def send_picture(ctx, *, tags=""):
    async with AsyncRule34() as r34:
        try:
            tag_list = tags.split() if tags else ["random"]
            post = await find_unique_post(r34, tag_list)
            if post is None:
                await ctx.send("я ничё не нашёл сходи нахуй. мяу!")
                return
            
            await ctx.send(post.file_url)
        except Exception as e:
            await ctx.send("что-то пошло не так а что я хуй знает пиши разрабу")
            await ctx.send(f"```{str(e)}```")
