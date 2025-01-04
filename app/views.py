from flask import Blueprint, request
from flask_restx import Resource, fields, Namespace
from app.models import db, Package

# Criar um namespace para pacotes
api_namespace = Namespace("packages", description="Operações relacionadas a pacotes")

# Modelo de Pacote para documentação
package_model = api_namespace.model("Package", {
    "id": fields.Integer(readonly=True, description="ID do pacote"),
    "origin": fields.String(required=True, description="Local de origem"),
    "destination": fields.String(required=True, description="Local de destino"),
    "status": fields.String(description="Status do pacote ('pending', 'shipped', 'delivered')"),
})

@api_namespace.route("/")
class PackageListResource(Resource):
    @api_namespace.doc("Listar pacotes com filtros")
    @api_namespace.param("status", "Filtrar por status do pacote")
    @api_namespace.param("destination", "Filtrar por destino do pacote")
    @api_namespace.marshal_list_with(package_model)
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

    @api_namespace.doc("Criar um novo pacote")
    @api_namespace.expect(package_model)
    def post(self):
        """Cria um novo pacote"""
        data = request.json
        package = Package(
            origin=data["origin"],
            destination=data["destination"],
            status=data.get("status", "pending"),
        )
        db.session.add(package)
        db.session.commit()
        return {"message": "Pacote criado com sucesso!"}, 201

@api_namespace.route("/<int:package_id>")
class PackageResource(Resource):
    @api_namespace.doc("Atualizar o status de um pacote")
    @api_namespace.expect({"status": fields.String(description="Novo status do pacote")})
    def patch(self, package_id):
        """Atualiza o status de um pacote"""
        data = request.json
        package = Package.query.get(package_id)
        if not package:
            return {"error": "Pacote não encontrado"}, 404

        package.status = data.get("status", package.status)
        db.session.commit()
        return {"message": "Status atualizado com sucesso!"}
