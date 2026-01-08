package com.simplepubg.audio
import android.app.Service
import android.content.Intent
import android.os.IBinder
class BackgroundMusicService : Service() {
    override fun onBind(intent: Intent?): IBinder? = null
    companion object { const val ACTION_PLAY = "PLAY"; const val ACTION_PAUSE = "PAUSE" }
}