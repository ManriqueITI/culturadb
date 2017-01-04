import json

class data:  
    data = []

    def read(self):
        with open('data/data.json','r') as file:
            data = json.load(file)
            self.data = data['results'] 

    def getEstado(self): 
        estados = []
        for row in self.data:
            estado = row['ESTADO']
            if estado not in estados:
                estados.append(estado)
        return estados

    def getFecha(self): 
        fechas = []
        for row in self.data:
            fecha = row['FECHADECONVENIOORIGINAL']
            if fecha not in fechas:
                fechas.append(fecha)
        return fechas      
        
    def getAnio(self, entidad, delito):
        inAnio = []  
        for row in self.data:
            inEntidad = row['ESTADO']
            inDelito = row['FECHADECONVENIOORIGINAL']
            if inEntidad == entidad and inDelito == delito:
                inAnio.append([row['ESTADO'], inDelito, row['DETONADO']])
        return inAnio      
                
