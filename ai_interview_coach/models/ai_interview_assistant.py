from odoo import models, fields, api
import google.generativeai as genai


class AIInterviewCoach(models.Model):
    _name = "ai.interview.coach"
    _description = "AI Interview Coach"

    name = fields.Char("Job Title", required=True)
    job_description = fields.Text("Job Description", required=True)
    interview_questions = fields.Text("Generated Questions")
    user_response = fields.Text("User Response")
    ai_feedback = fields.Text("AI Feedback")

    def generate_questions(self):
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
