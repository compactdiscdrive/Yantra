<script lang="ts">
  let topic = ""
  let fileType = "md"
  let sources = ""
  let status = ""
  let working = false
  let uploadedFiles: File[] = []
  import favicon from '$lib/assets/favicon.svg';

  function handleFile(e: Event) {
    const file = (e.target as HTMLInputElement).files?.[0]
    if (file) uploadedFiles = [...uploadedFiles, file]
  }

  async function generate() {
    if (!topic) return
    working = true
    const messages = [
      "scraping sources...",
      "putting on the finishing touches...",
      "reading content...",
      "just a moment more...",
      "generating document...",
      "almost there...",
      "finalizing the masterpiece...",
      "we're on it...",
      "cooking up your document...",
      "assembling the pieces...",
      "star us on github",
      "ollama ftw"
    ]
    let i = 0
    status = messages[0]
    const interval = setInterval(() => {
      i = (i + 1) % messages.length
      status = messages[i]
    }, 5000)

    const urlList = sources.split(" ").filter(s => s.trim() !== "")

    // use FormData so we can send both json data and files
    const formData = new FormData()
    formData.append("topic", topic)
    formData.append("file_type", fileType)
    formData.append("sources", JSON.stringify(urlList))
    uploadedFiles.forEach(f => formData.append("pdfs", f))

    const response = await fetch("http://localhost:8000/generate", {
      method: "POST",
      body: formData
    })

    clearInterval(interval)
    status = "downloading..."

    const blob = await response.blob()
    const url = URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = topic.replace(/ /g, "_") + "." + fileType
    a.click()

    status = "done!"
    working = false
  }
</script>

<svelte:head>
  <title>YANTRA</title>
  <meta name="description" content="YANTRA AI is a powerful document generation system that transforms raw inputs like topics, links, and PDFs into comprehensive documents. Powered by LLAMA 3.2 4B, it offers web scraping, PDF processing, and multi-format export capabilities." />
  <meta name="keywords" content="YANTRA AI, document generation, LLAMA 3.2 4B, web scraping, PDF processing, multi-format export, markdown, PDF, DOCX, TXT, HTML" />
  <meta name="author" content="Manik Sharma" />
</svelte:head>

<main class="bg-[#f5f5f0] dark:bg-[#22181C] min-h-screen flex flex-col items-center justify-center gap-4 text-[#26262a] dark:text-[#e8e8e0] font-mono">

  <h1 class="text-6xl font-black mb-4">YANTRA</h1>
  <p class="text-sm">if you can dream it, Yantra can make it!</p>
  <hr width=30% class="border-[#26262a] dark:border-[#e8e8e0]"/>

  <p class="text-sm">prompt (topic + addons eg: make it tabular)</p>
  <textarea
    bind:value={topic}
    placeholder="how humans evolved..."
    class="w-[500px] h-32 rounded-xl border-4 border-[#26262a] dark:border-[#e8e8e0] bg-[#f5f5f0] dark:bg-[#22181C] text-[#26262a] dark:text-[#e8e8e0] p-4 font-mono text-sm resize-none"
  ></textarea>

  <div class="flex items-center gap-8">

    <div class="flex flex-col items-start gap-1">
      <p class="text-sm">output:</p>
      <select bind:value={fileType} class="rounded-full px-6 py-1 bg-[#f5f5f0] dark:bg-[#22181C] text-[#26262a] dark:text-[#e8e8e0] font-mono border-2 border-[#26262a] dark:border-[#e8e8e0] cursor-pointer">
        <option value="md">MD</option>
        <option value="pdf">PDF</option>
        <option value="docx">DOCX</option>
        <option value="txt">TXT</option>
        <option value="html">HTML</option>
      </select>
    </div>

    <div class="flex flex-col items-start gap-1">
      <p class="text-sm">extra sources</p>
      <input
        bind:value={sources}
        placeholder="weblink(s)"
        class="rounded-full px-4 py-1 w-56 bg-[#f5f5f0] dark:bg-[#22181C] text-[#26262a] dark:text-[#e8e8e0] font-mono border-2 border-[#26262a] dark:border-[#e8e8e0]"
      />
      <input
        type="file"
        accept=".pdf"
        onchange={handleFile}
        class="hidden"
        id="fileInput"
      />
      <label for="fileInput" class="rounded-full px-4 py-1 bg-[#f5f5f0] dark:bg-[#22181C] text-[#26262a] dark:text-[#e8e8e0] font-mono border-2 border-[#26262a] dark:border-[#e8e8e0] cursor-pointer">
        + pdf
      </label>
    </div>

    <button
      onclick={generate}
      disabled={working}
      class="bg-[#26262a] dark:bg-[#e8e8e0] text-[#e8e8e0] dark:text-[#26262a] font-mono font-bold text-base rounded-xl px-6 py-4 hover:bg-[#f5f5f0] hover:dark:bg-[#22181C] hover:text-[#26262a] hover:dark:text-[#e8e8e0] border-4 border-[#26262a] dark:border-[#e8e8e0] cursor-pointer disabled:opacity-50 transition-all">
      {working ? "WORKING..." : "GENERATE"}
    </button>

  </div>

  {#if status}
    <p class="text-sm">{status}</p>
  {/if}

  <hr width=30% class="border-[#26262a] dark:border-[#e8e8e0]"/>

  <footer>
    <p class="text-xs">made by <a href="https://maniksharma.xyz" class="underline">manik sharma</a></p>
  </footer>

</main>