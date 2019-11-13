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

    let piece = SKSpriteNode(imageNamed: "test.png")
    let boardArray = [1, 3, 5, 7, 9, 11, 13, 15]
    
    override func didMove(to view: SKView) {
        addBoard()
        addPiece()
    }
    
    func addBoard() {
        let board = SKSpriteNode(imageNamed: "Board1.png")
        board.size = CGSize(width: size.width, height: size.height*0.575)
        board.position = CGPoint(x: size.width*0.5, y: size.height*0.5)
        piece.zPosition = 1
        self.addChild(board)
    }
    
    func addPiece() {
//        let piece = SKSpriteNode(imageNamed: "test.png")
        piece.size = CGSize(width: size.width*0.1, height: size.height*0.05)
        piece.position = CGPoint(x: size.width*0.5, y: size.height*0.5)
        piece.zPosition = 2
        self.addChild(piece)
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first!
        let touchLocation = touch.location(in: self.view)
        piece.size = CGSize(width: size.width*0.2, height: size.height*0.1)
        piece.position = CGPoint(x: touchLocation.x, y: size.height-touchLocation.y+40)
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first!
        let touchLocation = touch.location(in: self.view)
        piece.size = CGSize(width: size.width*0.2, height: size.height*0.1)
        piece.position = CGPoint(x: touchLocation.x, y: size.height-touchLocation.y+40)
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first!
        let touchLocation = touch.location(in: self.view)
        piece.size = CGSize(width: size.width*0.1, height: size.height*0.05)
        piece.position = CGPoint(x: touchLocation.x, y: size.height-touchLocation.y+20)
    }
    
}
