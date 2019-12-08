# importing the requests library
import requests
import solver

def make_request():
    URL = "http://www.cs.utep.edu/cheon/ws/sudoku/new/?"

# location given here
    size = 9
    level=3

# defining a params dict for the parameters to be sent to the API
    PARAMS = {'size':size , 'level':level}

# sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)



# extracting data in json format
    data = r.json()
    return data

def create_board(data):
    if data['response']:
        size = int(data['size'])
        board = [[0 for x in range(size)] for y in range(size)]
        #solver.print_board(board)
        squares = data['squares']

        for sq in squares:
            x = int(sq['x'])
            y=  int(sq['y'])
            value = int(sq['value'])
            board[x][y]=value

#        solver.print_board(board)
        return board


def get_request():
    data = make_request()
    board = create_board(data)
    solver.print_board(board)
    return board



#print(data['squares'])
