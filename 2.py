package com.whatsapp.myapplication;

import android.accessibilityservice.AccessibilityService;
import android.app.ActivityManager;
import android.content.Context;
import android.content.Intent;
import android.util.Log;
import android.view.accessibility.AccessibilityEvent;

public class WhatsappAccessibilityService extends AccessibilityService {
    private static final String TAG = "WhatsappAccessibilitySe";
    private static final String PACKAGE_NAME = "io.oxylabs.proxymanager";

    @Override
    protected void onServiceConnected() {
        Log.d(TAG, "onServiceConnected.");
        super.onServiceConnected();

        // Start a new thread to handle the repeated opening and closing of the app
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    try {
                        // Open the app
                        Intent launchIntent = getPackageManager().getLaunchIntentForPackage(PACKAGE_NAME);
                        if (launchIntent != null) {
                            launchIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                            startActivity(launchIntent);
                        }
                        Log.d(TAG, "App opened: " + PACKAGE_NAME);

                        // Wait for 10 seconds
                        Thread.sleep(10000);

                        // Close the app
                        closeApp(PACKAGE_NAME);
                        Log.d(TAG, "App closed: " + PACKAGE_NAME);

                        // Wait for 60 seconds before repeating
                        Thread.sleep(60000);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();
    }

    private void closeApp(String packageName) {
        ActivityManager activityManager = (ActivityManager) getSystemService(Context.ACTIVITY_SERVICE);
        if (activityManager != null) {
            // This will stop the package by killing its process
            activityManager.killBackgroundProcesses(packageName);

            // Use reflection to call forceStopPackage
            try {
                activityManager.getClass().getMethod("forceStopPackage", String.class).invoke(activityManager, packageName);
            } catch (Exception e) {
                Log.e(TAG, "Failed to stop package", e);
            }
        }
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
