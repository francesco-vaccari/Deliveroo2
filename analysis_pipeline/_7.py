def _7(data):
    return

# Senza guardare alla tipologia di esperimento, fare medie di metriche delle seguenti categorie:

# Desire:
# - satisfied con trigger function e executable alla fine dell'esperimento (executable at desire end)
# - satisfied con trigger function ma non executable alla fine dell'esperimento (numero trigger)
# - satisfied senza trigger function
# - non satisfied

# Intention:
# - generazione corretta e executable alla fine dell'esperimento
# - generazione corretta ma non executable alla fine dell'esperimento, invalidata durante desire trigger
# - generazione corretta ma non executable alla fine dell'esperimento, invalidata per via di dependency
# - generazione non corretta per via di errore di esecuzione
# - generazione non corretta per via di valutazione negativa

# e vedere se le categorie funzionanti contengono codice con metriche migliori
# Anche qua posso fare con ttest e vedere se le differenze sono significative