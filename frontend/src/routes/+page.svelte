<script lang="ts">
  import { goto } from '$app/navigation';
  function navigateToPrompt() {
    goto('/login');
  }
</script>

<svelte:head>
  <title>YANTRA - Transform Your Inputs into Comprehensive Documents</title>
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
      <!-- Divider -->
      <div class="h-1 bg-[#26262a] dark:bg-[#e8e8e0] mb-8"></div>
      <!-- Description -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12 text-lg">
        <div class="border-4 border-[#26262a] dark:border-[#e8e8e0] p-6">
          <p class="font-bold mb-2">CONCEPT</p>
          <p class="text-sm leading-relaxed">
            Transform raw input—topics, links, PDFs—into comprehensive documents. It could be anything. Recepies, research, ALL IN ONE.
            Pure functionality. if you can dream it, Yantra can make it!
          </p>
        </div>
        <div class="border-4 border-[#26262a] dark:border-[#e8e8e0] p-6">
          <p class="font-bold mb-2">CAPABILITIES</p>
          <p class="text-sm leading-relaxed">
            Web scraping. PDF processing. Multi-format export. Markdown, PDF, DOCX, TXT, HTML.
            All in one system. Complete control. Endless possibilities.
          </p>
        </div>
      </div>
      <!-- CTA Button -->
      <div class="flex justify-center mb-12">
        <button
          onclick={navigateToPrompt}
          class="border-4 border-[#26262a] dark:border-[#e8e8e0] bg-[#26262a] dark:bg-[#e8e8e0] text-[#e8e8e0] dark:text-[#26262a] px-12 py-4 text-xl font-bold hover:bg-[#f5f5f0] hover:dark:bg-[#22181C] hover:text-[#26262a] hover:dark:text-[#e8e8e0] transition-all transform active:translate-y-1"
        >
          ────────── START ──────────
        </button>
      </div>
      <!-- Features Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="border-4 border-[#26262a] dark:border-[#e8e8e0] p-8">
          <p class="text-4xl font-black mb-4">01</p>
          <p class="font-bold text-lg mb-2">WEB SCRAPING</p>
          <p class="text-sm">Automatically extract content from URLs</p>
        </div>
        <div class="border-4 border-[#26262a] dark:border-[#e8e8e0] p-8">
          <p class="text-4xl font-black mb-4">02</p>
          <p class="font-bold text-lg mb-2">PDF PROCESSING</p>
          <p class="text-sm">Upload and process multiple PDF files</p>
        </div>
        <div class="border-4 border-[#26262a] dark:border-[#e8e8e0] p-8">
          <p class="text-4xl font-black mb-4">03</p>
          <p class="font-bold text-lg mb-2">MULTI-FORMAT</p>
          <p class="text-sm">Export to 5 different document formats</p>
        </div>
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