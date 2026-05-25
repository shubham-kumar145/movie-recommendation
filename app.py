import requests
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-recommendation-ez05.onrender.com/"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"
TMDB_IMG_ORIGINAL = "https://image.tmdb.org/t/p/original"

st.set_page_config(
    page_title="CineMatch — Movie Recommendations",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================
# STYLES — Cinematic Dark Theme
# =============================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #e8e0d0;
}

[data-testid="stAppViewContainer"] {
    background: #0d0d0f;
    background-image:
        radial-gradient(ellipse 80% 50% at 20% 10%, rgba(220, 60, 60, 0.07) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(255, 160, 50, 0.05) 0%, transparent 60%);
}

[data-testid="stHeader"] { background: transparent; }

[data-testid="stSidebar"] {
    background: #121214 !important;
    border-right: 1px solid rgba(255,255,255,0.06);
}

.block-container {
    padding: 1.5rem 2rem 3rem;
    max-width: 1600px;
}

/* ── Typography ── */
h1, h2, h3 {
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 0.04em;
    color: #f0e8d8;
}

/* ── App Header ── */
.app-header {
    display: flex;
    align-items: baseline;
    gap: 16px;
    margin-bottom: 0.25rem;
}

.app-logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    letter-spacing: 0.1em;
    color: #f0e8d8;
    line-height: 1;
}

.app-logo span {
    color: #e63946;
}

.app-tagline {
    font-size: 0.82rem;
    color: #6b6860;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 400;
}

/* ── Section Headings ── */
.section-label {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.5rem;
    letter-spacing: 0.06em;
    color: #c8c0b0;
    margin: 1.5rem 0 0.75rem;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-label .pill {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.7rem;
    background: rgba(230, 57, 70, 0.2);
    color: #e63946;
    border: 1px solid rgba(230, 57, 70, 0.35);
    border-radius: 20px;
    padding: 2px 10px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    font-weight: 500;
}

/* ── Movie Cards ── */
.movie-card-wrap {
    position: relative;
    border-radius: 10px;
    overflow: hidden;
    background: #1a1a1e;
    border: 1px solid rgba(255,255,255,0.06);
    transition: transform 0.2s ease, border-color 0.2s ease;
    cursor: pointer;
}

.movie-card-wrap:hover {
    border-color: rgba(230, 57, 70, 0.5);
    transform: translateY(-3px);
}

.movie-poster-img {
    width: 100%;
    aspect-ratio: 2/3;
    object-fit: cover;
    display: block;
    border-radius: 10px 10px 0 0;
}

.movie-poster-placeholder {
    width: 100%;
    aspect-ratio: 2/3;
    background: linear-gradient(145deg, #1e1e22 0%, #252530 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.5rem;
    border-radius: 10px 10px 0 0;
}

.movie-card-info {
    padding: 10px 10px 8px;
}

.movie-card-title {
    font-size: 0.78rem;
    font-weight: 500;
    color: #d0c8b8;
    line-height: 1.3;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    min-height: 2.2em;
}

/* ── Details Layout ── */
.detail-backdrop {
    width: 100%;
    height: 380px;
    object-fit: cover;
    object-position: center 30%;
    border-radius: 12px;
    display: block;
    margin-bottom: 1.5rem;
    filter: brightness(0.75);
}

.detail-poster {
    border-radius: 10px;
    width: 100%;
    box-shadow: 0 20px 60px rgba(0,0,0,0.7);
    display: block;
}

.detail-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    letter-spacing: 0.05em;
    color: #f0e8d8;
    line-height: 1.05;
    margin-bottom: 0.5rem;
}

.detail-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 1rem;
}

.meta-badge {
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
}

.meta-badge.year {
    background: rgba(255,255,255,0.08);
    color: #a0987e;
    border: 1px solid rgba(255,255,255,0.1);
}

.meta-badge.genre {
    background: rgba(230, 57, 70, 0.12);
    color: #e88888;
    border: 1px solid rgba(230, 57, 70, 0.25);
}

.detail-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.07);
    margin: 1rem 0;
}

.overview-heading {
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #6b6860;
    font-weight: 500;
    margin-bottom: 0.6rem;
}

.overview-text {
    font-size: 0.95rem;
    line-height: 1.75;
    color: #a8a090;
    font-weight: 300;
}

/* ── Streamlit Widget Overrides ── */
.stTextInput > div > div > input {
    background: #1a1a1e !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    color: #e8e0d0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.65rem 1rem !important;
    transition: border-color 0.2s !important;
}

.stTextInput > div > div > input:focus {
    border-color: rgba(230, 57, 70, 0.6) !important;
    box-shadow: 0 0 0 3px rgba(230, 57, 70, 0.12) !important;
}

.stTextInput > div > div > input::placeholder { color: #4a4845 !important; }

.stSelectbox > div > div {
    background: #1a1a1e !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    color: #e8e0d0 !important;
}

div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label,
div[data-testid="stTextInput"] label {
    color: #6b6860 !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    font-weight: 500 !important;
}

.stButton > button {
    background: rgba(230, 57, 70, 0.15) !important;
    border: 1px solid rgba(230, 57, 70, 0.35) !important;
    color: #e88888 !important;
    border-radius: 6px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.05em !important;
    font-weight: 500 !important;
    padding: 0.35rem 0.5rem !important;
    transition: all 0.2s !important;
    width: 100% !important;
}

.stButton > button:hover {
    background: rgba(230, 57, 70, 0.3) !important;
    border-color: rgba(230, 57, 70, 0.6) !important;
    color: #f0a0a0 !important;
}

/* Back button */
.back-btn > div > button {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #908880 !important;
    border-radius: 6px !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.04em !important;
}

.back-btn > div > button:hover {
    background: rgba(255,255,255,0.09) !important;
    color: #d0c8b8 !important;
}

/* Sidebar */
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #1c1c20 !important;
}

[data-testid="stSidebar"] .stButton > button {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    color: #908880 !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,0.1) !important;
    color: #d0c8b8 !important;
}

/* Divider */
hr { border-color: rgba(255,255,255,0.06) !important; }

/* Info/Error boxes */
.stAlert { border-radius: 8px !important; }
.stInfo { background: rgba(255,255,255,0.04) !important; border: 1px solid rgba(255,255,255,0.08) !important; }
.stError { background: rgba(230, 57, 70, 0.1) !important; border: 1px solid rgba(230, 57, 70, 0.25) !important; }
.stWarning { background: rgba(255,160,50,0.08) !important; border: 1px solid rgba(255,160,50,0.2) !important; }

/* Caption text */
.stCaption { color: #4a4845 !important; font-size: 0.78rem !important; }

/* Slider */
.stSlider [data-baseweb="slider"] .slider { background: rgba(230,57,70,0.4) !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0d0d0f; }
::-webkit-scrollbar-thumb { background: #2a2a2e; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #3a3a3e; }
</style>
""",
    unsafe_allow_html=True,
)

# =============================
# STATE + ROUTING
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except Exception:
        pass


def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()


# =============================
# API HELPERS
# =============================
@st.cache_data(ttl=30)
def api_get_json(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=25)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}: {r.text[:300]}"
        return r.json(), None
    except Exception as e:
        return None, f"Request failed: {e}"


# =============================
# CARD RENDERER
# =============================
def poster_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.info("No movies to show.")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0

    for r in range(rows):
        colset = st.columns(cols, gap="small")
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1
            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")

            with colset[c]:
                # Poster image or placeholder
                if poster:
                    st.markdown(
                        f"""<div class="movie-card-wrap">
                            <img class="movie-poster-img" src="{poster}" alt="{title}" loading="lazy"/>
                            <div class="movie-card-info">
                                <div class="movie-card-title">{title}</div>
                            </div>
                        </div>""",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f"""<div class="movie-card-wrap">
                            <div class="movie-poster-placeholder">🎬</div>
                            <div class="movie-card-info">
                                <div class="movie-card-title">{title}</div>
                            </div>
                        </div>""",
                        unsafe_allow_html=True,
                    )

                if st.button(
                    "▶  Open",
                    key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}",
                    use_container_width=True,
                ):
                    if tmdb_id:
                        goto_details(tmdb_id)

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)


def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append(
                {
                    "tmdb_id": tmdb["tmdb_id"],
                    "title": tmdb.get("title") or x.get("title") or "Untitled",
                    "poster_url": tmdb.get("poster_url"),
                }
            )
    return cards


def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    keyword_l = keyword.strip().lower()

    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        raw_items = []
        for m in raw:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                }
            )
    elif isinstance(data, list):
        raw_items = []
        for m in data:
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            poster_url = m.get("poster_url")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": poster_url,
                    "release_date": m.get("release_date", ""),
                }
            )
    else:
        return [], []

    matched = [x for x in raw_items if keyword_l in x["title"].lower()]
    final_list = matched if matched else raw_items

    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    cards = [
        {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]}
        for x in final_list[:limit]
    ]
    return suggestions, cards


# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.markdown(
        """<div style="padding: 0.5rem 0 1rem;">
            <div style="font-family:'Bebas Neue',sans-serif; font-size:1.6rem; letter-spacing:0.08em; color:#f0e8d8;">
                CINE<span style="color:#e63946;">MATCH</span>
            </div>
            <div style="font-size:0.68rem; letter-spacing:0.1em; color:#4a4845; text-transform:uppercase; margin-top:2px;">
                Discover great films
            </div>
        </div>""",
        unsafe_allow_html=True,
    )

    if st.button("⬡  Home", use_container_width=True):
        goto_home()

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:0.68rem; letter-spacing:0.1em; color:#4a4845; text-transform:uppercase; margin-bottom:0.5rem;'>Browse Category</div>",
        unsafe_allow_html=True,
    )

    home_category = st.selectbox(
        "Category",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"],
        index=0,
        label_visibility="collapsed",
    )

    category_icons = {
        "trending": "🔥 Trending",
        "popular": "⭐ Popular",
        "top_rated": "🏆 Top Rated",
        "now_playing": "🎞 Now Playing",
        "upcoming": "📅 Upcoming",
    }

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:0.68rem; letter-spacing:0.1em; color:#4a4845; text-transform:uppercase; margin-bottom:0.5rem;'>Grid Columns</div>",
        unsafe_allow_html=True,
    )
    grid_cols = st.slider("Grid columns", 3, 8, 5, label_visibility="collapsed")

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:0.7rem; color:#3a3835; line-height:1.6;'>Powered by TMDB · Built with FastAPI + Streamlit</div>",
        unsafe_allow_html=True,
    )


# =============================
# HEADER (home only)
# =============================
if st.session_state.view == "home":
    st.markdown(
        """<div class="app-header">
            <div class="app-logo">CINE<span>MATCH</span></div>
        </div>
        <div class="app-tagline">Find your next favourite film</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)

# ==========================================================
# VIEW: HOME
# ==========================================================
if st.session_state.view == "home":

    typed = st.text_input(
        "Search",
        placeholder="🔍  Search movies — try 'Inception', 'Dark Knight', 'Parasite'...",
        label_visibility="collapsed",
    )

    # SEARCH MODE
    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Keep typing — need at least 2 characters.")
        else:
            data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"Search failed: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(data, typed.strip(), limit=24)

                if suggestions:
                    labels = ["— select a film —"] + [s[0] for s in suggestions]
                    col_drop, _ = st.columns([2, 3])
                    with col_drop:
                        selected = st.selectbox("Quick pick", labels, index=0, label_visibility="collapsed")
                    if selected != "— select a film —":
                        label_to_id = {s[0]: s[1] for s in suggestions}
                        goto_details(label_to_id[selected])
                else:
                    st.caption("No exact matches. Showing closest results.")

                if cards:
                    st.markdown(
                        f"<div class='section-label'>Results <span class='pill'>{len(cards)} films</span></div>",
                        unsafe_allow_html=True,
                    )
                    poster_grid(cards, cols=grid_cols, key_prefix="search_results")

        st.stop()

    # HOME FEED
    icon = category_icons.get(home_category, home_category)
    st.markdown(
        f"<div class='section-label'>{icon} <span class='pill'>24 films</span></div>",
        unsafe_allow_html=True,
    )

    home_cards, err = api_get_json(
        "/home", params={"category": home_category, "limit": 24}
    )
    if err or not home_cards:
        st.error(f"Couldn't load feed: {err or 'Unknown error'}")
        st.stop()

    poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")


# ==========================================================
# VIEW: DETAILS
# ==========================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("← Back to Home"):
            goto_home()
        st.stop()

    # Back button
    back_col, _ = st.columns([1, 8])
    with back_col:
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("← Back"):
            goto_home()
        st.markdown("</div>", unsafe_allow_html=True)

    # Load details
    data, err = api_get_json(f"/movie/id/{tmdb_id}")
    if err or not data:
        st.error(f"Could not load details: {err or 'Unknown error'}")
        st.stop()

    # Backdrop hero
    if data.get("backdrop_url"):
        st.markdown(
            f"""<div style="position:relative; border-radius:14px; overflow:hidden; margin-bottom:2rem;">
                <img src="{data['backdrop_url']}" style="width:100%; height:360px; object-fit:cover; object-position:center 30%; display:block; filter:brightness(0.6);" alt="backdrop"/>
                <div style="position:absolute; bottom:0; left:0; right:0; height:50%; background:linear-gradient(to top, #0d0d0f 0%, transparent 100%);"></div>
            </div>""",
            unsafe_allow_html=True,
        )

    # Poster + Info side by side
    left, right = st.columns([1, 2.6], gap="large")

    with left:
        if data.get("poster_url"):
            st.markdown(
                f'<img class="detail-poster" src="{data["poster_url"]}" alt="{data.get("title","")}" />',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div style="width:100%;aspect-ratio:2/3;background:#1a1a1e;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:3rem;">🎬</div>',
                unsafe_allow_html=True,
            )

    with right:
        title = data.get("title", "Unknown Title")
        release = (data.get("release_date") or "")[:4] or "—"
        genres = data.get("genres", [])
        overview = data.get("overview") or "No overview available."

        # Title
        st.markdown(f"<div class='detail-title'>{title}</div>", unsafe_allow_html=True)

        # Meta badges
        badges_html = f'<div class="detail-meta"><span class="meta-badge year">📅 {release}</span>'
        for g in genres:
            badges_html += f'<span class="meta-badge genre">{g["name"]}</span>'
        badges_html += "</div>"
        st.markdown(badges_html, unsafe_allow_html=True)

        st.markdown("<hr class='detail-divider'>", unsafe_allow_html=True)

        st.markdown("<div class='overview-heading'>Synopsis</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='overview-text'>{overview}</div>", unsafe_allow_html=True)

    # ── Recommendations ──
    title_for_search = (data.get("title") or "").strip()

    if title_for_search:
        bundle, err2 = api_get_json(
            "/movie/search",
            params={"query": title_for_search, "tfidf_top_n": 12, "genre_limit": 12},
        )

        if not err2 and bundle:
            tfidf_cards = to_cards_from_tfidf_items(bundle.get("tfidf_recommendations"))
            genre_cards = bundle.get("genre_recommendations", [])

            if tfidf_cards:
                st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
                st.markdown(
                    f"<div class='section-label'>🔎 Similar Films <span class='pill'>TF-IDF</span></div>",
                    unsafe_allow_html=True,
                )
                poster_grid(tfidf_cards, cols=grid_cols, key_prefix="details_tfidf")

            if genre_cards:
                st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
                st.markdown(
                    f"<div class='section-label'>🎭 More Like This <span class='pill'>Genre</span></div>",
                    unsafe_allow_html=True,
                )
                poster_grid(genre_cards, cols=grid_cols, key_prefix="details_genre")

        else:
            genre_only, err3 = api_get_json(
                "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
            )
            if not err3 and genre_only:
                st.markdown(
                    "<div class='section-label'>🎭 More Like This</div>",
                    unsafe_allow_html=True,
                )
                poster_grid(genre_only, cols=grid_cols, key_prefix="details_genre_fallback")
            else:
                st.info("No recommendations available right now.")
    else:
        st.info("No title available to compute recommendations.")
