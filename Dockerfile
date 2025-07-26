FROM odoo:17

USER root

# Copy configuration and custom addons
COPY odoo.conf /etc/odoo/
COPY ./ai_interview_coach /mnt/extra-addons/ai_interview_coach

ARG ODOO_ENV=production
ENV ODOO_ENV=${ODOO_ENV}

USER odoo

EXPOSE 8069

CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]