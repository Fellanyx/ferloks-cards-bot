import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

TOKEN = "8658294878:AAEUoXWCb0sLUQdloFrmSX_ZRpDX8ZdRX7c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

CARDS_FOLDER = "cards"

CARDS = {
    "Bellingham.png": ("🏴󠁧󠁢󠁥󠁮󠁧󠁿", "Bellingham", "98"),
    "Courtois.png": ("🇧🇪", "Courtois", "95"),
    "CristianoRonaldo.png": ("🇵🇹", "Cristiano Ronaldo", "88"),
    "Dembele.png": ("🇫🇷", "Dembele", "91"),
    "FerranTorres.png": ("🇪🇸", "Ferran Torres", "98"),
    "Gabriel.png": ("🇧🇷", "Gabriel", "97"),
    "Guler.png": ("🇹🇷", "Guler", "96"),
    "Haaland.png": ("🇳🇴", "Haaland", "92"),
    "Hazard.png": ("🇧🇪", "Hazard", "94"),
    "JoaoCancelo.png": ("🇵🇹", "Joao Cancelo", "95"),
    "LamineYamal.png": ("🇪🇸", "Lamine Yamal", "90"),
    "Lukaku.png": ("🇧🇪", "Lukaku", "95"),
    "Maldini.png": ("🇮🇹", "Maldini", "94"),
    "Maradona.png": ("🇦🇷", "Maradona", "99"),
    "MarcCucurella.png": ("🇪🇸", "Marc Cucurella", "95"),
    "Mbappe.png": ("🇫🇷", "Mbappe", "92"),
    "Messi.png": ("🇦🇷", "Messi", "97"),
    "NeymarJr.png": ("🇧🇷", "Neymar Jr", "97"),
    "NicoWilliams.png": ("🇪🇸", "Nico Williams", "96"),
    "PauCubarsi.png": ("🇪🇸", "Pau Cubarsi", "97"),
    "Pedri.png": ("🇪🇸", "Pedri", "92"),
    "Pogba.png": ("🇫🇷", "Pogba", "98"),
    "Raphinha.png": ("🇧🇷", "Raphinha", "97"),
    "Ronaldinho.png": ("🇧🇷", "Ronaldinho", "99"),
    "Salah.png": ("🇪🇬", "Salah", "97"),
    "Suarez.png": ("🇺🇾", "Suarez", "89"),
    "Valverde.png": ("🇺🇾", "Valverde", "98"),
    "VanDijk.png": ("🇳🇱", "Van Dijk", "99"),
    "ViniJr.png": ("🇧🇷", "Vini Jr", "90"),
    "Vozinha.png": ("🇨🇻", "Vozinha", "96"),
    "Zidane.png": ("🇫🇷", "Zidane", "95"),
}

def get_random_card():
    available = []
    for filename in CARDS:
        if os.path.exists(f"{CARDS_FOLDER}/{filename}"):
            available.append(filename)
    return random.choice(available) if available else None

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🃏 *Ferloks Cards* приветствует тебя!\n\n"
        "/FerloksCards — тянуть случайную карточку",
        parse_mode="Markdown"
    )

@dp.message(Command("FerloksCards"))
async def ferloks_cards(message: types.Message):
    card = get_random_card()
    
    if card is None:
        await message.answer("❌ Карточек нет. Закинь PNG в папку cards/")
        return
    
    flag, name, rating = CARDS[card]
    
    caption = (
        f"*{flag} Карточка {name} Разблокирована!*\n"
        f"⭐️ *Рейтинг: {rating}*"
    )
    
    photo = FSInputFile(f"{CARDS_FOLDER}/{card}")
    
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=caption,
        parse_mode="Markdown"
    )

async def main():
    print("⚽ Ferloks Cards запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
