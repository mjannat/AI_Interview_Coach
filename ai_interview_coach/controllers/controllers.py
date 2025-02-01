# -*- coding: utf-8 -*-
# from odoo import http


# class AiInterviewCoach(http.Controller):
#     @http.route('/ai_interview_coach/ai_interview_coach', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ai_interview_coach/ai_interview_coach/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ai_interview_coach.listing', {
#             'root': '/ai_interview_coach/ai_interview_coach',
#             'objects': http.request.env['ai_interview_coach.ai_interview_coach'].search([]),
#         })

#     @http.route('/ai_interview_coach/ai_interview_coach/objects/<model("ai_interview_coach.ai_interview_coach"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ai_interview_coach.object', {
#             'object': obj
#         })

