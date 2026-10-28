declare namespace Cloudflare {
  interface Env {
    ASSETS: Fetcher;
    DB?: D1Database;
    ANALYTICS_OWNER_EMAIL?: string;
    ANALYTICS_SECRET?: string;
    ANALYTICS_CAMPAIGNS?: string;
    ANALYTICS_CHAPTER_COUNT?: string;
    ANALYTICS_LANGUAGES?: string;
    BUCKET?: R2Bucket;
  }
}
