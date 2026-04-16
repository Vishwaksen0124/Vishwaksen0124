import sys
import json

data = json.loads(sys.argv[1])

t = str(data.get("total", 0))
c = str(data.get("commits", 0))
p = str(data.get("prs", 0))
s = str(data.get("stars", 0))
r = str(data.get("repos", 0))
f = str(data.get("followers", 0))

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="495" height="220" viewBox="0 0 495 220">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d1117;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#161b22;stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#58a6ff;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#1f6feb;stop-opacity:1"/>
    </linearGradient>
    <style>
      @keyframes fadeIn {{ from {{ opacity: 0; transform: translateX(-10px); }} to {{ opacity: 1; transform: translateX(0); }} }}
      @keyframes scaleIn {{ from {{ transform: scale(0); opacity: 0; }} to {{ transform: scale(1); opacity: 1; }} }}
      .stat-row {{ animation: fadeIn 0.6s ease-out forwards; opacity: 0; }}
      .r1 {{ animation-delay: 0.1s; }} .r2 {{ animation-delay: 0.2s; }} .r3 {{ animation-delay: 0.3s; }}
      .r4 {{ animation-delay: 0.4s; }} .r5 {{ animation-delay: 0.5s; }} .r6 {{ animation-delay: 0.6s; }}
      .rank-circle {{ animation: scaleIn 0.6s ease-out 0.3s forwards; transform-origin: center; opacity: 0; }}
      .title {{ font: 600 18px "Segoe UI", Ubuntu, sans-serif; fill: #58a6ff; }}
      .label {{ font: 400 13px "Segoe UI", Ubuntu, sans-serif; fill: #8b949e; }}
      .value {{ font: 700 13px "Segoe UI", Ubuntu, sans-serif; fill: #c9d1d9; }}
      .rank-text {{ font: 800 28px "Segoe UI", Ubuntu, sans-serif; fill: #58a6ff; }}
      .rank-label {{ font: 600 10px "Segoe UI", Ubuntu, sans-serif; fill: #8b949e; }}
      .icon {{ fill: #58a6ff; }}
    </style>
  </defs>
  <rect width="495" height="220" rx="6" fill="url(#grad)"/>
  <rect x="0.5" y="0.5" width="494" height="219" rx="6" fill="none" stroke="#30363d"/>
  <text x="25" y="36" class="title">Vishwaksen&#39;s GitHub Stats</text>
  <g transform="translate(25, 52)">
    <g class="stat-row r1" transform="translate(0, 0)">
      <svg x="0" y="0" width="16" height="16" viewBox="0 0 16 16" class="icon"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg>
      <text x="24" y="13" class="label">Total Contributions</text>
      <text x="290" y="13" class="value">{t}</text>
    </g>
    <g class="stat-row r2" transform="translate(0, 27)">
      <svg x="0" y="0" width="16" height="16" viewBox="0 0 16 16" class="icon"><path d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"/></svg>
      <text x="24" y="13" class="label">Commits</text>
      <text x="290" y="13" class="value">{c}</text>
    </g>
    <g class="stat-row r3" transform="translate(0, 54)">
      <svg x="0" y="0" width="16" height="16" viewBox="0 0 16 16" class="icon"><path d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"/></svg>
      <text x="24" y="13" class="label">Pull Requests</text>
      <text x="290" y="13" class="value">{p}</text>
    </g>
    <g class="stat-row r4" transform="translate(0, 81)">
      <svg x="0" y="0" width="16" height="16" viewBox="0 0 16 16" class="icon"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg>
      <text x="24" y="13" class="label">Stars Earned</text>
      <text x="290" y="13" class="value">{s}</text>
    </g>
    <g class="stat-row r5" transform="translate(0, 108)">
      <svg x="0" y="0" width="16" height="16" viewBox="0 0 16 16" class="icon"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg>
      <text x="24" y="13" class="label">Repositories</text>
      <text x="290" y="13" class="value">{r}</text>
    </g>
    <g class="stat-row r6" transform="translate(0, 135)">
      <svg x="0" y="0" width="16" height="16" viewBox="0 0 16 16" class="icon"><path d="M5.5 3.5a2 2 0 100 4 2 2 0 000-4zM2 5.5a3.5 3.5 0 115.898 2.549 5.507 5.507 0 013.034 4.084.75.75 0 11-1.482.235 4.001 4.001 0 00-7.9 0 .75.75 0 01-1.482-.236A5.507 5.507 0 013.102 8.05 3.49 3.49 0 012 5.5zM11 4a.75.75 0 100 1.5 1.5 1.5 0 01.666 2.844.75.75 0 00-.416.672v.352a.75.75 0 00.574.73c1.2.289 2.162 1.2 2.522 2.372a.75.75 0 101.434-.44 5.01 5.01 0 00-2.56-3.012A3 3 0 0011 4z"/></svg>
      <text x="24" y="13" class="label">Followers</text>
      <text x="290" y="13" class="value">{f}</text>
    </g>
  </g>
  <g class="rank-circle" transform="translate(415, 115)">
    <circle cx="0" cy="0" r="40" fill="none" stroke="#21262d" stroke-width="6"/>
    <circle cx="0" cy="0" r="40" fill="none" stroke="#58a6ff" stroke-width="6" stroke-dasharray="251.2" stroke-dashoffset="63" stroke-linecap="round" transform="rotate(-90)"/>
    <text x="0" y="5" text-anchor="middle" class="rank-text">B+</text>
    <text x="0" y="19" text-anchor="middle" class="rank-label">Top 50%</text>
  </g>
  <rect x="25" y="205" width="445" height="2" rx="1" fill="url(#barGrad)" opacity="0.3"/>
</svg>"""

with open("stats.svg", "w") as file:
    file.write(svg)
print(
    f"Generated stats.svg: Total={t}, Commits={c}, PRs={p}, Stars={s}, Repos={r}, Followers={f}"
)
