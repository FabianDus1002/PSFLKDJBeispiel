Installierte Pakete
linting: pylint
framework: django mit django-rest-framework

requirements:
'''pip install Django djangorestframework'''

Zum starten der api nach dem klonen:
cd seminar
python3 manage.py runserver

Die API kann über die Webapp Postman getestet werden.
Hierfür, muss der Postman Desktop Agent installiert sein.

Beispiel:
In Postman kann eine GET-Request auf http://127.0.0.1:8000/teilnehmer 
durchgeführt werden, um alle Teilnehmer zu erhalten.

Beschreibung:
Mit dieser simplen in Django geschriebenen API kann
auf die Beispiel-Ressource Teilnehmer zugegriffen werden.