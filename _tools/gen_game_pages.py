# Builds boards/, rogue-altitude/ and mindsprint/ index.html. Run from the repo root:
#   python3 _tools/gen_game_pages.py .

import os, sys
ROOT = sys.argv[1]

PLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#00D7FE" d="M3.6 1.8 13.4 12l-9.8 10.2c-.4-.2-.6-.7-.6-1.2V3c0-.5.2-1 .6-1.2Z"/><path fill="#FFCE00" d="m16.8 8.6-3.4 3.4 3.4 3.4 3.9-2.2c.8-.5.8-1.7 0-2.2l-3.9-2.4Z"/><path fill="#FF3A44" d="M13.4 12 3.6 22.2c.4.2.9.2 1.4 0l11.8-6.8-3.4-3.4Z"/><path fill="#00F076" d="M3.6 1.8c.4-.2.9-.2 1.4 0l11.8 6.8-3.4 3.4L3.6 1.8Z"/></svg>'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%233D4CAE'/%3E%3Ctext x='32' y='45' font-family='Arial,sans-serif' font-size='38' font-weight='800' text-anchor='middle' fill='%23F5C66B'%3ES%3C/text%3E%3C/svg%3E"

YT_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="1.5" y="5" width="21" height="14" rx="4" fill="#FF0000"/><path d="M10 9v6l5.2-3z" fill="#fff"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="#D62976" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1" fill="#D62976" stroke="none"/></svg>'
X_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 4l16 16M20 4L4 20"/></svg>'
SOCIAL = [
  ('YouTube', 'https://www.youtube.com/@shivisgames', YT_SVG),
  ('Instagram', 'https://www.instagram.com/shivisgames', IG_SVG),
  ('X', 'https://x.com/shivisgames', X_SVG),
]
PLAY_ICON = '<svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M6 4v16l14-8z"/></svg>'

def foot_social():
    return '<div class="foot-social">' + ''.join(f'<a href="{u}" rel="noopener" aria-label="{n}">{i}</a>' for n,u,i in SOCIAL) + '</div>'

def video_cards(videos):
    return ''.join(
        f'<button class="vid" type="button" data-yt="{v}" aria-label="Play video: {t}">'
        f'<img src="https://i.ytimg.com/vi/{v}/oar2.jpg" alt="" loading="lazy">'
        f'<span class="play-btn"><span>{PLAY_ICON}</span></span><span class="cap">{t}</span></button>'
        for v,t in videos)

APPS = {
 'boards': dict(
   cls='boards', page='page-boards', name='Boards', sub='Chess, Ludo &amp; Sudoku', icon='icon.png',
   play='https://play.google.com/store/apps/details?id=com.shivi.boards',
   meta='Boards: Chess, Ludo &amp; Sudoku. Classic board games and word puzzles in one free app: play the computer, pass one phone around, or play friends nearby over Bluetooth.',
   tagline='Classic board games and word puzzles in one free app. Play the computer at your level, pass one phone around, or connect with friends nearby over Bluetooth, no internet needed.',
   facts=['🆓 Free','🧩 9 games','📶 Bluetooth multiplayer','🗓️ Daily Challenge','🌍 7 languages'],
   shots=('portrait',7,'Boards screenshot'),
   shot_alts=['Boards app with Chess, Ludo and Sudoku: classic games all in one app', 'Chess against the computer, with levels, a game clock and learn mode', 'Ludo board for 2 to 6 players, against friends or the computer', 'Sudoku puzzle with notes, hints and best times', 'Guess the Word, one of four word games in Boards', 'Snakes and Ladders for up to 4 players on one phone', 'Sling Puck played with friends nearby over Bluetooth, no internet needed'],
   features=[
     ('🤖','Beat the computer','Computer opponents with levels to climb in Chess, Checkers, Carrom, Ludo and Sling Puck.'),
     ('📶','Play friends nearby','Connect phones over Bluetooth for Chess, Checkers, Carrom, Ludo, Snakes &amp; Ladders and Sling Puck.'),
     ('📱','Pass and play','Share one phone and take turns with family and friends.'),
     ('🗓️','Daily Challenge','A fresh set of puzzles and missions every day, with streaks to keep.'),
     ('🏆','Achievements &amp; stats','Track your wins, levels and best scores on your profile.'),
     ('🌍','Seven languages','English, Hindi, Spanish, Portuguese, French, Arabic and Urdu.'),
   ],
   list_title='The games', list_sub='Nine games in one app, from classic boards to brain-teasing puzzles.',
   items=[
     ('♟️','Chess','Play the computer or a friend, with move review.'),
     ('🔴','Checkers','Jump, capture and crown kings.'),
     ('🎲','Ludo','Race all four tokens home.'),
     ('🐍','Snakes &amp; Ladders','Roll the dice and race to 100.'),
     ('🎯','Carrom','Strike and pocket your coins.'),
     ('🏒','Sling Puck','Sling pucks through the gap before your rival.'),
     ('🔢','Sudoku','The classic number puzzle, with 1,000 levels that get harder as you go.'),
     ('🖼️','Nonogram','Use number clues to reveal pictures.'),
     ('🔤','Word Puzzle','Four word games in one: Word Search, Scramble, Guess the Word and Word Ladder.'),
   ],
   legal=[('privacy.html','Privacy Policy','What the app collects and why'),('terms.html','Terms of Use','The rules for using Boards')],
   # YouTube Shorts shown in "See it in action": (video ID, caption). Newest first.
   videos=[
     ('zBaGysvKhB8','Chess, Ludo, Carrom &amp; Sudoku in ONE app'),
     ('pa7NUEx0em8','Can you beat Level 4? Sling Puck'),
     ('Rq7iGxnjtNY','Multiple games in ONE app'),
   ],
 ),
 'rogue-altitude': dict(
   cls='rogue', page='page-rogue', name='Rogue Altitude', sub='Jetpack Arena', icon='rogue-altitude-icon-256.png',
   play=None,
   meta='Rogue Altitude: Jetpack Arena. Anime-style jetpack battles: train against bots, then fight friends over Bluetooth or local Wi-Fi.',
   tagline='Strap on a jetpack and take the fight skyward. Train against up to ten bots, then battle friends in the same room over Bluetooth or local Wi-Fi.',
   facts=['🆓 Free','🧑‍✈️ 12 pilots','🗺️ 9 arenas','🤖 Up to 10 bots','📶 Bluetooth &amp; LAN'],
   shots=('landscape',6,'Rogue Altitude screenshot'),
   shot_alts=['Rogue Altitude jetpack combat over a moonlit city', 'Battle with rifles, bows, shotguns and grenades at sunset', 'Local multiplayer jetpack battle with friends over Bluetooth or LAN', 'Choose your pilot and weapon from the loadout screen', 'Pick one of nine arenas, each with its own cover and high ground', 'Career ranks, daily contracts and cosmetic rewards'],
   features=[
     ('🚀','Jetpack combat','Boost, aim and dodge in fast arena fights with health, fuel and respawns.'),
     ('🎯','Train against bots','Pick from zero to ten bots and practise before you face real players.'),
     ('📶','Battle your friends','Local multiplayer over Bluetooth or the same Wi-Fi network, with no accounts.'),
     ('🧑‍✈️','Choose your pilot','Twelve pilots across five classes: Assault, Scout, Heavy, Ace and Marksman.'),
     ('🔫','Pick your weapon','Rifles, bows, shotguns and grenades: bullets fly straight, arrows arc and grenades bounce.'),
     ('🏅','Rank up','Earn career XP, climb the ranks, finish daily contracts and unlock gear.'),
   ],
   list_title='The arenas', list_sub='Nine maps, each with its own layout, cover and look.',
   items=[
     ('🌃','Neon Rooftops','Steel and neon high above the city.'),
     ('🔥','Ember Foundry','A fiery industrial foundry.'),
     ('🪐','Orbital Drift','Low gravity for long, floating flights.'),
     ('🌸','Sakura Citadel','Lacquered wood and stone lanterns.'),
     ('🏜️','Sandstone Ruins','Weathered sandstone ruins.'),
     ('⚓','Frostline Harbor','A frozen harbour front.'),
     ('🌕','Blood Moon District','City streets under a blood moon.'),
     ('❄️','Frozen Forge','A forge locked in ice.'),
     ('🏛️','Moonlit Ruins','Ancient ruins by moonlight.'),
   ],
   legal=[('rogue-altitude-privacy.html','Privacy Policy','What the game collects and why'),('rogue-altitude-terms.html','Terms of Use','The rules for playing Rogue Altitude'),('rogue-altitude-delete-data.html','Delete your data','How to remove your game data')],
 ),
 'mindsprint': dict(
   cls='mind', page='page-mind', name='MindSprint', sub='Focus &amp; Memory', icon='mindsprint-icon.png',
   play=None,
   meta='MindSprint: Focus &amp; Memory. Seven quick brain games in one free app, with hundreds of levels and a Daily Challenge.',
   tagline='Seven quick brain games in one free app. Sort, connect, plan and remember your way through hundreds of levels, with a Daily Challenge that grows with you.',
   facts=['🆓 Free','🧠 7 brain games','✈️ Play offline','🗓️ Daily challenges'],
   shots=('portrait',8,'MindSprint screenshot'),
   shot_alts=['MindSprint: seven brain games in one app', 'Water Sort: pour and sort the colours into tubes', 'Pipe Path: connect the numbers in order and fill every box', 'Garden Grid: plant the perfect garden logic puzzle', 'Memory Lanterns: watch the lights and repeat the pattern', 'Arrow Drift: clear the board arrow by arrow', 'Rider Rush: get every rider on board before the clock runs out', 'Hive Fill: drag and drop pieces to fit every space in the hive'],
   features=[
     ('🧠','Train your brain','Puzzles for focus, logic, planning and memory, a few minutes at a time.'),
     ('📈','Hundreds of levels','Levels unlock in order and get harder as you go. Replay any of them.'),
     ('🗓️','Daily Challenge','New puzzles every day, matched to the level you have reached.'),
     ('💡','Hints when stuck','Many puzzles offer a hint, so you can get unstuck without giving up.'),
     ('✈️','Play offline','No internet needed to play.'),
     ('🏆','Achievements','Collect achievements and track your progress on your profile.'),
   ],
   list_title='The games', list_sub='Seven puzzles, each training a different skill.',
   items=[
     ('🧪','Water Sort','Pour and sort the colours into tubes.'),
     ('🔗','Pipe Path','Connect the numbers in order with one path.'),
     ('🌱','Garden Grid','Plant the perfect garden using logic.'),
     ('🏮','Memory Lanterns','Remember the lights and repeat the pattern.'),
     ('➡️','Arrow Drift','Clear the board arrow by arrow.'),
     ('🏍️','Rider Rush','Get every rider on board.'),
     ('🐝','Hive Fill','Fit every piece in the hive.'),
   ],
   legal=[('mindsprint-privacy.html','Privacy Policy','What the app collects and why'),('mindsprint-terms.html','Terms of Use','The rules for using MindSprint')],
 ),
}

def webp(name):
    return name.rsplit('.',1)[0] + '.webp'

def app_ld(slug, a):
    import json as _j
    d = {"@context": "https://schema.org", "@type": "MobileApplication",
         "name": a['name'], "description": a['meta'].replace('&amp;', '&'),
         "operatingSystem": "ANDROID", "applicationCategory": "GameApplication",
         "url": f"https://shivisgames.com/{slug}/", "image": f"https://shivisgames.com/{a['icon']}",
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": {"@type": "Organization", "name": "Shivi Games", "url": "https://shivisgames.com/"}}
    if a['play']:
        d["downloadUrl"] = a['play']; d["installUrl"] = a['play']
    return _j.dumps(d)

def header():
    return '''<header class="top"><div class="wrap">
  <a class="logo" href="../" aria-label="Shivi Games home"><img class="logo-img" src="../assets/icons/logo-96.webp" alt="" width="34" height="34">Shivi Games</a>
  <nav aria-label="Main">
    <a href="../#games">Games</a>
    <a class="hide-sm" href="#legal">Privacy &amp; terms</a>
    <a href="../#contact">Contact</a>
  </nav>
</div></header>'''

def footer():
    return '''<footer><div class="wrap">
  <div class="foot-grid">
    <div><h4>Shivi Games</h4><p style="margin:0">Free mobile games for everyone.</p><ul><li><a href="../press/">Press kit</a></li><li><a href="../website-privacy.html">Website privacy</a></li></ul>''' + foot_social() + '''</div>
    <div><h4><a href="../boards/">Boards</a></h4><ul><li><a href="../privacy.html">Privacy Policy</a></li><li><a href="../terms.html">Terms of Use</a></li></ul></div>
    <div><h4><a href="../rogue-altitude/">Rogue Altitude</a></h4><ul><li><a href="../rogue-altitude-privacy.html">Privacy Policy</a></li><li><a href="../rogue-altitude-terms.html">Terms of Use</a></li><li><a href="../rogue-altitude-delete-data.html">Delete your data</a></li></ul></div>
    <div><h4><a href="../mindsprint/">MindSprint</a></h4><ul><li><a href="../mindsprint-privacy.html">Privacy Policy</a></li><li><a href="../mindsprint-terms.html">Terms of Use</a></li></ul></div>
  </div>
  <div class="copy">© 2026 Shivi Games · <a href="mailto:hello@shivisgames.com">hello@shivisgames.com</a></div>
</div></footer>'''

NOTIFY = {'rogue': 'https://docs.google.com/forms/d/e/1FAIpQLSernqcbTf-pWg8C9GBaFFRgnRoxBcFSFBVP7VU9N30g2vqWBQ/viewform?usp=pp_url&entry.2082480360=Rogue+Altitude+%28jetpack+arena+battles%29', 'mind': 'https://docs.google.com/forms/d/e/1FAIpQLSernqcbTf-pWg8C9GBaFFRgnRoxBcFSFBVP7VU9N30g2vqWBQ/viewform?usp=pp_url&entry.2082480360=MindSprint+%28focus+%26+memory+puzzles%29'}

def play_button(a):
    if a['play']:
        ref = '&referrer=utm_source%3Dshivisgames.com%26utm_medium%3Dwebsite%26utm_content%3D' + a['cls']
        return f'<a class="play" href="{a["play"]}{ref}" rel="noopener">{PLAY_SVG}<span><small>GET IT ON</small>Google Play</span></a>'
    notify = NOTIFY.get(a['cls'])
    btn = f'<a class="btn btn-gold notify" href="{notify}" target="_blank" rel="noopener">🔔 Notify me at launch</a>' if notify else ''
    return '<span class="soon">Coming soon to Google Play</span>' + btn

def page(slug, a):
    orient, n, alt = a['shots']
    alts = a.get('shot_alts') or [f'{alt} {i}' for i in range(1, n+1)]
    shots = ''.join(f'<img src="img/shot-{i}.webp" alt="{alts[i-1]}" loading="lazy" width="{"540" if orient=="portrait" else "960"}" height="{"960" if orient=="portrait" else "540"}">' for i in range(1, n+1))
    feats = ''.join(f'<div class="feature"><div class="em" aria-hidden="true">{e}</div><h3>{t}</h3><p>{d}</p></div>' for e,t,d in a['features'])
    items = ''.join(f'<div class="item"><div class="em" aria-hidden="true">{e}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for e,t,d in a['items'])
    legal = ''.join(f'<a class="legal-card" href="../{h}"><strong>{t}</strong><span>{d}</span></a>' for h,t,d in a['legal'])
    legal += '<a class="legal-card" href="mailto:hello@shivisgames.com"><strong>Contact support</strong><span>hello@shivisgames.com</span></a>'
    others = ''.join(f'<a class="other" href="../{s}/"><img src="../{webp(o["icon"])}" alt="" width="72" height="72" loading="lazy"><div><strong>{o["name"]}</strong><span>{o["sub"]}</span></div></a>' for s,o in APPS.items() if s != slug)
    facts = ''.join(f'<li>{f}</li>' for f in a['facts'])
    title_plain = f'{a["name"]}: {a["sub"]}'.replace('&amp;','&')
    vids = a.get('videos') or []
    videos_block = '' if not vids else f'''<section class="block" id="videos" style="scroll-margin-top:80px"><div class="wrap">
  <div class="section-head reveal"><h2>See it in action</h2><p>Gameplay clips from our YouTube channel. Tap a video to play.</p></div>
  <div class="vids">{video_cards(vids)}</div>
  <p class="vids-more reveal"><a class="btn btn-brand" href="https://www.youtube.com/@shivisgames" rel="noopener">More on YouTube →</a></p>
</div></section>

'''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_plain.replace("&","&amp;")} – Shivi Games</title>
<meta name="description" content="{a["meta"]}">
<link rel="icon" href="/favicon.ico" sizes="any">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Shivi Games">
<meta property="og:url" content="https://shivisgames.com/{slug}/">
<meta property="og:title" content="{title_plain.replace("&","&amp;")}">
<meta property="og:description" content="{a["meta"]}">
<meta property="og:image" content="https://shivisgames.com/assets/og/{slug}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@shivisgames">
<meta name="twitter:image" content="https://shivisgames.com/assets/og/{slug}.jpg">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/icons/favicon-192.png">
<link rel="icon" type="image/png" sizes="96x96" href="/assets/icons/favicon-96.png">
<link rel="icon" type="image/png" sizes="48x48" href="/assets/icons/favicon-48.png">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#3D4CAE">
<script type="application/ld+json">{app_ld(slug, a)}</script>
<link rel="canonical" href="https://shivisgames.com/{slug}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/site.css">
</head>
<body class="{a["page"]}">

{header()}

<main>
<section class="ghero {a["cls"]}">
  <div class="hero-dots" aria-hidden="true"></div>
  <div class="wrap">
    <img class="g-icon" src="../{webp(a["icon"])}" alt="{a["name"]} app icon" width="148" height="148">
    <div>
      <div class="crumbs"><a href="../">Shivi Games</a> › <a href="../#games">Games</a></div>
      <h1>{a["name"]}</h1>
      <div class="g-sub">{a["sub"]}</div>
      <p>{a["tagline"]}</p>
      <div class="g-actions">{play_button(a)}</div>
      <ul class="facts" aria-label="Quick facts">{facts}</ul>
    </div>
  </div>
</section>

<section class="block"><div class="wrap">
  <div class="section-head"><h2>Screenshots</h2></div>
  <div class="shots {orient}" tabindex="0" aria-label="{a["name"]} screenshots">{shots}</div>
</div></section>

{videos_block}<section class="block"><div class="wrap">
  <div class="section-head reveal"><h2>Features</h2></div>
  <div class="features">{feats}</div>
</div></section>

<section class="block"><div class="wrap">
  <div class="section-head reveal"><h2>{a["list_title"]}</h2><p>{a["list_sub"]}</p></div>
  <div class="list">{items}</div>
</div></section>

<section class="block" id="legal" style="scroll-margin-top:80px"><div class="wrap">
  <div class="section-head reveal"><h2>Privacy, terms &amp; support</h2><p>Everything about how {a["name"]} handles your information, and how to reach us.</p></div>
  <div class="legal-cards">{legal}</div>
</div></section>

<section class="block"><div class="wrap">
  <div class="section-head reveal"><h2>More from Shivi Games</h2></div>
  <div class="others">{others}</div>
</div></section>
</main>

{footer()}

<script src="../assets/site.js" defer></script>
</body>
</html>
'''

import re as _re
def new_tab(html):
    # open external http(s) links in a new tab
    def fix(m):
        t = m.group(0)
        if 'target=' in t: return t
        return t[:-1] + (' target="_blank">' if 'rel=' in t else ' target="_blank" rel="noopener">')
    return _re.sub(r'<a [^>]*href="https?://[^"]+"[^>]*>', fix, html)

for slug, a in APPS.items():
    os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
    with open(os.path.join(ROOT, slug, 'index.html'), 'w') as f:
        f.write(new_tab(page(slug, a)))
    print('wrote', slug)
