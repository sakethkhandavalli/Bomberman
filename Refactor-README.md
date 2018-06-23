#
Code Review

### The following changes are made for all occurences of these smells/bugs 

### Changes made while updating the code 
Code smell/Bug | Changes made
	---- | ----
	similar code | Remove the duplicate lines and write in a function and call that function
	too few public methods | Add few public methods 
	invalid variable name | Rename the variable using the allowed characters 
	invalid attribute name | Rename the attribute using the allowed characters
	missing class docstring | Add a string describing the class below the def of that class
	missing module docstring | Add a string describing the module below the def of that module
	missing method docstring | Add a string describing the method below the def of that method
	bad white-space | Remove the unnecessary spaces and add spaces at proper positions
	wrong import-order | Reaarange the modules into proper order
	len-as-condition | Remove 'len' from the 'if' condition
	invalid constant name | Rename the constant using allowed characters
	singleton-comparision | Use 'is' keyword instead of '=='
	used-before-assignment | Instantiate the variable before using it
	too-many-statements | Remove some of the lines in that function and keep them in another function
	too-many-branches | Rewrite the code using lesser 'if' conditions
	unused variable | Remove the variable
	redefining-outer-name | Use a different variable in the function
	trailing whitespace | Remove the unnecessary white spaces
	super-init-not-called | Call the init method of the inherited class
	unused-import | Remove the import statement
	Some enemies stop moving after one of the enemies is killed | Proper indices must be used in the explode method in the Bomb class
