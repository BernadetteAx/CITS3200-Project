"""Challenge identities must survive generation, gameplay and results."""
import unittest

from app.game_data.get_random_mission import get_mission
from app.sockets.handlers.mission import _normalise_challenges
from app.services.scoring_service import build_result_state


class ChallengeArtworkTests(unittest.TestCase):
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
