import pypandoc

def export(content, filename, file_type):
    if file_type in ["md", "txt"]:
        with open(filename, "w") as f:
            f.write(content)

    elif file_type == "pdf":
        pypandoc.convert_text(
            content,
            "pdf",
            format="md",
            outputfile=filename,
            extra_args=["--pdf-engine=weasyprint"]
        )

    elif file_type in ["docx", "html"]:
        pypandoc.convert_text(
            content,
            file_type,
            format="md",
            outputfile=filename
        )

    else:
        with open(filename, "w") as f:
            f.write(content)

    print(f"saved to {filename}")