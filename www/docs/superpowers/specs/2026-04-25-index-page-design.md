# index.html Redesign Spec

**Date:** 2026-04-25  
**Status:** Approved

## Goal

Replace the existing `index.html` with a modernized personal landing page for safnet.com. The new page drops Bootstrap, jQuery, and Font Awesome in favor of plain CSS and vanilla JS.

## Layout

Single-column, top-to-bottom:

1. Header
2. Hero banner
3. Recent blog posts
4. Other projects
5. Footer

---

## Sections

### Header

- Dark background bar; use `#1b1b1d` as starting value, fine-tune by inspecting blog.safnet.com with browser devtools
- Left: circular profile/logo image from `https://blog.safnet.com/img/BHCU-logo-safnet-small-darktheme.webp`
- Center-left: "Stephen A. Fuqua" as styled text link to `/`
- Nav links: "Blog" (→ `https://blog.safnet.com`) and "About" (→ `/about`)
- Right: GitHub icon link and LinkedIn icon link
- Icons: inline SVG (no external icon library)
- Matches the visual style of the blog header shown in the reference screenshot

### Hero Banner

- Full-width section, ~250px tall
- Background: `images/mexicanHat.png`, centered, `background-size: cover`
- Overlay text anchored bottom-left, white with `text-shadow` for legibility
- `<h1>`: "Stephen A. Fuqua (saf)"
- Subtitle `<p>`: "a Bahá'í, software engineer, and nature lover in Austin, Texas, USA"

### Recent Blog Posts

- `<section>` with `<h2>` heading "Recent Blog Posts"
- On page load, vanilla JS fetches `https://blog.safnet.com/rss.xml`
- Parsed with `DOMParser`; renders 5 latest items as `<ul>` of `<a>` links (title + href)
- On fetch/parse failure: fallback message linking to `https://blog.safnet.com`

### Other Projects

- `<section>` with `<h2>` heading "Other Projects"
- Placeholder `<ul>` with current known sites:
  - [Green Bahá'í](https://www.greenbahai.com)
  - [South Central Regional Training Institute](https://www.southcentralrti.org)
  - [InterfaithNews.Net (archive)](/inn/)
- Marked as placeholder — to be revised

### Footer

- Dark background, white text (matches header)
- Copyright © 2026 Stephen A. Fuqua, link to safnet.com
- Creative Commons Attribution-ShareAlike 3.0 license link
- MIT license link (→ `/LICENSE`)

---

## Technical Decisions

- **No external CSS frameworks** — plain CSS only, styles in `/styles/safnet.css` (existing file)
- **No jQuery** — vanilla JS for RSS fetch
- **No Font Awesome** — inline SVG for GitHub and LinkedIn icons
- **Google Analytics** — keep existing gtag snippet as-is (UA-550669-1); updating to GA4 is out of scope
- **RSS CORS** — fetch may be blocked; graceful fallback required
- **Fonts** — retain Google Fonts `Open Sans` import (already in safnet.css)

---

## Out of Scope

- Replacing the hero background image (deferred)
- Adding a Twitter/X link (current link is outdated; omit for now)
- Blog post dates or excerpts in the recent posts list (titles + links only)
