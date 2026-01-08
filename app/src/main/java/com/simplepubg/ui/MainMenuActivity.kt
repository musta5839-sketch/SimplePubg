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