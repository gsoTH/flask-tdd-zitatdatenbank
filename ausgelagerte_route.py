from flask import request

def init_app(app):
    @app.route("/")
    def hello_world():
        return "<h1>Hello, World!</h1>"

    @app.errorhandler(404)
    def page_not_found(e):
        return "Seite existiert nicht.", 404

    @app.route('/eintragen', methods=['GET'])
    def eintragen_get_nicht_erlaubt():
        if not request.is_json:
            return "Method Not Allowed", 405

    @app.route('/eintragen', methods=['POST'])
    def eintragen():
        if not request.is_json:
            return "Request was not JSON", 400


# Hier steckt noch der Wurm drin...
        # zitat = request.json.get('zitat')
        # quelle = request.json.get('quelle')

        # if not zitat:
        #     return "JSON must contain zitat", 400
        # if not quelle:
        #     return "JSON must contain quelle", 400

        # return "Zitat eingetragen.", 200
