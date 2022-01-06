from discord.ext import commands

def getMediaType(argument):
    switcher = {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/svg+xml": ".svg",
        "application/pdf": ".pdf",
        "video/webm": ".webm",
        "video/mp4": ".mp4",
    }
    result = switcher.get(argument, "nothing")
    if(result == "nothing"):
        raise ValueError("The given file format for this media is not compatible")
    return result