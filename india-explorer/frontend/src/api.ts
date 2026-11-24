export interface BreadcrumbItem {
  id: string;
  name: string;
  type: string;
}

export interface Place {
  id: string;
  name: string;
  type: "country" | "state" | "union-territory" | "district" | "taluk" | "village" | "place" | string;
  parent: string;
  path?: string;
  summary?: string;
  profile?: Record<string, string>;
  area?: string;
  population?: string;
  census_year?: string;
  points?: string[];
  wiki?: string;
  code?: number;
  taluk_count?: number;
  village_count?: number;
  source?: string;
  breadcrumbs?: BreadcrumbItem[];
}

export interface Stats {
  total: number;
  states: number;
  union_territories: number;
  districts: number;
  taluks?: number;
  villages?: number;
  landmarks: number;
}

const API_BASE = (import.meta.env.VITE_API || "http://localhost:8000").replace(/\/$/, "");

const cache = new Map<string, unknown>();

export async function get<T>(path: string): Promise<T> {
  const url = `${API_BASE}${path.startsWith("/") ? path : `/${path}`}`;
  if (cache.has(url)) {
    return cache.get(url) as T;
  }

  let res: Response;
  try {
    res = await fetch(url);
  } catch {
    throw new Error("Unable to connect to the India Explorer API. Please verify the backend is running.");
  }

  if (!res.ok) {
    const errorBody = await res.json().catch(() => ({}));
    const err: any = new Error(errorBody.error || `HTTP ${res.status}: Failed to fetch data`);
    err.status = res.status;
    throw err;
  }

  const data = await res.json();
  cache.set(url, data);
  return data as T;
}

export const getPlace = (id: string) => get<Place>(`/api/place/${id}`);
export const getChildren = (id: string, skip = 0, limit = 100) =>
  get<Place[]>(`/api/children/${id}?skip=${skip}&limit=${limit}`);
export const searchPlaces = (query: string) => get<Place[]>(`/api/search?q=${encodeURIComponent(query)}`);
export const getStats = () => get<Stats>("/api/stats");
