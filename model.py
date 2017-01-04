import web, datetime

db = web.database(dbn='mysql', host='ehc1u4pmphj917qf.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', db='fifi37b224vf71j7', user='u9jha17rlju1in1g', pw='x5l7bs48xrqdc3uw')

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
