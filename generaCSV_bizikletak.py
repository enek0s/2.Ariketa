import pandas as pd

SARRERA_BIZIKLETA = "datu_iturriak/bizikletak.csv"
SARRERA_ERABILERAK = "datu_iturriak/erabilerak.csv"

MOTA = "Elektrikoa"

def main():
      
   # Extract 
   df_bizikleta = pd.read_csv(SARRERA_BIZIKLETA)
   df_erabilera = pd.read_csv(SARRERA_ERABILERAK)

   df_bizikleta_mota = df_bizikleta[df_bizikleta["Mota"] == MOTA]

   print(df_bizikleta_mota.to_string())

if __name__ == "__main__":
   main()