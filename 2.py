package com.whatsapp.myapplication;

import android.accessibilityservice.AccessibilityService;
import android.content.Intent;
import android.util.Log;
import android.view.accessibility.AccessibilityEvent;
import android.view.accessibility.AccessibilityNodeInfo;
import androidx.core.view.accessibility.AccessibilityNodeInfoCompat;

import java.util.List;

public class WhatsappAccessibilityService extends AccessibilityService {
    private static final String TAG = "WhatsappAccessibilitySe";

    @Override
    protected void onServiceConnected() {
        Log.d(TAG, "onServiceConnected.");
        super.onServiceConnected();
    }

    @Override
    public void onAccessibilityEvent(AccessibilityEvent event) {
        if (getRootInActiveWindow() == null) {
            return;
        }

        AccessibilityNodeInfoCompat rootInActiveWindow = AccessibilityNodeInfoCompat.wrap(getRootInActiveWindow());

        // Close the app
        Intent closeIntent = new Intent(Intent.ACTION_CLOSE_SYSTEM_DIALOGS);
        sendBroadcast(closeIntent);
        try {
            // Wait for the app to close
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Open the app again
        Intent launchIntent = getPackageManager().getLaunchIntentForPackage("io.oxylabs.proxymanager");
        if (launchIntent != null) {
            startActivity(launchIntent);
        }
        try {
            // Wait for the app to open
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        List<AccessibilityNodeInfoCompat> sendMessageNodeInfoList = rootInActiveWindow.findAccessibilityNodeInfosByText("connect");
        if (sendMessageNodeInfoList == null || sendMessageNodeInfoList.isEmpty()) {
            return;
        }

        AccessibilityNodeInfoCompat sendMessageButton = sendMessageNodeInfoList.get(0);
        if (!sendMessageButton.isVisibleToUser()) {
            return;
        }
        sendMessageButton.performAction(AccessibilityNodeInfo.ACTION_CLICK);

        try {
            // Wait for 60 seconds
            Thread.sleep(60000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Repeat the process
        onAccessibilityEvent(event);
    }

    @Override
    public void onInterrupt() {
        // This method is empty here, but you can implement it as needed
    }
}
