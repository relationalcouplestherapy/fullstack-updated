"""
Relational Couples Therapy — Dr. Patrick Whalen, Ph.D.
Full-stack Flask application
"""

from flask import Flask, render_template, abort
from data.content import PAGES, BLOG_POSTS, SITE

app = Flask(__name__, static_folder="public", static_url_path="")

# ── Main pages ──────────────────────────────────────────
@app.route("/")
def home():
    return render_template("pages/home.html", site=SITE, page=PAGES["home"])

@app.route("/couples-therapy")
def couples():
    return render_template("pages/couples.html", site=SITE, page=PAGES["couples"])

@app.route("/the-approach")
def approach():
    return render_template("pages/approach.html", site=SITE, page=PAGES["approach"])

@app.route("/about")
def about():
    return render_template("pages/about.html", site=SITE, page=PAGES["about"])

@app.route("/affair-recovery")
def affair():
    return render_template("pages/affair.html", site=SITE, page=PAGES["affair"])

@app.route("/premarital-counseling")
def premarital():
    return render_template("pages/premarital.html", site=SITE, page=PAGES["premarital"])

@app.route("/intensives")
def intensives():
    return render_template("pages/intensives.html", site=SITE, page=PAGES["intensives"])

@app.route("/relationship-coaching")
def coaching():
    return render_template("pages/coaching.html", site=SITE, page=PAGES["coaching"])

@app.route("/investment")
def fees():
    return render_template("pages/fees.html", site=SITE, page=PAGES["fees"])

@app.route("/contact")
def contact():
    return render_template("pages/contact.html", site=SITE, page=PAGES["contact"])

# ── Blog ────────────────────────────────────────────────
@app.route("/writing")
def blog():
    return render_template("pages/blog.html", site=SITE, page=PAGES["blog"], posts=BLOG_POSTS)

@app.route("/writing/<slug>")
def post(slug):
    post_data = next((p for p in BLOG_POSTS if p["slug"] == slug), None)
    if not post_data:
        abort(404)
    return render_template("pages/post.html", site=SITE, post=post_data)

# ── Contact form handler ─────────────────────────────────
@app.route("/contact", methods=["POST"])
def contact_submit():
    # In production: send email / store to DB
    return render_template("pages/contact.html", site=SITE,
                           page=PAGES["contact"], submitted=True)

# ── 404 ─────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", site=SITE), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
