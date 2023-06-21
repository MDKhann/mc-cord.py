import threading
import discord
from discord.ext import commands
import customtkinter as tkinter


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gui_thread = None

    async def on_ready(self):
        print(f"Logged in as {self.user.name} ({self.user.id})")

    async def send_message(self, guild_id, channel_id, message):
        guild = self.get_guild(guild_id)
        if guild is None:
            print(f"Guild with ID {guild_id} not found.")
            return

        channel = guild.get_channel(channel_id)
        if channel is None:
            print(f"Channel with ID {channel_id} not found.")
            return

        await channel.send(message)


def start_gui(bot):
    root = tkinter.CTk()

    guild_id_var = tkinter.StringVar()
    channel_id_var = tkinter.StringVar()
    message_var = tkinter.StringVar()


    guild_id_entry = tkinter.CTkEntry(root, textvariable=guild_id_var)
    channel_id_entry = tkinter.CTkEntry(root, textvariable=channel_id_var)
    message_entry = tkinter.CTkEntry(root, textvariable=message_var)


    def send_message():
        guild_id = int(guild_id_var.get())
        channel_id = int(channel_id_var.get())
        message = message_var.get()
        bot.loop.create_task(bot.send_message(guild_id, channel_id, message))


    send_button = tkinter.CTkButton(root, text="Send", command=send_message, fg_color="green")

    guild_id_entry.grid(row=0, column=0)
    channel_id_entry.grid(row=1, column=0)
    message_entry.grid(row=2, column=0)
    send_button.grid(row=3, column=0)

    root.mainloop()

bot = Bot(command_prefix="!")


gui_thread = threading.Thread(target=start_gui, args=(bot,))
bot.gui_thread = gui_thread
gui_thread.start()


bot.run("MTA4Mzk2MTIzNTA1OTUxNTUwNA.GYKysP.YpQ2MmW18rFJ081ILg1vS55usne7kGvkP4xH_Y") # Tobias Alyana code