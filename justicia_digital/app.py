"""
Flask App
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def start():
    """Start page"""
    return render_template('layouts/start.jinja2', title="justiciadigital.gob.mx",)


@app.app_errorhandler(404)
def page_not_found(error):
    """Page not found"""
    return render_template('layouts/error.jinja2', title="404", description="PÁGINA NO ENCONTRADA",), 404
