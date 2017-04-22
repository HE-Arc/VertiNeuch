VertiNeuch
==========

Vertineuch est une plateforme qui réunit des offres d'activités proposées par des guides de montagne et moniteurs d'escalade de la région neuchâteloise et jurassienne afin de répondre à la demande croissante pour l'escalade en salle et les activités se déroulant en pleine nature.

.. Installation

renommer le fichier env.exemple et .env et l'adapter avec ses paramètres.
pip install -r requierments/local.txt
npm install  # pourquoi faire au juste?
python manage.py syncdb  # ce truc n'existe plus depuis Django 1.9
python manage.py migrate
python manage.py runserver
