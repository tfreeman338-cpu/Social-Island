# the Social Island

The complete dark TV dashboard: clock, weather, GCU Instagram followers, monthly calendar, university dates, men's basketball home games, and 48 Student Engagement events imported from the shared Monday view.

## Put it on GitHub Pages

1. Unzip this download. Create a GitHub repository, for example `social-island`, with `main` as its default branch.
2. Upload the **contents** of this folder to the root of the repository, including `.github/workflows/deploy.yml`. Do not upload the ZIP or place the website inside another folder. On a Mac, press Command + Shift + Period to show the `.github` folder in Finder. If GitHub's upload screen omits that folder, use **Add file → Create new file**, enter `.github/workflows/deploy.yml` as the filename, and paste the included workflow's contents.
3. In the repository, select **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Open **Actions → Publish Social Island → Run workflow**. When it finishes, the published address appears in **Settings → Pages** and in the workflow's deployment result.
5. Open that address on the computer connected to the TV and enter browser full-screen mode. Use 100% browser zoom and a landscape display of at least 900 × 600 pixels for the one-screen layout.

GitHub Pages does not include the ChatGPT sign-in protection of the original hosted site. Choose repository visibility and Pages availability appropriate to your workplace. GitHub Free supports Pages in public repositories; private repository availability depends on the GitHub plan.

## Automatic Instagram updates

The included GitHub Actions workflow checks the public Socialpruf page at 17 minutes past each hour, stores the latest verified count in `instagram-count.json`, and republishes the dashboard. No Instagram password or paid API key is required. The dashboard reads this file when opened and once an hour afterward.

GitHub schedules are approximate and can be delayed. Scheduled workflows run from the default branch; public repositories may have scheduled workflows disabled after 60 days without repository activity. Check the Actions tab if updates stop. Source data is only as fresh as Socialpruf's page. If the page changes format or is unavailable, the updater keeps the last verified count. The display marks a count older than two hours as the last saved check.

If your repository blocks workflow writes or protects the main branch, the workflow's snapshot commit may be rejected. Allow the workflow to update `instagram-count.json` or ask your repository administrator to configure an approved update process.

The `GITHUB_TOKEN` supplied by GitHub Actions handles repository and Pages access. Do not add any passwords to these files.

## Events and settings

- `university-events.js`: all 52 dated entries from the 2026–27 university calendar.
- `basketball-events.js`: 18 regular-season home games plus the October exhibition, with Phoenix times and promotions.
- `student-engagement-events.js`: 48 events from the public Monday view's next-three-month window, imported October 30, 2026. This is a snapshot, not an automatic Monday sync.
- `app.js`: behavior, clock, weather, calendar, and Instagram refresh.
- `styles.css`: dark theme and TV layout.
- `index.html`: page structure.

Imported event entries are included for every visitor. Events added through the dashboard and the selected weather location are saved in that browser only. Counts and custom events saved on the old hosted address do not transfer to a new GitHub Pages address. No TikTok tile is included.

## Preview locally

From this folder, run `python3 -m http.server 8000`, then open `http://localhost:8000`. Opening `index.html` directly can prevent the browser from loading the follower JSON. To test the data refresh locally, run `python3 scripts/update-instagram.py`.

## Sources

- Instagram: https://socialpruf.com/instagram/gcu
- Weather: https://open-meteo.com/
- Basketball: https://gculopes.com/sports/mens-basketball/schedule
- Student Engagement: the public Monday link supplied for this project.

GitHub setup references: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages and https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule

All interface icons use inline SVG with no icon-font, emoji, or external icon-library dependency.
