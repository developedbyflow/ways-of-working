# SEO audit

- **Bar:** every page you want people to find is:
  - crawlable and indexable;
  - has its content in the HTML;
  - has one canonical URL.

  Only public pages need this. Screens behind a login don't.
- **Tools:**
  - Google Search Console: the Page indexing report, URL Inspection;
  - Rich Results Test;
  - Lighthouse SEO;
  - view-source next to the rendered page.

## Checklist
- [ ] Pages that must rank have their content in the server HTML (SSR or SSG).
- [ ] Each page has a unique title and meta description.
- [ ] Each piece of content has one canonical URL. Moved pages redirect with 301 or 308.
- [ ] `robots.txt` doesn't block pages you need.
- [ ] Pages you don't want indexed use `noindex`, and are not blocked in `robots.txt`, or Google can't see the `noindex`.
- [ ] The sitemap lists only canonical, indexable URLs that return 200.
- [ ] Missing pages return a real 404 or 410, not a 200 (a soft 404).
- [ ] Filter and sort URLs point their canonical to the main page, or use `noindex`. No endless URL combinations.
- [ ] Structured data is valid (product, breadcrumb, article).
- [ ] Internal links are real `<a href>` elements.
- [ ] Language versions use `hreflang`. Each version lists all the others, and itself.
- [ ] Core Web Vitals → `audits/performance.md`.

## Concepts
- SEO for developers → [F22 SEO for developers](https://claude.ai/artifact/WGUAmuc7K77y93KeDT6Ui1)
- Server rendering and Next.js → [F09 Server rendering and Next.js](https://claude.ai/artifact/L4gfk2AGUL4wbuavqw4VJh)

## Changelog
- 2026-10-05: v1
