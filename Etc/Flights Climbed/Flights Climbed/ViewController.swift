//
//  ViewController.swift
//  Flights Climbed
//
//  Created by 이다진 on 12/11/2018.
//  Copyright © 2018 이다진. All rights reserved.
//

import UIKit
import HealthKit

let healthKitStore: HKHealthStore = HKHealthStore()

class ViewController: UIViewController {

    @IBOutlet weak var climbed: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        self.authorizeHealthKitinApp()
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    func authorizeHealthKitinApp() {
        let healthKitTypesToRead : Set<HKObjectType> = [
            HKObjectType.quantityType(forIdentifier: HKQuantityTypeIdentifier.flightsClimbed)!
            // 다른 것 추가 가능
        ]
        
        let healthKitTypesToWrite : Set<HKSampleType> = []
        
        if !HKHealthStore.isHealthDataAvailable() {
            print("Error: Health data is not available")
            return
        }
        
        healthKitStore.requestAuthorization(toShare: healthKitTypesToWrite, read: healthKitTypesToRead) { (success, error) -> Void in
            print("Read Write Authorization succeeded")
        }
        
        print("herehere")
        print(healthKitTypesToRead)
    }

}

