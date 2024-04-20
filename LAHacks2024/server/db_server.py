import reflex as rx
from pymongo import MongoClient
import uuid

CONNECTION_STRING = "mongodb+srv://jpan287:L2pEGi2Po7dUYYX5@lahacks24.3fh9yjd.mongodb.net/?retryWrites=true&w=majority"
MAX_PLAYERS = 8

class db_server:
    def __init__(self):
        client = MongoClient(CONNECTION_STRING)
        self.db = client['lahacks2024']
        self.collection = self.db['rooms']

    # Generates a unique 8-character room key
    def generate_room_key(self):
        return str(uuid.uuid4())[:8]
    
    # Generates a unique 8-character UID 
    def generate_user_id(self):
        return str(uuid.uuid4())[:8]

    # Creates a new room. Creates and returns a room_key.
    def create_room(self):
        room_key = self.generate_room_key()
        room_data = {
            'key': room_key,
            'player_ids': [],
            'player_names': [],
            'num_players': 0,
        }
        self.collection.insert_one(room_data)
        return room_key

    # Allows user to join room with valid ID.
    def join_room(self, room_key, user_name):
        # If room key doesn't exist, print error
        room = self.collection.find_one({'key': room_key})
        if not room:
            raise Exception('Room %s: not found' % (room_key))
        # Check if the room is full
        num_players = self.collection.find_one({'key': room_key}, {'num_players': 1})
        if num_players >= MAX_PLAYERS:
            raise Exception('Room %s: full' % (room_key))
        return True
    
    def check_username(self, room_key, user_name):
        # Check if the username already exists in database
        if len(self.collection.find({'player_names': {'$in': [user_name]}})) != 0:
            raise Exception('Room %s: name %s already taken' % (room_key, user_name))
        # Creates a user_id, increments the number of players in room, adds user info to room
        user_id = self.generate_user_id()
        self.collection.update_one({'key': room_key}, {'$inc': {'num_players': 1}})
        self.collection.update_one({'key': room_key}, {'$push': {'player_ids': user_id}})
        self.collection.update_one({'key': room_key}, {'$push': {'player_names': user_name}})
        return user_id