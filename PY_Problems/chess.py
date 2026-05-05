from functools import lru_cache

def simplifiedChessEngine(whites, blacks, moves):
    # Helper functions
    def pos_to_tuple(pos):
        # pos: ['K', 'a1'] -> ('K', 0, 0)
        piece, square = pos
        col = ord(square[0]) - ord('a')
        row = int(square[1]) - 1
        return (piece, col, row)

    def tuple_to_pos(piece, col, row):
        return [piece, chr(col + ord('a')) + str(row + 1)]

    def in_board(col, row):
        return 0 <= col < 8 and 0 <= row < 8

    # Piece movement deltas
    directions = {
        'K': [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)],
        'Q': [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)],
        'R': [(-1,0), (0,-1), (0,1), (1,0)],
        'B': [(-1,-1), (-1,1), (1,-1), (1,1)],
        'N': [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)],
        'P': [(-1,-1), (1,-1)], # white pawn captures, black will be mirrored
    }

    # Board state: { (col, row): (color, piece) }
    def build_board(whites, blacks):
        board = {}
        for p in whites:
            piece, col, row = pos_to_tuple(p)
            board[(col, row)] = ('W', piece)
        for p in blacks:
            piece, col, row = pos_to_tuple(p)
            board[(col, row)] = ('B', piece)
        return board

    # Find king position for color
    def find_king(board, color):
        for (col, row), (c, piece) in board.items():
            if c == color and piece == 'K':
                return (col, row)
        return None

    # Generate all moves for a color
    def generate_moves(board, color):
        moves = []
        for (col, row), (c, piece) in board.items():
            if c != color:
                continue
            if piece == 'N':
                for dc, dr in directions['N']:
                    nc, nr = col + dc, row + dr
                    if in_board(nc, nr):
                        if (nc, nr) not in board or board[(nc, nr)][0] != color:
                            moves.append(((col, row), (nc, nr)))
            elif piece == 'P':
                # Pawns only capture diagonally
                for dc, dr in directions['P']:
                    # White moves up, black moves down
                    dr = dr if color == 'W' else -dr
                    nc, nr = col + dc, row + dr
                    if in_board(nc, nr):
                        if (nc, nr) in board and board[(nc, nr)][0] != color:
                            moves.append(((col, row), (nc, nr)))
            else:
                for dc, dr in directions[piece]:
                    for mul in range(1, 8):
                        nc, nr = col + dc*mul, row + dr*mul
                        if not in_board(nc, nr):
                            break
                        if (nc, nr) in board:
                            if board[(nc, nr)][0] != color:
                                moves.append(((col, row), (nc, nr)))
                            break
                        moves.append(((col, row), (nc, nr)))
                        if piece == 'K':
                            break
        return moves

    # Check if color's king is under attack
    def is_in_check(board, color):
        king_pos = find_king(board, color)
        if not king_pos:
            return True
        opp_color = 'B' if color == 'W' else 'W'
        for (col, row), (c, piece) in board.items():
            if c != opp_color:
                continue
            if piece == 'N':
                for dc, dr in directions['N']:
                    nc, nr = col + dc, row + dr
                    if (nc, nr) == king_pos:
                        return True
            elif piece == 'P':
                for dc, dr in directions['P']:
                    dr = dr if opp_color == 'W' else -dr
                    nc, nr = col + dc, row + dr
                    if (nc, nr) == king_pos:
                        return True
            else:
                for dc, dr in directions[piece]:
                    for mul in range(1, 8):
                        nc, nr = col + dc*mul, row + dr*mul
                        if not in_board(nc, nr):
                            break
                        if (nc, nr) == king_pos:
                            return True
                        if (nc, nr) in board:
                            break
                        if piece == 'K':
                            break
        return False

    # Minimax with alpha-beta pruning

    def serialize(board):
        # For memoization
        return tuple(sorted((col, row, c, p) for (col, row), (c, p) in board.items()))

    def minimax(board, color, depth, alpha, beta):
        if depth == 0:
            return False
        if is_in_check(board, color):
            # If current player is in check and has no moves, it's checkmate
            moves = generate_moves(board, color)
            for move in moves:
                new_board = dict(board)
                src, dst = move
                piece = new_board.pop(src)
                if dst in new_board:
                    del new_board[dst]
                new_board[dst] = piece
                if not is_in_check(new_board, color):
                    return False
            return True
        moves = generate_moves(board, color)
        if not moves:
            return False
        opp_color = 'B' if color == 'W' else 'W'
        for move in moves:
            new_board = dict(board)
            src, dst = move
            piece = new_board.pop(src)
            if dst in new_board:
                del new_board[dst]
            new_board[dst] = piece
            if not minimax(new_board, opp_color, depth-1, alpha, beta):
                return True
            beta = min(beta, False)
            if beta <= alpha:
                break
        return False

    # Main logic
    board = build_board(whites, blacks)
    result = minimax(board, 'W', moves, False, True)
    return "YES" if result else "NO"