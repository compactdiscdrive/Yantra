<script lang="ts">
  import { goto } from '$app/navigation';
  import { auth, provider } from '$lib/firebase';
  import { signInWithPopup } from 'firebase/auth';

  async function signIn() {
    try {
      await signInWithPopup(auth, provider);
      goto('/ai');
    } catch (e) {
      console.error(e);
    }
  }
</script>

<svelte:head>
  <title>YANTRA - SignIn</title>
  <meta name="description" content="YANTRA AI is a powerful document generation system that transforms raw inputs like topics, links, and PDFs into comprehensive documents. Powered by LLAMA 3.2 4B, it offers web scraping, PDF processing, and multi-format export capabilities." />
  <meta name="keywords" content="YANTRA AI, document generation, LLAMA 3.2 4B, web scraping, PDF processing, multi-format export, markdown, PDF, DOCX, TXT, HTML" />
  <meta name  ="author" content="Manik Sharma" />
</svelte:head>

<main class="min-h-screen bg-[#f5f5f0] dark:bg-[#22181C] text-[#26262a] dark:text-[#e8e8e0] font-mono">
  <!-- Hero Section -->
  <div class="min-h-screen border-b-4 border-[#26262a] dark:border-[#e8e8e0] flex flex-col justify-center items-center px-4 py-12">
    <div class="w-full max-w-5xl">
      <!-- Title -->
      <h1 class="text-8xl md:text-9xl font-black mb-8 text-center leading-none tracking-tighter">
        YANTRA
      </h1>
      <!-- CTA Button -->
      <div class="flex justify-center mb-12">
        <button
            onclick={signIn}
            class="border-4 border-[#26262a] dark:border-[#e8e8e0] bg-[#26262a] dark:bg-[#e8e8e0] text-[#e8e8e0] dark:text-[#26262a] px-12 py-4 text-xl font-bold hover:bg-[#f5f5f0] hover:dark:bg-[#22181C] hover:text-[#26262a] hover:dark:text-[#e8e8e0] transition-all transform active:translate-y-1"
            >
            ────────── SIGN IN WITH GOOGLE ──────────
        </button>
      </div>
      </div>
      </div>
  <!-- Footer -->
  <footer class="border-t-4 border-[#26262a] dark:border-[#e8e8e0] py-8 px-4">
    <div class="max-w-4xl mx-auto">
      <p class="text-sm">
        MADE BY
        <a href="https://maniksharma.xyz" class="underline hover:no-underline font-bold">MANIK SHARMA</a>
      </p>
    </div>
  </footer>
</main>