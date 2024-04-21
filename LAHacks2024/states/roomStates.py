import reflex as rx
import asyncio
import time
from LAHacks2024.pages import naming
from LAHacks2024.server import DBServer

class RoomState(rx.State):
  num_rounds: int = 1
  host_bool: bool = False
  room_key: str = ""
  player_names: list[str]
  start: bool = False
  user_id: str

  async def get_data(self): 
    naming_state = await self.get_state(naming.NamingState)
    self.host_bool = naming_state.is_host
    self.user_id = naming_state.user_id
    print(self.host_bool)
    self.room_key = naming_state.room_key
    server = DBServer.DBServer()
    self.player_names = server.get_players(self.room_key)
    yield RoomState.db_refresh()

  def set_end(self, value:int):
    self.num_rounds = value

  def start_game(self):
    server = DBServer.DBServer()
    server.start_game(self.room_key)

  @rx.background
  async def db_refresh(self):
    server = DBServer.DBServer()
    while True:
      async with self:
        await asyncio.sleep(1)
        self.player_names = server.get_players(self.room_key)
        self.start = server.check_start(self.room_key)
        yield
        print(self.player_names)
        print(self.start)
        # If game started, end it and go to game screen 
        if self.start:
          yield rx.redirect('/abilities') # deal with dynamic routing later
          return