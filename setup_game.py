import os

# هيكلية المشروع والمحتوى
files = {
    "build.gradle.kts": """
plugins {
    id("com.android.application") version "8.2.0" apply false
    id("org.jetbrains.kotlin.android") version "1.9.20" apply false
}
""",
    "settings.gradle.kts": """
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "SimplePUBG"
include(":app")
""",
    "gradle.properties": """
org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
android.enableJetifier=true
""",
    "app/build.gradle.kts": """
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.simplepubg"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.simplepubg"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
    }
    
    // استخدام أيقونة افتراضية لمنع توقف البناء
    sourceSets {
        getByName("main") {
            res.srcDirs("src/main/res")
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
    buildFeatures {
        viewBinding = true
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("com.google.android.material:material:1.11.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
}
""",
    "app/src/main/AndroidManifest.xml": """
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application
        android:name=".SimplePubgApp"
        android:allowBackup="true"
        android:label="Simple PUBG"
        android:supportsRtl="true"
        android:theme="@style/Theme.SimplePUBG"
        android:enableOnBackInvokedCallback="true">
        
        <activity
            android:name=".ui.MainMenuActivity"
            android:exported="true"
            android:theme="@style/Theme.SimplePUBG">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>

        <activity
            android:name=".ui.GameActivity"
            android:exported="false"
            android:screenOrientation="portrait"
            android:theme="@style/Theme.SimplePUBG" />
            
        <service android:name=".audio.BackgroundMusicService" android:exported="false" />
    </application>
</manifest>
""",
    "app/src/main/res/values/themes.xml": """
<resources>
    <style name="Theme.SimplePUBG" parent="Theme.Material3.DayNight.NoActionBar">
        <item name="android:statusBarColor">#FF121216</item>
        <item name="android:navigationBarColor">#FF121216</item>
    </style>
</resources>
""",
    "app/src/main/res/values/colors.xml": """
<resources>
    <color name="splash_bg">#FF121216</color>
    <color name="purple_200">#FFBB86FC</color>
    <color name="white">#FFFFFFFF</color>
</resources>
""",
    # --- GitHub Actions Workflow ---
    ".github/workflows/build.yml": """
name: Build Android APK
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
    - name: Set up JDK 17
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
    - name: Setup Gradle
      uses: gradle/actions/setup-gradle@v3
    - name: Build Debug APK
      # نستخدم gradle مباشرة لأننا لم ننشئ gradlew في termux
      run: gradle assembleDebug
    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: simple-pubg-apk
        path: app/build/outputs/apk/debug/app-debug.apk
""",
    # --- Kotlin Code (Main App) ---
    "app/src/main/java/com/simplepubg/SimplePubgApp.kt": """
package com.simplepubg
import android.app.Application
class SimplePubgApp : Application()
""",
    # --- Kotlin Code (Activities) ---
    "app/src/main/java/com/simplepubg/ui/MainMenuActivity.kt": """
package com.simplepubg.ui
import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
class MainMenuActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val layout = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = android.view.Gravity.CENTER
        }
        val btn = Button(this).apply {
            text = "START GAME"
            setOnClickListener {
                startActivity(Intent(this@MainMenuActivity, GameActivity::class.java))
            }
        }
        layout.addView(btn)
        setContentView(layout)
    }
}
""",
    # --- Placeholder for GameActivity (Minimal to pass build) ---
    "app/src/main/java/com/simplepubg/ui/GameActivity.kt": """
package com.simplepubg.ui
import android.app.Activity
import android.os.Bundle
import android.widget.TextView
// وضعنا نسخة مبسطة لضمان نجاح البناء
class GameActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(TextView(this).apply { text = "Game Engine Loading..." })
    }
}
""",
    # --- Placeholder Service ---
    "app/src/main/java/com/simplepubg/audio/BackgroundMusicService.kt": """
package com.simplepubg.audio
import android.app.Service
import android.content.Intent
import android.os.IBinder
class BackgroundMusicService : Service() {
    override fun onBind(intent: Intent?): IBinder? = null
    companion object { const val ACTION_PLAY = "PLAY"; const val ACTION_PAUSE = "PAUSE" }
}
"""
}

def create_files():
    for path, content in files.items():
        # إنشاء المجلدات إذا لم تكن موجودة
        dir_name = os.path.dirname(path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        # كتابة الملف
        with open(path, "w") as f:
            f.write(content.strip())
        print(f"Created: {path}")

if __name__ == "__main__":
    create_files()
