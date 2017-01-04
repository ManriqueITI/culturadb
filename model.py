import web, datetime

db = web.database(dbn='mysql', host='tkck4yllxdrw0bhi.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', db='nqvs0ewn2go6ekkv', user='y9qwgd19ybp13olf', pw='s6504wxwwpxxoduf')

def get_posts():
    return db.select('carrerasuniversitarias',order='id DESC')

def get_post(id):
    try:
        return db.select('carrerasuniversitarias', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(carreraP, universidadP, duracionP, modalidadP, telefonoP, direccionP):
    db.insert('carrerasuniversitarias', carrera = carreraP, universidad = universidadP, duracion = duracionP,
    modalidad = modalidadP, telefono = telefonoP, direccion = direccionP)

def del_post(id):
    db.delete('carrerasuniversitarias', where="id=$id", vars=locals())

def update_post(id, carreraP, universidadP, duracionP, modalidadP, telefonoP, direccionP):
    db.update('carrerasuniversitarias', where="id=$id", vars=locals(),
    carrera = carreraP, universidad = universidadP, duracion = duracionP,
    modalidad = modalidadP, telefono = telefonoP, direccion = direccionP)
