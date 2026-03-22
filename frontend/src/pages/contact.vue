<script setup lang="ts">
import { ref } from 'vue'

const name    = ref('')
const email   = ref('')
const message = ref('')
const sent    = ref(false)
const error   = ref('')

// Replace with your actual email or form service endpoint
const CONTACT_EMAIL = 'your@email.com'

const submit = () => {
  if (!name.value || !email.value || !message.value) {
    error.value = 'Please fill in all fields.'
    return
  }
  // Opens default mail client — replace with API call if you add a contact endpoint
  const subject = encodeURIComponent(`Portfolio Contact from ${name.value}`)
  const body    = encodeURIComponent(`Name: ${name.value}\nEmail: ${email.value}\n\n${message.value}`)
  window.location.href = `mailto:${CONTACT_EMAIL}?subject=${subject}&body=${body}`
  sent.value = true
}
</script>

<template>
  <main class="container mx-auto px-4 py-16 max-w-xl">
    <h1 class="text-4xl font-bold mb-2">Contact</h1>
    <p class="text-gray-500 mb-8">Have a question or want to work together? Send me a message.</p>

    <div v-if="sent" class="bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-300 rounded-xl p-6 text-center">
      <p class="text-lg font-semibold">Message prepared!</p>
      <p class="text-sm mt-1">Your mail client should have opened with the message pre-filled.</p>
    </div>

    <form v-else class="space-y-5" @submit.prevent="submit">
      <div>
        <label class="block text-sm font-medium mb-1">Name</label>
        <input
          v-model="name"
          type="text"
          class="w-full border border-gray-200 dark:border-gray-700 rounded-lg px-4 py-2.5 bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Your name"
        />
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Email</label>
        <input
          v-model="email"
          type="email"
          class="w-full border border-gray-200 dark:border-gray-700 rounded-lg px-4 py-2.5 bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="you@example.com"
        />
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Message</label>
        <textarea
          v-model="message"
          rows="5"
          class="w-full border border-gray-200 dark:border-gray-700 rounded-lg px-4 py-2.5 bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
          placeholder="What's on your mind?"
        />
      </div>

      <p v-if="error" class="text-sm text-red-500">{{ error }}</p>

      <button
        type="submit"
        class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2.5 rounded-lg transition"
      >
        Send Message
      </button>
    </form>
  </main>
</template>
