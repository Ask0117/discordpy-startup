from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)

// Response for Uptime Robot
const http = require('http');
http.createServer(function(request, response)
{
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Discord bot is active now \n');
}).listen(3000);

client.on('ready', message =>
{
  client.user.setPresence({ game: { name: 'with discord.js' } });  
  console.log('bot is ready!');
    if(message.content.startsWith('addch ')) {
  
  var channelName = message.content.replace(/^addch /, ''); 
  
  message.guild.createChannel(channelName);
  return;
}
});
