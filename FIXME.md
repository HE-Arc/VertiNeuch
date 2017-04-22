# Le fix me

## Installation

- pas sûr que gunicorn et gevent soient nécessaires.
- le readme n'est pas à jour, syncdb vs migrate
- migrate ne fonctionne pas.
- npm install et ??
- vous avez conservez tout depuis cookie-cutter, du coup il y a pas mal de superflu.

## Python

- l'image par défaut ne devrait pas être dans media, mais static
- py.test casse ;-)
- un seul modèle! (Deux si on compte users)
- les templates liées à chaque application (users, lessons) pourrait vivre au sein de l'application.
- la regex du numéro de téléphone ne correspond pas à l'erreur
- `is_teacher` aurait pu être fait avec un role, oui.
- user est traductible, lessons ne l'est pas, dommage.
- les enums aurait pu être d'autres modèles, recherche, tri, etc.
- des contraintes d'intégrités non capturées (teacher_id) dans l'admin!

## UX

- `role=button` n'est pas si simple: <https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques/Using_the_button_role>
- Le Logo + Accueil servent le même rôle.
- en mode mobile, le menu hamburger est à peine visible
- `<style>` dans l'HTML se fait en HTML5 mais on risque le FOUC.
- une image de 960x590 pixel va être bien laide sur un écran plus grand ;-)
- la page d'accueil n'invite à rien??
