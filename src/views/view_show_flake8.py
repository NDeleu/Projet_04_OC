
class ShowPepHeight:

    def choice_flake8():
        return "\nVeuillez choisir le type d'affichage du pep8 désiré :\n" \
               "Afficher le pep8 sur console :      1\n" \
               "Créer un fichier exportable HTML :  2"

    choice_flake8 = staticmethod(choice_flake8)

    def result_check_flake_no_errors():
        return "\nAucune erreur n'a été relevée dans le code de ce " \
               "programme lors de la vérification du respect " \
               "de la charte PEP 8 par le module flake 8\n"

    result_check_flake_no_errors = staticmethod(result_check_flake_no_errors)

    def result_true_pep_html():
        return "Le fichier html pep 8 a été créé.\n" \
               "Vous pouvez le consulter directement " \
               "dans le dossier flake-report.\n" \
               "A cette fin, merci d'ouvrir le fichier index.html " \
               "dans un navigateur tels que Microsoft Edge, " \
               "Google Chrome ou encore Mozilla Firefox.\n" \
               "Pour d'avantage d'informations, " \
               "merci de vous reporter au README.\n"

    result_true_pep_html = staticmethod(result_true_pep_html)

    def result_false_pep_html():
        return "Une erreur est survenue lors de la création " \
               "du fichier html.\n" \
               "Veuillez réitérer l'opération.\n" \
               "Si le problème perssiste, merci de contacter le développeur\n"

    result_false_pep_html = staticmethod(result_false_pep_html)
