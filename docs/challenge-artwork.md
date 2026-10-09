# Challenge artwork refresh

Every current challenge has an explicit environment-specific scene: 276 mappings across Arctic Tundra (46), City (49), Desert (47), Jungle (51), Ocean (39), and Volcano (44). The refresh retains 93 suitable existing scenes and adds 183 illustrations in 16 image files.

Challenge selection now uses stable identities, including air/water/land transport variants, throughout generation, gameplay and results. Repeated challenges keep their matching image. Unknown challenges show no scene instead of unrelated planning artwork, and loading a new challenge clears stale artwork immediately.

## Review locally

Run `python3 tools/preview_challenge_artwork.py` with the application's dependencies installed, then open http://127.0.0.1:5052/artwork-review. The gallery uses the real scene renderer and manifests; its route is only registered by this standalone review tool. Filter with `location` and optional `challenge` query parameters.

## Maintain the catalog

Mappings live in `app/game_data/challenge_art/*.json`. Each stable challenge key specifies an image file, source identifier, square grid size and zero-based row-major cell. Add an exact mapping for every viable location when adding a challenge. Generation prompts for the new assets are preserved in `challenge-artwork-prompts.json`.

## Validation

- `python -m pytest tests/test_challenge_artwork.py -q`: 3 passed; checks all catalog variants, image dimensions, distinct hazard scenes and identity propagation through 100 generated missions.
- `node tests/test_scene_selection.js`: passed; checks exact selection and consistency across gameplay/results.
- `node tests/test_challenge_paint.js`: passed; checks loading, races, failed images and unknown scenes.
- Browser review confirmed the Lava Spout scene renders lava rather than a planning scene.

The broader results/generated-mission suites have 59 existing failures, reproduced on the pre-change commit c8cb839: missing top-level final_failure_desc in generated missions and an outdated pointsEarned expectation. These are outside this artwork change.
