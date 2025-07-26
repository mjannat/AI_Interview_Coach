from odoo import http
from odoo.http import request
from datetime import datetime

class CandidateLoginController(http.Controller):
    @http.route('/candidate/login', type='http', auth="public", website=True)
    def candidate_login(self, **kw):
        return request.render('ai_interview_coach.login_page', {})

    @http.route('/candidate/login/submit', type='http', auth="public", website=True)
    def candidate_login_submit(self, email, password, **kw):
        user = request.env['res.users'].sudo().search([('login', '=', email), ('password', '=', password)])
        if user:
            # Mark the user as a candidate
            user.is_candidate = True
            return request.redirect('/candidate/dashboard')
        else:
            return request.render('ai_interview_coach.login_page', {'error': 'Invalid credentials'})

class CandidateDashboardController(http.Controller):
    @http.route('/candidate/dashboard', type='http', auth="user", website=True)
    def candidate_dashboard(self, **kw):
        interview = request.env['ai.interview'].sudo().search([('user_id', '=', request.uid)], limit=1)
        if interview.status == 'not_started':
            interview.start_interview()
        # Calculate time left
        time_left = max(0, 60 - ((datetime.now() - interview.interview_start_time).total_seconds() // 60))
        return request.render('ai_interview_coach.candidate_dashboard', {'interview': interview, 'time_left': time_left})

    @http.route('/candidate/submit_answer', type='http', auth="user", website=True)
    def submit_answer(self, user_response, **kw):
        interview = request.env['ai.interview'].sudo().search([('user_id', '=', request.uid)], limit=1)
        interview.write({'user_response': user_response})

        # Analyze the response (via AI API)
        feedback = interview.analyze_user_response(user_response)
        interview.write({'ai_feedback': feedback, 'status': 'completed'})

        return request.render('ai_interview_coach.candidate_dashboard', {'interview': interview})
