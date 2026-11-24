import React, { lazy, Suspense, useEffect, useRef, useState } from "react";
import { Link, Route, Routes, useNavigate, useParams } from "react-router-dom";
import { BreadcrumbItem, getChildren, getPlace, getStats, Place, searchPlaces, Stats } from "./api";

const Globe = lazy(() => import("./Globe"));

function getTypeIcon(type?: string): string {
  switch (type) {
    case "country":
      return "🇮🇳";
    case "state":
      return "🗺️";
    case "union-territory":
      return "🏛️";
    case "district":
      return "🏙️";
    case "taluk":
      return "🏘️";
    case "village":
      return "🏡";
    case "place":
      return "📍";
    default:
      return "📌";
  }
}

function formatTypeName(type?: string): string {
  switch (type) {
    case "country":
      return "Country";
    case "state":
      return "State";
    case "union-territory":
      return "Union Territory";
    case "district":
      return "District";
    case "taluk":
      return "Sub-District (Taluk)";
    case "village":
      return "Census Village";
    case "place":
      return "Landmark & Heritage";
    default:
      return type ? type.charAt(0).toUpperCase() + type.slice(1) : "Place";
  }
}

function ErrorView({ code, message }: { code: number; message: string }) {
  return (
    <div className="error-card" role="alert">
      <div className="error-badge">{code}</div>
      <h2>{code === 404 ? "Place Not Found" : "Something Went Wrong"}</h2>
      <p>{message}</p>
      <div className="error-actions">
        <Link className="btn btn-primary" to="/p/india">Explore India</Link>
        <Link className="btn btn-secondary" to="/">Back to Home</Link>
      </div>
    </div>
  );
}

function SearchBar() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<Place[]>([]);
  const [loading, setLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (query.trim().length < 2) {
      setResults([]);
      setIsOpen(false);
      return;
    }

    setLoading(true);
    const timeout = setTimeout(() => {
      searchPlaces(query)
        .then((res) => {
          setResults(res);
          setIsOpen(true);
        })
        .catch(() => setResults([]))
        .finally(() => setLoading(false));
    }, 200);

    return () => clearTimeout(timeout);
  }, [query]);

  // Close dropdown when clicking outside
  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const handleSelect = (placeId: string) => {
    setQuery("");
    setIsOpen(false);
    navigate(`/p/${placeId}`);
  };

  return (
    <div className="search-container" ref={containerRef}>
      <form
        role="search"
        className="search-input-wrapper"
        onSubmit={(e) => {
          e.preventDefault();
          if (results.length > 0) {
            handleSelect(results[0].id);
          }
        }}
      >
        <label htmlFor="place-search" className="visually-hidden">
          Search places across India
        </label>
        <span className="search-icon" aria-hidden="true">🔍</span>
        <input
          id="place-search"
          name="search"
          type="search"
          autoComplete="off"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onFocus={() => query.length >= 2 && setIsOpen(true)}
          placeholder="Search states, districts, Taj Mahal..."
          aria-label="Search places across India"
        />
        {query && (
          <button
            type="button"
            className="search-clear-btn"
            onClick={() => {
              setQuery("");
              setResults([]);
            }}
            aria-label="Clear search"
          >
            ✕
          </button>
        )}
      </form>

      {isOpen && (
        <ul className="search-results-dropdown" role="listbox">
          {loading && <li className="search-status-item">Searching places...</li>}
          {!loading && results.length === 0 && (
            <li className="search-status-item">No matching places found for "{query}".</li>
          )}
          {!loading &&
            results.map((p) => (
              <li key={p.id}>
                <button
                  type="button"
                  onClick={() => handleSelect(p.id)}
                  className="search-result-btn"
                >
                  <span className="search-result-icon">{getTypeIcon(p.type)}</span>
                  <div className="search-result-info">
                    <span className="search-result-name">{p.name}</span>
                    <small className="search-result-path">
                      {p.path || p.name} • <em>{formatTypeName(p.type)}</em>
                    </small>
                  </div>
                </button>
              </li>
            ))}
        </ul>
      )}
    </div>
  );
}

function Breadcrumbs({ items, currentName }: { items?: BreadcrumbItem[]; currentName: string }) {
  return (
    <nav className="breadcrumbs" aria-label="Breadcrumbs">
      <Link to="/" className="crumb-link">Home</Link>
      <span className="crumb-sep">/</span>
      {items &&
        items.map((crumb) => (
          <React.Fragment key={crumb.id}>
            <Link to={`/p/${crumb.id}`} className="crumb-link">
              {crumb.name}
            </Link>
            <span className="crumb-sep">/</span>
          </React.Fragment>
        ))}
      <span className="crumb-current">{currentName}</span>
    </nav>
  );
}

function HomePage() {
  const [stats, setStats] = useState<Stats | null>(null);
  const [backendOffline, setBackendOffline] = useState(false);

  useEffect(() => {
    getStats()
      .then(setStats)
      .catch(() => setBackendOffline(true));
  }, []);

  return (
    <div className="home-view">
      {backendOffline && (
        <div className="offline-warning-banner" role="status">
          <span className="banner-icon">⚠️</span>
          <div className="banner-text">
            <strong>Backend API is offline:</strong> Cannot connect to <code>http://localhost:8000</code>.
            Please start the backend with <code>uvicorn main:app --reload</code> or run <code>docker compose up --build</code>.
          </div>
        </div>
      )}

      <section className="hero">
        <div className="hero-globe">
          <Suspense fallback={<div className="globe-placeholder">Loading 3D Globe...</div>}>
            <Globe />
          </Suspense>
        </div>

        <div className="hero-content">
          <span className="hero-badge">Discover the Subcontinent</span>
          <h1>India Explorer</h1>
          <p className="hero-desc">
            Journey across 28 states, 8 union territories, historic districts, and world-renowned
            cultural landmarks. Experience India's geography, rich traditions, and heritage monuments.
          </p>

          <div className="hero-cta-group">
            <Link className="btn btn-primary" to="/p/india">
              Explore All States & Territories ➔
            </Link>
            <Link className="btn btn-outline" to="/p/taj-mahal">
              Famous Heritage: Taj Mahal 🏛️
            </Link>
          </div>

          <div className="stats-strip">
            <div className="stat-card">
              <span className="stat-number">{stats ? stats.states : "28"}</span>
              <span className="stat-label">States</span>
            </div>
            <div className="stat-card">
              <span className="stat-number">{stats ? stats.union_territories : "8"}</span>
              <span className="stat-label">Union Territories</span>
            </div>
            <div className="stat-card">
              <span className="stat-number">40+</span>
              <span className="stat-label">UNESCO Sites</span>
            </div>
            <div className="stat-card">
              <span className="stat-number">1.4B+</span>
              <span className="stat-label">Subcontinent</span>
            </div>
          </div>
        </div>
      </section>

      <section className="quick-access-section">
        <h2>Popular Destinations</h2>
        <div className="quick-cards-grid">
          <Link to="/p/karnataka" className="quick-card">
            <span className="quick-icon">🌿</span>
            <h3>Karnataka</h3>
            <p>Silicon Plateau, Mysore Palace & Hampi ruins</p>
          </Link>
          <Link to="/p/uttar-pradesh" className="quick-card">
            <span className="quick-icon">🕌</span>
            <h3>Uttar Pradesh</h3>
            <p>Taj Mahal, sacred Varanasi & historic Lucknow</p>
          </Link>
          <Link to="/p/maharashtra" className="quick-card">
            <span className="quick-icon">🏙️</span>
            <h3>Maharashtra</h3>
            <p>Financial capital Mumbai & Ajanta-Ellora caves</p>
          </Link>
          <Link to="/p/rajasthan" className="quick-card">
            <span className="quick-icon">🏰</span>
            <h3>Rajasthan</h3>
            <p>Land of Kings, Jaipur, Amer Fort & Thar Desert</p>
          </Link>
          <Link to="/p/delhi-ut" className="quick-card">
            <span className="quick-icon">🏛️</span>
            <h3>Delhi (NCT)</h3>
            <p>National capital, Red Fort & Qutub Minar</p>
          </Link>
          <Link to="/p/kerala" className="quick-card">
            <span className="quick-icon">🌴</span>
            <h3>Kerala</h3>
            <p>God's Own Country, serene backwaters & spices</p>
          </Link>
        </div>
      </section>
    </div>
  );
}

function PlaceView() {
  const { id = "india" } = useParams();
  const [place, setPlace] = useState<Place | null>(null);
  const [children, setChildren] = useState<Place[]>([]);
  const [filterType, setFilterType] = useState<string>("all");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<any>(null);

  useEffect(() => {
    setLoading(true);
    setError(null);

    Promise.all([
      getPlace(id),
      getChildren(id),
    ])
      .then(([placeData, childrenData]) => {
        setPlace(placeData);
        setChildren(childrenData);
        setFilterType("all");
      })
      .catch((err) => {
        setError(err);
      })
      .finally(() => setLoading(false));
  }, [id]);

  useEffect(() => {
    if (place) {
      document.title = `${place.name} | India Explorer`;
    }
  }, [place]);

  if (error) {
    return (
      <ErrorView
        code={error.status || 500}
        message={
          error.status === 404
            ? `We couldn't find details for "${id}". It may not be seeded yet.`
            : error.message || "Failed to load place details."
        }
      />
    );
  }

  if (loading) {
    return (
      <div className="loading-state">
        <div className="spinner"></div>
        <p>Loading destination details...</p>
      </div>
    );

  }

  if (!place) return null;

  // Available filter options based on children
  const childTypes = Array.from(new Set(children.map((c) => c.type)));
  const filteredChildren =
    filterType === "all" ? children : children.filter((c) => c.type === filterType);

  // Exclude current item from breadcrumb list to display properly
  const breadcrumbList = (place.breadcrumbs || []).filter((b) => b.id !== place.id);

  return (
    <div className="place-view-layout">
      <Breadcrumbs items={breadcrumbList} currentName={place.name} />

      <div className="place-grid-layout">
        {/* Main Content Area: Children Places */}
        <section className="place-main-section">
          <div className="place-header-bar">
            <div>
              <span className="badge-type">{formatTypeName(place.type)}</span>
              <h1>{place.name}</h1>
              {place.path && <p className="place-path-sub">{place.path}</p>}
            </div>

            {place.parent && (
              <Link to={`/p/${place.parent}`} className="btn btn-sm btn-outline">
                ⬆ Parent Region
              </Link>
            )}
          </div>

          {/* Filter Pills */}
          {childTypes.length > 1 && (
            <div className="filter-pills" role="tablist">
              <button
                type="button"
                className={`filter-pill ${filterType === "all" ? "active" : ""}`}
                onClick={() => setFilterType("all")}
              >
                All ({children.length})
              </button>
              {childTypes.map((t) => (
                <button
                  key={t}
                  type="button"
                  className={`filter-pill ${filterType === t ? "active" : ""}`}
                  onClick={() => setFilterType(t)}
                >
                  {formatTypeName(t)} ({children.filter((c) => c.type === t).length})
                </button>
              ))}
            </div>
          )}

          {/* Children Cards */}
          {children.length === 0 ? (
            <div className="empty-children-box">
              <p>📍 You have reached the detailed landmark view for <strong>{place.name}</strong>.</p>
              <p>Explore the full details, highlights, and history in the panel beside this view.</p>
            </div>
          ) : (
            <div className="children-cards-grid">
              {filteredChildren.map((item) => (
                <Link key={item.id} to={`/p/${item.id}`} className="place-card">
                  <div className="place-card-top">
                    <span className="card-icon">{getTypeIcon(item.type)}</span>
                    <span className="card-type-chip">{formatTypeName(item.type)}</span>
                  </div>
                  <h3 className="card-title">{item.name}</h3>
                  {item.summary && <p className="card-summary">{item.summary}</p>}
                  <span className="card-link-prompt">Explore details ➔</span>
                </Link>
              ))}
            </div>
          )}
        </section>

        {/* Sidebar Panel: Detailed Info & Quick Facts */}
        <aside className="place-sidebar-panel" id="info">
          <div className="sidebar-header">
            <span className="sidebar-icon">{getTypeIcon(place.type)}</span>
            <h2>{place.name} Overview</h2>
          </div>

          {place.summary && <p className="sidebar-summary">{place.summary}</p>}

          {/* Quick Metrics */}
          <div className="quick-metrics">
            {place.area && (
              <div className="metric-chip">
                <span className="metric-label">Area</span>
                <span className="metric-value">{place.area}</span>
              </div>
            )}
            {place.population && (
              <div className="metric-chip">
                <span className="metric-label">Population</span>
                <span className="metric-value">{place.population}</span>
              </div>
            )}
          </div>

          {/* Profile Facts */}
          {place.profile && Object.keys(place.profile).length > 0 && (
            <div className="profile-section">
              <h3>Key Information</h3>
              <dl className="profile-list">
                {Object.entries(place.profile).map(([key, value]) => (
                  <div key={key} className="profile-item">
                    <dt>{key}</dt>
                    <dd>{value}</dd>
                  </div>
                ))}
              </dl>
            </div>
          )}

          {/* Highlights Points */}
          {place.points && place.points.length > 0 && (
            <div className="highlights-section">
              <h3>Key Highlights</h3>
              <ul className="highlights-list">
                {place.points.map((point, index) => (
                  <li key={index}>{point}</li>
                ))}
              </ul>
            </div>
          )}

          {/* Official Wikipedia Link */}
          {place.wiki && (
            <div className="sidebar-footer-action">
              <a
                href={place.wiki}
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-wiki"
              >
                Read More on Wikipedia ↗
              </a>
            </div>
          )}
        </aside>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <div className="app-wrapper">
      <header className="app-header">
        <div className="header-inner">
          <Link to="/" className="app-brand" aria-label="India Explorer Home">
            <span className="brand-flag">🇮🇳</span>
            <span className="brand-name">India Explorer</span>
          </Link>
          <SearchBar />
        </div>
      </header>

      <main className="app-main">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/p/:id" element={<PlaceView />} />
          <Route path="*" element={<ErrorView code={404} message="The requested page does not exist." />} />
        </Routes>
      </main>

      <footer className="app-footer">
        <div className="footer-inner">
          <div className="footer-brand">
            <span className="brand-flag">🇮🇳</span> <strong>India Explorer</strong>
            <p>An interactive digital guide to the geography, states, culture, and monuments of India.</p>
          </div>
          <div className="footer-links">
            <Link to="/">Home</Link>
            <Link to="/p/india">All States & UTs</Link>
            <a href="/sitemap.xml">Sitemap</a>
          </div>
        </div>
      </footer>
    </div>
  );
}
