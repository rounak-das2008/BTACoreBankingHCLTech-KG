import os, re, sys, json, subprocess

VIDEOS = {
    "coyle-ontologies-agents": "Sir59K8ZDPU",
    "hightower-zero-token-architecture": "A7WFt2JQ5sg",
    "pocock-software-fundamentals": "v4F1gFy-hqg",
    "eifrem-thinner-agents-semantic-layer": "VGN22pPpb-8",
    "reverse-engineering-enterprise-codebases": "1RM1XlDbYiA",
    "sahaj-reverse-engineering-talk": "FCODql2UWM8",
}

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw", "transcripts")
os.makedirs(OUT, exist_ok=True)


def via_api(vid):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        try:
            api = YouTubeTranscriptApi()
            fetched = api.fetch(vid, languages=["en", "en-US", "en-GB"])
            return " ".join(s.text for s in fetched)
        except AttributeError:
            segs = YouTubeTranscriptApi.get_transcript(vid, languages=["en", "en-US", "en-GB"])
            return " ".join(s["text"] for s in segs)
    except Exception as e:
        print(f"   api failed: {type(e).__name__}: {str(e)[:160]}")
        return None


def via_ytdlp(vid, name):
    tmp = os.path.join(OUT, f"_{name}")
    cmd = ["yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs",
           "--sub-langs", "en.*,en", "--sub-format", "vtt/srv3/best",
           "-o", tmp, f"https://www.youtube.com/watch?v={vid}"]
    try:
        subprocess.run(cmd, capture_output=True, timeout=180)
    except Exception as e:
        print(f"   yt-dlp error {e}")
    for f in sorted(os.listdir(OUT)):
        if f.startswith(f"_{name}") and (f.endswith(".vtt") or f.endswith(".srv3") or f.endswith(".json3")):
            path = os.path.join(OUT, f)
            raw = open(path, encoding="utf-8", errors="ignore").read()
            os.remove(path)
            lines, seen = [], None
            for ln in raw.splitlines():
                if "-->" in ln or ln.strip().isdigit() or ln.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
                    continue
                t = re.sub(r"<[^>]+>", "", ln).strip()
                if t and t != seen:
                    lines.append(t)
                    seen = t
            return " ".join(lines)
    return None


def meta(vid):
    try:
        r = subprocess.run(["yt-dlp", "--skip-download", "--print",
                            "%(title)s ||| %(uploader)s ||| %(duration)s ||| %(upload_date)s",
                            f"https://www.youtube.com/watch?v={vid}"],
                           capture_output=True, text=True, timeout=120)
        return r.stdout.strip()
    except Exception:
        return ""


for name, vid in VIDEOS.items():
    dest = os.path.join(OUT, f"{name}.txt")
    if os.path.exists(dest) and os.path.getsize(dest) > 2000:
        print(f"[skip] {name}")
        continue
    print(f"[fetch] {name} ({vid})")
    text = via_api(vid) or via_ytdlp(vid, name)
    m = meta(vid)
    if text:
        with open(dest, "w", encoding="utf-8") as f:
            f.write(f"# {name}\nURL: https://www.youtube.com/watch?v={vid}\nMETA: {m}\n\n{text}\n")
        print(f"   OK {len(text):,} chars | {m}")
    else:
        print(f"   FAILED | {m}")
