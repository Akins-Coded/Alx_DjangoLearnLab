from django import forms

class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)

    def clean_search_query(self):
        query = self.cleaned_data['search_query']
        # Example of sanitizing input or applying custom validation
        if 'DROP' in query.upper():  # Just a simple example
            raise forms.ValidationError("Invalid query.")
        return query

class ExampleForm(forms.Form):
    # Genre field (e.g., Fiction, Mystery, etc.)
    genre = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter book genre'}),
        error_messages={
            'required': 'Genre is required.',
            'max_length': 'Genre cannot be more than 50 characters.'
        }
    )

    # Rating field (An integer rating between 1 and 5)
    rating = forms.IntegerField(
        required=True,
        min_value=1, 
        max_value=5, 
        error_messages={
            'required': 'Please provide a rating.',
            'min_value': 'Rating must be between 1 and 5.',
            'max_value': 'Rating must be between 1 and 5.'
        }
    )

    # Name of the book
    name = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter book name'}),
        error_messages={
            'required': 'Book name is required.',
            'max_length': 'Book name cannot be longer than 100 characters.'
        }
    )

    # Author's name
    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter author\'s name'}),
        error_messages={
            'required': 'Author name is required.',
            'max_length': 'Author name cannot be longer than 100 characters.'
        }
    )

    # Optional: You can add additional validation or custom error messages
    def clean_genre(self):
        genre = self.cleaned_data.get('genre')
        # Example of custom validation for genre
        if not genre.isalpha():
            raise forms.ValidationError("Genre must contain only letters.")
        return genre

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Please provide a valid rating between 1 and 5.")
        return rating
