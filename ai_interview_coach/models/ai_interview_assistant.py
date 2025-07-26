from odoo import models, fields, api
from datetime import datetime
import google.generativeai as genai

class AIInterview(models.Model):
    _name = 'ai.interview'
    _description = 'AI Interview Coach'

    user_id = fields.Many2one('res.users', string='Candidate', required=True)
    job_description = fields.Text(string='Job Description', required=True)
    interview_question = fields.Text(string='Interview Questions')
    user_response = fields.Text(string='User Response')
    ai_feedback = fields.Text(string='AI Feedback')
    date_generated = fields.Datetime(string='Date Generated', default=fields.Datetime.now)
    interview_start_time = fields.Datetime(string='Interview Start Time', default=fields.Datetime.now)
    time_limit = fields.Integer(string="Time Limit (Minutes)", default=60)
    status = fields.Selection([
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('expired', 'Expired'),
    ], default='not_started', string="Interview Status")

    def start_interview(self):
        self.write({
            'status': 'in_progress',
            'interview_start_time': fields.Datetime.now(),
        })

    def check_time_limit(self):
        if self.status == 'in_progress':
            time_limit = self.time_limit * 60  # Convert to seconds
            elapsed_time = (fields.Datetime.now() - self.interview_start_time).total_seconds()
            if elapsed_time > time_limit:
                self.write({'status': 'expired'})

    def generate_interview_questions(self):
        """Generates interview questions using Gemini API"""
        genai.configure(api_key="key")

        prompt = f"Generate 5 interview questions for the following job description:\n\n{self.job_description}"
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        self.interview_questions = response.text

    def analyze_response(self):
        """Analyzes the interview response using Gemini API"""
        genai.configure(api_key="key")

        prompt = f"Analyze this response for the following job interview question. Provide feedback on clarity, correctness, and professionalism.\n\nQuestion: {self.interview_questions}\nResponse: {self.user_response}"
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        self.ai_feedback = response.text
