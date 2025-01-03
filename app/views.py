from flask import request
from flask_restx import Api, Resource, fields

# Configurando o Swagger
api = Api(app, version="1.0", title="Smart Logistics Hub API", description="APIs para gerenciamento logístico")

# Modelo de Pacote para documentação
package_model = api.model("Package", {
    "id": fields.Integer(readonly=True, description="ID do pacote"),
    "origin": fields.String(required=True, description="Local de origem"),
    "destination": fields.String(required=True, description="Local de destino"),
    "status": fields.String(description="Status do pacote ('pending', 'shipped', 'delivered')"),
})

@api.route("/packages")
class PackageListResource(Resource):
    @api.doc("Listar pacotes com filtros")
    @api.param("status", "Filtrar por status do pacote")
    @api.param("destination", "Filtrar por destino do pacote")
    @api.marshal_list_with(package_model)
    def get(self):
        """Lista pacotes com filtros opcionais por status e destino"""
        status = request.args.get("status")
        destination = request.args.get("destination")
        
        query = Package.query
        if status:
            query = query.filter(Package.status == status)
        if destination:
            query = query.filter(Package.destination.ilike(f"%{destination}%"))
        
        return query.all()

@app.route("/packages", methods=["POST"])
def create_package():
    data = request.json
    package = Package(
        origin=data["origin"],
        destination=data["destination"]
    )
    db.session.add(package)
    db.session.commit()
    return {"message": "Pacote criado com sucesso!"}, 201

@app.route("/packages", methods=["GET"])
def list_packages():
    """Lista pacotes com suporte a filtros por status e destino."""
    status = request.args.get("status")
    destination = request.args.get("destination")
    
    # Construindo a consulta com filtros opcionais
    query = Package.query
    if status:
        query = query.filter(Package.status == status)
    if destination:
        query = query.filter(Package.destination.ilike(f"%{destination}%"))
    
    packages = query.all()
    return [
        {"id": p.id, "origin": p.origin, "destination": p.destination, "status": p.status}
        for p in packages
    ], 200

@app.route("/packages/<int:package_id>", methods=["PATCH"])
def update_package_status(package_id):
    data = request.json
    package = Package.query.get(package_id)
    if not package:
        return {"error": "Pacote não encontrado"}, 404

    package.status = data.get("status", package.status)
    db.session.commit()
    return {"message": "Status atualizado com sucesso!"}
