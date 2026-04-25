# index.html Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the existing Bootstrap/jQuery `index.html` with a modernized, plain-CSS/vanilla-JS personal landing page matching the spec at `docs/superpowers/specs/2026-04-25-index-page-design.md`.

**Architecture:** Single-column HTML page with five sections — header, hero banner, recent posts (JS-populated), other projects (static), and footer. All styling lives in the existing `styles/safnet.css`. RSS fetching uses the browser `fetch` API with `DOMParser`; failures show a static fallback link.

**Tech Stack:** Plain HTML5, plain CSS, vanilla JS (ES2020), Google Fonts (Open Sans), inline SVG icons, Google Analytics gtag.

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `index.html` | Replace | Page structure: header, hero, sections, footer, RSS script |
| `styles/safnet.css` | Append | New CSS classes for all new components |

---

## Task 1: Replace `index.html` shell

**Files:**
- Replace: `index.html`

- [ ] **Step 1: Write the new `index.html` with head only, empty body**

Replace the entire file with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>safnet - Stephen A. Fuqua</title>
    <meta name="author" content="Stephen A. Fuqua">
    <meta name="description" content="Stephen A. Fuqua (SAF) is a Bahá'í, software engineer, and nature lover in Austin, Texas, USA.">
    <link rel="canonical" href="https://www.safnet.com/">
    <link rel="icon" href="/favicon.png">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
    <link rel="stylesheet" href="/styles/safnet.css">
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-550669-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-550669-1');
    </script>
</head>
<body>
</body>
</html>
```

- [ ] **Step 2: Verify in browser**

Open `index.html` in a browser (or local server). Expected: blank white page, no console errors, page title reads "safnet - Stephen A. Fuqua".

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "chore: replace index.html shell, remove Bootstrap/jQuery dependencies"
```

---

## Task 2: Add header HTML and CSS

**Files:**
- Modify: `index.html` (add header element inside `<body>`)
- Modify: `styles/safnet.css` (append header styles)

- [ ] **Step 1: Add header HTML to `index.html`**

Inside `<body>`, add:

```html
    <header class="site-header">
        <div class="header-inner">
            <a href="/" class="header-brand">
                <img src="https://blog.safnet.com/img/BHCU-logo-safnet-small-darktheme.webp"
                     alt="Stephen A. Fuqua"
                     class="header-logo">
                <span class="header-name">Stephen A. Fuqua</span>
            </a>
            <nav class="header-nav" aria-label="Primary">
                <a href="https://blog.safnet.com">Blog</a>
                <a href="https://blog.safnet.com/about">About</a>
            </nav>
            <div class="header-social">
                <a href="https://github.com/stephenfuqua" aria-label="GitHub">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
                    </svg>
                </a>
                <a href="https://linkedin.com/in/stephenfuqua" aria-label="LinkedIn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 23.998 23.227 23.998 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                    </svg>
                </a>
            </div>
        </div>
    </header>
```

- [ ] **Step 2: Append header CSS to `styles/safnet.css`**

```css
/* =====================
   Site Header
   ===================== */
.site-header {
    background-color: #1b1b1d;
    position: sticky;
    top: 0;
    z-index: 100;
}

.header-inner {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0.75rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
}

.header-brand {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    text-decoration: none;
    color: white;
    flex: 1;
}

.header-brand:hover {
    text-decoration: none;
    color: white;
}

.header-logo {
    width: 32px;
    height: 32px;
    border-radius: 50%;
}

.header-name {
    font-weight: 600;
    font-size: 1rem;
}

.header-nav {
    display: flex;
    gap: 1rem;
}

.header-nav a {
    color: #e0e0e0;
    text-decoration: none;
    font-size: 0.95rem;
}

.header-nav a:hover {
    color: white;
    text-decoration: none;
}

.header-social {
    display: flex;
    gap: 0.75rem;
    align-items: center;
}

.header-social a {
    color: #e0e0e0;
    display: flex;
    align-items: center;
}

.header-social a:hover {
    color: white;
}
```

- [ ] **Step 3: Verify in browser**

Open `index.html`. Expected: dark header bar across full width, circular logo image on the left, "Stephen A. Fuqua" text, "Blog" and "About" links in the middle, GitHub and LinkedIn icons on the right. Header stays fixed when scrolling.

- [ ] **Step 4: Commit**

```bash
git add index.html styles/safnet.css
git commit -m "feat: add site header matching blog.safnet.com style"
```

---

## Task 3: Add hero banner HTML and CSS

**Files:**
- Modify: `index.html` (add hero section after `</header>`)
- Modify: `styles/safnet.css` (append hero styles)

- [ ] **Step 1: Add hero HTML to `index.html`** (after the closing `</header>` tag)

```html
    <section class="hero" aria-label="Introduction">
        <div class="hero-text">
            <h1>Stephen A. Fuqua (saf)</h1>
            <p>a Bah&aacute;'&iacute;, software engineer, and nature lover in Austin, Texas, USA</p>
        </div>
    </section>
```

- [ ] **Step 2: Append hero CSS to `styles/safnet.css`**

```css
/* =====================
   Hero Banner
   ===================== */
.hero {
    background: url('/images/mexicanHat.png') center / cover no-repeat;
    height: 250px;
    position: relative;
}

.hero-text {
    position: absolute;
    bottom: 1rem;
    left: 1rem;
    color: white;
    text-shadow: 0.15rem 0.15rem 0.4rem black;
    text-transform: lowercase;
}

.hero-text h1 {
    font-size: 2rem;
    margin: 0 0 0.25rem 0;
}

.hero-text p {
    margin: 0;
    font-size: 1.1rem;
}
```

- [ ] **Step 3: Verify in browser**

Open `index.html`. Expected: Mexican Hat flower photo fills the banner, white text "stephen a. fuqua (saf)" anchored to the bottom-left with a dark shadow for legibility, tagline beneath it.

- [ ] **Step 4: Commit**

```bash
git add index.html styles/safnet.css
git commit -m "feat: add hero banner with flower background image"
```

---

## Task 4: Add recent posts and projects sections HTML and CSS

**Files:**
- Modify: `index.html` (add `<main>` with two sections after `</section>` hero)
- Modify: `styles/safnet.css` (append section and list styles)

- [ ] **Step 1: Add main content HTML to `index.html`** (after the closing `</section>` of hero)

```html
    <main>
        <section class="content-section">
            <h2>Recent Blog Posts</h2>
            <div id="recent-posts">Loading&hellip;</div>
        </section>

        <section class="content-section">
            <h2>Other Projects</h2>
            <ul>
                <li><a href="https://www.greenbahai.com">Green Bah&aacute;'&iacute;</a></li>
                <li><a href="https://www.southcentralrti.org">South Central Regional Training Institute</a></li>
                <li><a href="/inn/">InterfaithNews.Net (archive)</a></li>
            </ul>
        </section>
    </main>
```

- [ ] **Step 2: Append section CSS to `styles/safnet.css`**

```css
/* =====================
   Content Sections
   ===================== */
.content-section {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem 1.5rem;
}

.content-section h2 {
    font-size: 1.25rem;
    font-weight: 600;
    text-transform: lowercase;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
    color: #333;
}

.content-section ul {
    padding-left: 1.25rem;
}
```

- [ ] **Step 3: Verify in browser**

Open `index.html`. Expected: two sections below the banner — "recent blog posts" with "Loading…" placeholder text, and "other projects" with three links. Both use lowercase headings with a thin underline.

- [ ] **Step 4: Commit**

```bash
git add index.html styles/safnet.css
git commit -m "feat: add recent posts and other projects sections"
```

---

## Task 5: Add footer HTML and CSS

**Files:**
- Modify: `index.html` (add footer after `</main>`)
- Modify: `styles/safnet.css` (append footer styles)

- [ ] **Step 1: Add footer HTML to `index.html`** (after `</main>`)

```html
    <footer class="site-footer">
        <div class="footer-inner">
            <p>The information on this site, unless otherwise attributed, is the sole opinion of its author and should not be construed as reflecting the views of any organization or employer unless explicitly stated.</p>
            <p>Copyright &copy; 2026 <a href="https://www.safnet.com">Stephen A. Fuqua</a>. Content and design are published under the Creative Commons <a href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International</a> License.</p>
        </div>
    </footer>
```

- [ ] **Step 2: Append footer CSS to `styles/safnet.css`**

```css
/* =====================
   Site Footer
   ===================== */
.site-footer {
    background-color: #1b1b1d;
    color: #e0e0e0;
    margin-top: 2rem;
}

.footer-inner {
    max-width: 800px;
    margin: 0 auto;
    padding: 1.5rem;
    font-size: 0.875rem;
}

.site-footer a {
    color: #90b8f8;
    text-decoration: none;
}

.site-footer a:hover {
    text-decoration: underline;
}

.site-footer p {
    margin-bottom: 0.75rem;
}

.site-footer p:last-child {
    margin-bottom: 0;
}
```

- [ ] **Step 3: Verify in browser**

Open `index.html`. Expected: dark footer matching the header color, light-gray body text, blue-tinted links, copyright and license text correct.

- [ ] **Step 4: Commit**

```bash
git add index.html styles/safnet.css
git commit -m "feat: add footer with CC BY-SA 4.0 license"
```

---

## Task 6: Add RSS feed fetch script

**Files:**
- Modify: `index.html` (add `<script>` before `</body>`)

- [ ] **Step 1: Add the RSS fetch script to `index.html`** (just before `</body>`)

```html
    <script>
    (async function loadRecentPosts() {
        const container = document.getElementById('recent-posts');
        try {
            const res = await fetch('https://blog.safnet.com/rss.xml');
            if (!res.ok) throw new Error('fetch failed');
            const text = await res.text();
            const xml = new DOMParser().parseFromString(text, 'text/xml');
            const items = Array.from(xml.querySelectorAll('item')).slice(0, 5);
            if (items.length === 0) throw new Error('no items');
            const ul = document.createElement('ul');
            items.forEach(item => {
                const title = item.querySelector('title').textContent;
                const link = item.querySelector('link').textContent;
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = link.trim();
                a.textContent = title;
                li.appendChild(a);
                ul.appendChild(li);
            });
            container.replaceWith(ul);
        } catch {
            container.innerHTML = 'Visit <a href="https://blog.safnet.com">blog.safnet.com</a> for recent posts.';
        }
    })();
    </script>
```

- [ ] **Step 2: Verify in browser (online)**

Open `index.html` via a local server (e.g. `npx serve .` or VS Code Live Server) so the fetch can run.

- If the RSS fetch succeeds: "recent blog posts" section shows 5 titled links pointing to blog.safnet.com posts.
- If blocked by CORS: section shows "Visit blog.safnet.com for recent posts." with a working link. Both are acceptable outcomes — CORS behavior depends on the host's headers.

Open browser devtools → Network tab. Confirm: a request to `https://blog.safnet.com/rss.xml` is attempted. No unhandled JS errors in the Console tab.

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: load 5 latest posts from RSS feed with fallback"
```

---

## Self-Review Checklist

- [x] Header matches spec: dark bar, logo, name, Blog/About nav, GitHub/LinkedIn SVG icons
- [x] Hero: mexicanHat.png background, 250px, bottom-left text with shadow
- [x] Recent posts: fetch rss.xml, 5 items, fallback on error
- [x] Other projects: 3 placeholder links (Green Bahá'í, SCRTI, INN archive)
- [x] Footer: dark bg, CC BY-SA 4.0 link, copyright 2026
- [x] No Bootstrap, jQuery, or Font Awesome imports
- [x] Google Analytics gtag kept (UA-550669-1)
- [x] All `id` and class names consistent across HTML and CSS tasks
- [x] `#recent-posts` div referenced in Task 4 is targeted by script in Task 6 — consistent
