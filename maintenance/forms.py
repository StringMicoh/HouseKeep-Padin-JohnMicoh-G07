from django import forms
from .models import MaintenanceTask


class MaintenanceTaskForm(forms.ModelForm):
    class Meta:
        model = MaintenanceTask
        fields = ['task_name', 'description', 'category', 'due_date']
        widgets = {
            'task_name': forms.TextInput(attrs={
                'placeholder': 'Enter task name'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter task details',
                'rows': 3
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'e.g. Cleaning, Repair, Inspection'
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }

    def clean_task_name(self):
        task_name = self.cleaned_data['task_name'].strip()

        if not task_name:
            raise forms.ValidationError('Task name is required.')

        return task_name

    def clean_category(self):
        category = self.cleaned_data['category'].strip()

        if not category:
            raise forms.ValidationError('Category is required.')

        return category
