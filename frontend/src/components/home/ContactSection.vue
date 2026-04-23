<script setup lang="ts">
import { ref } from 'vue'

const name = ref('')
const email = ref('')
const message = ref('')
const sent = ref(false)
const error = ref('')

const CONTACT_EMAIL = 'your@email.com'

const submit = () => {
  if (!name.value || !email.value || !message.value) {
    error.value = 'Please fill in all fields.'
    return
  }

  const subject = encodeURIComponent(`Portfolio Contact from ${name.value}`)
  const body = encodeURIComponent(`Name: ${name.value}\nEmail: ${email.value}\n\n${message.value}`)
  window.location.href = `mailto:${CONTACT_EMAIL}?subject=${subject}&body=${body}`
  sent.value = true
}
</script>

<template>
  <section class="max-w-4xl mx-auto bg-white dark:bg-gray-900 rounded-3xl shadow-2xl p-8 sm:p-12">
    <div class="grid gap-8 lg:grid-cols-[1.2fr_0.8fr] items-start">
      <div>
        <p class="uppercase text-sm tracking-[0.3em] text-blue-600 dark:text-blue-400 mb-4">Contact</p>
        <h2 class="text-4xl font-bold mb-4">Let’s work together</h2>
        <p class="text-gray-600 dark:text-gray-300 leading-relaxed">
          Have a question, a project idea, or just want to connect? Send a message and I will respond soon.
        </p>
      </div>
      <div>
        <div v-if="sent" class="rounded-3xl bg-green-50 dark:bg-green-900/20 border border-green-200 dark:border-green-700 p-6 text-green-800 dark:text-green-200">
          <p class="text-lg font-semibold">Message prepared!</p>
          <p class="mt-2 text-sm">Your mail client should open with the message pre-filled.</p>
        </div>

        <form v-else class="space-y-5" @submit.prevent="submit">
          <div>
            <label class="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-200">Name</label>
            <input
              v-model="name"
              type="text"
              class="w-full border border-gray-200 dark:border-gray-700 rounded-2xl px-4 py-3 bg-gray-50 dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Your name"
            />
          </div>

          <div>
            <label class="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-200">Email</label>
            <input
              v-model="email"
              type="email"
              class="w-full border border-gray-200 dark:border-gray-700 rounded-2xl px-4 py-3 bg-gray-50 dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="you@example.com"
            />
          </div>

          <div>
            <label class="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-200">Message</label>
            <textarea
              v-model="message"
              rows="5"
              class="w-full border border-gray-200 dark:border-gray-700 rounded-2xl px-4 py-3 bg-gray-50 dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
              placeholder="What's on your mind?"
            />
          </div>

          <p v-if="error" class="text-sm text-red-500">{{ error }}</p>

          <button
            type="submit"
            class="w-full bg-gradient-to-r from-blue-500 to-purple-500 text-white font-semibold py-3 rounded-2xl hover:shadow-lg transition-all duration-300"
          >
            Send Message
          </button>
        </form>
      </div>
    </div>
  </section>
</template>
