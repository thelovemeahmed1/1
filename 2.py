package com.whatsapp.myapplication;

import android.accessibilityservice.AccessibilityService;
import android.content.Intent;
import android.util.Log;
import android.view.accessibility.AccessibilityEvent;
import android.view.accessibility.AccessibilityNodeInfo;
import androidx.core.view.accessibility.AccessibilityNodeInfoCompat;

public class WhatsappAccessibilityService extends AccessibilityService {
    private static final String TAG = "WhatsappAccessibilitySe";

    @Override
    protected void onServiceConnected() {
        Log.d(TAG, "onServiceConnected.");
        super.onServiceConnected();
        // Start a new thread to handle the repeated closing of the app
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    try {
                        // Close the app
                        Intent closeIntent = new Intent(Intent.ACTION_CLOSE_SYSTEM_DIALOGS);
                        sendBroadcast(closeIntent);

                        // Force-stop the app
                        String packageName = "io.oxylabs.proxymanager";
                        Runtime.getRuntime().exec("am force-stop " + packageName);

                        // Log the action
                        Log.d(TAG, "App closed: " + packageName);

                        // Wait for 60 seconds before repeating
                        Thread.sleep(60000);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();
    }

    @Override
    public void onAccessibilityEvent(AccessibilityEvent event) {
        // No need to handle events in this implementation
    }

    @Override
    public void onInterrupt() {
        // This method is empty here, but you can implement it as needed
    }
}
