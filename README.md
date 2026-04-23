# Relational Couples Therapy Website
### Dr. Patrick Whalen, Ph.D. — relationalcouplestherapy.com

A full-stack Flask web application.

---

## Project Structure

```
rct-site/
├── app.py                  # Flask server — all URL routes
├── requirements.txt        # Python dependencies
├── Procfile                # For Render/Railway/Heroku
├── render.yaml             # One-click Render deployment
├── data/
│   └── content.py          # ALL site copy lives here — edit to update text
├── public/
│   ├── css/main.css        # Complete stylesheet
│   ├── js/main.js          # Client JavaScript
│   └── images/
│       ├── patrick-whalen.jpg
│       └── patrick-terry-real.jpg
└── templates/
    ├── base.html           # Shared nav + footer layout
    ├── 404.html
    └── pages/
        ├── home.html
        ├── couples.html
        ├── approach.html
        ├── about.html
        ├── affair.html
        ├── premarital.html
        ├── intensives.html
        ├── fees.html
        ├── contact.html
        ├── blog.html
        └── post.html
```

---

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000 in your browser.

---

## Deploy to Render (Free Tier — Recommended)

1. Create a free account at **render.com**
2. Click **New → Web Service**
3. Connect your GitHub account and push this folder as a repo, OR upload as a zip
4. Render auto-detects the `render.yaml` and configures everything
5. Your site is live at a `*.onrender.com` URL

**Connect your GoDaddy domain:**
1. In Render dashboard → your service → Settings → Custom Domains
2. Add `relationalcouplestherapy.com` and `www.relationalcouplestherapy.com`
3. Render gives you a CNAME record value
4. In GoDaddy: DNS → Add Record → CNAME → `www` → paste Render's value
5. For the apex domain (`relationalcouplestherapy.com`): GoDaddy DNS → A Record → point to Render's IP
6. SSL certificate is issued automatically — no charge

---

## Updating Content

All text, fees, blog posts, and page copy are in **`data/content.py`**.

- To change a fee: find the `fees` list in `PAGES["fees"]` and edit the price
- To add a blog post: add a new dict to the `BLOG_POSTS` list at the bottom
- To update your address or phone: edit the `SITE` dict at the top
- To change any page headline or body copy: find it in `PAGES`

No template editing required for content updates.

---

## Adding New Blog Posts

In `data/content.py`, add to `BLOG_POSTS`:

```python
{
    "slug": "your-url-slug",           # becomes /writing/your-url-slug
    "title": "Post Title",
    "category": "Category Name",
    "date": "Month Year",
    "read_time": "X min read",
    "excerpt": "One paragraph summary shown on blog listing page.",
    "featured": False,                 # Set True for the large featured card
    "icon": "◎",                       # Decorative character for card thumbnail
    "body": """
<p>Your post content here. HTML is supported.</p>
<h2>Section heading</h2>
<p>More content.</p>
<blockquote>A pull quote.</blockquote>
"""
},
```

---

## Pages & URLs

| URL | Template |
|-----|----------|
| `/` | pages/home.html |
| `/couples-therapy` | pages/couples.html |
| `/the-approach` | pages/approach.html |
| `/about` | pages/about.html |
| `/affair-recovery` | pages/affair.html |
| `/premarital-counseling` | pages/premarital.html |
| `/intensives` | pages/intensives.html |
| `/investment` | pages/fees.html |
| `/writing` | pages/blog.html |
| `/writing/<slug>` | pages/post.html |
| `/contact` | pages/contact.html |
