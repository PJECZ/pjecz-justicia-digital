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
        title="Justicia Digital",
        message="Bienvenido a la nueva generación de sistemas de información del PJECZ.",
        video="https://www.youtube.com/embed/K0uxjdcZWyk",
    )


@app.route("/privacy_policy")
def privacy_policy():
    """Privacy Policy page"""
    return render_template(
        "layouts/app.jinja2",
        title="Política de Privacidad",
        content_json=url_for("static", filename="json/privacy_policy.json"),
    )


@app.route("/service_terms")
def service_terms():
    """Service terms page"""
    return render_template(
        "layouts/app.jinja2",
        title="Condiciones del Servicio",
        content_json=url_for("static", filename="json/service_terms.json"),
    )


@app.route("/contact")
def contact():
    """Contact page"""
    return render_template(
        "layouts/app.jinja2",
        title="Contacto",
        content="""
            <p class="lead">
                <a href="mailto:informatica@pjecz.gob.mx">informatica@pjecz.gob.mx</a>
            </p>
            <p class="lead">
                Blvd. Francisco Coss #945. Zona Centro. Saltillo, Coahuila de Zaragoza, México.<br>
                Teléfono 844 194 5100
            </p>
        """,
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
            title="ERROR 404",
            description="PÁGINA NO ENCONTRADA",
        ),
        404,
    )
