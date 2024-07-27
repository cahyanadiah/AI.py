import discord
from password import gen_pass
from discord.ext import commands
import os
import random
from AI import cek

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def bye(ctx, count_heh = 5):
    await ctx.send("bye" * count_heh)
    
@bot.command()
async def password(ctx, pass_length = 10):
    await ctx.send(gen_pass(pass_length))

@bot.command()
async def tebakkata(ctx):
    await ctx.send(f'Lemari apa yang bisa dimasukkan kantong? (jawab dengan $jawab jawaban)')

@bot.command()
async def jawab(ctx, jawaban=""):
    if jawaban.lower() == "lemaribuan":
        await ctx.send(f'Jawaban anda benar')
    else:
        await ctx.send(f'Jawaban anda salah')

@bot.command()
async def sampah(ctx, jenis=""):
    if jenis.lower() == "plastik":
        await ctx.send(f'plastik baru bisa terurai selama 1000 tahun lamanya')
    elif jenis.lower() == "kertas":
        await ctx.send(f'kertas dapat terurai selama 6 bulan')
    elif jenis.lower() == "makanan":
        await ctx.send(f'sampah makanan membutuhkan waktu terurai selama 4 minggu')


@bot.command()
async def mem(ctx):
    img_name =  random.choice(os.listdir('images'))

    with open('images/'+img_name, 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def save_image(ctx):
    # Cek jika ada lampiran dalam pesan
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Unduh dan simpan gambar menggunakan discord.py
                file_path = f'./{attachment.filename}'
                await attachment.save(file_path)
                await ctx.send(f'Gambar {attachment.filename} telah disimpan.')

                await ctx.send(cek(file_path))
    else:
        await ctx.send('Tidak ada lampiran gambar dalam pesan.')

# Jalankan bot
bot.run("")