<template>
  <div class="page">
    <header class="hero">
      <h1>PJ-base</h1>
      <p class="tagline">Reusable blueprint for FastAPI × Vue projects</p>
    </header>
    <main class="content">
      <LoopbackForm />
    </main>
    <footer class="footer">Built with FastAPI and Vue.js</footer>
  </div>
</template>

<script setup>
import LoopbackForm from "./components/LoopbackForm.vue";
</script>

<style scoped>
.page {
  max-width: 640px;
  margin: 0 auto;
  padding: 3rem clamp(1.5rem, 5vw, 3rem) 2rem;
  background: rgba(16, 33, 69, 0.85);
  border-radius: 24px;
  box-shadow: 0 24px 48px rgba(4, 12, 28, 0.4);
  backdrop-filter: blur(8px);
}

.hero {
  text-align: center;
  margin-bottom: 2.5rem;
}

.hero h1 {
  font-size: clamp(2.5rem, 8vw, 3.25rem);
  margin: 0;
  color: #81c0ff;
  letter-spacing: 0.08em;
}

.tagline {
  margin: 0.75rem 0 0;
  color: #a5c8f1;
  font-size: 1.05rem;
}

.content {
  display: flex;
  justify-content: center;
}

.footer {
  margin-top: 2.5rem;
  text-align: center;
  color: #5776a5;
  font-size: 0.85rem;
}
</style>
