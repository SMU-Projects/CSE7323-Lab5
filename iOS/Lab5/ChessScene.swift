
//
//  GameScene.swift
//  Lab5
//
//  Created by Will Lacey on 11/13/19.
//  Copyright © 2019 Will Lacey. All rights reserved.
//

import UIKit
import SpriteKit

class ChessScene: SKScene {

    // MARK: Scene Variables
    let pieceWidth = CGFloat(0.1)
    let pieceHeight = CGFloat(0.05)
    let boardWidth = CGFloat(1.0)
    let boardHeight = CGFloat(0.575)
    
    var selectedSquare: ChessSquare?
    
    lazy var chessBoard = generateChessSquares()
    
    // MARK: Scene Functions
    override func didMove(to view: SKView) {
        addBoard()
        setBoard()
    }
    
    func addBoard() {
        let board = SKSpriteNode(imageNamed: "Board1.png")
        board.size = CGSize(width: size.width * self.boardWidth, height: size.height * self.boardHeight)
        board.position = CGPoint(x: size.width*0.5, y: size.height*0.5)
        board.isUserInteractionEnabled = false
        board.zPosition = 0
        self.addChild(board)
    }
    
    func generateChessSquares() -> [[(ChessSquare)]] {
        var chessBoard = [[ChessSquare]]()
        
        for row in 0...7 {
            var chessRow = [ChessSquare]()
            for col in 0...7 {
                
                let yBoardOffset = 0.5 / 2
                let xSquareOffset = Double(self.boardWidth) / 8
                let ySquareOffset = Double(self.boardHeight) / 8
                
                let xPos = (xSquareOffset/2) + (xSquareOffset) * Double(col)
                let yPos = (yBoardOffset) + (ySquareOffset) * Double(7 - row)
                
                let square = ChessSquare.init(arrayRow: row, arrayCol: col, spriteScenePosition: CGPoint.init(x: xPos, y: yPos), xSquareOffset: CGFloat(xSquareOffset), ySquareOffset: CGFloat(ySquareOffset), inChessScene: self)
                chessRow.append(square)
            }
            chessBoard.append(chessRow)
        }
        return chessBoard
    }
    
    func setBoard() {
        // Pawns
        for i in 0...7 {
            self.chessBoard[1][i].setPiece(pieceSpriteFileName: "black_pawn")
        }
        for i in 0...7 {
            self.chessBoard[6][i].setPiece(pieceSpriteFileName: "white_pawn")
        }

        // Rooks
        self.chessBoard[0][0].setPiece(pieceSpriteFileName: "black_rook")
        self.chessBoard[0][7].setPiece(pieceSpriteFileName: "black_rook")
        self.chessBoard[7][0].setPiece(pieceSpriteFileName: "white_rook")
        self.chessBoard[7][7].setPiece(pieceSpriteFileName: "white_rook")

        // Knights
        self.chessBoard[0][1].setPiece(pieceSpriteFileName: "black_knight")
        self.chessBoard[0][6].setPiece(pieceSpriteFileName: "black_knight")
        self.chessBoard[7][1].setPiece(pieceSpriteFileName: "white_knight")
        self.chessBoard[7][6].setPiece(pieceSpriteFileName: "white_knight")

        // Bishops
        self.chessBoard[0][2].setPiece(pieceSpriteFileName: "black_bishop")
        self.chessBoard[0][5].setPiece(pieceSpriteFileName: "black_bishop")
        self.chessBoard[7][2].setPiece(pieceSpriteFileName: "white_bishop")
        self.chessBoard[7][5].setPiece(pieceSpriteFileName: "white_bishop")

        // Queens
        self.chessBoard[0][3].setPiece(pieceSpriteFileName: "black_queen")
        self.chessBoard[7][3].setPiece(pieceSpriteFileName: "white_queen")

        // Kings
        self.chessBoard[0][4].setPiece(pieceSpriteFileName: "black_king")
        self.chessBoard[7][4].setPiece(pieceSpriteFileName: "white_king")
    }
    
    func selectSquare(position: CGPoint) -> ChessSquare {
        
        var selectedRow = 0
        var selectedCol = 0
        
        for r in 0...7 {
            if position.y < self.chessBoard[r][0].getSquareTopBoundsPosition() {
                selectedRow = r
            }
        }
            
        for c in 0...7 {
            if position.x > self.chessBoard[0][c].getSquareLeftBoundsPosition() {
                selectedCol = c
            }
        }
        
        return self.chessBoard[selectedRow][selectedCol]
    }
    
    // Mark: Getters and Setters
    func getPieceWidth() -> CGFloat {
        return self.pieceWidth
    }
    
    func getPieceHeight() -> CGFloat {
        return self.pieceHeight
    }
    
    // MARK: Touch Functions
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        
        let touch:UITouch = touches.first!
        let touchPosition = touch.location(in: self)
        let xScenePos =  touchPosition.x / size.width
        let yScenePos = touchPosition.y / size.height
        let scenePosition = CGPoint(x: xScenePos, y: yScenePos)
        
        if self.selectedSquare != nil {
            
            let newSelectedSquare = self.selectSquare(position: scenePosition)
            let validMove = true // Todo: This has got to change bro
            
            if validMove {
                self.selectedSquare!.removePiece()
                if newSelectedSquare.hasPiece {
                    newSelectedSquare.removePiece()
                }
                newSelectedSquare.setPiece(pieceSpriteFileName: self.selectedSquare!.pieceSpriteFileName)
            }
            
            self.selectedSquare = nil
            
        } else {
            
            self.selectedSquare = self.selectSquare(position: scenePosition)
            if self.selectedSquare!.hasPiece {
                // get_valid_moves(color, row, col)
                // if valid moves
                    // highlight potential squares
                    // make move
                    // update game
                
//                var availableCoordinates = [(Int, Int)]()
//                availableCoordinates.append((self.selectedSquare!.row, self.selectedSquare!.col))
//                availableCoordinates.append((5,4))
//                availableCoordinates.append((4,4))
//                availableCoordinates.append((3,3))
//                for coordinate in availableCoordinates {
//                    let row = coordinate.0
//                    let col = coordinate.1
//                    self.chessBoard[row][col].isHighlightedSquare = true
//                }
                
            } else {
                self.selectedSquare = nil
            }
        }
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
//        let touch = touches.first!
//        let touchLocation = touch.location(in: self.view)
//        test.size = CGSize(width: 2 * size.width * self.pieceWidth, height: 2 * size.height * self.pieceHeight)
//        test.position = CGPoint(x: touchLocation.x, y: size.height - touchLocation.y + 40)
//        test.zPosition = 3
//        NSLog("\(test.position)")
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
//        let touch = touches.first!
//        let touchLocation = touch.location(in: self.view)
//        test.size = CGSize(width: size.width * self.pieceWidth, height: size.height * self.pieceHeight)
//        test.position = CGPoint(x: touchLocation.x, y: size.height - touchLocation.y + 20)
//        test.zPosition = 2
    }
    
}
