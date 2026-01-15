package com.aaa.engine.view

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.view.SurfaceHolder
import android.view.SurfaceView
import com.aaa.engine.core.GameLoop

class GameView(context: Context) : SurfaceView(context), SurfaceHolder.Callback {

    private lateinit var loop: GameLoop

    init {
        holder.addCallback(this)
    }

    override fun surfaceCreated(holder: SurfaceHolder) {
        loop = GameLoop(
            update = { },
            render = { drawFrame() }
        )
        loop.start()
    }

    private fun drawFrame() {
        val canvas: Canvas = holder.lockCanvas() ?: return
        canvas.drawColor(Color.BLACK)
        holder.unlockCanvasAndPost(canvas)
    }

    override fun surfaceDestroyed(holder: SurfaceHolder) {
        loop.stop()
    }

    override fun surfaceChanged(holder: SurfaceHolder, format: Int, width: Int, height: Int) {}
}
