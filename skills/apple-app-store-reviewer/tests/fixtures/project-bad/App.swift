import AVFoundation
import WebKit
import GoogleSignIn

let embeddedKey = "sk-proj-ABCDEFGHIJKLMNOPQRSTUVWX123456"
let insecureEndpoint = "http://example.com/api"

func createAccount() { print("signup") }
func openCamera() { _ = AVCaptureDevice.default(for: .video) }
func socialLogin() { _ = GIDSignIn.sharedInstance }
func loadWrapper() { _ = WKWebView(frame: .zero) }
func dynamicBehavior() { _ = dlopen("downloaded.dylib", RTLD_NOW) }
