import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import ollama
import sys
from scraper import scrape_url
from exporter import export
from rag import build_collection, retrieve

topic = sys.argv[1]
file_type = sys.argv[2]
sources = sys.argv[3:]

raw_sources = {}
for source in sources:
    if source.endswith(".pdf") and os.path.exists(source):
        print(f"reading pdf {source}...")
        from pdf_reader import read_pdf
        raw_sources[source] = read_pdf(source)
    else:
        print(f"scraping {source}...")
        raw_sources[source] = scrape_url(source)

if raw_sources:
    print("building knowledge base...")
    collection = build_collection(raw_sources)
    source_text = retrieve(collection, topic)
    print("generating document...")
else:
    source_text = ""

prompt = f"""Using ONLY the provided source material, write a detailed {file_type} document on:

{topic}

SOURCE MATERIAL:
{source_text}

STRICT REQUIREMENTS:

1. STRUCTURE (MANDATORY)
Organize the document into:
- Definition and Scope (include competing definitions and ambiguity)
- Legal Framework (analyze international law and conflicts)
- Case Studies (at least 2, with detailed analysis)
- Key Debate (arguments FOR and AGAINST enforcement operations)
- Implications (security, sovereignty, human rights)
- Policy Recommendations (specific and actionable)
- Sources

2. ANALYTICAL DEPTH
- Do NOT summarize passively
- Identify contradictions, debates, and uncertainties in the sources
- Highlight where terms (e.g., “narco-terrorism”) are contested or unclear
- Explain WHY actions were effective or ineffective in case studies

3. LEGAL ANALYSIS
- Explicitly address sovereignty, use of force, and legality
- Show where enforcement operations may violate or comply with international law

4. CASE STUDIES
- Use real-world examples from the sources
- Go beyond description: analyze outcomes, trade-offs, and consequences

5. ARGUMENTATION
- Present both sides of the debate:
- Pro-enforcement (security, counter-terrorism)
- Anti-enforcement (sovereignty, human rights)
- Avoid neutral “balanced essay” tone—be analytical and critical

6. SOURCE USAGE
- IF AND ONLY IF NO SOURCES ARE PROVIDED, generate your own material. Still, follow the structure, depth and other pointers. Make sure that the output WITHOUT SOURCES IS EQUALLY AS GOOD. In this case, do NOT try to cite sources and clearly add that the output is worse because sources are not provided.
- ONLY use the provided sources
- Cite inline using [Source](url)
- Do NOT invent or assume external facts
- Do NOT rely on general knowledge beyond the sources

7. WRITING QUALITY
- Avoid generic statements (e.g., “this is a complex issue”)
- Avoid repetition and filler
- Use precise, formal language

GOAL:
Produce a document that could be used in a high-level policy or MUN debate, not a school essay.

After generating,

Critically review the generated document.

Identify:
- Generic or weak arguments
- Missing legal nuance
- Lack of depth in case studies
- Any unsupported claims

Then rewrite ONLY the weak sections to improve analytical depth.

ALSO, Give sources for further learning if user has asked for researching/reading etc.
"""

response = ollama.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": prompt}]
)

content = response["message"]["content"]
filename = topic.replace(" ", "_") + "." + file_type
export(content, filename, file_type)