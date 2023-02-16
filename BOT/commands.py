# -*- coding: utf-8 -*-

import nextcord, requests
from nextcord.ext.commands import Cog, command
from utils import Debug, JSON, now, TextClearer
from nextcord import Embed, Interaction, SlashOption, slash_command

class Commands(Cog):

	def __init__(self, client): self.client = client

	@Cog.listener()
	async def on_ready(self): Debug.Good(f"{self.__cog_name__} loaded successfully!")

	@slash_command(name = "profile", description = "Profile command.")
	async def test(self, interaction: Interaction): pass

	#if no user is mentioned, it will check the author's profile
	@test.subcommand(name = "checkprofile", description = "Checks someone's profile or your own profile if no one is mentioned.")
	async def checkprofile(self, interaction: Interaction, user: nextcord.User = None):
		try:
			if user == None: 
				user = interaction.user
			else:
				user = user
			url = f"http://127.0.0.1:4000/api/discord/members/{user.id}"
			response = requests.get(url)
			data = response.json()
			embed = Embed(title = f"{user}'s profile", description = f"**Name:** {data['fname']}\n**Email:** {data['email']}", color = 0x00ff00)
			await interaction.response.send_message(embed = embed)
		except Exception as Error: await interaction.response.send_message(f"> **An error has occurred while checking your profile: ```\n{Error}```")

  

def setup(client):
	client.add_cog(Commands(client))