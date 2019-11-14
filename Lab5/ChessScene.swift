
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
    
    let test = SKSpriteNode(imageNamed: "black_pawn.png")
    lazy var gridPoints = generateGridPoints()
    
    var squares = [[ChessSquare]]()
    
    // MARK: Scene Functions
    override func didMove(to view: SKView) {
        addBoard()
        setBoard()
        test.zPosition = 2
        self.addChild(test)
    }
    
    func generateGridPoints()  -> [[(Double, Double)]] {
        
        var gridPoints = [[(Double, Double)]]()
        
        for row in 0...7 {
            var gridRow = [(Double, Double)]()
            for col in 0...7 {
                
                let yBoardOffset = 0.5 / 2
                let xSquareOffset = Double(self.boardWidth) / 8
                let ySquareOffset = Double(self.boardHeight) / 8
                
                let xPos = (xSquareOffset/2) + (xSquareOffset) * Double(col)
                let yPos = (yBoardOffset) + (ySquareOffset) * Double(row)
                let point = (xPos, yPos)
                gridRow.append(point)
            }
            gridPoints.append(gridRow)
        }
        return gridPoints
    }
    
    func addBoard() {
        let board = SKSpriteNode(imageNamed: "Board1.png")
        board.size = CGSize(width: size.width * self.boardWidth, height: size.height * self.boardHeight)
        board.position = CGPoint(x: size.width*0.5, y: size.height*0.5)
        board.zPosition = 1
        self.addChild(board)
    }
    
    func setBoard() {
        // Pawns
        for i in 0...7 {
            setPiece(pieceName: "black_pawn.png", piecePosition: self.gridPoints[6][i])
        }
        for i in 0...7 {
            setPiece(pieceName: "white_pawn.png", piecePosition: self.gridPoints[1][i])
        }
        
        // Rooks
        setPiece(pieceName: "black_rook.png", piecePosition: self.gridPoints[7][0])
        setPiece(pieceName: "black_rook.png", piecePosition: self.gridPoints[7][7])
        setPiece(pieceName: "white_rook.png", piecePosition: self.gridPoints[0][0])
        setPiece(pieceName: "white_rook.png", piecePosition: self.gridPoints[0][7])
        
        // Knights
        setPiece(pieceName: "black_knight.png", piecePosition: self.gridPoints[7][1])
        setPiece(pieceName: "black_knight.png", piecePosition: self.gridPoints[7][6])
        setPiece(pieceName: "white_knight.png", piecePosition: self.gridPoints[0][1])
        setPiece(pieceName: "white_knight.png", piecePosition: self.gridPoints[0][6])
        
        // Bishops
        setPiece(pieceName: "black_bishop.png", piecePosition: self.gridPoints[7][2])
        setPiece(pieceName: "black_bishop.png", piecePosition: self.gridPoints[7][5])
        setPiece(pieceName: "white_bishop.png", piecePosition: self.gridPoints[0][2])
        setPiece(pieceName: "white_bishop.png", piecePosition: self.gridPoints[0][5])
        
        // Queens
        setPiece(pieceName: "black_queen.png", piecePosition: self.gridPoints[7][3])
        setPiece(pieceName: "white_queen.png", piecePosition: self.gridPoints[0][3])

        // Kings
        setPiece(pieceName: "black_king.png", piecePosition: self.gridPoints[7][4])
        setPiece(pieceName: "white_king.png", piecePosition: self.gridPoints[0][4])
    }
    
    func setPiece(pieceName: String, piecePosition: (Double, Double)) {
        let piece = SKSpriteNode(imageNamed: pieceName)
        piece.size = CGSize(width: size.width * self.pieceWidth, height: size.height * self.pieceHeight)
        piece.position = CGPoint(x: size.width * CGFloat(piecePosition.0), y: size.height * CGFloat(piecePosition.1))
        piece.zPosition = 2
        self.addChild(piece)
    }
    
    // MARK: Touch Functions
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first!
        let touchLocation = touch.location(in: self.view)
        test.size = CGSize(width: 2 * size.width * self.pieceWidth, height: 2 * size.height * self.pieceHeight)
        test.position = CGPoint(x: touchLocation.x, y: size.height - touchLocation.y + 40)
        test.zPosition = 3
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first!
        let touchLocation = touch.location(in: self.view)
        test.size = CGSize(width: 2 * size.width * self.pieceWidth, height: 2 * size.height * self.pieceHeight)
        test.position = CGPoint(x: touchLocation.x, y: size.height - touchLocation.y + 40)
        test.zPosition = 3
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first!
        let touchLocation = touch.location(in: self.view)
        test.size = CGSize(width: size.width * self.pieceWidth, height: size.height * self.pieceHeight)
        test.position = CGPoint(x: touchLocation.x, y: size.height - touchLocation.y + 20)
        test.zPosition = 2
    }
    
}
