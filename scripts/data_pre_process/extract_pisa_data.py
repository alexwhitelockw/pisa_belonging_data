# Read PISA data and clean

import pandas as pd
import sqlite3

def read_pisa_data(country = "All"):
  
  conn = sqlite3.connect("data/pisa_raw_data/pisa_belonging_data.db")
  
  if country == "All":
    
    pisa_query = """
    SELECT *
    FROM belonging_student_responses
    """
  
    pisa_output = pd.read_sql(
      sql=pisa_query,
      con=conn
    )
  
  else:
    pisa_query = """
      SELECT *
      FROM belonging_student_responses
      WHERE country = :country
    """
  
    pisa_output = pd.read_sql(
      sql=pisa_query,
      con=conn,
      params={
        "country":country
      }
    )
  
  return pisa_output
  
