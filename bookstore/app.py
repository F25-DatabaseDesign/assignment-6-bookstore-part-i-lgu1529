from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)
categories = [
    [1, "Astrophotography"],
    [2, "Astronomy"],
    [3, "Meteorology"],
    [5, "Telescopes"]
]

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

books = [
    # Astrophotography
    [1, 1, "The Astrophotography Manual", "Chris Woodhouse", "13-9781138055063", 45.99, "astrophoto_manual.jpg", 1],
    [2, 1, "Deep-Sky Imaging Primer", "Charles Bracken", "13-9781107135345", 52.99, "deep_sky.jpg", 1],
    [3, 1, "Capturing the Stars: Astrophotography by the Masters", "Robert Gendler", "13-9780943396835", 34.99, "capturing_stars.jpg", 0],
    [4, 1, "The 100 Best Astrophotography Targets: A Monthly Guide for CCD Imaging with Amateur Telescopes", "Ruben Kier", "13-9783319275123", 39.99, "best_targets.jpg", 1],

    # Astronomy
    [5, 2, "Cosmos", "Carl Sagan", "13-9780345539434", 19.99, "cosmos.jpg", 1],
    [6, 2, "Nightwatch: A Practical Guide to Viewing the Universe", "Terence Dickinson", "13-9781554073580", 29.95, "nightwatch.jpg", 1],
    [7, 2, "Turn Left at Orion", "Guy Consolmagno", "13-9781108457569", 24.99, "turn_left_orion.jpg", 1],
    [8, 2, "The Backyard Astronomer's Guide", "Terence Dickinson", "13-9781554073849", 49.99, "backyard_guide.jpg", 0],

    # Meteorology
    [9, 3, "Midlatitude Synoptic Meteorology - Dynamics, Analysis, and Forecasting", "Gary Lackmann", "13-9781878220103", 85.99, "synoptic_meteorology.jpg", 1],
    [10, 3, "Meteorology Today", "C. Donald Ahrens", "13-9781305965799", 89.99, "meteorology_today.jpg", 0],
    [11, 3, "The Cloud Collector's Handbook", "Gavin Pretor-Pinney", "13-9780811875417", 16.99, "cloud_collector.jpg", 1],
    [12, 3, "Tropical Meteorology: An Introduction", "T.N. Krishnamurti", "13-9781461474081", 94.99, "tropical_meteorology.jpg", 0],

    # Physics
    [12, 4, "A Brief History of Time", "Stephen Hawking", "13-9780553380163", 18.99, "brief_history.jpg", 1],
    [13, 4, "The Elegant Universe", "Brian Greene", "13-9780393338102", 17.99, "elegant_universe.jpg", 0],
    [14, 4, "Six Easy Pieces", "Richard Feynman", "13-9780465025275", 14.99, "six_easy_pieces.jpg", 1],

    # Telescopes & Equipment
    [15, 5, "Choosing and Using a Dobsonian Telescope", "Neil English", "13-9781546580591", 32.99, "choosing_telescope.jpg", 0],
    [16, 5, "Star Ware: The Amateur Astronomer's Guide to Choosing, Buying, and Using Telescopes and Accessories", "Philip Harrington", "13-9781118638484", 44.99, "star_ware.jpg", 1],
    [17, 5, "Telescope Optics: A Comprehensive Manual for Amateur Astronomers", "Harrie G.J. Rutten", "13-9780943396187", 79.95, "telescope_optics.jpg", 1],
    [18, 5, "Amateur Astronomer's Handbook", "J.B. Sidgwick", "13-9780486240343", 24.99, "amateur_handbook.jpg", 0],
]



# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    #return render_template()
    return render_template("index.html", categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    category_id = request.args.get("categoryId", type=int)

    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = [b for b in books if b[1] == category_id]

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    #return render_template()
    return render_template(
        "category.html",
        selectedCategory=category_id,
        categories=categories,
        books=selected_books
    )

# we'll link this for project 2 to an sqlite3 database using flask's get_db() function
@app.route('/search')
def search():
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
