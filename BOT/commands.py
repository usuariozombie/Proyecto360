# -*- coding: utf-8 -*-

import nextcord, requests
from nextcord.ext.commands import Cog, command
from utils import Debug, JSON, now, TextClearer
from nextcord import Embed, Interaction, SlashOption, slash_command

class Forecast(Cog):

	def __init__(self, client): self.client = client

	@Cog.listener()
	async def on_ready(self): Debug.Good(f"{self.__cog_name__} loaded successfully!")

	@slash_command(name = "test", description = "Test command")
	async def test(self, interaction: Interaction): pass

	@test.subcommand(name = "test1", description = "Test command")
	async def test1(self, interaction: Interaction):
		await interaction.response.send_message("Test")
  

def setup(client):
	client.add_cog(Forecast(client))