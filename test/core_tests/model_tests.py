from core.model import User, Video, Game, Text
from gaegraph.model import Arc
from util.gae import GAETestCase


class TestModels(GAETestCase):
    def test_user_model(self):
        user = User()
        user.video_affinity = 0.07
        user.text_affinity = 0.03
        user.game_affinity = 0.01
        user.put()

        db_user = User.query().get()

        self.assertEquals(0.07, db_user.video_affinity)
        self.assertEquals(0.03, db_user.text_affinity)
        self.assertEquals(0.01, db_user.game_affinity)

    def test_content_graph(self):
        video = Video()
        video.put()

        text = Text()
        text.put()

        game = Game()
        game.put()

        arc = Arc()
        arc.origin = video.key
        arc.destination = text.key
        arc.put()

        arc = Arc()
        arc.origin = video.key
        arc.destination = game.key
        arc.put()

        nexts = Arc.find_destinations(video.key).fetch(100)

        self.assertEquals(text, nexts[0].destination.get())
        self.assertEquals(game, nexts[1].destination.get())
