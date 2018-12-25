from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.imdb.com/chart/moviemeter'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

films = soup.find_all('td', class_ = 'titleColumn')
reviews = soup.find_all('td', class_ = 'imdbRating')

film_names = []
film_years = []
film_ratings = []

films = soup.find_all('tbody', class_ = 'lister-list')

for film in films:
	film_rows = film.findChildren('tr')
	for film_row in film_rows:
		titles = film_row.findChildren('td', class_ = 'titleColumn')
		ratings = film_row.findChildren('td', class_ = 'imdbRating')
		for rating in ratings:
			review = rating.getText().replace('\n', '')
			film_ratings.append(review)
			name = title.find('a').getText()
			year = title.find('span', class_ = 'secondaryInfo').getText().replace('(', '').replace(')', '')
			film_names.append(name)
			film_years.append(year)

film_ratings = [float(x) if x != '' else None for x in film_ratings]

film_years = [int(y) for y in film_years]

imdb_frame = pd.DataFrame(
    {'Title': film_names,
     'Year of Release': film_years,
     'Rating': film_ratings
    })

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('imdb_famous.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
imdb_frame.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

imdb_frame.sort_values(['Rating'], ascending=False, inplace=True)

print("Highest rated film: " + imdb_frame['Title'].iloc[0])
print("Rating: " + str(imdb_frame['Rating'].iloc[0]))
print("Year of Release: " + str(imdb_frame['Year of Release'].iloc[0]))

input("Press Enter to close the application")