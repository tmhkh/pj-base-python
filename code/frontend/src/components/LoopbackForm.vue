<template>
  <section class="card">
    <h2>Message Echo</h2>
    <p class="description">Send a message and see the API echo it back instantly.</p>
    <form @submit.prevent="submit">
      <label class="field">
        <span>Message</span>
        <textarea
          v-model="form.text"
          placeholder="Type your message here"
          rows="4"
          required
        ></textarea>
      </label>
      <button type="submit" :disabled="loading">
        {{ loading ? "Sending..." : "Send to API" }}
      </button>
    </form>
    <p v-if="result" class="result">Echo: {{ result }}</p>
    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<script setup>
import { reactive, ref } from "vue";
import axios from "axios";

const form = reactive({ text: "" });
const loading = ref(false);
const result = ref("");
const error = ref("");

const rawBase = import.meta.env.VITE_API_BASE_URL ?? "";
const apiBase = rawBase.endsWith("/") ? rawBase.slice(0, -1) : rawBase;

const submit = async () => {
  if (!form.text.trim()) {
    error.value = "Please enter a message.";
    return;
  }

  loading.value = true;
  result.value = "";
  error.value = "";

  try {
  const { data } = await axios.post(`${apiBase}/api/v1/messages/echo`, {
      text: form.text
    });

    result.value = data.echo;
  } catch (ex) {
    error.value = "Failed to reach the API. Please confirm the backend is running.";
    console.error(ex);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.card {
  width: 100%;
  padding: clamp(1.5rem, 4vw, 2rem);
  background: rgba(7, 24, 52, 0.9);
  border-radius: 20px;
  box-shadow: inset 0 0 0 1px rgba(129, 192, 255, 0.2);
  display: grid;
  gap: 1.25rem;
}

.card h2 {
  margin: 0;
  font-size: 1.7rem;
  color: #9aceff;
}

.description {
  margin: 0;
  color: #7ea2d6;
}

.field {
  display: grid;
  gap: 0.6rem;
  color: #a3c6ff;
  font-size: 0.95rem;
}

textarea {
  resize: vertical;
  padding: 0.85rem;
  border-radius: 14px;
  border: none;
  background: rgba(15, 36, 71, 0.96);
  color: #e7efff;
  font-size: 1rem;
  font-family: inherit;
  box-shadow: 0 0 0 1px rgba(129, 192, 255, 0.3);
}

textarea:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(129, 192, 255, 0.6);
}

button {
  border: none;
  border-radius: 999px;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  color: #0a1f44;
  background: linear-gradient(120deg, #6db8ff 0%, #378bff 100%);
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

button:disabled {
  cursor: wait;
  opacity: 0.7;
}

button:not(:disabled):hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(61, 139, 255, 0.35);
}

.result {
  margin: 0;
  color: #81ffdd;
  font-weight: 600;
}

.error {
  margin: 0;
  color: #ff9da5;
}
</style>
