import reflex as rx
from pymongo import MongoClient
import uuid
import ssl

CONNECTION_STRING = "mongodb+srv://jpan287:L2pEGi2Po7dUYYX5@lahacks24.3fh9yjd.mongodb.net/?retryWrites=true&w=majority"
MAX_PLAYERS = 12

class DBServer:
    def __init__(self):
        client = MongoClient(CONNECTION_STRING, ssl=True, tlsAllowInvalidCertificates=True)
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
            'game_started': False,
            'host_start_time': -1,
            'arguments': [],
            'abilities': [],
            'response': '',
        }
        self.collection.insert_one(room_data)
        return room_key

    # Allows user to join room with valid ID.
    def join_room(self, room_key):
        # If room key doesn't exist, print error
        room = self.collection.find_one({'key': room_key})
        if not room:
            raise Exception('Room %s: not found' % (room_key))
        # Check if the room is full
        num_players = self.collection.find_one({'key': room_key}, {'num_players': 1, '_id': 0})['num_players']
        if num_players >= MAX_PLAYERS:
            raise Exception('Room %s: full' % (room_key))
        return True
    
    # Checks if the username user wants is taken yet or not
    def check_username(self, room_key, user_name):
        # Check if the username already exists in database
        username_query = self.collection.find_one({'key': room_key, 'player_names': {'$elemMatch': {'$eq': user_name}}})
        if username_query is not None:
            raise Exception('Room %s: name %s already taken' % (room_key, user_name))
        # Creates a user_id, increments the number of players in room, adds user info to room
        user_id = self.generate_user_id()
        self.collection.update_one({'key': room_key}, {'$inc': {'num_players': 1}})
        self.collection.update_one({'key': room_key}, {'$push': {'player_ids': user_id}})
        self.collection.update_one({'key': room_key}, {'$push': {'player_names': user_name}})
        return user_id

    # Gets the usernames of all the players
    def get_players(self, room_key):
        player_names_query = self.collection.find({'key': room_key}, {'_id': 0, 'player_names': 1})
        player_names = []
        for doc in player_names_query:
            if 'player_names' in doc:
                player_names.extend(doc['player_names'])
        return player_names
    
    def start_game(self, room_key):
        self.collection.update_one({'key': room_key}, {'$set': {'game_started': True}})
        return True

    def check_start(self, room_key):
        return self.collection.find_one({'key': room_key}, {'game_started': 1, '_id': 0})['game_started']
    
    def host_send_time(self, room_key, time):
        self.collection.update_one({'key': room_key}, {'$set': {'host_start_time': time}})

    def get_host_send_time(self, room_key):
        return self.collection.find_one({'key': room_key}, {'host_start_time': 1, '_id': 0})['host_start_time']
    
    def send_argument(self, room_key, user_id, argument):
        self.collection.update_one({'key': room_key}, {'$push': {'arguments': (user_id, argument)}})
    
    def get_arguments(self, room_key):
        # Get the list of arguments (tuples of (user_id, argument))
        arguments_query = self.collection.find({'key': room_key}, {'arguments': 1, '_id': 0})
        arguments = []
        for arg in arguments_query:
            if 'arguments' in arg:
                arguments.extend(arg['arguments'])
        # Get the list of user_ids
        user_ids_query = self.collection.find({'key': room_key}, {'player_ids': 1, '_id': 0})
        user_ids = []
        for id in user_ids:
            if 'player_ids' in id:
                user_ids.extend(id['player_ids'])
        # sorted_arguments = sorted(arguments, key=lambda x: user_ids.index(x[0]))
        return [t[1] for t in arguments]
    
    def set_abilities(self, room_key, abilities):
        for a in abilities:
            self.collection.update_one({'key': room_key}, {'$push': {'arguments': a}})
    
    def get_abilities(self, room_key):
        abilities_query = self.collection.find({'key': room_key}, {'_id': 0, 'abilities': 1})
        abilities = []
        for a in abilities:
            if 'abilities' in a:
                abilities.extend(a['abilities'])
        return abilities

    def set_response(self, room_key, response):
        self.collection.update_one({'key': room_key}, {'$set': {'response': response}})

    def get_response(self, room_key):
        self.collection.find_one({'key': room_key}, {'response': 1, '_id': 0})['response']