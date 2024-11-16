from django import forms

class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)

    def clean_search_query(self):
        query = self.cleaned_data['search_query']
        # Example of sanitizing input or applying custom validation
        if 'DROP' in query.upper():  # Just a simple example
            raise forms.ValidationError("Invalid query.")
        return query
