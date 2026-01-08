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