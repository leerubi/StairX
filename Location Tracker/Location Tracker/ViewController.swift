//
//  ViewController.swift
//  Location Tracker
//
//  Created by 이다진 on 13/11/2018.
//  Copyright © 2018 이다진. All rights reserved.
//

import UIKit
import CoreLocation
import CoreMotion
import MessageUI

class ViewController: UIViewController, CLLocationManagerDelegate, MFMailComposeViewControllerDelegate {
    
    let locationManager: CLLocationManager = CLLocationManager()
    let altimeter = CMAltimeter()
    var writeString = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        /*
         I_S01: Record GPS latitude and logitude
         Task: Add Information to One String
         */
        locationManager.delegate = self
        locationManager.requestAlwaysAuthorization()
        locationManager.startUpdatingLocation()
//        locationManager.distanceFilter = 100 // 100 m 움직일 때마다 GPS 좌표를 print
//        // 하지만 10초마다 업데이트? -> Blackbox
//        locationManager.stopUpdatingLocation()
        
        /*
         I_S03, I_S04: Record Relative Altitude and Pressure
         Task: Add Information to One String
         relativeAltitude unit: m
         pressure unit: hPA
         */
        if CMAltimeter.isRelativeAltitudeAvailable() {
            altimeter.startRelativeAltitudeUpdates(to: OperationQueue.main) { (data, error) in
        
//                print(NSDate().description)
//                print("relativeAltitude:"+String.init(format: "%.9f", (data?.relativeAltitude.floatValue)!))
//                print("pressure:"+String.init(format: "%.9f ", (data?.pressure.floatValue)!*10))
              
                self.writeString += "\(NSDate().description))\n"
                self.writeString += "relativeAltitude:"+String.init(format: "%.9f", (data?.relativeAltitude.floatValue)!)+"\n"
                self.writeString += "pressure:"+String.init(format: "%.9f ", (data?.pressure.floatValue)!*10)+"\n"
                
            }
        }

    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        
        for currentLocation in locations {
//            print(currentLocation.timestamp.description)
//            print("altitude:\(currentLocation.altitude)")
//            print("latitude:\(currentLocation.coordinate.latitude)")
//            print("longitude:\(currentLocation.coordinate.longitude)")
            
            self.writeString += "\(currentLocation.timestamp.description)\n"
            self.writeString += "altitude:\(currentLocation.altitude)\n"
            self.writeString += "latitude:\(currentLocation.coordinate.latitude)\n"
            self.writeString += "longitude:\(currentLocation.coordinate.longitude)\n"
        }
    }
    
    @IBOutlet weak var emailButton: UIButton!
    
    /*
     I_S05: Export Recorded Data
     Task: Send an email with attached file
     */
    @IBAction func sendEmail(_ sender: UIButton) {
        
        let mSubject = "StairX: Recorded data"
        
        let mBody = "This is an e-mail from StairX.\nPlease see the attached file.\nCreated at \(NSDate())"
        
        let mRecipients = ["dj112200@gmail.com", "knw3011506@postech.ac.kr"]
        
        let mAttachment = writeString.data(using: String.Encoding.utf8, allowLossyConversion: false)!
        
        /*
         시간 정보로 텍스트 파일 이름을 지정하고자 함.
         */
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
        
        let myString = formatter.string(from: Date())
        let yourDate = formatter.date(from: myString)
        formatter.dateFormat = "yyyy-MMM-dd_HH-mm-ss"
        let myStringafd = formatter.string(from: yourDate!)
    
        let mAttachmentName = "\(myStringafd).txt"
        
        doEmail(subject: mSubject, body: mBody, recipients: mRecipients, attachment: mAttachment, attachmentName: mAttachmentName)
        
        writeString = ""
    }
    
    func doEmail(subject: String, body: String, recipients: Array<Any>, attachment: Data, attachmentName: String ) {
        
        if MFMailComposeViewController.canSendMail() {
            
            let mailer = MFMailComposeViewController()
            
            mailer.mailComposeDelegate = self
            
            // the subject
            mailer.setSubject(subject)
            
            // the recepients: an Array of Strings
            mailer.setToRecipients(recipients as! [String])
            
            // make an attachment. You can attach anything, as long as it is a "Data?" object
            mailer.addAttachmentData(attachment, mimeType: "application/octet-stream", fileName: attachmentName)
            
            // the message body
            mailer.setMessageBody(body, isHTML: false)
            
            // present the mailer
            self.present(mailer, animated: true, completion: nil)
            
        }
            
        else
            
        {
            
            let alert = UIAlertController(title: "Mail Error", message: "Your device has not been configured to send e-mails", preferredStyle: .alert)
            
            let okAction = UIAlertAction(title: "Ok", style: .default, handler: nil)
            
            alert.addAction(okAction)
            
            self.present(alert,animated: true,completion: nil)
            
        }
    }
    
    // mailer delegate
    func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: Error?) {
        
        var  message = ""
        
        switch (result)
            
        {
            
        case .cancelled: message = "You cancelled the operation and no e-mail message was sent."
        case .saved: message = "You saved the e-mail message in the drafts folder."
        case .sent: message = "Mail send: e-mail message sent successfully."
        case .failed: message = "Mail failed: the e-mail message was not sent. Please check your e-mail settings."
            
        }
        
        let alert = UIAlertController(title: "Mailer", message: message, preferredStyle: .alert)
        let okAction = UIAlertAction(title: "Ok", style: .default, handler: nil)
        alert.addAction(okAction)
        
        self.present(alert,animated: true,completion: nil)
        
        // Remove the mail view
        self.dismiss(animated: true, completion: nil)
        
    }
    
}
