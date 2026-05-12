"""
Relational Couples Therapy — Dr. Patrick Whalen, Ph.D.
Full-stack Flask application
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
from flask import Flask, abort, jsonify, render_template, request

from data.content import BLOG_POSTS, PAGES, SITE

load_dotenv()

app = Flask(__name__, static_folder="public", static_url_path="")

MAIL_FROM    = os.environ.get("MAIL_FROM", "whalenpatrick@gmail.com")
MAIL_TO      = os.environ.get("MAIL_TO",   "whalenpatrick@gmail.com")
MAIL_USER    = os.environ.get("MAIL_USER",  MAIL_FROM)
MAIL_PASS    = os.environ.get("MAIL_PASS",  "")


def _send_contact_email(fields: dict) -> None:
    body = "\n".join(f"{k}: {v}" for k, v in fields.items() if v)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"New consultation request — {fields.get('name', 'unknown')}"
    msg["From"]    = MAIL_FROM
    msg["To"]      = MAIL_TO
    msg["Reply-To"] = fields.get("email", MAIL_FROM)
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(MAIL_USER, MAIL_PASS)
        smtp.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())

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
    fields = {
        "Name":             request.form.get("name", ""),
        "Partner":          request.form.get("partner_name", ""),
        "Email":            request.form.get("email", ""),
        "Phone":            request.form.get("phone", ""),
        "Reason":           request.form.get("reason", ""),
        "Message":          request.form.get("message", ""),
        "Contact pref":     request.form.get("contact_pref", ""),
    }
    try:
        _send_contact_email(fields)
    except Exception as exc:
        app.logger.error("Contact email failed: %s", exc)
        return jsonify(ok=False, error=str(exc)), 500
    return jsonify(ok=True)

# ── 404 ─────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", site=SITE), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
