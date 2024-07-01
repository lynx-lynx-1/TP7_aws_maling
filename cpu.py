import psutil
import smtplib
from email.message import EmailMessage

def afficher_informations_systeme():
    response = ""
    # Informations sur la mémoire
    memoire = psutil.virtual_memory()
    response += f"Memoire totale : {memoire.total / (1024 ** 3):.2f} Go\n"
    response += f"Memoire utilisee : {memoire.used / (1024 ** 3):.2f} Go\n"
    response += f"Memoire libre : {memoire.available / (1024 ** 3):.2f} Go\n\n"

    # Pourcentage du CPU
    pourcentage_cpu = psutil.cpu_percent()
    response += f"Pourcentage du CPU : {pourcentage_cpu}%\n\n"

    # Informations sur le stockage
    stockage = psutil.disk_usage('/')
    response += f"Espace de stockage total : {stockage.total / (1024 ** 3):.2f} Go\n"
    response += f"Espace de stockage utilise : {stockage.used / (1024 ** 3):.2f} Go\n"
    response += f"Espace de stockage libre : {stockage.free / (1024 ** 3):.2f} Go"
    
    return response 

def envoyer_email(destinataire, sujet, contenu):
    # Paramètres du serveur SMTP
    serveur_smtp = 'node218-eu.n0c.com'
    port_smtp = 587
    utilisateur_smtp = 'votre mail proffesionnel'
    mot_de_passe_smtp = 'mot de passe'

    # Création de l'objet EmailMessage
    message = EmailMessage()
    message['From'] = utilisateur_smtp
    message['To'] = destinataire
    message['Subject'] = sujet
    message.set_content(contenu)

    # Connexion au serveur SMTP
    try:
        with smtplib.SMTP(serveur_smtp, port_smtp) as smtp_obj:
            smtp_obj.starttls()
            smtp_obj.login(utilisateur_smtp, mot_de_passe_smtp)
            smtp_obj.send_message(message)
        print("E-mail envoyé avec succès!")
    except Exception as e:
        print("Erreur lors de l'envoi de l'e-mail:", str(e))

# Exemple d'utilisation
destinataire = 'mail du destinataire'
sujet = 'Rapport sur la performence du serveur'
contenu = afficher_informations_systeme()
envoyer_email(destinataire, sujet, contenu)

print(contenu)
