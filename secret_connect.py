import psycopg2

def secret_connection():
    return psycopg2.connect(database="Open_Policing", user="rdecal", host='/var/run/postgresql/')
