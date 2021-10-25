import numpy as np
# import discord
import discord
import asyncio
from discord import Member
from io import BytesIO
from PIL import Image, ImageChops, ImageDraw
from discord.ext import commands

botToken = '***'

client = commands.Bot(command_prefix='.')

img1 = Image.open("img/doctor.jpg")
img2 = Image.open("stethoscope-840125__340.webp")

# image = Image.blend(img1, img2, alpha=0.5)

# merged = ImageChops.multiply(img1, img2)

# merged.show()
@client.event
async def on_member_join(member: Member):
    welcome = Image.open("img/doctor.jpg")

    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    img = Image.open(data).convert("RGB")
    npImage = np.array(img)
    h, w = img.size

    alpha = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)
    npAlpha = np.array(alpha)
    npImage = np.dstack((npImage, npAlpha))
    pfp = Image.fromarray(npImage)
    welcome.paste(pfp, (657, 257))
    welcome.save("profile.jpg")
    
# async on_member = await on_member_join(Member)

print(on_member_join(Member))
