"""Challenge identities must survive generation, gameplay and results."""
import unittest
import struct
from pathlib import Path

from app.game_data.challenges import challenges_dict
from app.game_data.challenge_artwork import CHALLENGE_ART

from app.game_data.get_random_mission import get_mission
from app.sockets.handlers.mission import _normalise_challenges
from app.services.scoring_service import build_result_state


class ChallengeArtworkTests(unittest.TestCase):
    def test_every_catalog_variant_has_a_real_scene(self):
        for kind, group in challenges_dict.items():
            for internal, challenge in group.items():
                key = internal.split(' - ')[0].strip() if kind in ('Getaway', 'Travel To Rendezvous') else challenge['challenge_name']
                for location in challenge['viable_locations']:
                    with self.subTest(location=location, challenge=key):
                        scene = CHALLENGE_ART[location][key]
                        self.assertNotIn(scene['source'], ('phases', 'preparation', 'game'))
                        self.assertTrue(0 <= scene['cell'] < scene['grid'] ** 2)
                        image = Path(__file__).parents[1] / 'app/static/images/briefing' / scene['file']
                        data = image.read_bytes()
                        self.assertEqual(data[:8], b'\x89PNG\r\n\x1a\n')
                        width, height = struct.unpack('>II', data[16:24])
                        self.assertEqual(width, height)
                        self.assertGreaterEqual(width / scene['grid'], 200)

    def test_different_hazards_do_not_share_generic_art(self):
        for location, keys in {
            'Volcano': ['Lava Spout', 'Ash', 'Earthquake', 'Volcanic Gases'],
            'Jungle': ['Fire', 'Cyclone', 'Flash Flood', 'Deadly Insects', 'Deadly Marshland Gases', 'Fallen Trees Block Path'],
            'Arctic Tundra': ['Frozen Lake', 'Rockfall', 'Ice Cliff'],
            'Desert': ['Mirages', 'Quick Sand', 'Sand Dunes', 'Heat Wave', 'Sand Storm'],
        }.items():
            identities = [(CHALLENGE_ART[location][key]['source'], CHALLENGE_ART[location][key]['cell']) for key in keys]
            self.assertEqual(len(set(identities)), len(keys), location)

    def test_art_identity_survives_generation_and_results(self):
        for _ in range(100):
            generated = get_mission()
            challenges = _normalise_challenges(generated)
            for index, challenge in enumerate(challenges):
                raw = generated[f"challenge_{index + 1}"]
                self.assertEqual(challenge['artKey'], raw['art_key'])
                if raw['challenge_name'] in ('Getaway', 'Travel To Rendezvous Point'):
                    self.assertIn(raw['art_key'].split()[0], ('Air', 'Land', 'Water', 'Sand', 'Snow'))
            session = {'mission': {'status': 'complete', 'challenges': challenges},
                       'mission_result': {'score': 0, 'penalties': 0, 'outcomes': [
                           {'challengeIndex': i, 'challengeId': c['id'], 'success': True, 'penalty': 0}
                           for i, c in enumerate(challenges)]}}
            results = build_result_state(session)['challenges']
            self.assertEqual([c['artKey'] for c in results], [c['artKey'] for c in challenges])


if __name__ == '__main__':
    unittest.main()
