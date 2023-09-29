import azure.functions as func

import logging

import json

from pymongo import MongoClient




# Chaîne de connexion MongoDB

mongodb_connection_string = "mongodb://bddpython:ni9dqIme5PA2MDMWL1iOonzM4XLaLyExFolpIRRFl9xpbm0qMfx2M1JpWPNrsy4WgmpT0FloVHAFACDbYPfJOw==@bddpython.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@bddpython@"




# Créer un client MongoDB en utilisant la chaîne de connexion

client = MongoClient(mongodb_connection_string)




# Sélectionnez la base de données et la collection MongoDB

database_name = 'SampleDB'

collection_name = 'SampleCollectionFay'




def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')




    try:

        # Récupérer les données JSON de la requête HTTP

        req_body = req.get_json()

       

        # Vérifier si le corps de la requête contient des données JSON valides

        if not req_body:

            return func.HttpResponse("Les données JSON sont manquantes dans la requête.", status_code=400)




        # Accédez à la base de données et à la collection

        db = client[database_name]

        collection = db[collection_name]




        # Insérez les données JSON dans la collection

        result = collection.insert_one(req_body)




        # Renvoyez la réponse avec l'ID de l'élément créé

        response_data = {

            "message": "Élément créé avec succès.",

            "inserted_id": str(result.inserted_id)

        }




        return func.HttpResponse(json.dumps(response_data), mimetype="application/json", status_code=201)  # 201 Created

    except ValueError:

        return func.HttpResponse("Données JSON non valides.", status_code=400)

    except Exception as e:

        return func.HttpResponse(f"Erreur de création : {str(e)}", status_code=500)