'''
Name: Joseph Henrichs
Uniqname: jhenrich
'''

import sqlite3

def question0():
    ''' Constructs and executes SQL query to retrieve
    all fields from the Region table
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Region"
    result = cursor.execute(query).fetchall()

    return result

def question1():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Territory"
    result = cursor.execute(query).fetchall()

    return result


def question2():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT count(*) FROM Employee"
    result = cursor.execute(query).fetchall()

    return result

def question3():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Product order by Id desc limit 10"
    result = cursor.execute(query).fetchall()

    return result


def question4():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function 
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName, UnitPrice FROM Product order by UnitPrice desc limit 3"
    result = cursor.execute(query).fetchall()

    return result

def question5():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName, UnitPrice, UnitsInStock FROM Product where UnitsInStock between 60 and 100"
    result = cursor.execute(query).fetchall()

    return result

def question6():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName FROM Product where UnitsInStock < ReorderLevel"
    result = cursor.execute(query).fetchall()

    return result

def question7():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT Id FROM Order where ShipCountry = 'France' and ShipPostalCode like '%04'"
    result = cursor.execute(query).fetchall()

    return result

def question8():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT CompanyName, ContactName FROM Customer where Country = 'UK' AND Fax IS NOT NULL"
    result = cursor.execute(query).fetchall()

def question9():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName, UnitPrice FROM Product where CategoryId = 1"
    result = cursor.execute(query).fetchall()

def question10():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName FROM Product where CategoryId = 6 AND Discontinued = 1"
    result = cursor.execute(query).fetchall()

def question11():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT Id FROM Order where ShipCountry = 'France' and ShipPostalCode like '%04'"
    result = cursor.execute(query).fetchall()
    
    def question12():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("/Users/joseph/Desktop/U_of_M/Winter_2020/si_507/hw6/Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT Id FROM Order where ShipCountry = 'France' and ShipPostalCode like '%04'"
    result = cursor.execute(query).fetchall()



#################################################################
########################  ECs start here  #######################
#################################################################

#########
## EC1 ##
#########

def print_query_result(raw_query_result):
    ''' Pretty prints raw query result
    
    Parameters
    ----------
    list 
        a list of tuples that represent raw query result
    
    Returns
    -------
    None
    '''
    #TODO Implement function
    pass


if __name__ == "__main__":
    '''WHEN SUBMIT, UNCOMMENT THE TWO LINES OF CODE
    BELOW IF YOU COMPLETED EC1'''
 
    connection.close()
    # result = question9()
    # print_query_result(result)

#########
## EC2 ##
#########
    
    #TODO Implement interactive program here
    pass

