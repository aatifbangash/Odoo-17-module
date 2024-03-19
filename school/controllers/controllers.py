from odoo import http


class School(http.Controller):
    @http.route('/school', auth='public')
    def index(self, **kw):
        return "hello world"

    @http.route('/school/objects', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('school.listing', {
            'root': '/school',
            'objects': http.request.env['school.school'].search([]),
        })

    @http.route('/school/objects/<model("school.school"):obj>', auth='public', website=True)
    def object(self, obj, **kw):
        return http.request.render('school.single', {
            'object': obj
        })

