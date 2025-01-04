from flask import Blueprint, request
from flask_restx import Resource, fields, Namespace
from app.models import db, Package

# Namespace para pacotes
api_namespace = Namespace("packages", description="Operações de gerenciamento de pacotes")

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
    @api_namespace.marshal_with(package_model, code=201)
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
        return package, 201

@api_namespace.route("/<int:package_id>")
class PackageResource(Resource):
    @api_namespace.doc("Obter detalhes de um pacote")
    @api_namespace.marshal_with(package_model)
    def get(self, package_id):
        """Obtem detalhes de um pacote pelo ID"""
        package = Package.query.get(package_id)
        if not package:
            api_namespace.abort(404, "Pacote não encontrado")
        return package

    @api_namespace.doc("Atualizar um pacote")
    @api_namespace.expect(package_model)
    @api_namespace.marshal_with(package_model)
    def put(self, package_id):
        """Atualiza completamente um pacote pelo ID"""
        package = Package.query.get(package_id)
        if not package:
            api_namespace.abort(404, "Pacote não encontrado")

        data = request.json
        package.origin = data["origin"]
        package.destination = data["destination"]
        package.status = data["status"]
        db.session.commit()
        return package

    @api_namespace.doc("Excluir um pacote")
    def delete(self, package_id):
        """Exclui um pacote pelo ID"""
        package = Package.query.get(package_id)
        if not package:
            api_namespace.abort(404, "Pacote não encontrado")
        
        db.session.delete(package)
        db.session.commit()
        return {"message": "Pacote excluído com sucesso"}, 200
