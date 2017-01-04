import web
import model
import json
from data import data
from web import form


urls = (
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
    '/viewdata', 'Viewdata',
    '/mapa(:*)', 'mapa',
    '/(.*)', 'IndexD',
)


t_globals = {
    'datestr': web.datestr
}

render = web.template.render('templates', base='base', globals=t_globals)

data = data()  
data.read() 

myform = form.Form(  
            form.Dropdown('Estado', data.getEstado(), 
            form.notnull, description="ESTADO: "),
            form.Dropdown('Fecha', data.getFecha(),
            form.notnull, description="FECHA DE CONVENIO ORIGINAL: ") 
    ) 

class IndexD:  
    def GET(self, results):      
        form = myform
        return render.indexD(form, None) 

    def POST(self, results):  
        form = myform  
        if not form.validates(): 
            return render.indexD(form)
        else:
            user_data = web.input()   
            estado = user_data.Estado
            fecha = user_data.Fecha
            results = data.getAnio(estado, fecha) 
            return render.indexD(form, results) 

class View:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post)

class Viewdata:
    def GET(self):
        posts = model.get_posts()
        return render.viewdata(posts)

class New:
    def GET(self):
        return render.new()

    def POST(self):
        i = web.input()
        model.new_post(i.carreraP, i.universidadP, i.duracionP, i.modalidadP, i.telefonoP, i.direccionP)
        raise web.seeother('/viewdata')

class Delete:
    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/viewdata')

class Edit:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.edit(post)

    def POST(self, id):
        i = web.input()
        model.update_post(int(id),i.carreraP, i.universidadP, i.duracionP, i.modalidadP, i.telefonoP, i.direccionP)
        raise web.seeother('/viewdata')
        
class Login:
    def GET(self):
        return render.login()

    def POST(self):
        i = web.input()
        post = model.get_users()
        if len(i) == 0:
            return render.login()
        else:
            for row in post:
                if row.nombre == i.user and row.contrasena == i.pw:
                    raise web.seeother('/viewdata')
                else:
                    raise web.seeother('/login')

class mapa:        
    def GET(self, datos):
        datos=[]
        with open('data/data.json','r') as file:
            datos = json.load(file)
        return render.mapa(datos['results'])

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()