//
//  HomeViewController.swift
//  Lab5
//
//  Created by Will Lacey on 11/12/19.
//  Copyright © 2019 Will Lacey. All rights reserved.
//

import UIKit

class HomeViewController: UIViewController {
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        let navBar = self.navigationController?.navigationBar
        navBar?.isHidden = true
        
        self.view.backgroundColor = UIColor(red: 36/256, green: 45/256, blue: 61/256, alpha: 1)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    override var prefersStatusBarHidden: Bool {
        return true
    }

}
