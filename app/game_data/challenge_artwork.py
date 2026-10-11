"""Reviewed scene coordinates, keyed by environment and stable challenge identity."""
import json
from pathlib import Path

CHALLENGE_ART = {}
for manifest in sorted(Path(__file__).with_name('challenge_art').glob('*.json')):
    data = json.loads(manifest.read_text())
    CHALLENGE_ART[data['location']] = data['scenes']
