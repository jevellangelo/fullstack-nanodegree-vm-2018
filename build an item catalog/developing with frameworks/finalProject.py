from flask import Flask , render_template
# request, redirect, url_for, flash, jsonify
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


# engine = create_engine('sqlite:///restaurantmenu.db')
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()


#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name':'The CRUDdy Crab', 'id':'1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$0.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

# Show all restaurants
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
	return render_template('restaurants.html', restaurants = restaurants)
	#return "This page will show all my restaurants"

# Create a new restaurant
@app.route('/restaurant/new/')
def newRestaurant():
	return render_template('newRestaurant.html', restaurants = restaurants)
	# return "This page will be for making a new restaurant"

# Edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
	return render_template('editRestaurant.html',restaurants=restaurants)
	# return "This page will be for editing restaurant %s" % restaurant_id

# Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
	return render_template('deleteRestaurant.html', restaurants = restaurants)
	# return "This page will be for deleting restaurant %s" % restaurant_id

# Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
	return render_template('menu.html', restaurant = restaurant, items = items) 
	# return "This page is the menu for the restaurant %s" % restaurant_id

# Create a new menu item
@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
	return render_template('newMenuItem.html', restaurant = restaurant)
	# return "This page is for making a new menu item for restaurant %s" % restaurant_id

# Edit a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id,menu_id):
	return render_template('editMenuItem.html', restaurants = restaurants, items = items)
	# return "This page is for editing menu item %s" % menu_id

# Delete a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id,menu_id):
	return render_template('deleteMenuItem.html', restaurants = restaurants, items = items)
	# return "This page is for deleteing menu item %s" % menu_id


if __name__ == '__main__':
	# app.secret_key = 'super_secret_key'
    app.debug = True
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000,threaded=False)
