"""DOIs from Crossref's public API for a fixed list of citations, one request every few seconds; prints the top hits so that a match
is judged on journal, volume and page, never assumed. Responses are data from the web: only printed."""
import json
import time
import urllib.parse
import urllib.request

QUERIES = {
    "Mackie JCP 165 034104 (2026)": "Mackie Journal of Chemical Physics 165 034104 anharmonic polycyclic aromatic hydrocarbon",
    "power law scaling factors (2026)": "Vibrational scaling factors follow a power law",
    "Barone JCP 164 114309 (2026)": "Barone Journal of Chemical Physics 164 114309 2026",
    "Puzzarini Chem Rev 2019": "Accuracy and Interpretability: The Devil and the Holy Grail. New Routes across Old Boundaries in Computational Spectroscopy",
    "Bloino JCTC 2012": "General Perturbative Approach for Spectroscopy, Thermodynamics, and Kinetics: Methodological Background and Benchmark Studies",
    "Bloino JPCA 2015": "A VPT2 Route to Near-Infrared Spectroscopy: The Role of Mechanical and Electrical Anharmonicity",
    "Martin Taylor Lee CPL 275 414 (1997)": "The harmonic frequencies of benzene. A case for atomic natural orbital basis sets Martin Taylor Lee",
    "Moran JACS 128 9342 (2006)": "Popular Theoretical Methods Predict Benzene and Arenes To Be Nonplanar",
    "Mackie TCA 140 124 (2021)": "Mackie Candian Lee Tielens Theoretical Chemistry Accounts 140 124 2021",
}
for label, q in QUERIES.items():
    url = "https://api.crossref.org/works?rows=3&select=DOI,title,author,container-title,volume,page,article-number,issued&query.bibliographic=" + urllib.parse.quote(q)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "doi-lookup-script"}), timeout=40) as r:
                items = json.load(r)["message"]["items"]
            break
        except Exception as e:  # noqa: BLE001  a refused request is reported and retried after a pause
            items = None
            print(f"{label}: attempt {attempt + 1} failed ({str(e)[:60]})")
            time.sleep(15)
    print(f"== {label}")
    for it in items or []:
        first = (it.get("author") or [{}])[0].get("family", "?")
        print(f"   {it.get('DOI')} | {first} | {(it.get('container-title') or ['?'])[0][:40]} {it.get('volume', '?')}, "
              f"{it.get('page') or it.get('article-number') or '?'} ({(it.get('issued', {}).get('date-parts') or [['?']])[0][0]}) | "
              f"{(it.get('title') or ['?'])[0][:90]}")
    time.sleep(6)
