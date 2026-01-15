package com.aaa.engine.core

class GameLoop(
    private val update: (Float) -> Unit,
    private val render: () -> Unit
) {
    @Volatile private var running = false
    private var lastTime = System.nanoTime()

    fun start() {
        running = true
        Thread {
            while (running) {
                val now = System.nanoTime()
                val delta = (now - lastTime) / 1_000_000_000f
                lastTime = now

                update(delta)
                render()
                Thread.sleep(16)
            }
        }.start()
    }

    fun stop() {
        running = false
    }
}
