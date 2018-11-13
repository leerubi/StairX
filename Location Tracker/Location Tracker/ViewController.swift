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
    var FILE_URL: URL = URL(fileURLWithPath: "")
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        let fileName = "recordedData"
        let DocumentDirURL = try! FileManager.default.url(for: .documentDirectory, in: .userDomainMask, appropriateFor: nil, create: true)
        let fileURL = DocumentDirURL.appendingPathComponent(fileName).appendingPathExtension("txt")
        FILE_URL = fileURL
        
        print("File Path: \(fileURL.path)")
        
        let writeString = "dummy strings..."
        do {
            try writeString.write(to: fileURL, atomically: true, encoding: String.Encoding.utf8)
        } catch let error as NSError {
            print("Fail to write to URL ")
            print(error)
        }
        
        var readString = ""
        do {
            readString = try String(contentsOf: fileURL)
        } catch let error as NSError {
            print("Fail to read to URL ")
            print(error)
        }
        
        print("Contents of the file: \(readString)")
        
        locationManager.delegate = self
        locationManager.requestAlwaysAuthorization()
        locationManager.startUpdatingLocation()
        /*
         locationManager.distanceFilter = 100 // 100 m 움직일 때마다 GPS 좌표를 print
         // 하지만 10초마다 업데이트? -> Blackbox
         locationManager.stopUpdatingLocation()
         */
        
        if CMAltimeter.isRelativeAltitudeAvailable() {
            altimeter.startRelativeAltitudeUpdates(to: OperationQueue.main) { (data, error) in
                print(NSDate())
                print("relativeAltitude:"+String.init(format: "%.9f", (data?.relativeAltitude.floatValue)!))
                // relativeAltitude unit: m
                
                print("pressure:"+String.init(format: "%.9f ", (data?.pressure.floatValue)!*10))
                // pressure unit: hPA
            }
        }

    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        
        for currentLocation in locations {
            print(currentLocation.timestamp)
            print("altitude:\(currentLocation.altitude)")
            print("latitude:\(currentLocation.coordinate.latitude)")
            print("longitude:\(currentLocation.coordinate.longitude)")
//            print("movedDistance: \(currentLocation.distance(from: prevLocation))")

            
        }
    }
    
    @IBOutlet weak var emailButton: UIButton!
    
    @IBAction func sendEmail(_ sender: UIButton) {
        
        let mSubject = "The subject of the e-mail"
        
        let mBody = "Hi! This is an e-mail. Please see the attached file."
        
        let mRecipients = ["dj112200@gmail.com"]
        
        let mAttachment = "Some content".data(using: String.Encoding.utf8, allowLossyConversion: false)!
        
        let mAttachmentName = "recoredData.txt"
        
        doEmail(subject: mSubject, body: mBody, recipients: mRecipients, attachment: mAttachment, attachmentName: mAttachmentName)
        
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
