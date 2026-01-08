package com.example.bouncegame

import android.content.Context
import android.graphics.*
import android.view.SurfaceHolder
import android.view.SurfaceView

class GameView(context: Context) : SurfaceView(context), Runnable, SurfaceHolder.Callback {

    private var thread: Thread? = null
    @Volatile private var running = false
    private val paint = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.CYAN }

    private var x = 100f
    private var y = 100f
    private var vx = 10f
    private var vy = 12f
    private val r = 50f

    init {
        holder.addCallback(this)
    }

    override fun run() {
        while (running) {
            if (!holder.surface.isValid) continue
            val canvas = holder.lockCanvas() ?: continue

            x += vx
            y += vy
            if (x < r || x > width - r) vx = -vx
            if (y < r || y > height - r) vy = -vy

            canvas.drawColor(Color.BLACK)
            canvas.drawCircle(x, y, r, paint)
            holder.unlockCanvasAndPost(canvas)

            Thread.sleep(16)
        }
    }

    fun resume() {
        running = true
        thread = Thread(this)
        thread?.start()
    }

    fun pause() {
        running = false
        thread?.join()
    }

    override fun surfaceCreated(holder: SurfaceHolder) {}
    override fun surfaceChanged(holder: SurfaceHolder, format: Int, width: Int, height: Int) {}
    override fun surfaceDestroyed(holder: SurfaceHolder) {
        pause()
    }
}
