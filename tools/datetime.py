import datetime as dt

# Toolbox pour la gestion de date

def convert(a):
    """Lecture de date"""
    return dt.datetime.strptime(a,'%Y-%m-%d %H:%M')