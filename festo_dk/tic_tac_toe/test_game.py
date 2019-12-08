import game

def test_single_minimax_minimax():

    player0 = game.MinimaxPlayer(name="hans")
    player1 = game.MinimaxPlayer(name="robert")

    ttt = game.TicTacToe(player0, player1)

    ttt.play()

def test_single_alphabeta_alphabeta():

    player0 = game.AlphabetaPlayer(name="hans")
    player1 = game.AlphabetaPlayer(name="robert")

    ttt = game.TicTacToe(player0, player1)

    ttt.play()

def test_single_human_alphabeta():

    player0 = game.HumanPlayer(name="hans")
    player1 = game.AlphabetaPlayer(name="robert")

    ttt = game.TicTacToe(player0, player1)

    ttt.play()

if __name__ == '__main__':

    test_single_alphabeta_alphabeta()

    print('Evaluation time: {}s'.format(round(end - start, 7)))

    test_single_human_alphabeta()