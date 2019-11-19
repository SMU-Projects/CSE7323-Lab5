//
//  ChessSquare.swift
//  Lab5
//
//  Created by Will Lacey on 11/13/19.
//  Copyright © 2019 Will Lacey. All rights reserved.
//

import UIKit
import SpriteKit

class ChessSquare: NSObject {
    
    var spriteScenePosition = CGPoint(x:0, y:0)
    var xSquareOffset = CGFloat(0)
    var ySquareOffset = CGFloat(0)
    var row: Int
    var col: Int
    var hasPiece = false
    var chessScene: ChessScene
    
    // Initialize with a placeholder value
    var pieceSpriteFileName = "white_pawn"
    var pieceSprite = SKSpriteNode(imageNamed: "white_pawn")
    
    var highlightSpriteFileName = "black_pawn"
    var highlightSprite = SKSpriteNode(imageNamed: "black_pawn")
    var isHighlightedSquare = false {
        didSet{
            if isHighlightedSquare {
                self.highlightSprite = SKSpriteNode(imageNamed: highlightSpriteFileName)

                // Set size of piece sprite
                let highlightWidth = chessScene.size.width * chessScene.getPieceWidth()
                let highlightHeight = chessScene.size.height * chessScene.getPieceHeight()
                self.highlightSprite.size = CGSize(width: highlightWidth, height: highlightHeight)

                // Set location of piece sprite
                let xPos = chessScene.size.width * spriteScenePosition.x
                let yPos = chessScene.size.height * spriteScenePosition.y
                highlightSprite.position = CGPoint(x: xPos, y: yPos+5)
                highlightSprite.zPosition = 1

                chessScene.addChild(self.highlightSprite)
            } else {
                self.highlightSprite.removeFromParent()
            }
        }
    }
    
    init(arrayRow: Int, arrayCol: Int, spriteScenePosition: CGPoint, xSquareOffset: CGFloat, ySquareOffset: CGFloat, inChessScene: ChessScene) {
        self.row = arrayRow
        self.col = arrayCol
        self.spriteScenePosition = spriteScenePosition
        self.xSquareOffset = xSquareOffset
        self.ySquareOffset = ySquareOffset
        self.chessScene = inChessScene
        pieceSprite.isUserInteractionEnabled = false
    }
    
    func setPiece(pieceSpriteFileName: String) {
        
        self.hasPiece = true
        self.pieceSpriteFileName = pieceSpriteFileName
        self.pieceSprite = SKSpriteNode(imageNamed: pieceSpriteFileName)
        self.pieceSprite.name = pieceSpriteFileName
        
        // Set size of piece sprite
        let pieceWidth = chessScene.size.width * chessScene.getPieceWidth()
        let pieceHeight = chessScene.size.height * chessScene.getPieceHeight()
        self.pieceSprite.size = CGSize(width: pieceWidth, height: pieceHeight)
        
        // Set location of piece sprite
        let xPos = chessScene.size.width * spriteScenePosition.x
        let yPos = chessScene.size.height * spriteScenePosition.y
        pieceSprite.position = CGPoint(x: xPos, y: yPos)
        pieceSprite.zPosition = 2
        
        chessScene.addChild(pieceSprite)
    }
    
    func removePiece() {
        self.hasPiece = false
        self.pieceSprite.removeFromParent()
        
    }
    
    // Mark: Getters and Setters
    func getSquareTopBoundsPosition() -> CGFloat {
        return self.spriteScenePosition.y + (self.ySquareOffset / 2)
    }
    
    func getSquareLeftBoundsPosition() -> CGFloat {
        return self.spriteScenePosition.x - (self.xSquareOffset / 2)
    }
}
