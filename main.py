#!/usr/bin/python3
import time
import psycopg2

Db = psycopg2.connect(
    database = "hospital_management",
    user = "postgres",
    password = "new_password",
    host = "127.0.0.1",
    port = "5432"
)
