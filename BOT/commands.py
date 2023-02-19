# -*- coding: utf-8 -*-

import nextcord, requests
from nextcord.ext.commands import Cog
from utils import Debug, JSON
from nextcord import Embed, Interaction, slash_command

ConfigData = JSON.Read("config.json")

class Commands(Cog):

	def __init__(self, client): self.client = client

	@Cog.listener()
	async def on_ready(self): Debug.Good(f"{self.__cog_name__} loaded successfully!")

	@Cog.listener()
	#on join send welcome message
	async def on_member_join(self, member):
		channel = self.client.get_channel(ConfigData["WelcomeChannel"])
		embed = Embed(
			title = "¡Bienvenido/a a DAM/DAW Vedruna Sevilla!",
			description = f"¡Hola {member.mention}! Bienvenido/a a DAM/DAW Vedruna Sevilla, espero que disfrutes de tu estancia. Si tienes alguna duda, no dudes en contactar con un miembro del staff.\n\n**¡Recuerda pasarte por esta [página](http://usuariozombie.com/app360) para registrar tu perfil personal!**",
			color = 0x00ff00
		)
		embed.set_thumbnail(url = member.avatar)
		embed.set_footer(text = "Entregado por http://usuariozombie.com", icon_url = member.guild.icon)

		await channel.send(embed = embed)


	@slash_command(name = "profile", description = "Profile command.")
	async def test(self, interaction: Interaction): pass

	#if no user is mentioned, it will check the author's profile
	@test.subcommand(name = "checkprofile", description = "Checks someone's profile or your own profile if no one is mentioned.")
	async def check(self, interaction: Interaction, user: nextcord.User = None):
		try:
			if user == None: 
				user = interaction.user
			else:
				user = user
			url = f"https://api.usuariozombie.com/app360/members/{user.id}?token={ConfigData['APIToken']}"
			response = requests.get(url)
			data = response.json()

			if data['curso'] == '1': 
				data['curso'] = 'DAM'
			else:
				data['curso'] = 'DAW'

			if data['year'] == '1':
				data['year'] = '1º'
			elif data['year'] == '2':
				data['year'] = '2º'

			embed = Embed( 
				description = f"**Nombre:** {data['fname']}\n**Apellidos:** {data['lname']}\n\n**Email:** {data['email']}\n**Teléfono:** {data['phone']}\n\n**Curso:** {data['year']} de {data['curso']}\n\n**Redes Sociales:** [<:github:1076872412982939718>]({data['github']}) | [<:twitter:1076872496189542500>]({data['twitter']}) | [<:instagram:1076872763467370586>]({data['instagram']})\n\n**Sobre mí:** {data['description']}",
				color = 0x00ff00
			)
			embed.set_author(name = f"{user.name}#{user.discriminator}", icon_url = user.avatar.url)
			embed.set_thumbnail(url = user.avatar.url)
			embed.set_footer(text = "Solicitado por " + interaction.user.name + "#" + interaction.user.discriminator + " · " + "Entregado por http://usuariozombie.com", icon_url = interaction.user.avatar.url)

			await interaction.response.send_message(embed = embed)
		except Exception as Error: await interaction.response.send_message("¡El usuario no existe o no tiene perfil!")

  

def setup(client):
	client.add_cog(Commands(client))