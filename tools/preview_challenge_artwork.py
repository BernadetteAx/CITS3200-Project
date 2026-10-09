"""Local-only catalog review: python3 tools/preview_challenge_artwork.py.

Uses the real scene renderer and manifests. No preview route is registered by
normal application startup. Bind only to localhost.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from flask import render_template_string, request
from app import app
from app.game_data.challenge_artwork import CHALLENGE_ART

@app.route('/artwork-review')
def artwork_review():
    location = request.args.get('location', 'Volcano')
    if location not in CHALLENGE_ART:
        location = 'Volcano'
    names = list(CHALLENGE_ART[location])
    if request.args.get('challenge') in names:
        names = [request.args['challenge']]
    return render_template_string('''<!doctype html><html lang="en"><head>
    <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Challenge artwork review</title>
    <link rel="stylesheet" href="/static/css/game_visuals.css">
    <style>body{background:#081321;color:#edf4f7;font:16px system-ui;margin:32px;padding:0}
    h1{margin-bottom:10px}p{color:#a5b6c8}nav{display:flex;flex-wrap:wrap;gap:16px}a{color:#6cdbd0}
    main{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:20px;margin-top:28px}
    figure{margin:0;padding:12px;background:#122236;border-radius:10px;max-width:520px}
    .game-scene{width:100%;border:0;border-radius:6px}.game-ambience{display:none}
    figcaption{padding:12px 0 0}.scene-layer{transition:none}</style>
    <script defer src="/static/js/game_visuals.js"></script></head>
    <body data-artwork-root="/static/images/briefing/">
    <script id="visualCatalog" type="application/json">{{game_visual_catalog|tojson}}</script>
    <h1>{{location}} challenge artwork</h1><p>Local review using the game's actual scene renderer. Gameplay and results use the same mapping.</p>
    <nav>{% for loc in locations %}<a href="{{url_for('artwork_review',location=loc)}}">{{loc}}</a>{% endfor %}</nav>
    <main>{% for name in names %}<figure><div class="game-scene" role="img" data-art-key="{{name}}"></div><figcaption>{{name}}</figcaption></figure>{% endfor %}</main>
    <script>document.addEventListener('DOMContentLoaded',()=>{
      document.querySelectorAll('[data-art-key]').forEach(frame=>{
        const name=frame.dataset.artKey;
        const scene=window.gameVisuals.challengeVisual({name,artKey:name},{{location|tojson}});
        window.gameVisuals.paint(frame,scene.cell,scene.source,scene.alt,false);
      });
    });</script></body></html>''', location=location, names=names, locations=list(CHALLENGE_ART))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5052, threaded=True)
