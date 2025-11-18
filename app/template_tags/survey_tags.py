# questionnaire/templatetags/survey_tags.py
from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def likert_row(bound_field):
    question = bound_field.label or bound_field.name.replace('_', ' ').title()
    html = f'<tr><td>{question}</td>'
    for radio in bound_field:
        html += f'''
          <td class="text-center">
            {radio.tag()}
            <label class="form-check-label small">{radio.choice_label}</label>
          </td>
        '''
    html += '</tr>'
    return mark_safe(html)