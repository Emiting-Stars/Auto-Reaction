from pyrogram import Client
from config import Config as tg

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="tgbot",
            api_id=tg.API_ID,
            api_hash=tg.API_HASH,
            bot_token=tg.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=10,
        )

    
    async def start(self):
        await super().start()
        me = await self.get_me()
        self.name = me.first_name
        print(f'{me.first_name} Is sᴛᴀʀᴛᴇᴅ...🥶')

    async def stop(self, *args):
        await super().stop()      
        print("Bᴏᴛ ʀᴇsᴛᴀʀᴛɪɴɢ...✨")
       
                           
  
app = Bot()
app.run()


        










