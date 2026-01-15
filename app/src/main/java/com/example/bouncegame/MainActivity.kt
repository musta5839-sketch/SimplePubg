package com.example.bouncegame

import android.app.Activity
import android.os.Bundle
import android.view.WindowManager
import com.aaa.engine.view.GameView

class MainActivity : Activity() {

    private lateinit var gameView: GameView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)

        gameView = GameView(this)
        setContentView(gameView)
    }
}
