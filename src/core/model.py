from gaegraph.model import Node
from google.appengine.ext import ndb


class User(ndb.Model):
	video_affinity = ndb.FloatProperty(required=True)
	text_affinity = ndb.FloatProperty(required=True)
	game_affinity = ndb.FloatProperty(required=True)


class Video(Node):
	pass


class Game(Node):
	pass


class Text(Node):
	pass