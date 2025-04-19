import pandas as pd

# Sample data for service providers
data = {
    'id': ['', '', '', 1, 2],  # Empty for new entries
    'name': [
        'Rajesh Kumar',
        'Priya Patel',
        'Amit Shah',
        'Sneha Verma',
        'Vikram Singh'
    ],
    'profile_pic': [
        'https://servicebuddy.com/profiles/rajesh.jpg',
        'https://servicebuddy.com/profiles/priya.jpg',
        'https://servicebuddy.com/profiles/amit.jpg',
        'https://servicebuddy.com/profiles/sneha.jpg',
        'https://servicebuddy.com/profiles/vikram.jpg'
    ],
    'description': [
        'Expert plumber specializing in bathroom and kitchen repairs. Available 24/7 for emergencies.',
        'Professional electrician with expertise in home wiring and smart home installations.',
        'Skilled carpenter offering custom furniture making and wood repair services.',
        'Experienced painter providing interior and exterior painting services.',
        'Professional house cleaner with eco-friendly cleaning solutions.'
    ],
    'service': [
        'Plumber',
        'Electrician',
        'Carpenter',
        'Painter',
        'House Cleaner'
    ],
    'rating': [4.8, 4.9, 4.5, 4.7, 4.6],
    'availability': [1, 1, 1, 0, 1],  # 1 for True, 0 for False
    'experience': [8.5, 12.0, 6.5, 10.0, 7.5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel file
df.to_excel('sample_service_providers.xlsx', index=False)

print("""
Sample Excel file created successfully!

File Structure:
--------------
1. First 3 rows: New service providers (empty id)
2. Last 2 rows: Existing providers (with id) for updating

Notes:
------
- Leave id empty for new entries
- Service names must match exactly with your database
- Rating should be between 0.0 and 5.0
- Availability: 1 for True, 0 for False
- Experience is in years (decimal allowed)
""") 