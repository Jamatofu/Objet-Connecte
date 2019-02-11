# Commandes disponibles


# Exemple de construction de page

header:
    title : Mon titre

body:
    container:
        form:
            buttonText : Envoyer vos infos
            destination : http://www.google.fr
            requestKind : POST
            items :
                - type : text
                  description : Nom
                  value : Clement
                - type : number
                  description : Age
                  value : 22
    container:
        chart:
            name : dataChart
            yAxe :
                - min : 20
                  max : 40
