#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AGomez, 2021-Dec-07, finished adding code and tested to see if it works
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        cdinfoline: Formatting each of the objects to save to the file
        __str__: Formatting each of the objects when reading from the file

    """
    # -- Fields -- #
    # -- Constructor -- #
    def __init__(self, ID, Title, Artist):
        # -- Attributes -- #
        self.cd_id = ID
        self.cd_title = Title
        self.cd_artist = Artist

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = value

    @property
    def cd_title(self):
        return self.__cd_title.title()

    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value

    @property
    def cd_artist(self):
        return self.__cd_artist.title()

    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = value


    # -- Methods -- #
    def cdinfoline(self):
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)
    
    def __str__(self):
        return '{}\t{} (by: {})\n'.format(self.cd_id, self.cd_title, self.cd_artist)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Saves objects into a list and writes those objects from the list into the file:
    
        Args:
            file_name (string): Name of the file
            lst_Inventory (list): List of CD's (ID, Title, Artist)
    
        Returns:
            None    
        """
        objFile = open(file_name, 'w')
        for object in lst_Inventory:
            objFile.write(CD.cdinfoline(object))
        objFile.close()
        return

    def load_inventory(file_name):
        """Loads list (table) of objects from the file:
    
        Args:
            file_name (string): Name of the file
    
        Returns:
            table (list): List of CD's objects (ID, Title, Artist)
        """
        table =[]
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                table.append(CD(data[0], data[1],data[2]))
            objFile.close()
        except FileNotFoundError:
            print('Text file does not exist!')
        return table

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Processes data from/to the user:

    properties:

    methods:
        print_menu(): Displays menu to user
        menu_choice(): Menu input from user
        show_inventory(table): Displays inventory table
        new_CD(): CD input from user 

    """
    @staticmethod
    def print_menu():
        """Displays menu to user
        
        Args:
            None
            
        Returns:
            None
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Menu input from user
        
        Args:
            None
            
        Returns:
            choice (string): a lower cased string of the input choice from the user
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays inventory table
        
        Args:
            table (list of lines): Table list made up from lines from the object
            
        Returns:
            None
        """
        try:
            print('======= The Current Inventory: =======')
            print('ID\tCD Title (by: Artist)\n')
            for line in table:
                print(line)
            print('======================================')
        except Exception:
            print("Error")

    @staticmethod
    def new_CD():
        """CD input from user 
        
        Args:
            None
            
        Returns:
            CD(strID, strTitle, strArtist) (object): Object to be ready to append into a new list
        """
        strID = input('Enter New ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
                
        return CD(strID, strTitle, strArtist)
        

# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start

lstOfCDObjects = FileIO.load_inventory(strFileName)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:\n\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist

        # 3.3.2 Add item to the table
        lstOfCDObjects.append(IO.new_CD())
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n]\n\n').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

