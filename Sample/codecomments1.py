code = [

    '''public CoffeeMaker() {
            recipeBook = new RecipeBook();
            inventory = new Inventory();
        }''',

    '''public boolean addRecipe(Recipe r) {
            return recipeBook.addRecipe(r);
        }''',

    '''public String deleteRecipe(int recipeToDelete) {
            return recipeBook.deleteRecipe(recipeToDelete);
        }''',

    '''public String editRecipe(int recipeToEdit, Recipe r) {
            return recipeBook.editRecipe(recipeToEdit, r);
        }''',

    '''public synchronized void addInventory(String amtCoffee, String amtMilk, String amtSugar, String amtChocolate) throws InventoryException {
            inventory.addCoffee(amtCoffee);
            inventory.addMilk(amtMilk);
            inventory.addSugar(amtSugar);
            inventory.addChocolate(amtChocolate);
        }''',

    '''public synchronized String checkInventory() {
            return inventory.toString();
        }''',

    '''public synchronized int makeCoffee(int recipeToPurchase, int amtPaid) {
            int change = 0;

            if (getRecipes()[recipeToPurchase] == null) {
                change = amtPaid;
            } else if (getRecipes()[recipeToPurchase].getPrice() <= amtPaid) {
                if (inventory.useIngredients(getRecipes()[recipeToPurchase])) {
                    change = amtPaid - getRecipes()[recipeToPurchase].getPrice();
                } else {
                    change = amtPaid;
                }
            } else {
                change = amtPaid;
            }

            return change;
        }''',
    '''public synchronized Recipe[] getRecipes() {
            return recipeBook.getRecipes();
        }''',
    '''protected AbstractTitle(int position, int horizontalAlignment, int verticalAlignment,
                                Insets insets) {

            // check position
            if (!this.isValidPosition(position)) {
                throw new IllegalArgumentException("AbstractTitle: Invalid position.");
            }

            // check the horizontal and vertical alignment
            if ((horizontalAlignment!=LEFT) &&
                (horizontalAlignment!=CENTER) &&
                (horizontalAlignment!=RIGHT)) {
                throw new IllegalArgumentException("AbstractTitle: Invalid horizontal alignment.");
            }

            if ((verticalAlignment!=TOP) &&
                (verticalAlignment!=BOTTOM) &&
                (verticalAlignment!=MIDDLE)) {
                throw new IllegalArgumentException("AbstractTitle: Invalid vertical alignment.");
            }

            this.position = position;
            this.horizontalAlignment = horizontalAlignment;
            this.verticalAlignment = verticalAlignment;
            this.insets = insets;
            this.listeners = new java.util.ArrayList();
            this.notify = true;
        }''',
    '''protected AbstractTitle(int position, int horizontalAlignment, int verticalAlignment) {
            this(position, horizontalAlignment, verticalAlignment, new Insets(2, 2, 2, 2));
        }''',
    '''protected AbstractTitle() {
            this(TOP, CENTER, MIDDLE);
        }''',
    '''public Object clone() {
            AbstractTitle duplicate = null;
            try {
                duplicate = (AbstractTitle)(super.clone());
            }
            catch (CloneNotSupportedException e) {
                // this should never happen because Cloneable is implemented
                throw new RuntimeException("AbstractTitle.clone()");
            }

            duplicate.setNotify(false);
            duplicate.setInsets((Insets)this.getInsets().clone());
            duplicate.setNotify(true);
            return duplicate;
        }''',
    '''public boolean getNotify() {
            return this.notify;
        }''',
    '''public void setNotify(boolean flag) {
            this.notify = flag;
        }''',
    '''public int getPosition() {
            return this.position;
        }''',
    '''public void setPosition(int position) {
            if (this.position!=position) {
                // check that the position is valid
                this.position = position;
                notifyListeners(new TitleChangeEvent(this));
            }
        }''',
    '''public int getHorizontalAlignment() {
            return this.horizontalAlignment;
        }''',
    '''public void setHorizontalAlignment(int alignment) {
            if (this.horizontalAlignment!=alignment) {
                this.horizontalAlignment = alignment;
                notifyListeners(new TitleChangeEvent(this));
            }
        }''',
    '''public int getVerticalAlignment() {
            return this.verticalAlignment;
        }''',
    '''public void setVerticalAlignment(int alignment) {
            if (this.verticalAlignment!=alignment) {
                this.verticalAlignment = alignment;
                notifyListeners(new TitleChangeEvent(this));
            }
        }''',
    '''public Insets getInsets() {
            return this.insets;
        }''',
    '''public void setInsets(Insets insets) {
            if (!this.insets.equals(insets)) {
                this.insets = insets;
                notifyListeners(new TitleChangeEvent(this));
            }
        }''',
]

comments = [

"Constructor for the coffee maker",
"Returns true if the recipe is added to the list of recipes in the CoffeeMaker and false otherwise.",
" Returns the name of the successfully deleted recipe or null if the recipe cannot be deleted.",
"Returns the name of the successfully edited recipe or null if the recipe cannot be edited.",
"Returns true if inventory was successfully added",
"Returns the inventory of the coffee maker",
"Returns the change of a user's beverage purchase, or the user's money if the beverage cannot be made",
"Returns the list of Recipes in the RecipeBook.",
"Full constructor - builds an abstract title with the specified position and alignment. This class defines constants for the valid position and alignment values---an IllegalArgumentException will be thrown if invalid values are passed to this constructor.",
"Standard constrcutor - builds an abstract title with the specified position and alignment, with a default inset of 2 pixels around the title.  This class defines constants for the valid position and alignment values---an IllegalArgumentException will be thrown if invalid values are passed to this constructor.",
"Default constructor - builds an AbstractTitle positioned at the top of the page, centered horizontally and vertically within its space.",
"Returns a clone of the title. One situation when this is useful is when editing the title properties - you can edit a clone, and then it is easier to cancel the changes if necessary.",
"Returns the flag that indicates whether or not the notification mechanism is enabled.",
"Sets the flag that indicates whether or not the notification mechanism is enabled.  There are certain situations (such as cloning) where you want to turn notification off temporarily.",
"Returns the relative position of the title---represented by one of four integer constants defined in this class: TOP, BOTTOM, RIGHT or LEFT (or the equivalent NORTH, SOUTH, EAST and WEST).",
"Sets the position for the title.",
"Returns the horizontal alignment of the title.  The constants LEFT, CENTER and RIGHT (defined in this class) are used.",
"Sets the horizontal alignment for the title, and notifies any registered listeners of the change.  The constants LEFT, CENTER and RIGHT (defined in this class) can be used to specify the alignment.",
"Returns the vertical alignment of the title.  The constants TOP, MIDDLE and BOTTOM (defined in this class) are used.",
"Sets the vertical alignment for the title, and notifies any registered listeners of the change. The constants TOP, MIDDLE and BOTTOM (defined in this class) can be used to specify the alignment.",
"Returns the insets (the blank space around the edges) for this title.",
"Sets the insets for the title, and notifies registered listeners of the change."
]

code_arr = []
comments_arr = []
for i in range(len(code)):
    code_arr.append(code[i].split())
    comments_arr.append(comments[i].split())

print code_arr,comments_arr