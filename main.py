import config
from mcstatus import JavaServer
from mcrcon import MCRcon

ip = input()
server = JavaServer.lookup(ip)
query = server.query()
status = server.status()
print(status.players.online)
print(query.players.max)
print(query.players.names)
print(query.software.plugins)

command = input()
rcon = MCRcon(config.RCON_IP, config.RCON_PASSWORD)
rcon.connect()
resp = rcon.command(command)
print(resp)



