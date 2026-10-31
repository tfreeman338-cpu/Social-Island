"""Refresh a public follower count. Leaves the last verified count intact on failure."""
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://socialpruf.com/instagram/gcu'
OUTPUT = ROOT / 'instagram-count.json'

def parse_count(html):
    patterns = [
        r'profileData:[\s\S]{0,250}?username:\s*"gcu"[\s\S]{0,350}?followerCount:\s*(\d+)',
        r'username:\s*"gcu"[\s\S]{0,150}?platform:\s*"instagram"[\s\S]{0,350}?followerCount:\s*(\d+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            count = int(match.group(1))
            if 0 <= count <= 9999999999:
                return count
    raise ValueError('Could not verify the @gcu Instagram follower count')

def main():
    try:
        request = urllib.request.Request(SOURCE, headers={'Accept': 'text/html'})
        with urllib.request.urlopen(request, timeout=30) as response:
            html = response.read(5_000_000).decode('utf-8')
        data = {
            'count': parse_count(html),
            'checkedAt': datetime.now(timezone.utc).isoformat(),
            'source': 'Socialpruf',
            'sourceUrl': SOURCE,
            'stale': False,
        }
        temporary = OUTPUT.with_suffix('.tmp')
        temporary.write_text(json.dumps(data, indent=2) + '\n')
        temporary.replace(OUTPUT)
        print(f"Updated Instagram followers: {data['count']:,}")
    except Exception as error:
        print(f'::warning::Instagram refresh unavailable ({type(error).__name__}); retaining the last verified count.')
        if not OUTPUT.exists():
            raise

if __name__ == '__main__':
    main()
