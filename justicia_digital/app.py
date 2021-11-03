"""
Flask App
"""
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def start():
    """Start page"""
    return render_template(
        "layouts/start.jinja2",
        title="Bienvenido",
    )


@app.route("/privacy_policy")
def privacy_policy():
    """Privacy Policy page"""
    return render_template(
        "layouts/app.jinja2",
        title="Política de Privacidad",
        content_json=url_for("static", filename="json/privacy_policy.json"),
    )


@app.route("/video")
def video():
    """Video page"""
    return render_template(
        "layouts/app.jinja2",
        title="Video sobre Justicia Digital",
        content="Video en YouTube en el que expliques cómo usarás los datos del usuario de Google que obtienes de los permisos.",
    )


@app.route("/contact")
def contact():
    """Contact page"""
    return render_template(
        "layouts/app.jinja2",
        title="Contacto",
        content="Pendiente datos de contacto...",
    )


@app.route("/favicon.ico")
def favicon():
    """Favicon"""
    return redirect(url_for("static", filename="favicon.ico"))


@app.errorhandler(404)
def page_not_found(error):
    """Page not found"""
    return (
        render_template(
            "layouts/error.jinja2",
            title="404",
            description="PÁGINA NO ENCONTRADA",
        ),
        404,
    )
