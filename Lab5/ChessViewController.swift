//
//  GameViewController.swift
//  Lab5
//
//  Created by Will Lacey on 11/13/19.
//  Copyright © 2019 Will Lacey. All rights reserved.
//

import UIKit
import SpriteKit

class ChessViewController: UIViewController {

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        let navBar = self.navigationController?.navigationBar
        navBar?.isHidden = true
        
        //setup game scene
        let scene = GameScene(size: view.bounds.size)
        let skView = view as! SKView // the view in storyboard must be an SKView
        skView.showsFPS = true
        skView.showsNodeCount = true
        skView.ignoresSiblingOrder = true
        scene.scaleMode = .resizeFill
        skView.presentScene(scene)
        scene.backgroundColor = UIColor(red: 36/256, green: 45/256, blue: 61/256, alpha: 1)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    override var prefersStatusBarHidden : Bool {
        return true
    }
    
    @IBAction func exitButtonPressed(_ sender: Any) {
        self.navigationController?.popViewController(animated: true)
    }
}
