from os import environ as env

class Config:
    API_ID = int(env.get("API_ID", "28744454")) #TG API ID
    API_HASH = env.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7") #TG API HASH
    BOT_TOKEN = env.get("BOT_TOKEN", "7560586869:AAG7uvxJQXURcatwG92E38kq_zEsDJ7WIdQ") #Add Bot Token, get from botfather
    FSUB_ID = int(env.get("FSUB_ID", "-1002410513772"))  #Add Your FSub Channel Id -100xxxxxxxxx
    FSUB = bool(env.get("FSUB", True)) #Keep True If U Want Force Subscribe         
    #Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
    PICS = (os.environ.get("PICS", "https://envs.sh/sJX.jpg https://envs.sh/Uc0.jpg https://envs.sh/UkA.jpg https://envs.sh/Uk_.jpg https://envs.sh/Ukc.jpg https://envs.sh/UkZ.jpg https://envs.sh/UkK.jpg")).split() #Required 
    BOT_USERNAME = env.get("BOT_USERNAME", "Emiting_Auto_Reaction_Bot") # Add Bot Username Without @
    EMOJIS = [
        "👍", "😚", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢",
        "🥶", "🤩", "🤮", "🤯",
        "🙏", "👌", "🤣", "🤡",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "🍼", "🏆",
        "💔", "🤨", "😐", "😡",
        "💥", "🆒", "💦", "😈",
        "😴", "😭", "👻", "⚡",
        "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]

#Emiting_Stars
#RexySama
